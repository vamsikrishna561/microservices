from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from upload import models, database
import json
import os

app = FastAPI()
database.init_db()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_or_create_type(db: Session, type_name: str):
    catalog_type = db.query(models.CatalogType).filter_by(Name=type_name).first()
    if not catalog_type:
        catalog_type = models.CatalogType(Name=type_name)
        db.add(catalog_type)
        db.commit()
        db.refresh(catalog_type)
    return catalog_type

def get_or_create_brand(db: Session, brand_name: str):
    catalog_brand = db.query(models.CatalogBrand).filter_by(Name=brand_name).first()
    if not catalog_brand:
        catalog_brand = models.CatalogBrand(Name=brand_name)
        db.add(catalog_brand)
        db.commit()
        db.refresh(catalog_brand)
    return catalog_brand

@app.get("/load-catalog/")
def load_catalog(db: Session = Depends(get_db)):
    file_path = os.path.join(os.path.dirname(__file__), "data", "catalog.json")

    try:
        with open(file_path, "r") as f:
            items = json.load(f)

        inserted_count = 0
        for item in items:
            # Ensure CatalogType and CatalogBrand exist
            cattype = get_or_create_type(db, item["Type"])
            catbrand = get_or_create_brand(db, item["Brand"])

            # Create the CatalogItem
            catalog_item = models.CatalogItem(
                Id=item["Id"],
                Name=item["Name"],
                CatalogTypeId=cattype.Id,
                CatalogBrandId=catbrand.Id,
                AvailableStock=100,
                RestockThreshold=10,
                MaxStockThreshold=200,
                Description=item.get("Description"),
                Price=item["Price"],
                PictureFileName=f"{item["Id"]}.webp",
            )
            db.add(catalog_item)
            inserted_count += 1

        db.commit()
        return {"message": f"{inserted_count} catalog items inserted successfully."}
    except Exception as e:
        return {"error": str(e)}
