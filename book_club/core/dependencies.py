from sqlalchemy.orm import Session
from book_club.core.data_base import DB_Session


def get_session() -> Session:
    try:
        session: Session = DB_Session()
    finally:
        return session
