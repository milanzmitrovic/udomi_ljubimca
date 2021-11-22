
from sqlmodel import SQLModel, select, Session
from app.private_users.models import AnimalAssociation


def read_animal_association(keycloak_id, engine_):

    """

    """

    with Session(engine_) as session:
        statement = select(AnimalAssociation).where(AnimalAssociation.keycloak_id == keycloak_id)
        result = session.execute(statement)
        found_user = result.first()[0]
        return found_user

