from pydantic import BaseModel, BaseConfig, HttpUrl, Field

from app.utils import convert_field_to_camel_case


class DetectedIngredient(BaseModel):
    label: str
    count: int = Field(..., alias="ingredientCount")

    class Config(BaseConfig):
        allow_population_by_field_name = True


class Recipe(BaseModel):
    label: str
    image: HttpUrl
    url: HttpUrl
    ingredientLines: list[str]
    calories: float
    totalWeight: float
    mealType: list[str]


class FoodstuffRecognitionResponse(BaseModel):
    detected_ingredients: list[DetectedIngredient]
    recipes_count: int
    recipes: list[Recipe]

    class Config(BaseConfig):
        alias_generator = convert_field_to_camel_case
        allow_population_by_field_name = True
