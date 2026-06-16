from sqlalchemy import Column, Integer, String
from database import Base

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    incident_type = Column(String)
    location = Column(String)
    status = Column(String)

class EmergencyTeam(Base):
    __tablename__ = "emergency_teams"

    id = Column(Integer, primary_key=True, index=True)
    team_name = Column(String)
    region = Column(String)
    status = Column(String)


class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    resource_name = Column(String)
    quantity = Column(Integer)
    location = Column(String)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    role = Column(String)