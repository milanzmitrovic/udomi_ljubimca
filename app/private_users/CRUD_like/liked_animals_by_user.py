
from app.private_users.models import LikePrivateUser
from sqlmodel import Session, select
# from app.main import engine


def liked_animals_by_user(keycloak_id, engine_):

    with Session(engine_) as session:
        statement = select(LikePrivateUser).where(LikePrivateUser.keycloak_id == keycloak_id)
        results = session.exec(statement)
        results = results.all()
        return results
