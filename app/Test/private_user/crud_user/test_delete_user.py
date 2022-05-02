
from main import engine
from app.private_users.CRUD_user.delete_user import delete_user


# SQL_ALCHEMY_DATABASE_URL = 'postgresql://postgres:@localhost/postgres'
# engine = create_engine(SQL_ALCHEMY_DATABASE_URL)


delete_user(keycloak_id_=1112, engine_=engine)



