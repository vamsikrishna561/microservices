'use client'
import Link from 'next/link'
import { useCartStore } from "../lib/store/cartStore";

export default function NavBar() {
  const itemCount = useCartStore((state) =>
    state.items.reduce((total, item) => total + item.quantity, 0)
  )

  return (
    <nav className="flex justify-between items-center px-6 py-4 bg-white shadow">
      <Link href="/" className="text-2xl font-bold text-gray-800">
        🏕️ Products
      </Link>
      <Link href="/cart" className="relative text-lg font-semibold">
        🛒 Cart
        {itemCount > 0 && (
          <span className="absolute -top-2 -right-3 bg-red-600 text-white text-xs px-2 py-0.5 rounded-full">
            {itemCount}
          </span>
        )}
      </Link>
    </nav>
  )
}
