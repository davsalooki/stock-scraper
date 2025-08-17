<script lang="ts">
	import type { ComponentProps } from 'svelte';
	import ArrowUpDownIcon from '@lucide/svelte/icons/arrow-up-down';
	import { Button } from '$lib/components/ui/button/index.js';

	interface TableSortButtonProps extends ComponentProps<typeof Button> {
		headerName: string;
	}
	let { headerName, variant = 'ghost', ...restProps }: TableSortButtonProps = $props();
</script>

<Button {variant} {...restProps}>
	{headerName}
	<ArrowUpDownIcon class="ml-2" />
</Button>
