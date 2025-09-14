<script lang="ts">
	import AddStockDialog from './components/AddStockDialog.svelte';
	import DataTable from './components/watchlist-table/DataTable.svelte';
	import RemoveStockWarning from './components/RemoveStockWarning.svelte';
	import { columns } from './components/watchlist-table/columns.js';
	import StockInfo from './components/StockInfo.svelte';

	let { data } = $props();
	let selectedStockCode = $state<string | undefined>();
</script>

<DataTable data={data.watchlist} {columns} bind:selectedStockCode />

<div class="flex space-x-1">
	<RemoveStockWarning {selectedStockCode} />
	<AddStockDialog data={data.addStockItems} />
	<StockInfo />
</div>
