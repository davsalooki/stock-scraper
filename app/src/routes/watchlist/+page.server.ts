import type { Actions } from '@sveltejs/kit';
import { PUBLIC_API_URL } from '$env/static/public';
import type { StockIdentifier } from './types.js';

export const actions: Actions = {
    create: async ({ request }) => {
        const formData = await request.formData();
        const stocks = formData.getAll('stocks') as string[];
        for (const stock of stocks) {
            const [exchange, ticker] = stock.split(':');
            const body: StockIdentifier = { exchange_code: exchange, ticker_symbol: ticker };

            const res = await fetch(`${PUBLIC_API_URL}/watchlist`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(body)
            });

            if (!res.ok) {
                console.error(`Failed to add stock: ${res.statusText}`);
            }
        }
    }
}
