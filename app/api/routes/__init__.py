import json
import time
from pathlib import Path

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.image_generator import generate_image_base64


# region agent log
try:
    log_entry = {
        "sessionId": "a26327",
        "runId": "pre-fix",
        "hypothesisId": "H1",
        "location": "app/api/routes/__init__.py:1",
        "message": "routes module imported",
        "data": {},
        "timestamp": int(time.time() * 1000),
    }
    log_path = Path("debug-a26327.log")
    with log_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")
except Exception:
    # logging must not break app import
    pass
# endregion


router = APIRouter(prefix="/images", tags=["images"])


class GenerateRequest(BaseModel):
    prompt: str


class GenerateResponse(BaseModel):
    image_base64: str


@router.post("/generate", response_model=GenerateResponse)
async def generate(request: GenerateRequest) -> GenerateResponse:
    try:
        image_b64 = generate_image_base64(request.prompt)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    return GenerateResponse(image_base64=image_b64)