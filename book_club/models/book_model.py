from sqlalchemy import Column, Integer, String, Float, Boolean
from book_club.core.config import settings
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    ...


class BookModel(Base):
    __tablename__ = settings.TABLE_NAME

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    title: str = Column(String(256))
    stars: int = Column(Integer)
    price: float = Column(Float)
    is_available: bool = Column(Boolean)
    category: str = Column(String(128))

    def __repr__(self) -> str:
        return f"{self.title}"
