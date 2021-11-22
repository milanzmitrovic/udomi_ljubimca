
from sqlmodel import create_engine, Session, select
from app.private_users.models import PrivateUser

SQL_ALCHEMY_DATABASE_URL = 'postgresql://postgres:@localhost/postgres'
engine = create_engine(SQL_ALCHEMY_DATABASE_URL)


def does_user_exist(keycloak_id: int, engine_):

    """

    We are checking if there is active user.

    Active user = user that has not been deleted in past.

    :param keycloak_id, engine_:
    :type keycloak_id:
    :return:
    :rtype:
    """

    with Session(engine_) as session1:

        statement = select(PrivateUser).where(PrivateUser.keycloak_id == keycloak_id).where(PrivateUser.is_active == 1)
        result = session1.execute(statement)
        found_user = result.first()

        if found_user is not None:
            return 'user exist'
        else:
            return 'user does not exist'


def does_user_exist_active_or_not(keycloak_id: int, engine_):
    """
    This is only used for creating user.
    Keycloak_ID should be not present in database, now or earlier.

    If there is deleted user (active_status = 0), there shouldn't be created new user
    with same keycloak_id.


    :param keycloak_id, engine_:

    :type keycloak_id:
    :return:
    :rtype:
    """

    with Session(engine_) as session:

        statement = select(PrivateUser).where(PrivateUser.keycloak_id == keycloak_id)
        result = session.execute(statement)
        found_user = result.first()

        if found_user is not None:
            return 'user exist'
        else:
            return 'user does not exist'




