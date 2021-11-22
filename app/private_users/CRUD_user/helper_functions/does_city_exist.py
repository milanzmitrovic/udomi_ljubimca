
from sqlmodel import create_engine, Session, select
from app.private_users.models import City

SQL_ALCHEMY_DATABASE_URL = 'postgresql://postgres:@localhost/postgres'
engine = create_engine(SQL_ALCHEMY_DATABASE_URL)


def does_city_exist(city_id_: int, engine_):
    """

    city_id_
    :param city_id_, engine_:
    :type city_id_:
    :return:
    :rtype:
    """

    with Session(engine_) as session:

        statement = select(City).where(City.city_id == city_id_)
        result = session.execute(statement)
        found_city = result.first()

        if found_city is not None:
            return 'City exist'
        else:
            return 'City does not exist'



