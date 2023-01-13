from app.models.schemas.recipes import Recipe


class RecipesAPIClient:
    def prepare_url(self, **params) -> str:
        ...

    async def parse_recipes(
        self, credentials: dict[str, str], words: list[str] | tuple[str]
    ) -> list[Recipe]:
        ...
