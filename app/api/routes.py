# app/api/routes.py
from fastapi import APIRouter, Depends, Request, HTTPException
from pydantic import BaseModel

router = APIRouter()

class InferenceRequest(BaseModel):
    text: str

class InferenceResponse(BaseModel):
    score: float
    meta: dict

@router.post("/infer", response_model=InferenceResponse)
async def infer(req: InferenceRequest, request: Request):
    model_service = request.app.state.model_service
    if not model_service.is_ready():
        raise HTTPException(status_code=503, detail="Model not ready")
    result = await model_service.infer(req.text)
    return {"score": result["score"], "meta": result.get("meta", {})}

@router.get("/health")
async def health(request: Request):
    ms = request.app.state.model_service
    return {"status": "ok", "model_loaded": ms.is_ready()}
