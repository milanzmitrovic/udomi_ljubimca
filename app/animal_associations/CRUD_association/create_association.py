
from app.private_users.models import AnimalAssociation
from sqlmodel import Session


def create_animal_association(animal_association: AnimalAssociation, engine_):

    """

    """

    with Session(engine_) as session:
        association = animal_association

        session.add(association)

        session.commit()


