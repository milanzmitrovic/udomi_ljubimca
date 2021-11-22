
# from app.private_users.CRUD_user.helper_functions.does_user_exist import does_user_exist_active_or_not
from app.private_users.models import PrivateUser
from sqlmodel import Session


def create_user(private_user: PrivateUser, engine_):

    """
    :param private_user:
    :type private_user:
    :param engine_:
    :type engine_:
    :return:
    :rtype:

    Check if user already exists.

        If exist, return that info.

        If not exist,

    """

    # if does_user_exist_active_or_not(private_user.keycloak_id) == 'user exist':
    #     return 'user already exist'

    with Session(engine_) as session:
        user_1 = private_user

        session.add(user_1)

        session.commit()



