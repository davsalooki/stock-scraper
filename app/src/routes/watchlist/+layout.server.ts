import type { AddStockItem } from './components/add-stock-table/columns.js';
import type { WatchlistItem } from './components/watchlist-table/columns.js';

export async function load() {
	// logic to fetch watchlist data here
	const watchlist: WatchlistItem[] = [
		{
			exchange: 'NASDAQ',
			ticker: 'AAPL',
			name: 'Apple Inc.',
			last: 150,
			percentageChange: 1.5
		},
		{
			exchange: 'NASDAQ',
			ticker: 'GOOGL',
			name: 'Alphabet Inc.',
			last: 2800,
			percentageChange: 2.3
		},
		{
			exchange: 'NASDAQ',
			ticker: 'AMZN',
			name: 'Amazon.com Inc.',
			last: 3400,
			percentageChange: -0.5
		},
		{
			exchange: 'NASDAQ',
			ticker: 'MSFT',
			name: 'Microsoft Corporation',
			last: 299,
			percentageChange: 1.2
		}
	];

	const addStockItems: AddStockItem[] = watchlist.map(item => ({
		exchange: 'ASX',
		ticker: item.ticker,
		name: item.name
	}));

	const extraStockItems: AddStockItem[] = [
		{ exchange: 'ASX', ticker: 'BHP', name: 'BHP Group Ltd' },
		{ exchange: 'ASX', ticker: 'CBA', name: 'Commonwealth Bank of Australia' },
		{ exchange: 'ASX', ticker: 'WBC', name: 'Westpac Banking Corporation' },
		{ exchange: 'ASX', ticker: 'NAB', name: 'National Australia Bank Ltd' },
		{ exchange: 'ASX', ticker: 'TLS', name: 'Telstra Corporation Ltd' },
		{ exchange: 'ASX', ticker: 'WOW', name: 'Woolworths Group Ltd' },
		{ exchange: 'ASX', ticker: 'ANZ', name: 'Australia and New Zealand Banking Group Ltd' },
		{ exchange: 'ASX', ticker: 'MQG', name: 'Macquarie Group Ltd' },
		{ exchange: 'ASX', ticker: 'CSL', name: 'CSL Ltd' },
		{ exchange: 'ASX', ticker: 'QAN', name: 'Qantas Airways Ltd' },
		{ exchange: 'ASX', ticker: 'GMG', name: 'Goodman Group' },
		{ exchange: 'ASX', ticker: 'STO', name: 'Santos Ltd' },
		{ exchange: 'ASX', ticker: 'WES', name: 'Wesfarmers Ltd' },
		{ exchange: 'ASX', ticker: 'APA', name: 'APA Group' },
		{ exchange: 'ASX', ticker: 'ALL', name: 'Aristocrat Leisure Ltd' },
		{ exchange: 'ASX', ticker: 'TCL', name: 'Transurban Group' },
		{ exchange: 'ASX', ticker: 'DMP', name: 'Domino\'s Pizza Enterprises Ltd' },
		{ exchange: 'ASX', ticker: 'S32', name: 'South32 Ltd' },
		{ exchange: 'ASX', ticker: 'RIO', name: 'Rio Tinto Ltd' },
		{ exchange: 'ASX', ticker: 'FLT', name: 'Flight Centre Travel Group Ltd' },
		{ exchange: 'ASX', ticker: 'CBA', name: 'Commonwealth Bank of Australia' },
		{ exchange: 'ASX', ticker: 'BXS', name: 'Brambles Ltd' },
		{ exchange: 'ASX', ticker: 'NCM', name: 'Newcrest Mining Ltd' },
		{ exchange: 'ASX', ticker: 'COH', name: 'Cochlear Ltd' },
		{ exchange: 'ASX', ticker: 'MPL', name: 'Medibank Private Ltd' },
		{ exchange: 'ASX', ticker: 'SYC', name: 'Synergy Group Ltd' },
		{ exchange: 'ASX', ticker: 'VUK', name: 'Virgin Australia Holdings Ltd' }
	];

	addStockItems.push(...extraStockItems);

	return {
		watchlist,
		addStockItems,
		extraStockItems
	};
}
