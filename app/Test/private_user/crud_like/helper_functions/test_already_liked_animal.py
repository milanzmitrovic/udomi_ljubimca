
from app.private_users.models import LikePrivateUser
from app.private_users.CRUD_like.helper_functions.already_liked_animal import already_liked


new_row = LikePrivateUser(animal_id=3, keycloak_id=11122)

already_liked(user_animal_pair=new_row)



