#!/usr/bin/env python

"""
Purpose: unit and integration tests
- click.testing invokes command-line app and verifies app behavior in isolation
- fastapi.testclient simulates HTTP requests and verifies API without starting the server
"""

import json
import unittest
from unittest.mock import patch

import requests
from click.testing import CliRunner
from fastapi.testclient import TestClient

from pkg_15903.cli import main
from pkg_15903.main import app


class TestMain(unittest.TestCase):

    """
    Click Testing on CLI
    """
    def setUp(self):
        self.runner = CliRunner()
        self.client = TestClient(app)

    """ assert zero exit code with url success """
    def test_cli_main_success(self):
        result = self.runner.invoke(main, ['--url', 'https://example.com'])
        self.assertEqual(result.exit_code, 0)

    """ assert non-zero exit code with ClsValidate chk_url raise ValueError """
    def test_cli_main_validate_error(self):
        result = self.runner.invoke(main, ['--url', 'https://iamnotarobotdot.ai'])
        self.assertNotEqual(result.exit_code, 0)

    """ assert non-zero exit code with HTTPError """
    def test_cli_main_http_error(self):
        result = self.runner.invoke(main, ['--url', 'https://example.com/thepathdoesnotexist'])
        self.assertNotEqual(result.exit_code, 0)

    """ assert ConnectionError in mock_get result.exception """
    @patch('requests.get')
    def test_cli_main_connection_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.ConnectionError()
        result = self.runner.invoke(main, ['--url', 'https://example.com'])
        # result.exception: 500: Error_Type - ConnectionError
        self.assertIn("500: Error_Type - ConnectionError", str(result.exception))

    """ assert RequestException in mock_get result.exception """
    @patch('requests.get')
    def test_cli_main_requests_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException()
        result = self.runner.invoke(main, ['--url', 'https://example.com'])
        # result.exception: 400: Error_Type - RequestException
        self.assertIn("400: Error_Type - RequestException", str(result.exception))

    """
    FastAPI Test Client on API Router
    """
    """ assert status code 405 with get /api """
    def test_fastapi_api_get_error(self):
        result = self.client.get("/api")
        self.assertEqual(result.status_code, 405)

    """ assert api request with valid URL to result in success """
    def test_fastapi_api_post_success(self):
        result = self.client.post("/api", json={"url": "https://example.com"})
        self.assertEqual(result.status_code, 200)

    """ assert status code 422 with post /api """
    def test_fastapi_api_post_error_nojson(self):
        result = self.client.post("/api")
        result_text = json.loads(result.text)
        self.assertEqual(result.status_code, 422)
        self.assertEqual(result_text.get("Error"), "Invalid data - Field required")

    """ assert api request with empty URL to result in validation error """
    def test_fastapi_api_post_error_invalidjson(self):
        result = self.client.post("/api", json={"url": ""})
        result_text = json.loads(result.text)
        # result_text: {'Error': "Invalid data - (1) Expect data in JSON KV Pair Structure {'url': 'http(s)://xxxx'}"}
        self.assertIn("Expect data in JSON KV Pair Structure", str(result_text))

    """ assert api request with empty JSON data to result in validation error """
    def test_fastapi_api_post_error_nulljson(self):
        result = self.client.post("/api", json={})
        result_text = json.loads(result.text)
        # result_text: {'Error': "Invalid data - (2) Expect data in JSON KV Pair Structure {'url': 'http(s)://xxxx'}"}
        self.assertIn("Expect data in JSON KV Pair Structure", str(result_text))

    """
    FastAPI Test Client on Health Router
    """
    """ assert zero exit code with / to redirect to /health """
    def test_fastapi_health_success_redirect(self):
        result = self.client.get("/")
        self.assertEqual(result.status_code, 200)

    """ assert zero exit code with /health """
    def test_fastapi_health_success_direct(self):
        result = self.client.get("/health")
        self.assertEqual(result.status_code, 200)

    """
    FastAPI Test Client on Versions Router
    """
    """ assert zero exit code with /versions """
    def test_fastapi_url_versions(self):
        result = self.client.get("/versions")
        self.assertEqual(result.status_code, 200)

    """
    FastAPI Test Client on Info Router
    """
    """ assert healthy status with /info """
    def test_fastapi_url_info_healthy(self):
        result = self.client.get("/info")
        result_text = json.loads(result.text)
        # result_text: {"status":"healthy","system":{"cpu_usage":"3.1%","mem_usage":"63.3%",
        # "disk_usage":"12.6%","load_avg":{"1 min":"2.55","5 min":"2.67","15 min":"2.55"}}}
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result_text.get("status"), "healthy")

    """ assert warning status with /info """
    @patch('psutil.cpu_percent')
    def test_fastapi_url_info_warning(self, mock_cpu):
        mock_cpu.return_value = 96.0
        result = self.client.get("/info")
        result_text = json.loads(result.text)
        # result_text: {'status': 'warning', 'system': {'cpu_usage': '96.0%', 'mem_usage': '63.8%',
        # 'disk_usage': '12.6%', 'load_avg': {'1 min': '2.73', '5 min': '2.67', '15 min': '2.47'}}}
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result_text.get("status"), "warning")


if __name__ == "__main__":
    unittest.main()
