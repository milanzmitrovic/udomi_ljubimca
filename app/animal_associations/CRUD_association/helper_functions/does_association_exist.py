

from sqlmodel import Session, select
from app.private_users.models import AnimalAssociation


def does_animal_association_exist(keycloak_id: int, engine_):

    """
    This is for updating user.

    Only active user can be updated.
    """

    with Session(engine_) as session1:

        statement = select(AnimalAssociation).where(AnimalAssociation.keycloak_id == keycloak_id
                                                    ).where(AnimalAssociation.is_active == 1)
        result = session1.execute(statement)
        found_association = result.first()

        if found_association is not None:
            return 'association exist'
        else:
            return 'association does not exist'


def does_animal_association_exist_active_or_not(keycloak_id: int, engine_):
    """
    This is only used for creating user.
    Keycloak_ID should be not present in database, now or earlier.

    If there is deleted user (active_status = 0), there shouldn't be created new user
    with same keycloak_id.


    :param keycloak_id, engine_:

    :type keycloak_id:
    :return:
    :rtype:
    """

    with Session(engine_) as session:

        statement = select(AnimalAssociation).where(AnimalAssociation.keycloak_id == keycloak_id)
        result = session.execute(statement)
        found_association = result.first()

        if found_association is not None:
            return 'association exist'
        else:
            return 'association does not exist'



