import type { Actions } from "./$types";

export async function load({ params }) {
    const exchange = params.exchange;
    const stock = params.stock;
    const financials = await getStockFinancials(exchange, stock);


    return { financials };
}

const url = 'http://localhost:8000';

async function getStockFinancials(exchange: string, stock: string) {
    const res = await fetch(`${url}/stocks/${exchange}/${stock}/financials`);
    const data = await res.json();
    return data;
}

export const actions: Actions = {
	delete: async ({ request }) => {
		const formData = await request.formData();
		const exchange = formData.get('exchange');
		const ticker = formData.get('ticker');

		// logic to delete the stock from the watchlist
        const res = await fetch(`${url}/watchlist/stocks/${exchange}/${ticker}`, {
            method: 'DELETE'
        });
        if (!res.ok) {
            return { success: false, message: 'Failed to delete stock from watchlist' };
        }
        return { success: true, message: 'Stock deleted from watchlist' };
	}
}
