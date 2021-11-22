
# from app.main import engine
from app.private_users.CRUD_user.create_user import create_user
from app.private_users.models import PrivateUser
from sqlmodel import create_engine


SQL_ALCHEMY_DATABASE_URL = 'postgresql://postgres:@localhost/postgres'
engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

f = PrivateUser(keycloak_id=11122, name='qqqq', surname='eee',username='qwqw', email='fffddd')


create_user(f, engine_=engine)



