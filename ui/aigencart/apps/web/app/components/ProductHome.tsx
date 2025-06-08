import { Product } from "@repo/ui/types/product";
import SidebarFilters from "./SidebarFilters";
import ProductCard from "./ProductCard";

interface ProductProps {
  products: Product[]; // The product data to display in the card.
}
export default function ProductHome({  products}: ProductProps) {
  // Fallback image URL in case the provided image URL is invalid or missing.
  return (<><aside className="w-64 hidden lg:block">
        <SidebarFilters />
      </aside>
      <section className="flex-1">
        {/* Sort bar */}
        <div className="flex justify-between items-center mb-6">
          <h2 className="text-2xl font-bold">Shop All</h2>
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