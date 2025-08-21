<script lang="ts">
	import Button from '$lib/components/ui/button/button.svelte';
	import DialogClose from '$lib/components/ui/dialog/dialog-close.svelte';
	import * as Dialog from '$lib/components/ui/dialog/index.js';
</script>

<Dialog.Root>
	<Dialog.Trigger>
		<Button variant="outline" size="lg">Add Stock</Button>
	</Dialog.Trigger>
	<Dialog.Content>
		<Dialog.Header>
			<Dialog.Title>Add stock to watchlist</Dialog.Title>
			<Dialog.Description>
				This action cannot be undone. This will permanently delete your account and remove your data
				from our servers.
			</Dialog.Description>
			<Dialog.Footer>
				<Dialog.Close>
					<Button>Cancel</Button>
				</Dialog.Close>
			</Dialog.Footer>
		</Dialog.Header>
	</Dialog.Content>
</Dialog.Root>
