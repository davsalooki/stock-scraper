<script lang="ts">
	import AddStockDialog from './components/AddStockDialog.svelte';
	import DataTable from './components/watchlist-table/DataTable.svelte';
	import RemoveStockWarning from './components/RemoveStockWarning.svelte';
	import { columns } from './components/watchlist-table/columns.js';
	import { page } from '$app/state';

	let { data, children } = $props();

	console.log(page.params, page.route, page.url);

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
