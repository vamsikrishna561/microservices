// 'use client';
import { Product } from "@repo/ui/types/product";
import SidebarFilters from "./SidebarFilters";
import ProductCard from "./ProductCard";
import ChatWidget from "./ChatWidget";
// import { useState } from "react";

interface ProductProps {
  products: Product[]; // The product data to display in the card.
}
export default function ProductHome({  products}: ProductProps) {
  //  const [searchTerm, setSearchTerm] = useState("");

  // // Filter products based on search term (case insensitive)
  // const filteredProducts = products.filter((p) =>
  //   p.name.toLowerCase().includes(searchTerm.toLowerCase())
  // );
  // Fallback image URL in case the provided image URL is invalid or missing.
  return (<><aside className="w-64 hidden lg:block">
        <SidebarFilters />
      </aside>
      <section className="flex-1">
        {/* Sort bar */}
        <div className="flex justify-between items-center mb-6 space-x-4">
          <h2 className="text-2xl font-bold">Shop All</h2>
                      <input
              type="text"
              placeholder="Search products..."
              className="border rounded px-3 py-1 flex-grow"
              //value={searchTerm}
              //onChange={(e) => setSearchTerm(e.target.value)}
              aria-label="Search products"
            />
          <select className="border rounded px-3 py-1">
            <option>Featured</option>
            <option>Price: Low to High</option>
            {/* More */}
          </select>
        </div>

        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-6">
          {products.map((p) => (
            <ProductCard key={p.id} product={p} />
          ))}
        </div>
        
      </section></>);
}