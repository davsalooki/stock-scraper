import { getPayoutMultiplier, getRetentionMultiplier } from './multipliers';

interface CalculateIntrinsicValueParams {
	equity: number; // Total equity of the company
	shares: number; // Total number of shares outstanding
	roe: number; // Return on Equity (as a decimal, e.g., 0.15 for 15%)
	eps: number; // Earnings Per Share
	dps: number; // Dividends Per Share
	requiredReturn: number; // Required rate of return (as a decimal, e.g., 0.10 for 10%)
}

export function calculateIntrinsicValue({
	equity,
	shares,
	roe,
	eps,
	dps,
	requiredReturn
}: CalculateIntrinsicValueParams): number {
	const payoutRatio = dps / eps;
	const payoutMultiplier = getPayoutMultiplier(roe, requiredReturn);
	const retentionMultiplier = getRetentionMultiplier(roe, requiredReturn);
	const equityPerShare = equity / shares;
	const intrinsicValue =
		equityPerShare * payoutMultiplier * payoutRatio +
		equityPerShare * retentionMultiplier * (1 - payoutRatio);
	return intrinsicValue;
}
