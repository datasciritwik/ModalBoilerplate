# app/services/model_service.py
import asyncio
import os
import logging

logger = logging.getLogger(__name__)

class ModelService:
    def __init__(self):
        self._ready = False
        self._model = None
        self._lock = asyncio.Lock()

    async def load_model(self):
        async with self._lock:
            if self._ready:
                return
            logger.info("Loading model into container...")
            # Example: load a small sklearn object, or a transformer
            # For demo, we simulate load delay. Replace with real model load.
            await asyncio.sleep(1)
            self._model = {"version": os.getenv("MODEL_VERSION", "v1")}
            self._ready = True
            logger.info("Model loaded.")

    def is_ready(self):
        return self._ready

    async def infer(self, text: str):
        # Keep inference synchronous if using CPU libs; wrap in threadpool if blocking
        if not self._ready:
            raise RuntimeError("Model not ready")
        # Replace with actual inference logic; keep it small and safe
        # Example dummy score:
        score = float(len(text)) % 100 / 100.0
        return {"score": score, "meta": {"model_version": self._model["version"]}}

    async def cleanup(self):
        logger.info("Cleaning up model resources")
        self._model = None
        self._ready = False
