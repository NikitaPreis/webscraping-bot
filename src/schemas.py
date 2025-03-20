from pydantic import BaseModel, HttpUrl, field_validator


class WebResourceCreateSchema(BaseModel):
    """Schema of web resources for scraping."""

    title: str
    url: str
    xpath: str

    class Config:
        from_attributes = True

    @field_validator('url')
    def validate_url(cls, value):
        HttpUrl(url=value)
        return value
