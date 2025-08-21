<script lang="ts">
	import * as AlertDialog from '$lib/components/ui/alert-dialog/index.js';
	import Button from '$lib/components/ui/button/button.svelte';
	const { selectedStockCode } = $props();
</script>

<AlertDialog.Root>
	<AlertDialog.Trigger disabled={selectedStockCode == null}>
		<Button disabled={selectedStockCode == null}>Delete</Button>
	</AlertDialog.Trigger>
	<AlertDialog.Content>
		<AlertDialog.Header>
			<AlertDialog.Title>Are you absolutely sure?</AlertDialog.Title>
			<AlertDialog.Description>
				You are deleting {selectedStockCode} from your watchlist.
			</AlertDialog.Description>
		</AlertDialog.Header>
		<AlertDialog.Footer>
			<form>
				<AlertDialog.Cancel>Cancel</AlertDialog.Cancel>
				<AlertDialog.Action>Confirm</AlertDialog.Action>
			</form>
		</AlertDialog.Footer>
	</AlertDialog.Content>
</AlertDialog.Root>
