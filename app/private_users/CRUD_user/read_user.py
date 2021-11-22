from sqlmodel import SQLModel, select, Session, create_engine

# from app.private_users.CRUD_user.helper_functions.does_user_exist import does_user_exist
from app.private_users.models import PrivateUser

# SQL_ALCHEMY_DATABASE_URL = 'postgresql://postgres:@localhost/postgres'
# engine = create_engine(SQL_ALCHEMY_DATABASE_URL)


def read_user(keycloak_id, engine_):

    """
    :param keycloak_id:
    :type keycloak_id:
    :param engine_:
    :type engine_:
    :return:
    :rtype:

    If user exists - return user.

    If user doesnt exist, return that information.

    """

    # if does_user_exist(keycloak_id) == 'user does not exist':
    #     return 'user not exist'

    with Session(engine_) as session:
        statement = select(PrivateUser).where(PrivateUser.keycloak_id == keycloak_id)
        result = session.execute(statement)
        found_user = result.first()[0]
        return found_user




