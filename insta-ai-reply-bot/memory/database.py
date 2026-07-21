from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from config import config


engine = create_engine(
    config.DATABASE_URL,
    pool_pre_ping=True
)


Session = sessionmaker(
    bind=engine
)


Base = declarative_base()


def get_session():

    return Session()