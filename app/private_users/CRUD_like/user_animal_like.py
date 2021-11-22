
from sqlmodel import Session
# from app.private_users.CRUD_like.helper_functions.already_liked_animal import already_liked
from app.private_users.models import LikePrivateUser

# from app.private_users.CRUD_like.helper_functions.is_animal_present import animal_present

# from app.private_users.CRUD_user.helper_functions.does_user_exist import does_user_exist


def like(new_row: LikePrivateUser, engine_):

    # if animal_present(animal_id=new_row.animal_id) == 'Animal does not exist':
    #     return 'Non existing animal'

    # if does_user_exist(keycloak_id=new_row.keycloak_id) == 'user does not exist':
    #     return 'Non existing user'
    #
    # # Already liked CHECK !!!
    # if already_liked(new_row) == 'User already liked this animal':
    #     return "Like can't be performed. User already liked that animal"

    with Session(engine_) as session:
        session.add(new_row)
        session.commit()





