
from sqlmodel import select, Session
from app.private_users.models import LikePrivateUser


def already_liked(user_animal_pair: LikePrivateUser, engine_):

    with Session(engine_) as session:

        statement = select(LikePrivateUser).where(LikePrivateUser.keycloak_id == user_animal_pair.keycloak_id).where(
            LikePrivateUser.animal_id == user_animal_pair.animal_id)
        results = session.exec(statement)

        if results.first() is None:

            return 'User did not liked this animal!'
        else:
            return 'User already liked this animal'

