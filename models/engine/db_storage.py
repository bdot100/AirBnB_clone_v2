#!/usr/bin/python3
"""DBStorage Engine"""
from models.base_model import BaseModel, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """ DBStorage Engine Class """
    __engine = None
    __session = None
    
    def __init__(self) -> None:
        """ Creates the engine by linking to mysql DB
        and user """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)
            
    def all(self, cls=None):
        """ queries on the current database session (self.__session)
        all objects depending of the class name (argument cls)"""
        obj_dict = {}

        if cls is None:
            obj_list = self.__session.query(State).all()
            obj_list.extend(self.__session.query(City).all())
            obj_list.extend(self.__session.query(User).all())
            obj_list.extend(self.__session.query(Place).all())
            obj_list.extend(self.__session.query(Review).all())
            obj_list.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            obj_list = self.__session.query(cls).all()

        for obj in obj_list:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            obj_dict[key] = obj

        return obj_dict
    
    def new(self, obj):
        """ adds the object to the current database session (self.__session) """
        self.__session.add(obj)

    def save(self):
        """ commits all changes of the current database session (self.__session) """
        self.__session.commit()
        
    def delete(self, obj=None):
        """deletes from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)
    
    def reload(self):
        """ creates all tables in the database (feature of SQLAlchemy
        ) (WARNING: all classes who inherit from Base must be 
        imported before calling """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()