from app.core.config import get_app_settings
from app.services.recipes_parsing.types import RecipesAPIClient
from app.services.ai_model.app import detect
from app.models.schemas.recipes import (
    DetectedIngredient,
    FoodstuffRecognitionResponse,
)

settings = get_app_settings()


def get_foodstuff_scanner():
    return FoodstuffDetector()


class FoodstuffDetector:
    async def detect(
        self,
        image: bytes,
        parser: RecipesAPIClient,
    ):
        detected_objects_dict, _ = detect(image)

        recipes = await parser.parse_recipes(
            credentials={
                "app_id": settings.recipes_api_id,
                "app_key": settings.recipes_api_token,
            },
            words=tuple(detected_objects_dict.keys()),
        )
        return FoodstuffRecognitionResponse(
            detected_ingredients=[
                DetectedIngredient(label=label, count=count)
                for label, count in detected_objects_dict.items()
            ],
            recipes_count=len(recipes),
            recipes=recipes,
        )
