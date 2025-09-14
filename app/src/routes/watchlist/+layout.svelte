<script lang="ts">
	import AddStockDialog from './components/AddStockDialog.svelte';
	import DataTable from './components/watchlist-table/DataTable.svelte';
	import RemoveStockWarning from './components/RemoveStockWarning.svelte';
	import { columns } from './components/watchlist-table/columns.js';
	import { page } from '$app/state';

	let { data, children } = $props();

	console.log(page.params, page.route, page.url);

	let selectedStockCode = $state<SelectedStock | null>(null);
	if (page.url.pathname.includes('stocks')) {
		selectedStockCode = {
			exchange: page.params.exchange,
			ticker: page.params.stock
		};
	}
</script>

<DataTable data={data.watchlist} {columns} bind:selectedStockCode />

<div class="flex space-x-1">
	<RemoveStockWarning {selectedStockCode} />
	<AddStockDialog data={data.addStockItems} />
</div>

{@render children()}
