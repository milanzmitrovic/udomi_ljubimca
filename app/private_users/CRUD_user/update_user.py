
from sqlmodel import SQLModel, Session, select, create_engine

from app.private_users.CRUD_user.helper_functions.does_user_exist import does_user_exist
from app.private_users.models import PrivateUser

SQL_ALCHEMY_DATABASE_URL = 'postgresql://postgres:@localhost/postgres'

engine = create_engine(SQL_ALCHEMY_DATABASE_URL)


def update_user(user: PrivateUser, engine_):

    """
    :param user:
    :type user:
    :param engine_:
    :type engine_:
    :return:
    :rtype:

    Check is user exist.

        If exist, perform update.

        It doesn't exist, return that information.

    """

    # if does_user_exist(user.keycloak_id) == 'user does not exist':
    #     return 'user not exist'

    with Session(engine_) as session:
        statement = select(PrivateUser).where(PrivateUser.keycloak_id == user.keycloak_id)
        new_user = session.exec(statement).one()

        new_user.name = user.name
        new_user.surname = user.surname
        new_user.username = user.username
        new_user.email = user.email

        new_user.city_id = user.city_id
        new_user.about_me = user.about_me
        new_user.date_of_birth = user.date_of_birth

        # new_user.test_column = user.test_column

        session.add(new_user)
        session.commit()
        session.refresh(new_user)

    return new_user




