import { Product } from "@repo/ui/types/product";
import React from "react";
import ProductHome from "./components/ProductHome";
import ChatWidget from "./components/ChatWidget";
async function fetchProducts(): Promise<Product[]> {
  try {
    const res = await fetch("http://localhost:8080/product/items"); // Adjust the URL as needed
    if (!res.ok) {
      throw new Error("Failed to fetch products");
    }
    const data = await res.json();
    return data;
  } catch (error) {
    console.error("Error fetching products:", error);
    throw error; // Re-throw the error to be handled by the caller
  }
}
export default async function Home() {
  const data = await fetchProducts(); // Fetch products from the Spring Boot Catalog API
  // Placeholder API endpoint. Replace with your actual Spring Boot Catalog API endpoint.

  return (
    <div className="flex max-w-7xl mx-auto px-4 py-8 gap-8">
      <ProductHome products={data}></ProductHome>
      
    </div>
  );
}
