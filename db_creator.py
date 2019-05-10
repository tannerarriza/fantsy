from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///myplayer.db', echo=True)
Base = declarative_base()


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "<Player: {}>".format(self.name)


class Point(Base):
    """"""
    __tablename__ = "point"

    id = Column(Integer, primary_key=True)
    title = Column(String)


    player_id = Column(Integer, ForeignKey("player.id"))
    artist = relationship("Player", backref=backref(
        "points", order_by=id))


# create tables
Base.metadata.create_all(engine)