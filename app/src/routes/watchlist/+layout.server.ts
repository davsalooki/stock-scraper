import { PUBLIC_API_URL } from '$env/static/public';
import type { AddStockItem } from './components/add-stock-table/columns.js';
import type { WatchlistItem } from './components/watchlist-table/columns.js';
import type { StockOverview } from './types.js';

export async function load() {
	// Fetch both APIs in parallel for better performance
	const [watchlistRes, stocksRes] = await Promise.all([
		fetch(`${PUBLIC_API_URL}/watchlist`),
		fetch(`${PUBLIC_API_URL}/stocks`)
	]);

	if (!watchlistRes.ok || !stocksRes.ok) {
		throw new Error('Failed to fetch data');
	}

	const [watchlistData, stocksData]: [StockOverview[], StockOverview[]] = await Promise.all([
		watchlistRes.json(),
		stocksRes.json()
	]);

	const watchlist: WatchlistItem[] = watchlistData.map((item) => ({
		exchange: item.exchange_code,
		ticker: item.ticker_symbol,
		name: item.name,
		last: item.last
	}));

	const addStockItems: AddStockItem[] = stocksData.map((item) => ({
		exchange: item.exchange_code,
		ticker: item.ticker_symbol,
		name: item.name
	}));

	return {
		watchlist,
		addStockItems
	};
}
