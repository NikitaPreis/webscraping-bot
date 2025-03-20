from dataclasses import dataclass
from typing import ValuesView

import pandas as pd
from pydantic import ValidationError

from src.exceptions import AllResourcesInvalidException
from src.models import WebScrapingResource
from src.repository import WebResourceRepository
from src.schemas import WebResourceCreateSchema


@dataclass
class WebScrapingService:
    """Service of web resources for scraping."""

    web_resource_repository: WebResourceRepository

    async def add_websites_for_scraping(
        self, excel_filepath: str
    ):
        """Get web resources data from excel file and add to db."""
        resources_data = await self._parse_excell_file(
            filepath=excel_filepath
        )
        resource_schemas = await self._validate_and_get_resource_schemas(
            data=resources_data
        )

        if not resource_schemas:
            raise AllResourcesInvalidException
        resource_models = await self._create_web_resource_models(
            resource_schemas=resource_schemas
        )

        await self.web_resource_repository.create_resources(
            resources=resource_models
        )
        return resource_schemas

    async def _parse_excell_file(
        self, filepath: str
    ) -> ValuesView[dict[str, str]]:
        """
        Get web resources data from excel file.
        """
        df = pd.read_excel(filepath)
        return df.T.to_dict('dict').values()

    async def _validate_and_get_resource_schemas(
        self, data: ValuesView,
    ):
        """
        Validate web resources data and create schemas.
        """
        schemas = []

        for data_value in data:
            try:
                current_schema = WebResourceCreateSchema(
                    title=data_value['title'],
                    url=data_value['url'],
                    xpath=data_value['xpath']
                )
                schemas.append(current_schema)
            except ValidationError:
                pass
        return schemas

    async def _create_web_resource_models(
        self, resource_schemas: list[WebResourceCreateSchema],
    ):
        """
        Validate web resources data and create models.
        """
        resource_models = []
        for resource_schema in resource_schemas:
            resource_model = WebScrapingResource(
                title=resource_schema.title,
                url=resource_schema.url,
                xpath=resource_schema.xpath
            )
            resource_models.append(resource_model)
        return resource_models
