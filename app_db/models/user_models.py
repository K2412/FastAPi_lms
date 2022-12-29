from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship
import enum
from ..db_setup import Base

class Role(enum.Enum):
    teacher = 1
    student = 2

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key= True, Index= True )
    email = Column(String(100), unique= True, Index= True, nullable= False )
    role = Column(Enum(Role), primary_key= True, Index= True )


