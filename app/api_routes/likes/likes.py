from typing import List

from fastapi import APIRouter, HTTPException
from sqlmodel import create_engine

from app.private_users.CRUD_like.helper_functions.already_liked_animal import already_liked
from app.private_users.CRUD_like.helper_functions.is_animal_present import animal_present
from app.private_users.CRUD_like.liked_animals_by_user import liked_animals_by_user
from app.private_users.CRUD_like.user_animal_dislike import dis_like
from app.private_users.CRUD_like.user_animal_like import like
from app.private_users.CRUD_user.helper_functions.does_user_exist import does_user_exist
from app.private_users.models import LikeDislikeModel, LikePrivateUser, LikePrivateUserResponse

router = APIRouter(
    prefix="/private_users_likes",
    tags=["Private Users - Likes"]

)

SQL_ALCHEMY_DATABASE_URL = 'postgresql://postgres:@localhost/postgres'
engine = create_engine(SQL_ALCHEMY_DATABASE_URL)


@router.post('/like_animal')
def f_like_animal(new_like: LikeDislikeModel):

    # Does user exist
    if does_user_exist(keycloak_id=new_like.keycloak_id, engine_=engine) == 'user does not exist':
        raise HTTPException(status_code=404, detail='user not exist')

    # Does animal exist
    if animal_present(animal_id=new_like.animal_id) == 'Animal does not exist':
        raise HTTPException(status_code=404, detail='Animal does not exist')

    # Purpose of this step is to make API more user friendly
    # Only necessary parameters can be typed in
    pair_ = LikePrivateUser()
    pair_.keycloak_id = new_like.keycloak_id
    pair_.animal_id = new_like.animal_id

    # Already liked animal
    if already_liked(user_animal_pair=pair_, engine_=engine) == 'User already liked this animal':
        raise HTTPException(status_code=404, detail='User already liked this animal')

    like(new_row=pair_, engine_=engine)

    return "like created"


@router.post('/dislike_animal')
def f_dislike_animal(new_dislike: LikeDislikeModel):

    if animal_present(animal_id=new_dislike.animal_id) == 'Animal does not exist':
        raise HTTPException(status_code=404, detail='Non existing animal')

    if does_user_exist(keycloak_id=new_dislike.keycloak_id, engine_=engine) == 'user does not exist':
        raise HTTPException(status_code=404, detail='Non existing user')

    # Purpose of this step is to make API more user friendly
    # Only necessary parameters can be typed in
    pair_ = LikePrivateUser()
    pair_.keycloak_id = new_dislike.keycloak_id
    pair_.animal_id = new_dislike.animal_id

    # Animal already liked by user. CHECK !!!
    if already_liked(user_animal_pair=pair_, engine_=engine) == 'User did not liked this animal!':
        raise HTTPException(status_code=404, detail="Can't be performed dislike. User didn't even liked that animal before")

    dis_like(new_row=pair_, engine_=engine)

    return "Animal disliked"


@router.get('/liked_animals_by_user', response_model=List[LikePrivateUserResponse])
def f_liked_animal_by_user(keycloak_id_: int):

    if does_user_exist(keycloak_id=keycloak_id_, engine_=engine) == 'user does not exist':
        raise HTTPException(status_code=404, detail='Non existing user')

    results = liked_animals_by_user(keycloak_id=keycloak_id_, engine_=engine)

    return results
