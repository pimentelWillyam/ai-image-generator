from fastapi import APIRouter
from app.schemas.image_schema import ImageRequest
from app.services.image_service import ImageService
from fastapi.responses import StreamingResponse
import io

router = APIRouter()

image_service = ImageService()


@router.post("/generate")
def generate_image(data: ImageRequest):

    image = image_service.generate(data.prompt)

    img_bytes = io.BytesIO()
    image.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    return StreamingResponse(img_bytes, media_type="image/png")