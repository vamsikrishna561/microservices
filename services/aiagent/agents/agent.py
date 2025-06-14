from typing import Optional

#import openai
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
from agents.tools import ProductSearchResult, semantic_search_products_tool

# ollama_client = openai.OpenAI(
#     base_url="http://localhost:11434/v1",
#     api_key="sk-ollama-dummy-key" # Can be any non-empty string, or even os.getenv("OLLAMA_API_KEY", "dummy")
# )


# # --- Agent Initialization ---
# # Initialize the Pydantic AI Agent directly with the openai.OpenAI client
# product_search_agent = Agent(
#     model="ollama:dummy-model",
#    # model=ollama_client, # <--- Pass the direct openai client here!
#     # model_name="phi3:medium",
#     system_prompt=(
#         "You are an intelligent e-commerce assistant. Your sole purpose is to help users find products. "
#         "When a user asks for *any* product, or describes a product, or mentions a price, "
#         "you **MUST** use the 'search_products' tool. "
#         "Always extract the `query` and, if mentioned, the `price_limit` for the tool. "
#         "Do NOT attempt to answer product-related questions without using the tool. "
#         "Once you receive the search results, summarize them clearly, mentioning product names, "
#         "brief descriptions, and prices. If no products are found by the tool, "
#         "inform the user and suggest broadening their search or checking spelling."
#     )
# )

ollama_provider = OpenAIProvider(
    base_url="http://localhost:11434/v1",
)

# Instantiate OpenAIModel for Phi-3
phi3_model = OpenAIModel(
    model_name="llama3.1", # Ensure this is the correct model name from Ollama
    provider=ollama_provider    
)

# Initialize the agent
product_search_agent = Agent(
    phi3_model,
    system_prompt=(
        "You are an intelligent e-commerce assistant. Your primary function is to help users find products "
        "by utilizing the 'search_products' tool. When a user asks for products, or mentions a price, "
        "you MUST use the 'search_products' tool with appropriate arguments for query and price_limit. "
        "If you need more details to refine the search, ask clarifying questions. "
        "Always summarize the search results clearly, mentioning product names, descriptions (briefly), "
        "and prices. If no products are found, inform the user and suggest broadening their search."
    )
)

# Register the tool with the agent
@product_search_agent.tool_plain
async def search_products(
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
    # This acts as the public interface for the LLM to call your internal tool logic
    return await semantic_search_products_tool(query=query, price_limit=price_limit)
