from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import ipdb


Base = declarative_base()
creator_engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=creator_engine)
session = Session()

# company_devs = Table('company-devs', Base.metadata, Column('company-id', ForeignKey))
company_dev = Table('company_devs', Base.metadata, Column('company_id', ForeignKey('companies.id'), primary_key = True), Column('dev_id', ForeignKey('devs.id'), primary_key = True))

class Company(Base):

    __tablename__ = 'companies'

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    founding_year = Column(Integer())

    freebies = relationship('Freebie', backref=backref('company'))
    devs = relationship('Dev', secondary=company_dev, back_populates='companies')


class Dev(Base):

    __tablename__ = 'devs'

    id = Column(Integer(), primary_key = True)
    name = Column(String())

    freebies = relationship('Freebie', backref= backref('dev'))
    companies = relationship('Company',secondary=company_dev, back_populates='devs')

class Freebie(Base):

    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key = True)
    item_name = Column(String())
    value = Column(Integer())
    dev_id = Column(Integer(), ForeignKey('devs.id'))
    company_id = Column(Integer(), ForeignKey('companies.id'))

dev1 = session.query(Dev).first()
company1 = session.query(Company).first()
freebie1 = session.query(Freebie).first()
ipdb.set_trace()



