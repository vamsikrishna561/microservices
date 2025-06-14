import "@repo/ui/globals.css";
import NavBar from "./components/NavBar";
import ChatWidget from "./components/ChatWidget";

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        <NavBar />
        {children}
        <ChatWidget />
      </body>
    </html>
  );
}
