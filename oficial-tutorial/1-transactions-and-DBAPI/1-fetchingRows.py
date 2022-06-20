from main import engine
from sqlalchemy import text

# # Select the data from the coord_table
# # ----- Different ways of accessing ROW object -----

# Attribute Name
print("\n###### Executing SELECT (Attribute Name): ######")
with engine.connect() as conn:
    result = conn.execute(text("SELECT x, y FROM coord_table"))
    for row in result:
        print(f"x: {row.x}, y: {row.y}")

# Tuple Assignment
# print("\n###### Executing SELECT (Tuple Assignment): ######")
# with engine.connect() as conn:
#     result = conn.execute(text("SELECT x, y FROM coord_table"))
#     for (x, y) in result:
#         print(f"x: {x}, y: {y}")

# # Integer Index
# print("\n###### Executing SELECT (Integer Index): ######")
# with engine.connect() as conn:
#     result = conn.execute(text("SELECT x, y FROM coord_table"))
#     for row in result:
#         print(f"x: {row[0]}, y: {row[1]}")

# # Mapping Access
# print("\n###### Executing SELECT (Mapping Access): ######")
# with engine.connect() as conn:
#     result = conn.execute(text("SELECT x, y FROM coord_table"))
#     for dict_row in result.mappings():
#         # print(dict_row)
#         print(f"x: {dict_row['x']}, y: {dict_row['y']}")
