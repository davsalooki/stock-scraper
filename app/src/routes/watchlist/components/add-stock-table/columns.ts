import { type ColumnDef } from '@tanstack/table-core';
import { renderComponent } from '$lib/components/ui/data-table/index.js';
import SortButton from './TableSortButton.svelte';
import { Checkbox } from '$lib/components/ui/checkbox';

// This type is used to define the shape of our data.
// You can use a Zod schema here if you want.
export type AddStockItem = {
	exchange: string;
	code: string;
	name: string;
};

export const columns: ColumnDef<AddStockItem>[] = [
	{
		id: "select",
		header: ({ table }) =>
		renderComponent(Checkbox, {
			checked: table.getIsAllPageRowsSelected(),
			indeterminate:
			table.getIsSomePageRowsSelected() &&
			!table.getIsAllPageRowsSelected(),
			onCheckedChange: (value) => table.toggleAllPageRowsSelected(!!value),
			"aria-label": "Select all",
		}),
		cell: ({ row }) =>
		renderComponent(Checkbox, {
			checked: row.getIsSelected(),
			onCheckedChange: (value) => row.toggleSelected(!!value),
			"aria-label": "Select row",
		}),
		enableSorting: false,
		enableHiding: false,
	},
	{
		accessorKey: 'exchange',
		header: 'Exchange',
	},
	{
		accessorKey: 'code',
		header: ({ column }) =>
			renderComponent(SortButton, {
				headerName: 'Code',
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
	}
];
