from fastapi import APIRouter, Depends, File, UploadFile

from app.models.schemas.recipes import FoodstuffRecognitionResponse
from app.services.foodstuff_recognition import FoodstuffDetector, get_foodstuff_scanner
from app.services.recipes_parsing.edamam import EdamamAPIClient

router = APIRouter()


@router.post(
    "/detect",
    response_model=FoodstuffRecognitionResponse,
    name="recipes:foodstuff_scan",
)
async def post_detect_foodstuff(
    image: UploadFile = File(description="Image with foodstuff."),
    service: FoodstuffDetector = Depends(get_foodstuff_scanner),
):
    return await service.detect(image=image.file.read(), parser=EdamamAPIClient())
