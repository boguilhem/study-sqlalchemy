import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text

print("###### SqlAlchemy Version: #####")
print(sqlalchemy.__version__)

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

# # selecting without commit
# with engine.connect() as conn:
#     print("\n###### Executing SELECT: ######")
#     result = conn.execute(text("select 'hello world'"))
#     print(result.all())

# commit the data. Style: "commit as you go"
print("\n###### Executing CREATE TABLE with 'commit as you go': ######")
with engine.connect() as conn:
    conn.execute(text("CREATE TABLE coord_table (x int, y int)"))
    print("\n###### Executing INSERT: ######")
    conn.execute(
        text("INSERT INTO coord_table (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 2}, {"x": 3, "y": 4}, {"x": 5, "y": 6}, {"x": 7, "y": 8}],
    )
    conn.commit()

# # commit the data. Style: "Begin once"
# print("\n###### Executing INSERT with 'Begin once': ######")
# with engine.begin() as conn:
#     conn.execute(text("INSERT INTO coord_table (x, y) VALUES (:x, :y)"), [{"x": 6, "y": 8}, {"x": 9, "y": 10}])
