export async function load({ params }) {
    const exchange = params.exchange;
    const stock = params.stock;
    const financials = await getStockFinancials(exchange, stock);


    return { financials };
}

const url = 'http://localhost:8000';

async function getStockFinancials(exchange: string, stock: string) {
    const res = await fetch(`${url}/stocks/${exchange}/${stock}/financials`);
    const data = await res.json();
    return data;
}
