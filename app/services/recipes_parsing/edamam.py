from typing import Any, Tuple
from urllib import parse

from aiohttp import ClientSession
from aiohttp.http_exceptions import HttpProcessingError
from starlette import status
from pydantic import BaseModel

from app.models.schemas.recipes import Recipe
from app.services.recipes_parsing.types import RecipesAPIClient


EDAMAM_RECIPES_SEARCH_URL = "https://api.edamam.com/api/recipes/v2"


def get_recipes_api_client():
    return EdamamAPIClient()


# def dict_to_pydantic_instance(pydantic_model: BaseModel, root_key: str | None = None) -> callable:
#     if root_key:
#
#     def func(instance_dict: dict) -> BaseModel:
#         return pydantic_model(**instance_dict)
#
#     return func


class EdamamAPIClient(RecipesAPIClient):
    async def make_request(self, url: str) -> Tuple[int, dict[Any]]:
        async with ClientSession() as session:
            async with session.get(url) as resp:
                return resp.status, await resp.json()

    async def parse_recipes(
        self, credentials: dict[str, str], words: list[str] | tuple[str]
    ) -> list[Recipe]:
        url = f"{EDAMAM_RECIPES_SEARCH_URL}?{self.prepare_url(q=' '.join(words), type='public', **credentials)}"
        status_code, response = await self.make_request(url)
        # from loguru import logger

        # logger.warning(f"{response[0].keys()} :: {response[0]}")

        if status_code == status.HTTP_200_OK:
            return [Recipe(**rsp_recipe["recipe"]) for rsp_recipe in response["hits"]]

        raise HttpProcessingError(
            message=f"Status code: {status_code}; Body: {response}"
        )

    def prepare_url(self, **params) -> str:
        return parse.urlencode(params, quote_via=parse.quote)
