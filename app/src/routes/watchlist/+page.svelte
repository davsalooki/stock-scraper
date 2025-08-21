<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import AddStockDialog from './components/AddStockDialog.svelte';
	import DataTable from './components/watchlist-table/DataTable.svelte';
	import RemoveStockWarning from './components/RemoveStockWarning.svelte';
	import { columns } from './components/watchlist-table/columns.js';

	let { data } = $props();
	let open = $state(false)
	let selectedStockCode = $state<string | null>(null);
</script>

<DataTable data={data.watchlist} {columns} bind:selectedStockCode />

<div class="flex space-x-1">
	<RemoveStockWarning {selectedStockCode} />
	<Button onclick={() => open = true}>Add Stock</Button>
</div>

<input name="id" value=2 />

