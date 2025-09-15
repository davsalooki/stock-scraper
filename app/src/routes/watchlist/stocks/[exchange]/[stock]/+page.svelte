<script lang="ts">
	import { Slider } from '$lib/components/ui/slider/index.js';
	import { calculateIntrinsicValue } from '$lib/instrinsic-value/calculation.js';

    let { data } = $props();

    const equityPerShare = $derived(data.financials.stats.bookValue);
    const roe = $derived(data.financials.stats.returnEquity);
    const eps = $derived(data.financials.stats.earnings);
    const dps = $derived(data.financials.stats.dividends);
    let requiredReturn = $state(10);

    const intrinsicValue = $derived.by(() => {
        return calculateIntrinsicValue({
            equity: equityPerShare,
            shares: 1,
            roe,
            eps,
            dps,
            requiredReturn
        });
    });
</script>

<p>Intrinsic value: {intrinsicValue}</p>
<p>Required return: {requiredReturn}</p>
<Slider type="single" min={4} max={15} step={1} bind:value={requiredReturn} />

<img src={data.financials.earnings_roe_chart} alt="Earnings and Return on Equity Chart" />
