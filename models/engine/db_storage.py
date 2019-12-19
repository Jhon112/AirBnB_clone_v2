#!/usr/bin/python3
"""This is the database engine for mysql database"""
from models.base_model import BaseModel, Base
from models import User, State, City, Amenity, Place, Review
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
import os


class DBStorage:
    """
    New engine that will create tables for models
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Constructor. Inits an engine
        """

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(os.getenv("HBNB_MYSQL_USER"),
                                              os.getenv("HBNB_MYSQL_PWD"),
                                              os.getenv("HBNB_MYSQL_HOST"),
                                              os.getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        search on database
        """
        if cls is None:
            obj_types = [User, State, Place, City, Amenity, Review]
            res_list = [list(self.__session.query(type).all()) for
                        type in obj_types]
                        
            # res_list.append(list(self.__session.query(User).all()))
            # res_list.append(list(self.__session.query(State).all()))
            # res_list.append(list(self.__session.query(Place).all()))
            # res_list.append(list(self.__session.query(City).all()))
            # res_list.append(list(self.__session.query(Amenity).all()))
            # res_list.append(list(self.__session.query(Review).all()))
        else:
            if cls == "State":
                res_list = list(self.__session.query(State).all())
            if cls == "User":
                res_list = list(self.__session.query(User).all())
            if cls == "Place":
                res_list = list(self.__session.query(Place).all())
            if cls == "City":
                res_list = list(self.__session.query(City).all())
            if cls == "Amenity":
                res_list = list(self.__session.query(Amenity).all())
            if cls == "Review":
                res_list = list(self.__session.query(Review).all())
        my_dict = {}
        for obj in res_list:
            class_name = type(obj).__name__
            key = class_name + "." + str(obj.id)
            try:
                if obj._sa_instance_state:
                    del obj._sa_instance_state
            except:
                pass
            my_dict[key] = obj

        return my_dict

    def new(self, obj):
        """Add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
