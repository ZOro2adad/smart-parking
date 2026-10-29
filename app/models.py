from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.database import Base

class ParkingLot(Base):
    __tablename__ = "parking_lots"

    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    address = Column(String)


class Spot(Base):
    __tablename__ = "spots"
    id = Column(Integer, primary_key = True)
    number = Column(String, nullable = False)
    lot_id = Column(Integer, ForeignKey("parking_lots.id"), nullable = False)
    is_occupied = Column(Boolean, default = False)