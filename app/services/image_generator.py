import base64
from io import BytesIO
from typing import Optional

import torch
from diffusers import StableDiffusionPipeline


_pipeline: Optional[StableDiffusionPipeline] = None


def _get_pipeline() -> StableDiffusionPipeline:
    global _pipeline

    if _pipeline is None:
        _pipeline = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch.float16,
        )
        device = "cuda" if torch.cuda.is_available() else "cpu"
        _pipeline.to(device)

    return _pipeline


def generate_image_base64(prompt: str) -> str:
    pipeline = _get_pipeline()
    images = pipeline(prompt).images
    image = images[0]

    buffer = BytesIO()
    image.save(buffer, format="PNG")
    image_bytes = buffer.getvalue()

    return base64.b64encode(image_bytes).decode("utf-8")

