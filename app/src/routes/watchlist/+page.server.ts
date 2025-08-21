import type { WatchlistItem } from './components/watchlist-table/columns.js';

export async function load() {
	// logic to fetch watchlist data here
	const watchlist: WatchlistItem[] = [
		{
			code: 'AAPL',
			name: 'Apple Inc.',
			last: 150,
			percentageChange: 1.5
		},
		{
			code: 'GOOGL',
			name: 'Alphabet Inc.',
			last: 2800,
			percentageChange: 2.3
		},
		{
			code: 'AMZN',
			name: 'Amazon.com Inc.',
			last: 3400,
			percentageChange: -0.5
		},
		{
			code: 'MSFT',
			name: 'Microsoft Corporation',
			last: 299,
			percentageChange: 1.2
		}
	];
	return {
		watchlist
	};
}
