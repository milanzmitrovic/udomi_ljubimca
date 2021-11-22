
from app.private_users.CRUD_like.user_animal_like import like
from app.private_users.models import LikePrivateUser


new_combination = LikePrivateUser(animal_id=6, keycloak_id=11122)

like(new_row=new_combination)

