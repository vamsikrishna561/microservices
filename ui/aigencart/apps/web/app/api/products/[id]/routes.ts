import { NextResponse } from 'next/server';
export async function GET(request: NextResponse) {
    try {
        const response = await fetch('http://localhost:8080/products'); // Replace with your actual API endpoint
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const product = await response.json();
        return NextResponse.json(product);
    } catch (error) {
        console.error('Error fetching product:', error);
        return NextResponse.json({ error: 'Failed to fetch product' }, { status: 500 });
    }
}