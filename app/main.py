from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from models import Base, Incident , EmergencyTeam , Resource , User

Base.metadata.create_all(bind=engine)

app = FastAPI(title="DisasterAlert Cloud")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {
        "message": "DisasterAlert Emergency Response Cloud Running"
    }


@app.post("/incident")
def create_incident(
    incident_type: str,
    location: str,
    status: str,
    db: Session = Depends(get_db)
):
    incident = Incident(
        incident_type=incident_type,
        location=location,
        status=status
    )

    db.add(incident)
    db.commit()
    db.refresh(incident)

    return incident


@app.get("/incidents")
def get_incidents(db: Session = Depends(get_db)):
    return db.query(Incident).all()


@app.put("/incident/{incident_id}")
def update_incident(
    incident_id: int,
    status: str,
    db: Session = Depends(get_db)
):
    incident = db.query(Incident).filter(
        Incident.id == incident_id
    ).first()

    if not incident:
        return {"error": "Incident not found"}

    incident.status = status

    db.commit()

    return {"message": "Incident updated"}


@app.delete("/incident/{incident_id}")
def delete_incident(
    incident_id: int,
    db: Session = Depends(get_db)
):
    incident = db.query(Incident).filter(
        Incident.id == incident_id
    ).first()

    if not incident:
        return {"error": "Incident not found"}

    db.delete(incident)
    db.commit()

    return {"message": "Incident deleted"}

@app.post("/team")
def create_team(team_name: str, region: str, status: str, db: Session = Depends(get_db)):
    team = EmergencyTeam(team_name=team_name, region=region, status=status)
    db.add(team)
    db.commit()
    db.refresh(team)
    return team


@app.get("/teams")
def get_teams(db: Session = Depends(get_db)):
    return db.query(EmergencyTeam).all()


@app.post("/resource")
def create_resource(resource_name: str, quantity: int, location: str, db: Session = Depends(get_db)):
    resource = Resource(resource_name=resource_name, quantity=quantity, location=location)
    db.add(resource)
    db.commit()
    db.refresh(resource)
    return resource


@app.get("/resources")
def get_resources(db: Session = Depends(get_db)):
    return db.query(Resource).all()


@app.get("/dashboard")
def dashboard(db: Session = Depends(get_db)):
    return {
        "total_incidents": db.query(Incident).count(),
        "active_incidents": db.query(Incident).filter(Incident.status == "Active").count(),
        "total_teams": db.query(EmergencyTeam).count(),
        "available_resources": db.query(Resource).count()
    }