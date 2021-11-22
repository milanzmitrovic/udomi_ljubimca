
# from app.main import engine
from app.private_users.CRUD_user.read_user import read_user
from sqlmodel import create_engine, Session, select

from app.private_users.models import PrivateUser


SQL_ALCHEMY_DATABASE_URL = 'postgresql://postgres:@localhost/postgres'
engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

user = read_user(77, engine)

print(user)
