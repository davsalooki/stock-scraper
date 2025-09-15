<script lang="ts">
	import AddStockDialog from './components/AddStockDialog.svelte';
	import DataTable from './components/watchlist-table/DataTable.svelte';
	import RemoveStockWarning from './components/RemoveStockWarning.svelte';
	import { columns, type WatchlistItem } from './components/watchlist-table/columns.js';
	import { page } from '$app/state';
	import type { AddStockItem } from './components/add-stock-table/columns';
	import type { Snippet } from 'svelte';

	type WatchlistProps = {
		data: {
			watchlist: WatchlistItem[];
			addStockItems: AddStockItem[];
		};
		children: Snippet;
	};
	let { data, children }: WatchlistProps = $props();

	let selectedStock = $state<StockIdentifier | null>(null);
	if (page.url.pathname.includes('stocks')) {
		selectedStock = {
			exchange: page.params.exchange,
			ticker: page.params.stock
		};
	}
</script>

<DataTable data={data.watchlist} {columns} bind:selectedStock={selectedStock} />

<div class="flex space-x-1">
	<RemoveStockWarning selectedStock={selectedStock} />
	<AddStockDialog data={data.addStockItems} />
</div>

{@render children()}
