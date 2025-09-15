import { redirect } from "@sveltejs/kit";
import type { Actions } from "./$types";
import { PUBLIC_API_URL } from "$env/static/public";

export async function load({ params }) {
    const exchange = params.exchange;
    const stock = params.stock;
    const financials = await getStockFinancials(exchange, stock);


    return { financials };
}

async function getStockFinancials(exchange: string, stock: string) {
    const res = await fetch(`${PUBLIC_API_URL}/stocks/${exchange}/${stock}/financials`);
    const data = await res.json();
    return data;
}

export const actions: Actions = {
	delete: async ({ request }) => {
		const formData = await request.formData();
		const exchange = formData.get('exchange');
		const ticker = formData.get('ticker');

        const res = await fetch(`${PUBLIC_API_URL}/watchlist/stocks/${exchange}/${ticker}`, {
            method: 'DELETE'
        });

        if (!res.ok) {
            return { success: false, message: 'Failed to delete stock from watchlist' };
        }
        redirect(303, '/watchlist');
	}
}
