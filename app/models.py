from sqlalchemy import Column, Integer, String
from app.database import Base

class ParkingLot(Base):
    __tablename__ = "parking_lots"

    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    address = Column(String)
    