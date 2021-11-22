from typing import List

from fastapi import APIRouter, HTTPException
from sqlmodel import create_engine

from app.private_users.CRUD_user.create_user import create_user
from app.private_users.CRUD_user.delete_user import delete_user
from app.private_users.CRUD_user.helper_functions.does_city_exist import does_city_exist
from app.private_users.CRUD_user.helper_functions.does_user_exist import does_user_exist_active_or_not, does_user_exist
from app.private_users.CRUD_user.read_user import read_user
from app.private_users.CRUD_user.update_user import update_user
from app.private_users.models import PrivateUser, PrivateUserUpdate, PrivateUserCreate


router = APIRouter(
    prefix="/private_users",
    tags=["Private Users"]

)

SQL_ALCHEMY_DATABASE_URL = 'postgresql://postgres:@localhost/postgres'
engine = create_engine(SQL_ALCHEMY_DATABASE_URL)


@router.post('/create_private_user')
def f_create_private_user(new_user: PrivateUserCreate):

    if does_user_exist_active_or_not(keycloak_id=new_user.keycloak_id, engine_=engine) == 'user exist':
        raise HTTPException(status_code=404, detail='user already exist')

    if len(new_user.email) > 50:
        raise HTTPException(status_code=404, detail="Length of email is too long.")

    if len(str(new_user.keycloak_id)) > 100:
        raise HTTPException(status_code=404, detail="Length of keycloak_id is too long")

    if len(new_user.username) > 50:
        raise HTTPException(status_code=404, detail="Length of username is too long.")

    if len(new_user.name) > 50:
        raise HTTPException(status_code=404, detail="Length of name is too long.")

    if len(new_user.surname) > 50:
        raise HTTPException(status_code=404, detail="Length of surname is too long.")

    # Purpose of this step is to make API more user friendly
    # Only necessary parameters can be typed in
    user_ = PrivateUser()
    user_.keycloak_id = new_user.keycloak_id
    user_.name = new_user.name
    user_.surname = new_user.surname
    user_.username = new_user.username
    user_.email = new_user.email

    create_user(private_user=user_, engine_=engine)
    return "user created"


@router.get('/read_private_user', response_model=PrivateUser)
def f_read_private_user(keycloak_id: int):

    if does_user_exist(keycloak_id=keycloak_id, engine_=engine) == 'user does not exist':
        raise HTTPException(status_code=404, detail='user not exist')

    user = read_user(keycloak_id=keycloak_id, engine_=engine)
    return user


@router.put('/update_private_user')
def f_update_private_user(existing_user: PrivateUserUpdate):
    if does_city_exist(city_id_=existing_user.city_id, engine_=engine) == 'City does not exist':
        raise HTTPException(status_code=404, detail='City does not exist')

    if does_user_exist(keycloak_id=existing_user.keycloak_id, engine_=engine) == 'user does not exist':
        raise HTTPException(status_code=404, detail='user not exist')

    #
    if len(existing_user.email) > 50:
        raise HTTPException(status_code=404, detail="Length of email is too long.")

    if len(str(existing_user.keycloak_id)) > 100:
        raise HTTPException(status_code=404, detail="Length of keycloak_id is too long")

    if len(existing_user.username) > 50:
        raise HTTPException(status_code=404, detail="Length of username is too long.")

    if len(existing_user.name) > 50:
        raise HTTPException(status_code=404, detail="Length of name is too long.")

    if len(existing_user.surname) > 50:
        raise HTTPException(status_code=404, detail="Length of surname is too long.")

    if len(existing_user.about_me) > 500:
        raise HTTPException(status_code=404, detail="Length of about me value is too long.")

    # Purpose of this step is to make API more user friendly
    # Only necessary parameters can be typed in
    user_ = PrivateUser()
    user_.keycloak_id = existing_user.keycloak_id
    user_.name = existing_user.name
    user_.surname = existing_user.surname
    user_.username = existing_user.username
    user_.email = existing_user.email

    user_.city_id = existing_user.city_id
    user_.about_me = existing_user.about_me
    user_.date_of_birth = existing_user.date_of_birth

    update_user(user=user_, engine_=engine)
    return f'User with keycloak_id {existing_user.keycloak_id} has been updated.'


@router.delete('/delete_private_user')
def f_delete_private_user(keycloak_id: int):
    if does_user_exist(keycloak_id=keycloak_id, engine_=engine) == 'user does not exist':
        raise HTTPException(status_code=404, detail='user not exist')
    delete_user(keycloak_id_=keycloak_id, engine_=engine)
    return f"User with keycloak_id {keycloak_id} has been deleted"
