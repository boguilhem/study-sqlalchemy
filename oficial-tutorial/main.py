from __future__ import with_statement
from venv import create
from click import echo
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text

print("###### SqlAlchemy Version: ######")
print(sqlalchemy.__version__)
print("\n")

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

with engine.connect() as conn:
    print("###### Executing Select: ######")
    result = conn.execute(text("select 'hello world'"))
    print(result.all())
