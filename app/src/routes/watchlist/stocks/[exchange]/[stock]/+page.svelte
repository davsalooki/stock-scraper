<script lang="ts">
	import { Slider } from '$lib/components/ui/slider/index.js';
	import { calculateIntrinsicValue } from '$lib/instrinsic-value/calculation.js';
	import { maxDate } from '@internationalized/date';

	let { data } = $props();

	const equityPerShare = $derived(data.financials.stats.bookValue);
	const roe = $derived(data.financials.stats.returnEquity);
	const eps = $derived(data.financials.stats.earnings);
	const dps = $derived(data.financials.stats.dividends);
	let requiredReturn = $state(10);

	const intrinsicValue = $derived.by(() => {
		console.log('Calculating intrinsic value with:', {
			equityPerShare,
			shares: 1,
			roe: Math.min(roe, 60),
			eps,
			dps,
			requiredReturn
		});
		return calculateIntrinsicValue({
			equity: equityPerShare,
			shares: 1,
			roe: Math.min(roe, 60),
			eps,
			dps,
			requiredReturn
		});
	});
</script>

<div>
	<div class="mb-4 flex items-center gap-4">
		<p>Intrinsic value: {Math.round(intrinsicValue * 100) / 100}</p>
		<p>Required return: {requiredReturn}</p>
		<div class="flex-1">
			<Slider type="single" min={4} max={15} step={1} bind:value={requiredReturn} />
		</div>
	</div>

	<img src={data.financials.earnings_roe_chart} alt="Earnings and Return on Equity Chart" />

	{#if roe > 60}
		<div class="basis-1/4 p-5 text-center text-red-500">
			<p>Warning: ROE is very high ({roe}%), capping at 60% for intrinsic value calculation.</p>
		</div>
	{/if}
</div>
