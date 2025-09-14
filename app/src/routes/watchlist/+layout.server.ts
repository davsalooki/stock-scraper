import type { AddStockItem } from './components/add-stock-table/columns.js';
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

	const addStockItems: AddStockItem[] = watchlist.map(item => ({
		exchange: 'ASX',
		code: item.code,
		name: item.name
	}));

	const extraStockItems: AddStockItem[] = [
		{ exchange: 'ASX', code: 'BHP', name: 'BHP Group Ltd' },
		{ exchange: 'ASX', code: 'CBA', name: 'Commonwealth Bank of Australia' },
		{ exchange: 'ASX', code: 'WBC', name: 'Westpac Banking Corporation' },
		{ exchange: 'ASX', code: 'NAB', name: 'National Australia Bank Ltd' },
		{ exchange: 'ASX', code: 'TLS', name: 'Telstra Corporation Ltd' },
		{ exchange: 'ASX', code: 'WOW', name: 'Woolworths Group Ltd' },
		{ exchange: 'ASX', code: 'ANZ', name: 'Australia and New Zealand Banking Group Ltd' },
		{ exchange: 'ASX', code: 'MQG', name: 'Macquarie Group Ltd' },
		{ exchange: 'ASX', code: 'CSL', name: 'CSL Ltd' },
		{ exchange: 'ASX', code: 'QAN', name: 'Qantas Airways Ltd' },
		{ exchange: 'ASX', code: 'GMG', name: 'Goodman Group' },
		{ exchange: 'ASX', code: 'STO', name: 'Santos Ltd' },
		{ exchange: 'ASX', code: 'WES', name: 'Wesfarmers Ltd' },
		{ exchange: 'ASX', code: 'APA', name: 'APA Group' },
		{ exchange: 'ASX', code: 'ALL', name: 'Aristocrat Leisure Ltd' },
		{ exchange: 'ASX', code: 'TCL', name: 'Transurban Group' },
		{ exchange: 'ASX', code: 'DMP', name: 'Domino\'s Pizza Enterprises Ltd' },
		{ exchange: 'ASX', code: 'S32', name: 'South32 Ltd' },
		{ exchange: 'ASX', code: 'RIO', name: 'Rio Tinto Ltd' },
		{ exchange: 'ASX', code: 'FLT', name: 'Flight Centre Travel Group Ltd' },
		{ exchange: 'ASX', code: 'CBA', name: 'Commonwealth Bank of Australia' },
		{ exchange: 'ASX', code: 'BXS', name: 'Brambles Ltd' },
		{ exchange: 'ASX', code: 'NCM', name: 'Newcrest Mining Ltd' },
		{ exchange: 'ASX', code: 'COH', name: 'Cochlear Ltd' },
		{ exchange: 'ASX', code: 'MPL', name: 'Medibank Private Ltd' },
		{ exchange: 'ASX', code: 'SYC', name: 'Synergy Group Ltd' },
		{ exchange: 'ASX', code: 'VUK', name: 'Virgin Australia Holdings Ltd' }
	];

	addStockItems.push(...extraStockItems);

	return {
		watchlist,
		addStockItems,
		extraStockItems
	};
}
