from src import text
from src.schemas import WebResourceCreateSchema


def get_added_resources_text(
    web_resources: list[WebResourceCreateSchema]
):
    """Generate message text with successfully processed sites."""

    added_resources = ''
    for index, resource in enumerate(web_resources, start=1):
        added_resources += text.added_resouce.format(
            index=index,
            title=resource.title,
            url=resource.url,
            xpath=resource.xpath
        )
    return text.add_resources_start_message + added_resources
