<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import AddStockDialog from './AddStockDialog.svelte';
	import DataTable from './DataTable.svelte';
	import RemoveStockWarning from './RemoveStockWarning.svelte';
	import { columns } from './components/watchlist-table/columns.js';

	let { data } = $props();
	let open = $state(false)
</script>

<DataTable data={data.watchlist} {columns} />

<div class="flex space-x-1">
	<AddStockDialog />
	<Button onclick={() => open = true}>Add Stock</Button>
</div>
