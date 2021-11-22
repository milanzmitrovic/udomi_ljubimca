
from app.private_users.CRUD_like.user_animal_dislike import dis_like
from app.private_users.models import LikePrivateUser

new_pair = LikePrivateUser(animal_id=6, keycloak_id=11122)


dis_like(new_row=new_pair)

