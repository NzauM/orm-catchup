from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from faker import Faker
from models import Dev, Company, Freebie, company_dev
import random

creator_engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=creator_engine)
session = Session()

fake = Faker()


if __name__ == '__main__':

    print("Clearng DB**********")
    session.query(Dev).delete()
    session.query(Freebie).delete()
    session.query(Company).delete()
    print("Done")
    
    print("seeding devs ..... ")
    devs = []
    for i in range(10):
        new_dev = Dev(name=fake.name())
        session.add(new_dev)
        session.commit()
        devs.append(new_dev)
    print("seeded devs")

    print("Seeding COMPANIIIEEESSS")

    for i in range(10):
        company = Company(name=fake.company(), founding_year= fake.random_number(digits=4))
        session.add(company)
        session.commit()

    print("*******COMPANY SEEDING DONE ***********")

    print("Now seeding Freebies.............")
    for dev in devs:
        freebies = [(Freebie(item_name = fake.emoji(), value=fake.random_number(digits=4), dev_id= dev.id, company_id = random.randint(0,9))) for i in range(3)]
        session.add_all(freebies)
        session.commit()
    print("*******DEV SEEDING DONE ***********")


    print("Seed Company Devs")
    for i in session.query(Freebie).all():
        assigned = company_dev.insert().values(dev_id=i.dev_id, company_id=i.company_id)
        session.execute(assigned)
        session.commit()
    print("Seed Company Devs Done")

    session.close()