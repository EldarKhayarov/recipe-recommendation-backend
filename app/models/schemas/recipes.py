from pydantic import BaseModel, HttpUrl


class RecognizedIngredient(BaseModel):
    label: str
    count: int


class Recipe(BaseModel):
    label: str
    image: HttpUrl
    url: HttpUrl
    ingredientLines: list[str]
    calories: float
    totalWeight: float
    mealType: list[str]


class FoodstuffRecognitionResponse(BaseModel):
    recognized_ingredients: list[RecognizedIngredient]
    recipes_count: int
    recipes: list[Recipe]
