from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine, Engine
from book_club.core.config import settings

engine: Engine = create_engine(settings.db_url, echo=True)

DB_Session: Session = sessionmaker(
    autocommit=False, autoflush=False, class_=Session, bind=engine
)

db_session = DB_Session()
