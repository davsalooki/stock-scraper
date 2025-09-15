export type StockOverview = {
	exchange_code: string;
	ticker_symbol: string;
	name: string;
	last: number;
};

export type StockIdentifier = {
	exchange_code: string;
	ticker_symbol: string;
};
