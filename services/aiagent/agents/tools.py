import asyncio
from concurrent.futures import ThreadPoolExecutor
from pydantic import BaseModel
from typing import List, Optional
import psycopg2
from sentence_transformers import SentenceTransformer

# Load your embedding model
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

executor = ThreadPoolExecutor(max_workers=5) # Adjust max_workers as needed

# Database connection details
DB_CONFIG = {
    "dbname": "eshop",
    "user": "postgres",
    "password": "vamsi",
    "host": "localhost",
    "port": 5433
}

# --- 4. Define Pydantic Models for Tool Input/Output ---

class Product(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    # Add other relevant product fields if your DB returns them
    # e.g., category: Optional[str] = None, url: Optional[str] = None

class ProductSearchResult(BaseModel):
    products: List[Product]
    total_results: int
    search_query: str
    source: str = "semantic_product_database"
    message: str = "Search completed successfully."


async def run_db_search(sql: str, params: tuple) -> List[tuple]:
    """Runs a blocking psycopg2 query in a thread pool."""
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(
        executor,
        lambda: _execute_psycopg2_query(sql, params)
    )

def _execute_psycopg2_query(sql: str, params: tuple) -> List[tuple]:
    """Synchronous function to execute psycopg2 query."""
    conn = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        cur.execute(sql, params)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except Exception as e:
        print(f"Database error: {e}")
        if conn:
            conn.close()
        raise


async def semantic_search_products_tool(
    query: str,
    price_limit: Optional[float] = None
) -> ProductSearchResult:
    """
    Performs a semantic search for products in the database, optionally filtering by price.
    This tool uses an embedding model and vector similarity for intelligent search.

    Args:
        query (str): The natural language query for the product search (e.g., "gaming headset", "comfortable office chair").
        price_limit (float, optional): The maximum price of the product. Products above this price will be filtered out.

    Returns:
        ProductSearchResult: A structured list of matching products.
    """
    if embedding_model is None:
        print("Embedding model not loaded, cannot perform search.")
        return ProductSearchResult(
            products=[],
            total_results=0,
            search_query=query,
            message="Error: Embedding model not available."
        )

    print(f"\n[Tool Call] Semantic Search: Query='{query}', Price Limit='{price_limit}'")

    query_embedding = embedding_model.encode(query).tolist()

    # Modify SQL to filter by price directly in the DB for efficiency
    sql = """
    SELECT name, description, price
    FROM catalog
    WHERE %s IS NULL OR price <= %s -- Filter by price if price_limit is provided
    ORDER BY embedding <#> %s::vector -- <<<<<<<<<<<<<<<<<<<< MODIFIED HERE
    LIMIT 5;
    """
    sql_params = (price_limit, price_limit, query_embedding)

    try:
        rows = await run_db_search(sql, sql_params)

        results = []
        for name, desc, price in rows:
            results.append({"name": name, "description": desc, "price": price})

        # Note: total_results here would be after all filters and limits.
        # If you need total before limit, you'd need a separate COUNT query.
        return ProductSearchResult(
            products=results,
            total_results=len(results),
            search_query=query,
            message=f"Found {len(results)} products matching your criteria."
        )
    except Exception as e:
        print(f"Error during product search tool execution: {e}")
        return ProductSearchResult(
            products=[],
            total_results=0,
            search_query=query,
            message=f"An error occurred during search: {str(e)}"
        )