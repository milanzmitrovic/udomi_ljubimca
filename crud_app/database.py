from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_ALCHEMY_DATABASE_URL = 'postgres://postgres:@localhost/postgres'

engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

# This is kind of 'middle-man' class
# Database session has not yet been created at this moment
# It will be used later on, in the future, for creating independent sessions
# One session for one request
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

