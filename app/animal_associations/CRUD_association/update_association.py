
from sqlmodel import Session, select

from app.private_users.models import AnimalAssociation


def update_animal_association(association: AnimalAssociation, engine_):

    """

    """

    with Session(engine_) as session:
        statement = select(AnimalAssociation).where(AnimalAssociation.keycloak_id == association.keycloak_id)
        new_association = session.exec(statement).one()

        new_association.association_name = association.association_name
        new_association.association_username = association.association_username
        new_association.email = association.email

        new_association.phone_number = association.phone_number
        new_association.city_id = association.city_id
        new_association.about_association = association.about_association

        session.add(new_association)
        session.commit()
        session.refresh(new_association)

    return new_association




