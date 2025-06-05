from pydantic import BaseModel
from typing import Optional

class CatalogItemCreate(BaseModel):
    Name: str
    CatalogTypeId: int
    CatalogBrandId: int
    AvailableStock: int
    OnReorder: bool
    RestockThreshold: int
    MaxStockThreshold: int
    Description: Optional[str]
    Price: float
    PictureFileName: Optional[str]
