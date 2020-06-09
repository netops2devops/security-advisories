import os
import logging
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, backref
from sqlalchemy import create_engine

Base = declarative_base()

class Post(Base):
   __tablename__ = 'post'

   id = Column(Integer, primary_key=True)
   title = Column(String(100))
   body = Column(String(100000))

class Link(Base):
   __tablename__ = 'link'

   id = Column(Integer, primary_key=True)
   link_for = Column(String(100))
   uid = Column(String(100))
   post_id = Column(Integer, ForeignKey('post.id'))
   post = relationship('Post', backref=backref('links'))

class Visit(Base):
   __tablename__ = 'visit'

   id = Column(Integer, primary_key=True)
   link_id = Column(Integer, ForeignKey('link.id'))
   link = relationship('Link', backref=backref('visits'))
   dt = Column(String(100))
   ip = Column(String(100))
   ref = Column(String(1000))

engine = create_engine(os.getenv('DB_URL'))
logging.info('Creating tables')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

get_session = sessionmaker(bind=engine)