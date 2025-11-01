# ModalBoilerplate
Comperhansive boillerplace code for modal deploynment - LLM Inference.


## How to manage secrets

Create secrets in Modal dashboard or with CLI: modal secret create MY_API_KEYS KEY=VALUE. Then reference them in your `stub.asgi_app(..., secrets=[...])`. Modal injects them into the container as env vars and they are not stored in repo.

## Health, monitoring & logs
Modal collects logs per app; view with `modal app logs <name> and use modal app rollback` to revert a broken deployment. Add structured logs and emit metrics (Prometheus pushgateway or a cloud metrics API) inside inference path.

## Rollback & versioning
Modal records deployment history. Use `modal app history and modal app rollback <deploy-id>` to switch back if needed. Align your model versions with MODEL_VERSION env var and include model checksum in release notes. 
Modal

## Local dev vs Modal container caveats
For local dev, uvicorn `app.main:create_app --reload` works but remember environment parity (Python versions / dependency versions). For Modal, you supply `Image.debian_slim().pip_install(...)` — this becomes the runtime image, so ensure everything your code needs is installed there.

## Quick checklist to productionize further (practical)
- Add integration tests that spin up the whole app (run in CI).

- Add real model loading with lazy caching and threadpooling for blocking libs.

- Add request tracing (open-telemetry) and metrics (latency, success rate, error count).

- Add rate limiting & auth (JWT, API key) at FastAPI level or via API gateway.

- Add rollback playbook & automated canary deploys (Modal supports staged deploy patterns; implement in CI).

- Add automated model validation (smoke tests for each model version before traffic).

## Sources / docs used
- Modal deploy / CLI docs. 

- Modal FastAPI / web endpoints guide (ASGI lifespan, fastapi examples). 

- Modal Secrets & environment variables. 

- Modal app management & logs / rollback. 

- Modal CI/CD guidance (GitHub Actions). 