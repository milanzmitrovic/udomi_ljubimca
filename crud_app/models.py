from crud_app.database import Base, engine

Base.metadata.reflect(engine, schema='udomi_ljubimca')


class PersonalUsers(Base):

    __table__ = Base.metadata.tables['udomi_ljubimca.personal_users']


class AnimalAssociations(Base):
    __table__ = Base.metadata.tables['udomi_ljubimca.animal_associations']






