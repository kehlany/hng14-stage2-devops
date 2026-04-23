\# FIXES.md



All bugs found and fixed in the starter repository.



\---



\## Bug 1

\*\*File:\*\* `api/main.py`

\*\*Line:\*\* 6

\*\*Problem:\*\* Redis host hardcoded as `localhost` — fails inside Docker because services run in separate containers and cannot reach each other via localhost.

\*\*Fix:\*\* Replaced with `os.getenv("REDIS\_HOST", "redis")` to read from environment variable.



\---



\## Bug 2

\*\*File:\*\* `api/main.py`

\*\*Line:\*\* 6

\*\*Problem:\*\* Redis port hardcoded as `6379`.

\*\*Fix:\*\* Replaced with `int(os.getenv("REDIS\_PORT", 6379))` to read from environment variable.



\---



\## Bug 3

\*\*File:\*\* `api/main.py`

\*\*Line:\*\* 6

\*\*Problem:\*\* Redis connection had no password authentication despite `REDIS\_PASSWORD` being defined in the `.env` file.

\*\*Fix:\*\* Added `password=os.getenv("REDIS\_PASSWORD", None)` to the Redis connection.



\---



\## Bug 4

\*\*File:\*\* `api/main.py`

\*\*Line:\*\* N/A (missing)

\*\*Problem:\*\* No `/health` endpoint existed — required for Docker HEALTHCHECK to work.

\*\*Fix:\*\* Added a `/health` GET endpoint returning `{"status": "ok"}`.



\---



\## Bug 5

\*\*File:\*\* `worker/worker.py`

\*\*Line:\*\* 2

\*\*Problem:\*\* `import timeimport os` — two import statements merged on one line, causing a syntax error.

\*\*Fix:\*\* Split into two separate lines: `import time` and `import os`.



\---



\## Bug 6

\*\*File:\*\* `worker/worker.py`

\*\*Line:\*\* 4

\*\*Problem:\*\* Redis host hardcoded as `localhost` — same Docker networking issue as the API.

\*\*Fix:\*\* Replaced with `os.getenv("REDIS\_HOST", "redis")`.



\---



\## Bug 7

\*\*File:\*\* `worker/worker.py`

\*\*Line:\*\* 4

\*\*Problem:\*\* Redis port hardcoded as `6379`.

\*\*Fix:\*\* Replaced with `int(os.getenv("REDIS\_PORT", 6379))`.



\---



\## Bug 8

\*\*File:\*\* `worker/worker.py`

\*\*Line:\*\* 4

\*\*Problem:\*\* Redis connection had no password authentication.

\*\*Fix:\*\* Added `password=os.getenv("REDIS\_PASSWORD", None)` to the Redis connection.



\---



\## Bug 9

\*\*File:\*\* `worker/worker.py`

\*\*Line:\*\* N/A (missing)

\*\*Problem:\*\* `signal` was imported but never used — no graceful shutdown handler implemented. Worker would terminate abruptly on SIGTERM, potentially dropping jobs mid-process.

\*\*Fix:\*\* Implemented SIGTERM and SIGINT handlers using a `running` flag so the worker finishes the current job before stopping.



\---



\## Bug 10

\*\*File:\*\* `frontend/app.js`

\*\*Line:\*\* 5

\*\*Problem:\*\* `API\_URL` hardcoded as `http://localhost:8000` — fails inside Docker because the API runs in a separate container.

\*\*Fix:\*\* Replaced with `process.env.API\_URL || "http://api:8000"` to read from environment variable.



\---



\## Bug 11

\*\*File:\*\* `frontend/package.json`

\*\*Line:\*\* 13

\*\*Problem:\*\* Missing closing `}` — invalid JSON, causes `npm install` to fail entirely.

\*\*Fix:\*\* Added the missing closing `}`.



\---



\## Bug 12

\*\*File:\*\* `frontend/views/index.html`

\*\*Line:\*\* 44

\*\*Problem:\*\* `â€"` — UTF-8 encoding corruption of the em dash character.

\*\*Fix:\*\* Replaced with the correct `–` character.



\---



\## Bug 13

\*\*File:\*\* `api/.env`

\*\*Line:\*\* N/A

\*\*Problem:\*\* `.env` file containing credentials was committed to the repository — a critical security violation.

\*\*Fix:\*\* Removed from git tracking using `git rm --cached api/.env`, added `.env` to `.gitignore`.

