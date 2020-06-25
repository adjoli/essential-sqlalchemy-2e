from pprint import pprint
from sqlalchemy import MetaData, create_engine, Table, select

metadata = MetaData()
engine = create_engine('sqlite:///chinook.db')

metadata.reflect(bind=engine)

