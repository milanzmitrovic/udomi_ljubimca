

from sqlmodel import SQLModel, Session, select, create_engine

from app.private_users.models import PrivateUser

from app.private_users.CRUD_user.helper_functions.does_user_exist import does_user_exist

SQL_ALCHEMY_DATABASE_URL = 'postgresql://postgres:@localhost/postgres'

engine = create_engine(SQL_ALCHEMY_DATABASE_URL)


def delete_user(keycloak_id_, engine_):

    """
    :param keycloak_id_:
    :type keycloak_id_:
    :param engine_:
    :type engine_:
    :return:
    :rtype:

    Check if user exist.

        If exist, delete user.

        If doesn't exist, return that information.

    """

    # if does_user_exist(keycloak_id_) == 'user does not exist':
    #     return 'user not exist'

    with Session(engine_) as session:
        statement = select(PrivateUser).where(PrivateUser.keycloak_id == keycloak_id_)
        old_user = session.exec(statement).one()

        old_user.is_active = 0

        session.add(old_user)
        session.commit()
        session.refresh(old_user)

    return old_user




