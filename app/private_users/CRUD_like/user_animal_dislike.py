
from sqlmodel import Session, select
# from app.private_users.CRUD_like.helper_functions.already_liked_animal import already_liked
from app.private_users.models import LikePrivateUser

# from app.private_users.CRUD_like.helper_functions.is_animal_present import animal_present

# from app.private_users.CRUD_user.helper_functions.does_user_exist import does_user_exist


def dis_like(new_row: LikePrivateUser, engine_):

    # if animal_present(animal_id=new_row.animal_id) == 'Animal does not exist':
    #     return 'Non existing animal'
    #
    # if does_user_exist(keycloak_id=new_row.keycloak_id) == 'user does not exist':
    #     return 'Non existing user'
    #
    # # Animal already liked by user. CHECK !!!
    # if already_liked(new_row) == 'User did not liked this animal!':
    #     return "Can't be performed dislike. User didn't even liked that animal before"

    with Session(engine_) as session:
        # session.add(new_row)
        statement = select(LikePrivateUser).where(LikePrivateUser.keycloak_id == new_row.keycloak_id).where(LikePrivateUser.animal_id == new_row.animal_id)
        results = session.exec(statement).one()

        session.delete(results)
        session.commit()




