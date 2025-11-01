# modal_app.py
import modal
from app.main import create_app  # returns FastAPI instance
from modal import Image

# Name the app — helpful for modal app management & logs
APP_NAME = "sports-analytics-api"

# Create Modal App (deployment unit)
stub = modal.App(APP_NAME)

# Build image: minimal Debian + python deps installed from wheel/pip
image = (
    Image.debian_slim()
    .pip_install("fastapi[standard]", "uvicorn", "pydantic", "numpy", "scikit-learn")
    # add any extra libs like torch, transformers if needed
)

# If you need a GPU, use modal.GpuSpec("A10G", count=1) or image that has CUDA libs (Modal supports GPU images)
# See docs for GPU options if you plan to run heavy inference.

# Attach secrets (must be created with `modal secret create` or via dashboard)
SECRETS = ["MY_API_KEYS"]

# Expose FastAPI as an asgi app
@stub.asgi_app(image=image, secrets=SECRETS)
def fastapi_app():
    # create_app constructs the FastAPI application and wiring
    return create_app()
