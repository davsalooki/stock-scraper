from typing import Annotated

from fastapi.params import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///../db/stock-scraper.db", echo=True)  
Session = sessionmaker(bind=engine)

def get_session():
    # Context manager for closing session and autocommitting transactions
    with Session() as session, session.begin():
        yield session

SessionDep = Annotated[sessionmaker, Depends(get_session)]
