from typing import Any
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from upload import models, database
from sentence_transformers import SentenceTransformer
import json
import os
from agents.agent import product_search_agent

encoder = SentenceTransformer("all-MiniLM-L6-v2")

app = FastAPI()
database.init_db()

class QueryInput(BaseModel):
    query: str

class APIResponse(BaseModel):
    result: Any # Can be str, ProductSearchResult, etc.

@app.post("/query", response_model=APIResponse)
async def ask(query_input: QueryInput):
    """
    Processes a natural language query using the AI agent to search for products semantically.
    """
    try:
        agent_result = await product_search_agent.run(query_input.query)
        return {"result": agent_result.output}
    except Exception as e:
        print(f"Error processing query in API endpoint: {e}")
        # Return a more user-friendly error message
        return {"result": f"An error occurred while processing your request: {str(e)}"}


def get_embedding(name: str, description: str | None):
    # Combine name and description, handle missing description
    text = name
    if description:
        text += " " + description
    embedding = encoder.encode(text)
    return embedding.tolist()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_or_create_type(db: Session, type_name: str):
    catalog_type = db.query(models.CatalogType).filter_by(name=type_name).first()
    if not catalog_type:
        catalog_type = models.CatalogType(name=type_name)
        db.add(catalog_type)
        db.commit()
        db.refresh(catalog_type)
    return catalog_type

def get_or_create_brand(db: Session, brand_name: str):
    catalog_brand = db.query(models.CatalogBrand).filter_by(name=brand_name).first()
    if not catalog_brand:
        catalog_brand = models.CatalogBrand(name=brand_name)
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
                id=item["Id"],
                name=item["Name"],
                catalogtype_id=cattype.id,
                catalogbrand_id=catbrand.id,
                available_stock=100,
                restock_threshold=10,
                max_stock_threshold=200,
                description=item.get("Description"),
                price=item["Price"],
                picture_file_name=f"{item["Id"]}.webp",
                embedding=get_embedding(item["Name"], item.get("Description"))
            )
            db.add(catalog_item)
            inserted_count += 1

        db.commit()
        return {"message": f"{inserted_count} catalog items inserted successfully."}
    except Exception as e:
        return {"error": str(e)}

@app.get("/search_products")
def search_products(q: str, max_price: float = None,db: Session = Depends(get_db)):
    query_embedding = encoder.encode(q).tolist()
    # SQL to do vector search + price filter
    sql = """
    SELECT id, name, price, embedding <=> :query_embedding AS distance
    FROM catalog
    WHERE (:max_price IS NULL OR price <= :max_price)
    ORDER BY distance
    LIMIT 10
    """
    result = db.execute(text(sql), {"query_embedding": query_embedding, "max_price": max_price})
    return [dict(row) for row in result]
