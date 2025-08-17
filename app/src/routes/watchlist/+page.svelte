<script lang="ts">
	import DataTable from './DataTable.svelte';
	import { columns } from './columns.js';

	let { data } = $props();
</script>

<DataTable data={data.watchlist} {columns} />
