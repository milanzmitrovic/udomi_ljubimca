from typing import List

from fastapi import APIRouter, HTTPException
from sqlmodel import create_engine

from app.animal_associations.CRUD_association.create_association import create_animal_association
from app.animal_associations.CRUD_association.delete_association import delete_animal_association
from app.animal_associations.CRUD_association.helper_functions.does_association_exist import \
    does_animal_association_exist_active_or_not, does_animal_association_exist
from app.animal_associations.CRUD_association.read_association import read_animal_association
from app.animal_associations.CRUD_association.update_association import update_animal_association
from app.private_users.CRUD_user.helper_functions.does_city_exist import does_city_exist
from app.private_users.models import AnimalAssociationCreate, AnimalAssociation, AnimalAssociationUpdate, \
    AnimalAssociationReturnAll

from sqlmodel import Session, select


router = APIRouter(
    prefix="/animal_associations",
    tags=["Animal Associations"]

)

SQL_ALCHEMY_DATABASE_URL = 'postgresql://postgres:@localhost/postgres'
engine = create_engine(SQL_ALCHEMY_DATABASE_URL)


@router.post('/create_animal_association')
def f_create_animal_association(new_association: AnimalAssociationCreate):

    if does_animal_association_exist_active_or_not(keycloak_id=new_association.keycloak_id, engine_=engine) == 'association exist':
        raise HTTPException(status_code=404, detail='association already exist')

    if len(str(new_association.keycloak_id)) > 100:
        raise HTTPException(status_code=404, detail="Your keycloak_id is too long.")

    if len(new_association.email) > 50:
        raise HTTPException(status_code=404, detail="Your email is too long.")

    if len(new_association.association_username) > 50:
        raise HTTPException(status_code=404, detail="Your association username is too long.")

    if len(new_association.association_name) > 50:
        raise HTTPException(status_code=404, detail="Your association name is too long.")

    association_ = AnimalAssociation()
    association_.keycloak_id = new_association.keycloak_id
    association_.email = new_association.email
    association_.association_name = new_association.association_name
    association_.association_username = new_association.association_username

    create_animal_association(animal_association=association_, engine_=engine)
    return "association created"


@router.get('/read_animal_association', response_model=AnimalAssociation)
def f_read_animal_association(keycloak_id: int):

    if does_animal_association_exist(keycloak_id=keycloak_id, engine_=engine) == 'association does not exist':
        raise HTTPException(status_code=404, detail='association not exist')

    association = read_animal_association(keycloak_id=keycloak_id, engine_=engine)
    return association


@router.put('/update_animal_association')
def f_update_animal_association(existing_association: AnimalAssociationUpdate):

    if does_city_exist(city_id_=existing_association.city_id, engine_=engine) == 'City does not exist':
        raise HTTPException(status_code=404, detail='City does not exist')

    if does_animal_association_exist(keycloak_id=existing_association.keycloak_id, engine_=engine) == 'association does not exist':
        raise HTTPException(status_code=404, detail='association not exist')

    if len(str(existing_association.keycloak_id)) > 100:
        raise HTTPException(status_code=404, detail="Your keycloak_id is too long.")

    if len(existing_association.email) > 50:
        raise HTTPException(status_code=404, detail="Your email is too long.")

    if len(existing_association.association_username) > 50:
        raise HTTPException(status_code=404, detail="Your association username is too long.")

    if len(existing_association.association_name) > 50:
        raise HTTPException(status_code=404, detail="Your association name is too long.")

    if len(existing_association.phone_number) > 50:
        raise HTTPException(status_code=404, detail="Your phone number is too long")

    if len(existing_association.about_association) > 500:
        raise HTTPException(status_code=404, detail="Your field about association is too long.")

    association_ = AnimalAssociation()
    association_.keycloak_id = existing_association.keycloak_id
    association_.association_name = existing_association.association_name
    association_.association_username = existing_association.association_username
    association_.email = existing_association.email
    association_.city_id = existing_association.city_id
    association_.phone_number = existing_association.phone_number
    association_.about_association = existing_association.phone_number

    update_animal_association(association=association_, engine_=engine)
    return f'User with keycloak_id {existing_association.keycloak_id} has been updated.'


@router.delete('/delete_animal_association')
def f_delete_animal_association(keycloak_id: int):
    if does_animal_association_exist(keycloak_id=keycloak_id, engine_=engine) == 'association does not exist':
        raise HTTPException(status_code=404, detail='association not exist')
    delete_animal_association(keycloak_id_=keycloak_id, engine_=engine)
    return f"Association with keycloak_id {keycloak_id} has been deleted"


@router.get('/all_animal_associations', response_model=List[AnimalAssociationReturnAll])
def f_all_animal_associations():

    with Session(engine) as session:
        statement_ = select(AnimalAssociation)
        associations = session.exec(statement_).all()

    return associations
