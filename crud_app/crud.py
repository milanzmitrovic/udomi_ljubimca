from sqlalchemy.orm import Session
from crud_app import models, schemas


def get_personal_user(db: Session, keycloak_id: str):
    return db.query(models.PersonalUsers).filter(models.PersonalUsers.keycloak_id == keycloak_id).first()


def get_animal_association(db: Session, keycloak_id: str):
    return db.query(models.AnimalAssociations).filter(models.AnimalAssociations.keycloak_id == keycloak_id).first()


def create_personal_user(db: Session, user: schemas.PersonalUserCreate):
    db_user = models.PersonalUsers(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_animal_association(db: Session, user: schemas.AnimalAssociationCreate):
    db_item = models.AnimalAssociations(**user.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item




