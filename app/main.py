

# Napraviti posebnu schema-u za create_user *** *** ***

# Posebna šema za update (is_active should not exist, created_date also) *****

# Varchar(1000) ***

# Autoincrement


import os
import sys
from typing import List

import uvicorn
from sqlmodel import create_engine
from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Session, select

cwd = os.getcwd()
sys.path.append(cwd)

from app.animal_associations.CRUD_association.create_association import create_animal_association
from app.animal_associations.CRUD_association.delete_association import delete_animal_association
from app.animal_associations.CRUD_association.helper_functions.does_association_exist import \
    does_animal_association_exist, does_animal_association_exist_active_or_not
from app.animal_associations.CRUD_association.read_association import read_animal_association
from app.animal_associations.CRUD_association.update_association import update_animal_association
from app.private_users.CRUD_like.helper_functions.already_liked_animal import already_liked
from app.private_users.CRUD_like.helper_functions.is_animal_present import animal_present
from app.private_users.CRUD_like.liked_animals_by_user import liked_animals_by_user
from app.private_users.CRUD_like.user_animal_dislike import dis_like
from app.private_users.CRUD_like.user_animal_like import like
from app.private_users.CRUD_user.create_user import create_user
from app.private_users.CRUD_user.delete_user import delete_user
from app.private_users.CRUD_user.helper_functions.does_city_exist import does_city_exist
from app.private_users.CRUD_user.helper_functions.does_user_exist import does_user_exist_active_or_not, does_user_exist
from app.private_users.CRUD_user.read_user import read_user
from app.private_users.CRUD_user.update_user import update_user
from app.private_users.models import PrivateUser, LikePrivateUser, City, LikePrivateUserResponse, AnimalAssociation, \
    PrivateUserCreate, PrivateUserUpdate, LikeDislikeModel, AnimalAssociationCreate, AnimalAssociationUpdate

# cwd = os.getcwd()
# sys.path.append(cwd)

from app.private_users.models import PrivateUser

from app.api_routes.private_user import private_users
from app.api_routes.likes import likes
from app.api_routes.animal_association import animal_association

app = FastAPI()

app.include_router(private_users.router)
app.include_router(likes.router)
app.include_router(animal_association.router)

# ----------------------------------------------------------------------


# ----------------------------------------------------------------------

#
# @app.post('/create_private_user')
# def f_create_private_user(new_user: PrivateUserCreate):
#
#     if does_user_exist_active_or_not(keycloak_id=new_user.keycloak_id, engine_=engine) == 'user exist':
#         raise HTTPException(status_code=404, detail='user already exist')
#
#     # Purpose of this step is to make API more user friendly
#     # Only necessary parameters can be typed in
#     user_ = PrivateUser()
#     user_.keycloak_id = new_user.keycloak_id
#     user_.name = new_user.name
#     user_.surname = new_user.surname
#     user_.username = new_user.username
#     user_.email = new_user.email
#
#     create_user(private_user=user_, engine_=engine)
#     return "user created"
#
#
# @app.get('/read_private_user', response_model=PrivateUser)
# def f_read_private_user(keycloak_id: int):
#
#     if does_user_exist(keycloak_id=keycloak_id, engine_=engine) == 'user does not exist':
#         raise HTTPException(status_code=404, detail='user not exist')
#
#     user = read_user(keycloak_id=keycloak_id, engine_=engine)
#     return user
#
#
# @app.put('/update_private_user')
# def f_update_private_user(existing_user: PrivateUserUpdate):
#     if does_city_exist(city_id_=existing_user.city_id, engine_=engine) == 'City does not exist':
#         raise HTTPException(status_code=404, detail='City does not exist')
#
#     if does_user_exist(keycloak_id=existing_user.keycloak_id, engine_=engine) == 'user does not exist':
#         raise HTTPException(status_code=404, detail='user not exist')
#
#     # Purpose of this step is to make API more user friendly
#     # Only necessary parameters can be typed in
#     user_ = PrivateUser()
#     user_.keycloak_id = existing_user.keycloak_id
#     user_.name = existing_user.name
#     user_.surname = existing_user.surname
#     user_.username = existing_user.username
#     user_.email = existing_user.email
#
#     user_.city_id = existing_user.city_id
#     user_.about_me = existing_user.about_me
#     user_.date_of_birth = existing_user.date_of_birth
#
#     update_user(user=user_, engine_=engine)
#     return f'User with keycloak_id {existing_user.keycloak_id} has been updated.'
#
#
# @app.delete('/delete_private_user')
# def f_delete_private_user(keycloak_id: int):
#     if does_user_exist(keycloak_id=keycloak_id, engine_=engine) == 'user does not exist':
#         raise HTTPException(status_code=404, detail='user not exist')
#     delete_user(keycloak_id_=keycloak_id, engine_=engine)
#     return f"User with keycloak_id {keycloak_id} has been deleted"
#
#
# @app.post('/like_animal')
# def f_like_animal(new_like: LikeDislikeModel):
#
#     # Does user exist
#     if does_user_exist(keycloak_id=new_like.keycloak_id, engine_=engine) == 'user does not exist':
#         raise HTTPException(status_code=404, detail='user not exist')
#
#     # Does animal exist
#     if animal_present(animal_id=new_like.animal_id) == 'Animal does not exist':
#         raise HTTPException(status_code=404, detail='Animal does not exist')
#
#     # Purpose of this step is to make API more user friendly
#     # Only necessary parameters can be typed in
#     pair_ = LikePrivateUser()
#     pair_.keycloak_id = new_like.keycloak_id
#     pair_.animal_id = new_like.animal_id
#
#     # Already liked animal
#     if already_liked(user_animal_pair=pair_, engine_=engine) == 'User already liked this animal':
#         raise HTTPException(status_code=404, detail='User already liked this animal')
#
#     like(new_row=pair_, engine_=engine)
#
#     return "like created"
#
#
# @app.post('/dislike_animal')
# def f_dislike_animal(new_dislike: LikeDislikeModel):
#
#     if animal_present(animal_id=new_dislike.animal_id) == 'Animal does not exist':
#         raise HTTPException(status_code=404, detail='Non existing animal')
#
#     if does_user_exist(keycloak_id=new_dislike.keycloak_id, engine_=engine) == 'user does not exist':
#         raise HTTPException(status_code=404, detail='Non existing user')
#
#     # Purpose of this step is to make API more user friendly
#     # Only necessary parameters can be typed in
#     pair_ = LikePrivateUser()
#     pair_.keycloak_id = new_dislike.keycloak_id
#     pair_.animal_id = new_dislike.animal_id
#
#     # Animal already liked by user. CHECK !!!
#     if already_liked(user_animal_pair=pair_, engine_=engine) == 'User did not liked this animal!':
#         raise HTTPException(status_code=404, detail="Can't be performed dislike. User didn't even liked that animal before")
#
#     dis_like(new_row=pair_, engine_=engine)
#
#     return "Animal disliked"
#
#
# @app.get('/liked_animals_by_user', response_model=List[LikePrivateUserResponse])
# def f_liked_animal_by_user(keycloak_id_: int):
#
#     if does_user_exist(keycloak_id=keycloak_id_, engine_=engine) == 'user does not exist':
#         raise HTTPException(status_code=404, detail='Non existing user')
#
#     results = liked_animals_by_user(keycloak_id=keycloak_id_, engine_=engine)
#
#     return results

# -----------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------

#
# @app.post('/create_animal_association')
# def f_create_animal_association(new_association: AnimalAssociationCreate):
#
#     if does_animal_association_exist_active_or_not(keycloak_id=new_association.keycloak_id, engine_=engine) == 'association exist':
#         raise HTTPException(status_code=404, detail='association already exist')
#
#     association_ = AnimalAssociation()
#     association_.keycloak_id = new_association.keycloak_id
#     association_.email = new_association.email
#     association_.association_name = new_association.association_name
#     association_.association_username = new_association.association_username
#
#     create_animal_association(animal_association=association_, engine_=engine)
#     return "association created"
#
#
# @app.get('/read_animal_association', response_model=AnimalAssociation)
# def f_read_animal_association(keycloak_id: int):
#
#     if does_animal_association_exist(keycloak_id=keycloak_id, engine_=engine) == 'association does not exist':
#         raise HTTPException(status_code=404, detail='association not exist')
#
#     association = read_animal_association(keycloak_id=keycloak_id, engine_=engine)
#     return association
#
#
# @app.put('/update_animal_association')
# def f_update_animal_association(existing_association: AnimalAssociationUpdate):
#
#     if does_city_exist(city_id_=existing_association.city_id, engine_=engine) == 'City does not exist':
#         raise HTTPException(status_code=404, detail='City does not exist')
#
#     if does_animal_association_exist(keycloak_id=existing_association.keycloak_id, engine_=engine) == 'association does not exist':
#         raise HTTPException(status_code=404, detail='association not exist')
#
#     association_ = AnimalAssociation()
#     association_.keycloak_id = existing_association.keycloak_id
#     association_.association_name = existing_association.association_name
#     association_.association_username = existing_association.association_username
#     association_.email = existing_association.email
#     association_.city_id = existing_association.city_id
#     association_.phone_number = existing_association.phone_number
#     association_.about_association = existing_association.phone_number
#
#     update_animal_association(association=association_, engine_=engine)
#     return f'User with keycloak_id {existing_association.keycloak_id} has been updated.'
#
#
# @app.delete('/delete_animal_association')
# def f_delete_animal_association(keycloak_id: int):
#     if does_animal_association_exist(keycloak_id=keycloak_id, engine_=engine) == 'association does not exist':
#         raise HTTPException(status_code=404, detail='association not exist')
#     delete_animal_association(keycloak_id_=keycloak_id, engine_=engine)
#     return f"Association with keycloak_id {keycloak_id} has been deleted"
#
#
# @app.get('/all_animal_associations')
# def f_all_animal_associations():
#     statement = select(AnimalAssociation)
#     associations = session.exec(statement).all()
#
#     return associations
#

if __name__ == '__main__':

    SQL_ALCHEMY_DATABASE_URL = 'postgresql://postgres:@localhost/postgres'
    engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

    with Session(engine) as session:
        # session.execute("create schema if not exists test_udomi_ljubimca;")
        session.commit()

    # This also should be run at every start of the app!
    SQLModel.metadata.create_all(engine)

    # This should be in main file. Run on every start of the app.
    # Adding field to SQL table with current date time when row is entered
    with Session(engine) as session:
        session.execute("""



        alter table test_udomi_ljubimca.privateuser add column 

        IF NOT EXISTS time_row_added timestamp default 
        current_timestamp not null;

        alter table test_udomi_ljubimca.likeprivateuser add column 

        IF NOT EXISTS time_row_added timestamp default 
        current_timestamp not null;

        -- 
        --CREATE SEQUENCE IF NOT EXISTS serial_1 START 1;
        --alter table test_udomi_ljubimca.privateuser
        --alter column id set default nextval('serial_1');



        """)

        session.commit()

    uvicorn.run(app=app, port=8000, host="0.0.0.0")





