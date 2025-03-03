from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Country(Base):
    __tablename__ = 'country'
    Code = Column(String(3), primary_key=True)
    Name = Column(String(50))
    Population = Column(Integer)

engine = create_engine("mysql+pymysql://root:root@localhost/world")
Session = sessionmaker(bind=engine)
session = Session()

# Výpis států
countries = session.query(Country).limit(5).all()
for country in countries:
    print(country.Name, country.Population)

session.close()
