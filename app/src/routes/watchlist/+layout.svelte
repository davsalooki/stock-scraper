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

<div class="flex h-[80vh] gap-4">
	<aside class="flex min-w-0 flex-1 flex-col">
		<div class="flex-1 overflow-auto">
			<DataTable data={data.watchlist} {columns} bind:selectedStock />
		</div>
		<div class="flex-shrink-0">
			<RemoveStockWarning {selectedStock} />
			<AddStockDialog data={data.addStockItems} />
		</div>
	</aside>

	<main class="flex min-w-0 flex-1 items-center justify-center">
		{@render children()}
	</main>
</div>
