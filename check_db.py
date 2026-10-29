from sqlalchemy import inspect
from app.database import engine

print(inspect(engine).get_table_names())