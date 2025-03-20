from typing import Any

from sqlalchemy.orm import (
    DeclarativeBase, declared_attr, Mapped, mapped_column
)


class Base(DeclarativeBase):
    id: Any
    __name__: str

    __allow_unmapped__ = True

    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()


class WebScrapingResource(Base):
    __tablename__ = 'web_scraping_resources'

    id: Mapped[int] = mapped_column(
        primary_key=True, nullable=False, unique=True
    )
    title: Mapped[str]
    url: Mapped[str]
    xpath: Mapped[str]
