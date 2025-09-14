import { getPayoutMultiplier, getRetentionMultiplier } from "./multipliers";

export function calculateIntrinsicValue(equity: number, shares: number, roe: number, eps: number, dps: number, requiredReturn: number): number {
  const payoutRatio = dps / eps;
  const payoutMultiplier = getPayoutMultiplier(roe, requiredReturn);
  const retentionMultiplier = getRetentionMultiplier(roe, requiredReturn);

  const equityPerShare = equity / shares;

  const intrinsicValue = equityPerShare * payoutMultiplier * payoutRatio + equityPerShare * retentionMultiplier * (1 - payoutRatio);
  return intrinsicValue;
}

