<script lang="ts">
	import * as AlertDialog from '$lib/components/ui/alert-dialog/index.js';
	import Button from '$lib/components/ui/button/button.svelte';

	type RemoveStockProps = {
		selectedStock: StockIdentifier | null;
	};

	const { selectedStock }: RemoveStockProps = $props();
</script>

<AlertDialog.Root>
	<AlertDialog.Trigger disabled={selectedStock == null}>
		<Button disabled={selectedStock == null}>Delete</Button>
	</AlertDialog.Trigger>
	<AlertDialog.Content>
		<AlertDialog.Header>
			<AlertDialog.Title>Are you absolutely sure?</AlertDialog.Title>
			<AlertDialog.Description>
				You are deleting {selectedStock?.exchange}:{selectedStock?.ticker} from your watchlist.
			</AlertDialog.Description>
		</AlertDialog.Header>
		<AlertDialog.Footer>
			<AlertDialog.Cancel>Cancel</AlertDialog.Cancel>
			<form method="POST" action="?/delete">
				<input type="hidden" name="exchange" value={selectedStock?.exchange} />
				<input type="hidden" name="ticker" value={selectedStock?.ticker} />
				<AlertDialog.Action>Confirm</AlertDialog.Action>
			</form>
			
		</AlertDialog.Footer>
	</AlertDialog.Content>
</AlertDialog.Root>
