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


class TestCLI(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def test_cli_main_success(self):
        result = self.runner.invoke(main, ['--url', 'https://example.com'])
        self.assertEqual(result.exit_code, 0)
        self.assertIsNone(result.exception)

    def test_cli_main_validate_error(self):
        result = self.runner.invoke(main, ['--url', 'https://iamnotarobotdot.ai'])
        self.assertNotEqual(result.exit_code, 0)

    def test_cli_main_http_error(self):
        result = self.runner.invoke(main, ['--url', 'https://example.com/thepathdoesnotexist'])
        self.assertIn("HTTPError", str(result.exception))
        self.assertNotEqual(result.exit_code, 0)

    @patch('pkg_15903.core.cls_requests.requests.get')
    def test_cli_main_connection_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.ConnectionError()
        result = self.runner.invoke(main, ['--url', 'https://example.com'])
        self.assertIn("500: Error_Type - ConnectionError", str(result.exception))
        self.assertNotEqual(result.exit_code, 0)

    @patch('pkg_15903.core.cls_requests.requests.get')
    def test_cli_main_requests_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException()
        result = self.runner.invoke(main, ['--url', 'https://example.com'])
        self.assertIn("400: Error_Type - RequestException", str(result.exception))
        self.assertNotEqual(result.exit_code, 0)


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_fastapi_api_get_error(self):
        result = self.client.get("/api")
        self.assertEqual(result.status_code, 405)

    def test_fastapi_api_post_success(self):
        result = self.client.post("/api", json={"url": "https://example.com"})
        self.assertEqual(result.status_code, 200)

    def test_fastapi_api_post_error_nojson(self):
        result = self.client.post("/api")
        result_text = json.loads(result.text)
        error_message = result_text.get("Error", "")
        self.assertEqual(result.status_code, 422)
        self.assertIn("Invalid data - Field required", error_message)
        self.assertIn("application/json", result.headers.get("content-type", ""))

    def test_fastapi_api_post_error_emptyurlvalue(self):
        result = self.client.post("/api", json={"url": ""})
        result_text = json.loads(result.text)
        # result_text: {'Error': "Invalid data - (1) Expect data in JSON KV Pair Structure {'url': 'http(s)://xxxx'}"}
        self.assertEqual(result.status_code, 422)
        self.assertIn("Expect data in JSON KV Pair Structure", str(result_text))

    def test_fastapi_api_post_error_nulljson(self):
        result = self.client.post("/api", json={})
        result_text = json.loads(result.text)
        # result_text: {'Error': "Invalid data - (2) Expect data in JSON KV Pair Structure {'url': 'http(s)://xxxx'}"}
        self.assertEqual(result.status_code, 422)
        self.assertIn("Expect data in JSON KV Pair Structure", str(result_text))

    # FastAPI Test Client on Health Router
    def test_fastapi_health_success_redirect(self):
        result = self.client.get("/")
        self.assertEqual(result.status_code, 200)

    def test_fastapi_health_success_direct(self):
        result = self.client.get("/health")
        self.assertEqual(result.status_code, 200)

    # FastAPI Test Client on Versions Router
    def test_fastapi_versions(self):
        result = self.client.get("/versions")
        self.assertEqual(result.status_code, 200)

    # FastAPI Test Client on Info Router
    def test_fastapi_info_healthy(self):
        result = self.client.get("/info")
        result_text = json.loads(result.text)
        # result_text: {"status":"healthy","system":{"cpu_usage":"3.1%","mem_usage":"63.3%",
        # "disk_usage":"12.6%","load_avg":{"1 min":"2.55","5 min":"2.67","15 min":"2.55"}}}
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result_text.get("status"), "healthy")

    @patch('psutil.cpu_percent')
    def test_fastapi_info_warning(self, mock_cpu):
        mock_cpu.return_value = 96.0
        result = self.client.get("/info")
        result_text = json.loads(result.text)
        # result_text: {'status': 'warning', 'system': {'cpu_usage': '96.0%', 'mem_usage': '63.8%',
        # 'disk_usage': '12.6%', 'load_avg': {'1 min': '2.73', '5 min': '2.67', '15 min': '2.47'}}}
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result_text.get("status"), "warning")


if __name__ == "__main__":
    unittest.main()
