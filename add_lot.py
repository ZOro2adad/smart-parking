from app.database import SessionLocal
from app.models import ParkingLot

db = SessionLocal()

lot = ParkingLot(name = "Dostyk Plaza", address = "микрорайон Самал-2, 111")

db.add(lot)
db.commit()

print("Добавлена парковка с id = ", lot.id)

db.close()