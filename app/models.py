from sqlalchemy import Column, Integer, String
from database import Base

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    incident_type = Column(String(100))
    location = Column(String(100))
    status = Column(String(100))

class EmergencyTeam(Base):
    __tablename__ = "emergency_teams"

    id = Column(Integer, primary_key=True, index=True)
    team_name = Column(String(100))
    region = Column(String(100))
    status = Column(String(100))


class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    resource_name = Column(String(100))
    quantity = Column(Integer)
    location = Column(String(100))


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True)
    role = Column(String(50))