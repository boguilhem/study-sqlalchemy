from sqlalchemy import text
from main import engine

# # Select the data with condition WHERE
# # ----- Sending Parameter -----

with engine.connect() as conn:
    result = conn.execute(text("SELECT x, y FROM coord_table WHERE y > :y"), {"y": 4})
    for row in result:
        print(f"x: {row.x} y: {row.y}")


# # ----- Sending Multiple Parameters -----

with engine.connect() as conn:
    result = conn.execute(
        text("INSERT INTO coord_table (x, y) VALUES (:x, :y)"), [{"x": 9, "y": 10}, {"x": 11, "y": 12}]
    )
    conn.commit()
