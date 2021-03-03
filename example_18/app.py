from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
   __tablename__= "users"

   id = Column(Integer, primary_key=True)
   firstName= Column(Text)
   lastName= Column(Text)

   def __init__(self, fn="youssef", ln="baddi"):

       self.firstName=fn
       self.lastName=ln 

   def __str__(self):
       return str(self.id) + " " + self.firstName + " " + self.lastName

class Article(Base):
    
   __tablename__= "articles"


if __name__ == '__main__':
   
   engine= create_engine('mysql+mysqldb://root:baddiroot@localhost/python_traning', echo$
   
   print('---------')
   Base.metadata.create_all(engine)

   Session = sessionmaker(bind=engine)
   session = Session()

   user = User()
   user_1 = User('johan','blanc')
   session.add(user)
   session.add(user_1)

   users = session.query(User)

   for u in users: print(u)

   user_id_2 = session.query(User).get(2)
   print(user_id_2)

   users_joh = session.query(User).filter( User.firstName.startswith("joh"))
   for us in users_joh: print(us)

   user_id_1 = session.query(User).get(1)
   if user_id_1:
       user_id_1.lastName += " karim"

       session.delete(user_id_1)

   session.commit()