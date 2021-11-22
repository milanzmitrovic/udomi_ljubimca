
from typing import Optional

from sqlmodel import Field, SQLModel, Column, Integer, Sequence, VARCHAR, String

import datetime

from pydantic import BaseModel


USER_ID_SEQ = Sequence('user_id_seq')  # define sequence explicitly


class PrivateUser(SQLModel, table=True):
    __table_args__ = {'schema': 'test_udomi_ljubimca'}
    keycloak_id: int = Field(primary_key=True,)
    name: str
    surname: str
    username: str
    email: str

    # test_column: str = Field(sa_column=String(length=10))

    # id: Optional[int] = Column(Integer, USER_ID_SEQ, server_default=USER_ID_SEQ.next_value())
    # id: Optional[int] = Field() # 13.10.2021. added
    is_active: int = Field(default=1)
    city_id: Optional[int] = Field(default=None, foreign_key="test_udomi_ljubimca.city.city_id")
    about_me: Optional[str]
    date_of_birth: Optional[datetime.datetime]
    user_creation_date: datetime.date = datetime.datetime.now()


class City(SQLModel, table=True):
    __table_args__ = {'schema': 'test_udomi_ljubimca'}
    # id: int = Field(default=None, primary_key=True)
    city_id: int = Field(primary_key=True)
    city_name: str


class AnimalAssociation(SQLModel, table=True):
    __table_args__ = {'schema': 'test_udomi_ljubimca'}
    keycloak_id: int = Field(primary_key=True,)
    email: str
    association_name: str
    association_username: str

    is_active: int = Field(default=1)
    city_id: Optional[int] = Field(default=None, foreign_key="test_udomi_ljubimca.city.city_id")
    phone_number: Optional[str]
    about_association: Optional[str]
    user_creation_date: datetime.date = datetime.datetime.now()


#
class LikePrivateUser(SQLModel, table=True):
    __table_args__ = {'schema': 'test_udomi_ljubimca'}
    id: int = Field(default=None, primary_key=True)
    animal_id: int
    keycloak_id: int = Field(default=None, foreign_key="test_udomi_ljubimca.privateuser.keycloak_id")


# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------
class LikePrivateUserResponse(SQLModel):
    animal_id: int
    keycloak_id: int


class PrivateUserCreate(BaseModel):
    keycloak_id: int
    name: str
    surname: str
    username: str
    email: str


class PrivateUserUpdate(BaseModel):
    keycloak_id: int
    name: str
    surname: str
    username: str
    email: str

    city_id: Optional[int]
    about_me: Optional[str]
    date_of_birth: Optional[datetime.datetime]


class LikeDislikeModel(BaseModel):
    animal_id: int
    keycloak_id: int


class AnimalAssociationCreate(BaseModel):
    keycloak_id: int = Field(primary_key=True,)
    email: str
    association_name: str
    association_username: str


class AnimalAssociationUpdate(BaseModel):
    keycloak_id: int = Field(primary_key=True,)
    email: str
    association_name: str
    association_username: str

    city_id: Optional[int]
    phone_number: Optional[str]
    about_association: Optional[str]


class AnimalAssociationReturnAll(BaseModel):
    email: str
    association_name: str
    association_username: str

    is_active: int
    city_id: Optional[int]
    phone_number: Optional[str]
    about_association: Optional[str]
    user_creation_date: Optional[datetime.date]
