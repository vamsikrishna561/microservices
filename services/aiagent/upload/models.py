from sqlalchemy import Column, Integer, Boolean, Numeric, String, DateTime, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from pgvector.sqlalchemy import Vector
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

# Example model class - you can modify or add more as needed
class CatalogItem(Base):
    __tablename__ = 'catalog'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    catalogtype_id = Column(Integer, ForeignKey('catalog_type.id'), nullable=False)
    catalogbrand_id = Column(Integer, ForeignKey('catalog_brand.id'), nullable=False)
    available_stock = Column(Integer, nullable=False, default=0)
    on_reorder = Column(Boolean, nullable=False, default=False)
    restock_threshold = Column(Integer, nullable=False, default=0)
    max_stock_threshold = Column(Integer, nullable=False, default=0)
    catalog_type = relationship("CatalogType")
    catalog_brand = relationship("CatalogBrand")
    description = Column(String(500), nullable=True)
    price = Column(Numeric, nullable=False)
    embedding = Column(Vector(384), nullable=True)  # For storing vector as JSON string
    picture_file_name = Column(String(500), nullable=True)

class CatalogType(Base):
    __tablename__ = 'catalog_type'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)

class CatalogBrand(Base):
    __tablename__ = 'catalog_brand'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)