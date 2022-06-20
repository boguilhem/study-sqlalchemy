from sqlalchemy.orm import Session
from sqlalchemy import text
from main import engine

stmt = text("SELECT x, y FROM coord_table WHERE y > :y ORDER BY x, y").bindparams(y=4)

with Session(engine) as session:
    result = session.execute(stmt)
    for row in result:
        print(f"x: {row.x}, y: {row.y}")

with Session(engine) as session:
    result = session.execute(text("UPDATE coord_table SET y=:y WHERE x=:x"), [{"x": 5, "y": 10}, {"x": 7, "y": 14}])
    session.commit()

with Session(engine) as session:
    result = session.execute(text("SELECT x, y FROM coord_table"))
    for row in result:
        print(f"x: {row.x}, y: {row.y}")
