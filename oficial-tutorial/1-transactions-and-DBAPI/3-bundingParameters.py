from sqlalchemy import text
from main import engine

stmt = text("SELECT x, y FROM coord_table WHERE y > :y ORDER BY x, y").bindparams(y=4)

with engine.connect() as conn:
    result = conn.execute(stmt)
    for row in result:
        print(f"x: {row.x} y: {row.y}")
