import { type ColumnDef } from '@tanstack/table-core';
import { renderComponent } from '$lib/components/ui/data-table/index.js';
import SortButton from './TableSortButton.svelte';

// This type is used to define the shape of our data.
// You can use a Zod schema here if you want.
export type WatchlistItem = {
	exchange: string;
	ticker: string;
	name: string;
	last: number;
	percentageChange: number;
};

export const columns: ColumnDef<WatchlistItem>[] = [
	{
		accessorKey: 'exchange',
		header: 'Exchange',
	},
	{
		accessorKey: 'ticker',
		header: ({ column }) =>
			renderComponent(SortButton, {
				headerName: 'Ticker',
				onclick: column.getToggleSortingHandler()
			}),
	},
	{
		accessorKey: 'name',
		header: ({ column }) =>
			renderComponent(SortButton, {
				headerName: 'Name',
				onclick: column.getToggleSortingHandler()
			}),
	},
	{
		accessorKey: 'last',
		header: 'Last Price'
	},
	{
		accessorKey: 'percentageChange',
		header: 'Change %'
	}
];
