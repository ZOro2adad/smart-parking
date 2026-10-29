from app.database import SessionLocal
from app.models import ParkingLot

db = SessionLocal()

lots = db.query(ParkingLot).all()
for lot in lots:
    print(lot.id, lot.name, lot.address)

db.close()