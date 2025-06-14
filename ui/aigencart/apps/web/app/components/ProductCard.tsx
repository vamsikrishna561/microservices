// This component demonstrates a product card using Next.js, Radix UI, and Tailwind CSS.
// It is designed to be fully responsive and visually appealing.
"use client";
import Image from "next/image";
import { Product } from "@repo/ui/types/product";
import { useCartStore } from "../lib/store/cartStore";
// Define the props for the ProductCard component.
interface ProductCardProps {
  product: Product; // The product data to display in the card.
}

/**
 * ProductCard component displays a single product with its image, name, and price.
 * It uses Radix UI components for structure and Tailwind CSS for styling.
 * @param {ProductCardProps} { product } - The product object containing details.
 */
export default function ProductCard({ product }: ProductCardProps) {
  // Fallback image URL in case the provided image URL is invalid or missing.
  // Using placehold.co for a dynamic placeholder.
  const addToCart = useCartStore((state) => state.addToCart);
  const fallbackImageUrl = `https://placehold.co/400x300/e0e0e0/555555?text=No+Image`;
  const imageURL = `http://localhost:8080/pics/${product.pictureFileName}`; // Adjust this URL based on your image storage.
  return (
    <div className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition">
      <div className="relative w-full aspect-[3/2] rounded overflow-hidden mb-3">
        <Image
          src={imageURL || fallbackImageUrl}
          alt={product.name}
          fill
          sizes="(max-width: 768px) 100vw, 33vw"
          className="object-cover"
        />
      </div>

      <div className="p-2 flex flex-col">
        <h3 className="text-lg font-medium truncate">{product.name}</h3>
        <p className="mt-1 text-gray-600">${product.price.toFixed(2)}</p>
        <button
          onClick={() =>
            addToCart({
              id: product.id,
              name: product.name,
              price: product.price,
              image: product.pictureFileName,
            })
          }
          className="mt-3 bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        >
          Add to Cart
        </button>
      </div>
    </div>
  );
}
