

from sqlmodel import Session, select

from app.private_users.models import AnimalAssociation


def delete_animal_association(keycloak_id_, engine_):

    """

    """

    # if does_user_exist(keycloak_id_) == 'user does not exist':
    #     return 'user not exist'

    with Session(engine_) as session:
        statement = select(AnimalAssociation).where(AnimalAssociation.keycloak_id == keycloak_id_)
        old_association = session.exec(statement).one()

        old_association.is_active = 0

        session.add(old_association)
        session.commit()
        session.refresh(old_association)

    return old_association




