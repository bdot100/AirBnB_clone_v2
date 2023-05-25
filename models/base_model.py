#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String
import models

Base = declarative_base()


class BaseModel:
    """ A base class for all hbnb models """

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs or ("updated_at" not in kwargs and
                          "created_at" not in kwargs):
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            pass
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']

            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        st = self.__dict__.copy()
        st.pop("_sa_instance_state", None)
        return "[{}] ({}) {}".format(type(self).__name__, self.id, st)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """This Returns the dictionary representation of the
        Base_model instance"""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = str(type(self).__name__)
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary.pop("_sa_instance_state", None)
        return dictionary

    def delete(self):
        """ Delete the current instance from the storage """
        models.storage.delete(self)
