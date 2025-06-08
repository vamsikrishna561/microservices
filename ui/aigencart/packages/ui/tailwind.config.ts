import type { Config } from "tailwindcss";

export const config = {
  darkMode: ["class", "dark"],
  content: [
    "./pages/**/*.{ts,tsx}",
    "./components/**/*.{ts,tsx}",
    "./app/**/*.{ts,tsx}",
    "./src/**/*.{ts,tsx}",
    "../../packages/ui/src/**/*.{ts,tsx}",
  ],
  prefix: "ui-",
  theme: {
    extend: {
    },
  },
  plugins: [],
} satisfies Config;

export default config;