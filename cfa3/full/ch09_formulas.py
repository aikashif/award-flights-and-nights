from summary_lib import *
from helpers import P

def add(chap, sub):
    chap("F", "Formula Sheet (all readings)", "revise last", 5)
    sub("Equity (P1–P3)", 5,
      F("Tracking error = SD(Rₚ − Rᵦ)\nE(R_A) = IC × √BR × σ_A × TC\nActive Share = ½ Σ |wₚᵢ − wᵦᵢ|\nContribution to variance CVᵢ = wᵢ × Cov(rᵢ, rₚ) ; % = CVᵢ / σₚ²\nContribution to active variance = (wₚᵢ − wᵦᵢ) × Σⱼ (wₚⱼ − wᵦⱼ) Cov(RAᵢ, RAⱼ)\nGross exposure = long + |short| ; net = long − short\nR_g ≈ R_a − σ²/2"))
    sub("Liability-driven & yield curve (P4–P5)", 5,
      F("MD = Macaulay duration / (1 + periodic YTM)\n%ΔValue ≈ −MD × ΔY + ½ C (ΔY)²\nBPV = MD × value × 0.0001\nFutures BPV ≈ BPV_CTD / CF_CTD ; contracts = (BPV_L − BPV_A) / BPV_futures\nSwap NP = BPV gap / swap BPV per 1 of notional ; swap BPV = (D_fixed − D_float) × 0.0001\nEffective duration = (PV₋ − PV₊) / (2 × Δcurve × PV₀)\nEffective convexity = (PV₋ + PV₊ − 2PV₀) / (Δcurve² × PV₀)\nKey rate duration = −(ΔPV / PV) / Δkey rate\nButterfly spread = −short + 2 × medium − long\nR_DC = (1 + R_FC)(1 + R_FX) − 1\nForward (CIRP) F = S × [(1 + r_DC)/(1 + r_FC)]^T") +
      K("Bonds with options: use effective, not modified, duration"))
    sub("Credit (P6)", 5,
      F("Credit spread ≈ POD × LGD\nEffSpreadDur = (PV₋ − PV₊) / (2 × Δspread × PV₀)\nEffSpreadCon = (PV₋ + PV₊ − 2PV₀) / (Δspread² × PV₀)\n%Δprice ≈ −EffSpreadDur × Δs + ½ × EffSpreadCon × (Δs)²\n%Δrelative value ≈ −spread duration × Δspread\nDTS = EffSpreadDur × spread\nExpected excess spread ≈ spread − (EffSpreadDur × Δspread) − (POD × LGD)\nFRN discount margin: price from (MRR + DM) vs coupon MRR + QM\nCDS price ≈ (fixed coupon − CDS spread) × EffSpreadDur_CDS"))
    sub("Trading (P7)", 5,
      F("IS = paper return − actual return\n= delay + trading (execution) + opportunity cost + fixed fees\nCost (bp) = Side × (P_exec − P_bench)/P_bench × 10,000   (buy +1, sell −1)\nMarket-adjusted cost = arrival cost − β × index cost\nAdded value = arrival cost − pre-trade estimated cost  (negative = trader added value)"))
