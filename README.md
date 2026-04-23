\# Stage 2 DevOps — Job Processing System



This is my Stage 2 HNG DevOps submission. The app is a simple job processing system

with three services talking to each other through Redis. I containerized everything,

wired it up with Docker Compose, and built a full CI/CD pipeline with GitHub Actions.



\---



\## What's Running



\- \*\*Frontend\*\* — Node.js app where you submit and track jobs (port 3000)

\- \*\*API\*\* — FastAPI service that creates jobs and serves status (port 8000 internal)

\- \*\*Worker\*\* — Python process that picks jobs off the queue and processes them

\- \*\*Redis\*\* — The queue sitting between the API and worker (internal only, not exposed)



\---



\## Prerequisites



\- Docker Desktop (make sure it's actually running before you start)

\- Git



\---



\## How to Run It



Clone the repo:



```bash

git clone https://github.com/kehlany/hng14-stage2-devops.git

cd hng14-stage2-devops

```



Set up your environment:



```bash

cp .env.example .env

```



Open `.env` and set your Redis password — don't leave it as the placeholder.



Start everything:



```bash

docker compose up --build

```



Wait for all 4 services to show as healthy, then open your browser at:http://localhost:3000



Hit \*\*Submit New Job\*\*. You'll see it go from `queued` to `completed` in a few seconds.

That means the frontend, API, worker and Redis are all talking correctly.



\---



\## Running the Tests



```bash

cd api

pip install -r requirements.txt

pytest tests/ -v --cov=. --cov-report=term

```



\---



\## Stopping Everything



```bash

docker compose down -v

```



\---



\## Environment Variables



| Variable | What it's for |

|---|---|

| REDIS\_HOST | Hostname for Redis — keep it as `redis` |

| REDIS\_PORT | Redis port — default 6379 |

| REDIS\_PASSWORD | Password for Redis auth |

| API\_URL | How the frontend reaches the API internally |



\---



\## Pipeline



GitHub Actions runs 6 stages in order — lint, test, build, security scan,

integration test, and deploy. If any stage fails, everything after it is skipped.

The deploy stage only runs on pushes to main and does a rolling update,

meaning the new container has to pass its health check before the old one is stopped.

