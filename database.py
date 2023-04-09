import os
from sqlalchemy import create_engine, text

my_secret = os.environ['db_string']

connection_string = my_secret
engine = create_engine(connection_string, echo=True)


def get_table():
  with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM example"))

    print(result.all())


def get_name():
  with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM example WHERE name = :name"), dict(name="Ashley"))

  for row in result.mappings():
    print('Type of row[name]', type(row["name"]))
    print("Author:" , row["name"])



def get_name2(var):
  with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM example WHERE name = :name"), dict(name=var))

    print("result type is:", type(result))
    print("result is:", result.all())
    
    for row in result.mappings():
      print('Type of row[name]', type(row["name"]))
      print("Author:" , row["name"])
      return(row["name"])

#get_name2("Ashley")
get_table()