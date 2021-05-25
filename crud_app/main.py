from typing import List

import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

# from . import crud, models, schemas
from crud_app import crud, models, schemas
from crud_app.database import SessionLocal, engine


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/personal_users/{keycloak_id}/", response_model=schemas.PersonalUser)
def read_user(keycloak_id: str, db: Session = Depends(get_db)):
    db_user = crud.get_personal_user(db=db, keycloak_id=keycloak_id)
    print('-----------------------------------------------------------')
    print(keycloak_id)
    print(db_user)
    print('-----------------------------------------------------------------------')
    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return db_user


@app.get("/personal_animal_association/{keycloak_id}/", response_model=schemas.AnimalAssociation)
def read_user(keycloak_id: str, db: Session = Depends(get_db)):
    db_user = crud.get_animal_association(db=db, keycloak_id=keycloak_id)
    print('-----------------------------------------------------------')
    print(keycloak_id)
    print(db_user)
    print('-----------------------------------------------------------------------')
    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return db_user


@app.post("/personal_users/", response_model=schemas.PersonalUser)
def create_user(user: schemas.PersonalUserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_personal_user(db=db, keycloak_id=user.keycloak_id)
    print('-------------')
    print(db_user)
    print(user.keycloak_id)
    print(type(db_user))
    print('-------------')
    if db_user:
        raise HTTPException(status_code=404, detail='User has been already registered!')
    return crud.create_personal_user(db=db, user=user)


@app.post("/animal_association/", response_model=schemas.AnimalAssociation)
def create_user(user: schemas.AnimalAssociationCreate, db: Session = Depends(get_db)):
    db_user = crud.get_animal_association(db=db, keycloak_id=user.keycloak_id)
    print('-------------')
    print(db_user)
    print(user.keycloak_id)
    print(type(db_user))
    print('-------------')
    if db_user:
        raise HTTPException(status_code=404, detail='User has been already registered!')
    return crud.create_animal_association(db=db, user=user)


if __name__ == '__main__':
    uvicorn.run(app=app)

