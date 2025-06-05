from sqlalchemy import Column, Integer, Boolean, Numeric, String, DateTime, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

# Example model class - you can modify or add more as needed
class CatalogItem(Base):
    __tablename__ = 'Catalog'

    Id = Column(Integer, primary_key=True)
    Name = Column(String(255), nullable=False)
    CatalogTypeId = Column(Integer, ForeignKey('CatalogType.Id'), nullable=False)
    CatalogBrandId = Column(Integer, ForeignKey('CatalogBrand.Id'), nullable=False)
    AvailableStock = Column(Integer, nullable=False, default=0)
    OnReorder = Column(Boolean, nullable=False, default=False)
    RestockThreshold = Column(Integer, nullable=False, default=0)
    MaxStockThreshold = Column(Integer, nullable=False, default=0)
    CatalogType = relationship("CatalogType")
    CatalogBrand = relationship("CatalogBrand")
    Description  = Column(String(500), nullable=True)
    Price = Column(Numeric, nullable=False)
    #Embedding = Column(String(2048), nullable=True)  # For storing vector as JSON string
    PictureFileName = Column(String(500), nullable=True)

class CatalogType(Base):
    __tablename__ = 'CatalogType'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(255), nullable=False)

class CatalogBrand(Base):
    __tablename__ = 'CatalogBrand'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(255), nullable=False)