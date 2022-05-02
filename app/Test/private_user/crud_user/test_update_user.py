
from main import engine
# from sqlmodel import create_engine

from app.private_users.CRUD_user.update_user import update_user
from app.private_users.models import PrivateUser


# SQL_ALCHEMY_DATABASE_URL = 'postgresql://postgres:@localhost/postgres'
# engine = create_engine(SQL_ALCHEMY_DATABASE_URL)


p = PrivateUser(keycloak_id=11122, name='111 uuuuuxxxxxxxuuu', surname='222', username='333', email='444')
update_user(p, engine_=engine)

print(p)


