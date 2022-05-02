

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

# cwd = os.getcwd()
# sys.path.append(cwd)

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





