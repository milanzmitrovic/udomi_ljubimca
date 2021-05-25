from pydantic import BaseModel


# Personal user class
class PersonalUserBase(BaseModel):
    name: str
    surname: str
    email: str
    terms_and_condition_accepted: str
    about_me: str
    city: str
    age: int


class PersonalUserCreate(PersonalUserBase):
    keycloak_id: str


class PersonalUser(PersonalUserBase):

    class Config:
        orm_mode = True


# Animal association class
class AnimalAssociationBase(BaseModel):
    name: str
    city: str
    email: str
    contact_phone: str
    government_id_number: str
    website: str
    terms_and_condition_accepted: str


class AnimalAssociationCreate(AnimalAssociationBase):
    keycloak_id: str


class AnimalAssociation(AnimalAssociationBase):

    class Config:
        orm_mode = True





