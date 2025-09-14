<script lang="ts">
	import Button from '$lib/components/ui/button/button.svelte';
	import DialogClose from '$lib/components/ui/dialog/dialog-close.svelte';
	import AddStockTable from './add-stock-table/AddStockTable.svelte';
	import * as Dialog from '$lib/components/ui/dialog/index.js';
	import { columns } from './add-stock-table/columns.js';
	import { type AddStockItem }	from './add-stock-table/columns.js';

	let { data } = $props();

	let selectedStocks: AddStockItem[] = $state([]);
</script>

<Dialog.Root>
	<Dialog.Trigger>
		<Button variant="outline" size="lg">Add Stock</Button>
	</Dialog.Trigger>
	<Dialog.Content>
		<Dialog.Header>
			<Dialog.Title>Add stock to watchlist</Dialog.Title>
			<Dialog.Description>
				<AddStockTable {data} {columns} bind:selectedStocks/>
				<p>Selected stocks:</p>
				<ul>
					{#each selectedStocks as stock (stock.ticker)}
						<li>{stock.name}</li>
					{/each}
				</ul>
			</Dialog.Description>
			<Dialog.Footer>
				<Dialog.Close>
					<Button>Cancel</Button>
				</Dialog.Close>
				<form>
					<Button type="submit">Confirm</Button>
				</form>
			</Dialog.Footer>
		</Dialog.Header>
	</Dialog.Content>
</Dialog.Root>
