

# Napraviti posebnu schema-u za create_user *** *** ***

# Posebna šema za update (is_active should not exist, created_date also) *****

# Varchar(1000) ***

# Autoincrement


import os
import sys
from typing import List

import uvicorn
from sqlmodel import create_engine
from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Session, select


from app.api_routes.private_user import private_users
from app.api_routes.likes import likes
from app.api_routes.animal_association import animal_association

app = FastAPI()

app.include_router(private_users.router)
app.include_router(likes.router)
app.include_router(animal_association.router)


if __name__ == '__main__':

    SQL_ALCHEMY_DATABASE_URL = 'postgresql://postgres:@localhost/postgres'
    engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

    with Session(engine) as session:
        # session.execute("create schema if not exists test_udomi_ljubimca;")
        session.commit()

    # This also should be run at every start of the app!
    SQLModel.metadata.create_all(engine)

    # This should be in main file. Run on every start of the app.
    # Adding field to SQL table with current date time when row is entered
    with Session(engine) as session:
        session.execute("""



        alter table test_udomi_ljubimca.privateuser add column 

        IF NOT EXISTS time_row_added timestamp default 
        current_timestamp not null;

        alter table test_udomi_ljubimca.likeprivateuser add column 

        IF NOT EXISTS time_row_added timestamp default 
        current_timestamp not null;

        -- 
        --CREATE SEQUENCE IF NOT EXISTS serial_1 START 1;
        --alter table test_udomi_ljubimca.privateuser
        --alter column id set default nextval('serial_1');



        """)

        session.commit()

    uvicorn.run(app=app, port=8000, host="0.0.0.0")





