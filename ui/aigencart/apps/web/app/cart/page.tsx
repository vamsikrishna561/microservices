'use client'
import { useCartStore } from '../lib/store/cartStore'

export default function CartPage() {
  const { items, removeFromCart, updateQuantity } = useCartStore()

  const total = items.reduce((sum, item) => sum + item.price * item.quantity, 0)
  const fallbackImageUrl = `https://placehold.co/400x300/e0e0e0/555555?text=No+Image`;
  return (
    <div className="max-w-3xl mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Shopping Cart</h1>
      {items.length === 0 ? (
        <p>Your cart is empty.</p>
      ) : (
        <>
          {items.map((item) => (
            <div key={item.id} className="flex items-center gap-4 border-b py-4">
              <img src={item.image ? `http://localhost:8080/pics/${item.image}` : fallbackImageUrl} alt={item.name} className="w-20 h-20 object-cover" />
              <div className="flex-1">
                <h2 className="text-lg font-semibold">{item.name}</h2>
                <p>${item.price.toFixed(2)}</p>
                <input
                  type="number"
                  value={item.quantity}
                  onChange={(e) => updateQuantity(item.id, parseInt(e.target.value))}
                  className="w-16 border rounded p-1 mt-1"
                  min="1"
                />
              </div>
              <button
                onClick={() => removeFromCart(item.id)}
                className="text-red-600 font-medium"
              >
                Remove
              </button>
            </div>
          ))}
          <div className="text-right font-bold text-xl mt-4">Total: ${total.toFixed(2)}</div>
        </>
      )}
    </div>
  )
}
