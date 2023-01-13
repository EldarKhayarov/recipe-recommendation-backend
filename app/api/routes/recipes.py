from fastapi import APIRouter, Depends, File, UploadFile

from app.models.schemas.recipes import FoodstuffRecognitionResponse
from app.services.foodstuff_recognition import FoodstuffScanner, get_foodstuff_scanner
from app.services.recipes_parsing.edamam import EdamamAPIClient

router = APIRouter()


@router.post(
    "/scan", response_model=FoodstuffRecognitionResponse, name="recipes:foodstuff_scan"
)
async def post_scan_foodstuff(
    image: UploadFile = File(description="Image with foodstuff."),
    service: FoodstuffScanner = Depends(get_foodstuff_scanner),
):
    return await service.scan(image=image.file.read(), parser=EdamamAPIClient())
