from summary_lib import *
from helpers import P

def add(chap, sub):
    chap(4, "P4 Liability-Driven & Index-Based Fixed Income", "14% of PM", 5)
    sub("Immunisation & duration basics", 5,
      P("<b>In plain words:</b> immunisation means building a bond portfolio that will be worth enough to pay a known future bill, whatever happens to interest rates. The easiest way is one zero-coupon bond maturing on the bill date. Otherwise you match <b>duration</b>, so price risk and reinvestment risk cancel.") +
      K("Macaulay duration = PV-weighted average time to cash flows; zero-coupon = its maturity",
        "If rates rise: price loss offset by higher reinvestment income (and vice versa) — for one small, immediate, parallel shift",
        "Modified duration = Macaulay ÷ (1 + periodic yield) → better for immediate price change; Macaulay → better for immunisation timing",
        "Use <b>portfolio statistics from aggregate cash flows</b> (portfolio IRR, duration, dispersion, convexity), not market-value weighted averages; same only if curve is flat; with upward slope the cash-flow IRR and duration are higher",
        "Goal = earn the initial <b>portfolio IRR</b>, not average YTM") +
      F("%ΔValue ≈ −MD × ΔY + ½ × C × (ΔY)²\nBPV (PVBP, 'value of an 01') = MD × Value × 0.0001"))
    sub("Single-liability immunisation rules & structural risk", 5,
      F("1. PV assets ≥ PV liability\n2. Macaulay duration of assets = liability due date\n3. <b>Minimise</b> convexity (least dispersion of asset cash flows around the liability)\n4. Rebalance regularly (trade-off with transaction costs)") +
      T(["Curve move (barbell assets around bullet liability)","Effect"],
        [["Parallel shift up or down","Assets beat liability (asset convexity &gt; liability) → OK"],
         ["Steepening twist","PV assets falls below PV liability → risk (may still work if IRR rises enough)"],
         ["Flattening twist","PV assets rises but IRR falls → risk"],
         ["Positive butterfly (wings up, middle down)","PV assets ↓, PV liability ↑ → significant risk"],
         ["Negative butterfly","PV assets ↑, PV liability ↓ → favourable but not guaranteed"]]) +
      K("Immunisation = <b>zero replication</b>: success if portfolio IRR moves like the replicating zero's yield",
        "Parallel shift is <b>sufficient but not necessary</b> for success","Not buy-and-hold: coupon bond duration falls slower than the liability's → rebalance") +
      TRAP("Minimise convexity for a single liability — positive convexity is good for price, but more dispersion means more structural risk."))
    sub("Multiple liabilities: cash-flow vs duration matching", 5,
      T(["Method","How","Notes"],
        [["Cash-flow matching (dedication)","Bonds whose coupons/principal match each payment","Can legally <b>defease</b> (remove from balance sheet) with govt bonds; costly"],
         ["Duration matching","Match <b>BPV</b> of assets and liabilities","Cheaper, flexible; structural risk"],
         ["Contingent immunisation","Manage actively while surplus &gt; 0; immunise if surplus hits zero","Needs a significant surplus"]]) +
      F("Multiple-liability rules: 1. PV A ≥ PV L  2. BPV A = BPV L  3. Asset dispersion &amp; convexity <b>exceed</b> liabilities (but not by much)  4. Rebalance") +
      F("UK company: Portfolio B — BPV closely matches, convexity slightly above liabilities → best\nExpect very large parallel shifts → Portfolio C (much higher convexity) despite weaker BPV match") +
      TRAP("Single liability: minimise convexity. Multiple liabilities: asset convexity must be <b>greater</b> than liability convexity, but minimised subject to that."))
    sub("Closing a duration gap with futures", 5,
      F("Futures BPV ≈ BPV_CTD ÷ CF_CTD\nNumber of contracts = (BPV_L − BPV_A) ÷ BPV_futures   → positive = BUY\nUK: gap = 218,517 − 203,456 = 15,061\n5-yr: BPV = 48.1650/0.9237 = 52.14 → buy <b>289</b> ; 10-yr: 86.7001/0.9169 = 94.56 → buy <b>159</b>\nLiability duration 8.99 → 10-yr contract is the closer match → less structural risk") +
      F("Pension: PBO $2.57bn, duration 9.35 → BPV_L = 2.57bn × 9.35 × 0.0001 = 2,402,950\nAssets $3.07bn: 60% equity (duration 0) + 40% bonds duration 2.85 → BPV_A = 1.228bn × 2.85 × 0.0001 = 349,980\nGap = 2,052,970 ; CTD BPV 128.98, CF 0.9436 → contract BPV 136.69\n100% hedge: buy ≈ 15,019 ; expect rates ↓ → overhedge (110%) ≈ 16,521 ; expect rates ↑ → underhedge (90%) ≈ 13,517") +
      K("CTD = cheapest-to-deliver; seller delivers 100,000 par, buyer pays price × conversion factor; Ultra 10-year narrows deliverables",
        "Each 1/32 move = $31.25 per contract → daily margin cash flows → 100% hedges are rare in practice",
        "Equity duration assumed zero","ABO (legal, if closed now) &lt; PBO (ongoing plan — usually more realistic)") +
      TRAP("Assets' BPV below liabilities' → <b>buy</b> futures / receive fixed. Expect rates to rise → hedge <b>less</b>; expect rates to fall → hedge <b>more</b>."))
    sub("Swaps, swaptions and collars for the duration gap", 5,
      F("Swap BPV per 100 notional = (D_fixed − D_floating) × 100 × 0.0001\nNotional = BPV gap ÷ (swap BPV / 100)\nPension: (9.18 − 0.25) × 0.01 = 0.0893 → NP = 2,052,970 / 0.000893 ≈ <b>$2.30bn</b> receive-fixed\nRange 30–70%: expect rates ↑ → 30% = $0.69bn ; then expect ↓ → 70% = $1.61bn (add $0.92bn)\nQuiz: gap $300,000, D 8.25 and 0.5 → BPV 0.0775 → NP = <b>$387m</b>") +
      F("US plan: gap 450,000, swap BPV 0.2571 per 100 → 50% hedge = 450,000 × 0.5 / 0.002571 = <b>$87.5m</b> receive-fixed\nWant 35% if rates rise → buy <b>payer</b> swaption on 15% = $26.25m; premium 55 bp = <b>$144,397</b>\nExercise if new swap rates &gt; 2.7% strike") +
      T(["Need more asset duration — choice","Optimal when new swap fixed rate (SFR) is…"],
        [["Receive-fixed swap at 2.5%","≤ 2.5% (rates fall)"],["Collar: buy 2.3% receiver + sell 3.3% payer (zero cost)","Between 2.5% and 3.3%"],["Buy 2.3% receiver swaption","Well above 3.3% (cost capped at premium)"]]) +
      K("Receive-fixed = + duration; pay-fixed = − duration","Payer/receiver always describe the <b>buyer's</b> fixed leg","Swaption premium is sunk — ignore it in the exercise decision",
        "Swaps now often margined → same cash-flow issues as futures"))
    sub("LDI risks", 4,
      K("Duration-only hedges ignore convexity","Duration assumes parallel shifts","Curve twists → structural risk",
        "Model risk in estimating DB liabilities","Measurement error from weighted averages","CTD can change → futures BPV changes",
        "<b>Spread risk</b>: asset (govt/swap) rate vs liability (corporate) discount rate move differently","Counterparty risk (OTC)","Collateral/margin cash-flow risk","Asset liquidity risk"))
    sub("Bond indexing: why it's hard & how to match", 5,
      K("Bond market huge, issues varied → full replication impractical","Issuers have many issues of different liquidity","OTC dealer market; post-2008 capital rules → less inventory, wider spreads",
        "Most bonds don't trade → <b>matrix / evaluated pricing</b>","Index composition changes quickly") +
      T(["Match","Controls"],
        [["Modified (effective, if options) duration","Parallel shifts"],["<b>Key rate durations</b> / PV distribution of cash flows","<b>Non-parallel</b> shifts"],
         ["Sector &amp; quality weights; spread duration","Spread changes"],["Sector/coupon/maturity cells; callable/MBS weights","Convexity, options"],["Issuer exposure","Event risk"]]) +
      K("Enhanced indexing: match risk factors, not holdings; <b>stratified sampling / cell matching</b>; can include ESG exclusions/inclusions",
        "Add value: cut costs · tilt to cheap sectors/curve points (avoid spread widening) · overweight callables when rate volatility expected low"))
    sub("Passive exposure alternatives & benchmark choice", 4,
      T(["Vehicle","Points"],
        [["Separately managed (full/enhanced index)","Control; high cost"],["Index mutual fund","Small investors; daily NAV; fees, loads; never matures"],
         ["ETF","Trades all day; authorised participants create/redeem in kind → arbitrage (weaker for illiquid bonds)"],
         ["Total return swap","Receive index total return, pay MRR + spread = buying index with borrowed money; leveraged if not collateralised; counterparty risk; negative returns paid by receiver"]]) +
      K("Start from objectives/constraints → strategic allocation → index","Static portfolio duration falls as bonds age","Issuance shifts change index duration",
        "Custom 'smart beta' benchmark, e.g. <b>credit barbell</b>: long Treasuries for duration + short corporates for spread"))
