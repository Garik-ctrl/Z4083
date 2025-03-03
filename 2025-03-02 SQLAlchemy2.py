from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://root:root@localhost/world")

with engine.connect() as conn:
    result = conn.execute(text("SELECT Name, Population FROM country LIMIT 5"))

    for row in result:
        print(row)
