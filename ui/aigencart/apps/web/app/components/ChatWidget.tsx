'use client';
import { useChat } from "@ai-sdk/react";
import { useState } from "react";
import { X } from "lucide-react";

export default function ChatWidget() {
  const [isOpen, setIsOpen] = useState(false);
  const { messages, input, handleInputChange, handleSubmit, isLoading } = useChat();

  return (
    <div>
      {/* Floating button */}
      <button
        className="fixed bottom-4 right-4 bg-blue-600 text-white p-3 rounded-full shadow-lg z-50 hover:bg-blue-700"
        onClick={() => setIsOpen(!isOpen)}
      >
        💬
      </button>

      {/* Chat box */}
      {isOpen && (
        <div className="fixed bottom-20 right-4 w-80 h-96 bg-white border rounded-xl shadow-lg flex flex-col z-50">
          <div className="flex items-center justify-between p-3 border-b">
            <h4 className="font-semibold">AI Assistant</h4>
            <button onClick={() => setIsOpen(false)}>
              <X className="w-5 h-5" />
            </button>
          </div>

          <div className="flex-1 overflow-y-auto p-3 space-y-2">
            {messages.map((m) => (
              <div
                key={m.id}
                className={`text-sm ${
                  m.role === "user" ? "text-right" : "text-left"
                }`}
              >
                <span
                  className={`inline-block px-3 py-2 rounded-lg ${
                    m.role === "user" ? "bg-blue-100" : "bg-gray-100"
                  }`}
                >
                  {m.content}
                </span>
              </div>
            ))}
          </div>

          <form
            onSubmit={handleSubmit}
            className="p-3 border-t flex items-center gap-2"
          >
            <input
              type="text"
              value={input}
              onChange={handleInputChange}
              className="flex-1 border rounded px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Ask me anything..."
            />
            <button
              type="submit"
              disabled={!input.trim() || isLoading}
              className="bg-blue-600 text-white px-3 py-2 rounded disabled:opacity-50"
            >
              Send
            </button>
          </form>
        </div>
      )}
    </div>
  );
}
