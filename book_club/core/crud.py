from book_club.core.config import settings
from book_club.core.dependencies import get_session
from book_club.models.book_model import BookModel, Base
from sqlalchemy import select
from book_club.core.data_base import engine


def create_db() -> str:
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    return f"Table {settings.TABLE_NAME} created."


def insert_db(book: BookModel | list[BookModel]) -> str:
    print(book)
    with get_session() as session:
        match book:
            case BookModel():
                session.add(book)
            case list():
                session.add_all(book)
        session.commit()
    return book


def select_db(id: int | list[int]) -> str:
    session = get_session()
    match id:
        case int():
            return session.query(select(BookModel, BookModel.id.in_(id)))
        case list():
            return session.query(BookModel).filter(BookModel.id.in_(id)).all()
        case _:
            raise Exception(f"book with {id} not found.")

def num_rows() -> int:
    session = get_session()
    return session.query(BookModel).count()