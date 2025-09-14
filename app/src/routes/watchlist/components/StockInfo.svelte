<script lang="ts">
    import { onMount } from 'svelte';
    import selectedStockCode from '../+page.svelte';
    let stockInfo = $state<{ price: number; variation: string; volume: number } | null>(null);

    // onMount(async () => {
    //     stockInfo = await getStockInfo(selectedStockCode);
    // });

    // derived intrinsic value
</script>

<table>
  <tbody>
    <tr><th>Price</th><td>$100</td></tr>
    <tr><th>Variation</th><td>+2%</td></tr>
    <tr><th>Volume</th><td>5000</td></tr>
  </tbody>
</table>