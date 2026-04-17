# FastAPI Server App

## Run App...from CLI
### Get Help
```
(python-test) Mon Jan 1 01:01:01 ~ $ python src/pkg_15903/cli.py --help
Usage: cli.py [OPTIONS]

Options:
  --url CHK_URL  [required]
  --version      Show the version and exit.
  --help         Show this message and exit.
```

### Client Access
```
(python-test) Mon Jan 1 01:01:01 ~ $ python src/pkg_15903/cli.py --url https://example.com
Starting Requests...
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "checklinks", "_m": "cls_requests.py:26", "_d": "url: https://example.com, status: 200"}
```

<br>

## Start FastAPI Server App...from CLI
```
(python-test) Mon Jan 1 01:01:01 ~ $ python src/pkg_15903/main.py
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "bind_socket", "_m": "config.py:545", "_d": "Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)"}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "run", "_m": "multiprocess.py:148", "_d": "Started parent process [4881]"}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "_serve", "_m": "server.py:92", "_d": "Started server process [4883]"}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "_serve", "_m": "server.py:92", "_d": "Started server process [4886]"}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "_serve", "_m": "server.py:92", "_d": "Started server process [4884]"}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "_serve", "_m": "server.py:92", "_d": "Started server process [4885]"}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "startup", "_m": "on.py:48", "_d": "Waiting for application startup."}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "startup", "_m": "on.py:48", "_d": "Waiting for application startup."}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "startup", "_m": "on.py:48", "_d": "Waiting for application startup."}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "startup", "_m": "on.py:48", "_d": "Waiting for application startup."}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "startup", "_m": "on.py:62", "_d": "Application startup complete."}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "startup", "_m": "on.py:62", "_d": "Application startup complete."}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "startup", "_m": "on.py:62", "_d": "Application startup complete."}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "startup", "_m": "on.py:62", "_d": "Application startup complete."}
```

### Client Access
```
(python-test) Mon Jan 1 01:01:01 ~ $ curl http://localhost:8000/api
{"detail":"Method Not Allowed"}

(python-test) Mon Jan 1 01:01:01 ~ $ curl -X POST http://localhost:8000/api -H "Content-Type: application/json" -d '{"url": "https://example.com"}'
{"url":"https://example.com","status":"200"}

(python-test) Mon Jan 1 01:01:01 ~ $ curl -L http://localhost:8000
{"status":"ok"}

(python-test) Mon Jan 1 01:01:01 ~ $ curl http://localhost:8000/health
{"status":"ok"}
```

### Server Logs
```
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "send", "_m": "httptools_impl.py:484", "_d": "127.0.0.1:57667 - "GET /api HTTP/1.1" 405"}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "checklinks", "_m": "cls_requests.py:26", "_d": "url: https://example.com, status: 200"}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "send", "_m": "httptools_impl.py:484", "_d": "127.0.0.1:55938 - "POST /api HTTP/1.1" 200"}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "send", "_m": "httptools_impl.py:484", "_d": "127.0.0.1:57651 - "GET / HTTP/1.1" 307"}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "send", "_m": "httptools_impl.py:484", "_d": "127.0.0.1:57651 - "GET /health HTTP/1.1" 200"}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "send", "_m": "httptools_impl.py:484", "_d": "127.0.0.1:55947 - "GET /health HTTP/1.1" 200"}
```

<br>

## Start FastAPI Server App...from Docker
### Build and Run
```
docker buildx build --platform linux/amd64 -t py-slim:1.0.0 .
docker run --rm -d --name urltest -p 8000:8000/tcp py-slim:1.0.0
```

### Initial Server Logs
```
(python-test) Mon Jan 1 01:01:01 ~ $ docker logs urltest -f
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "bind_socket", "_m": "config.py:545", "_d": "Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)"}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "run", "_m": "multiprocess.py:148", "_d": "Started parent process [1]"}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "_serve", "_m": "server.py:92", "_d": "Started server process [10]"}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "startup", "_m": "on.py:48", "_d": "Waiting for application startup."}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "_serve", "_m": "server.py:92", "_d": "Started server process [9]"}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "startup", "_m": "on.py:62", "_d": "Application startup complete."}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "_serve", "_m": "server.py:92", "_d": "Started server process [8]"}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "startup", "_m": "on.py:48", "_d": "Waiting for application startup."}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "startup", "_m": "on.py:48", "_d": "Waiting for application startup."}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "startup", "_m": "on.py:62", "_d": "Application startup complete."}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "startup", "_m": "on.py:62", "_d": "Application startup complete."}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "_serve", "_m": "server.py:92", "_d": "Started server process [11]"}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "startup", "_m": "on.py:48", "_d": "Waiting for application startup."}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "startup", "_m": "on.py:62", "_d": "Application startup complete."}
```

### Client Access
```
(python-test) Mon Jan 1 01:01:01 ~ $ curl http://localhost:8000/api
{"detail":"Method Not Allowed"}

(python-test) Mon Jan 1 01:01:01 ~ $ curl -X POST http://localhost:8000/api -H "Content-Type: application/json" -d '{}'
{"Error":"Invalid data - (2) Expect data in JSON KV Pair Structure {'url': 'http(s)://xxxx'}"}

(python-test) Mon Jan 1 01:01:01 ~ $ curl -X POST http://localhost:8000/api -H "Content-Type: application/json" -d '{"url": "https://example.com"}'
{"url":"https://example.com","status":"200"}

(python-test) Mon Jan 1 01:01:01 ~ $ curl -L http://localhost:8000
{"status":"ok"}

(python-test) Mon Jan 1 01:01:01 ~ $ curl http://localhost:8000/health
{"status":"ok"}

(python-test) Mon Jan 1 01:01:01 ~ $ curl http://localhost:8000/info
{"status":"healthy","system":{"cpu_usage":"1.3%","mem_usage":"15.7%","disk_usage":"11.7%","load_avg":{"1 min":"0.32","5 min":"0.0664","15 min":"0.0215"}}}

(python-test) Mon Jan 1 01:01:01 ~ $ curl http://localhost:8000/versions
{"versions":{"apitest":"0.1.100","fastapi":"0.135.3"}}
```

### Server Logs
```
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "send", "_m": "httptools_impl.py:484", "_d": "127.0.0.1:57667 - "GET /api HTTP/1.1" 405"}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "send", "_m": "httptools_impl.py:484", "_d": "172.17.0.1:52610 - "POST /api HTTP/1.1" 422"}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "checklinks", "_m": "cls_requests.py:26", "_d": "url: https://example.com, status: 200"}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "send", "_m": "httptools_impl.py:484", "_d": "172.17.0.1:44008 - "POST /api HTTP/1.1" 200"}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "send", "_m": "httptools_impl.py:484", "_d": "127.0.0.1:57651 - "GET / HTTP/1.1" 307"}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "send", "_m": "httptools_impl.py:484", "_d": "127.0.0.1:57651 - "GET /health HTTP/1.1" 200"}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "send", "_m": "httptools_impl.py:484", "_d": "172.17.0.1:53766 - "GET /health HTTP/1.1" 200"}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "send", "_m": "httptools_impl.py:484", "_d": "172.17.0.1:39034 - "GET /info HTTP/1.1" 200"}
{"_t": "2026-01-01 01:01:01.010", "_l": "INFO", "_f": "send", "_m": "httptools_impl.py:484", "_d": "172.17.0.1:60530 - "GET /versions HTTP/1.1" 200"}
```
