from summary_lib import *
from helpers import P

def add(chap, sub):
    chap(4, "P4 Liability-Driven & Index-Based Fixed Income", "14% of PM", 5)
    sub("What this reading is about", 3,
      P("<b>In plain words:</b> part 1 (LDI) — hold bonds so you can pay known future bills (liabilities) whatever rates do: immunisation, duration matching, closing a 'duration gap' with futures, swaps and swaptions, and the risks left over. Part 2 — copying a bond index cheaply, other ways to get passive bond exposure, and choosing a bond benchmark.") +
      T(["LOS","Topic"],[["P4.a","Managing a single liability (immunisation)"],["P4.b","Single vs multiple liabilities; ways to implement"],
        ["P4.c","Liability strategies under rate scenarios (futures, swaps, swaptions, collars)"],["P4.d","Risks of managing against liabilities"],
        ["P4.e","Bond indexes and the challenges of indexing"],["P4.f","Passive bond exposure: funds, ETFs, total return swaps"],["P4.g","Selecting a bond benchmark"]]))
    sub("Duration refresher: Macaulay, modified, price vs reinvestment risk", 5,
      P("<b>In plain words:</b> <b>immunisation</b> = manage a bond portfolio so its value at a set date is predictable, so a known bill can be paid. The perfect tool is one default-free zero-coupon bond maturing on the bill date — no coupons to reinvest, nothing to sell early.") +
      T(["Term","Meaning"],
        [["Macaulay duration","PV-weighted average time to receive cash flows. Zero-coupon = its maturity; coupon bond &lt; maturity"],
         ["Price risk","Uncertain proceeds if you must <b>sell</b> before maturity"],
         ["Reinvestment risk","Uncertain value of coupons <b>reinvested</b> to the horizon"],
         ["Balance point","At horizon = Macaulay duration the two risks cancel — for one small, immediate, parallel rate change"],
         ["Modified duration","Macaulay ÷ (1 + periodic yield): slightly better for <b>immediate price change</b>"]]) +
      K("Rates up: price loss offset by higher reinvestment income · Rates down: price gain offset by lower reinvestment income",
        "Macaulay is slightly better for immunisation <b>timing</b>") +
      F("%ΔValue ≈ (−MD × ΔY) + (½ × C × ΔY²)"))
    sub("Portfolio statistics from aggregate cash flows", 4,
      P("<b>In plain words:</b> for liability work, compute yield, duration and convexity from the portfolio's <b>combined cash flows</b>, not as market-value-weighted averages of each bond. (You will not compute these on the exam — understand how to use them.)") +
      F("1. List every portfolio cash flow by six-month period\n2. Add cash flows in each period\n3. Portfolio IRR = rate that equates them to current market value\n4. PV each cash flow at the IRR (sum = market value)\n5. Weight w = PV ÷ total PV\n6. Macaulay duration = Σ t × w (÷ 2 for years)\n7. Dispersion = weighted variance of timing around duration\n8. Convexity = Σ [t (t + 1) w] ÷ (1 + periodic IRR)²") +
      K("Flat curve: same answer either way","<b>Upward-sloping curve</b>: portfolio IRR and duration are <b>higher</b> than the averages (long bonds count for longer)",
        "Goal = earn the initial <b>portfolio IRR</b>, not average YTM","Averages are used in practice as approximations — they add error",
        "<b>Dispersion and convexity</b> show exposure to structural risk from curve shifts and twists"))
    sub("Effects of yield curve changes on a barbell immunising a bullet", 5,
      P("<b>In plain words:</b> a 5-year liability, matched by a barbell of a short (S) and a long (L) bond with the same duration (M = 5). Assets have more convexity than the liability. What happens when the curve moves?") +
      T(["Curve move","PV assets vs PV liability","Result"],
        [["Parallel up (large)","Assets fall less than PVL (convexity); IRR and discount rate rise equally","FVA &gt; FVL → <b>success</b>"],
         ["Parallel down (large)","Assets rise more than PVL","FVA &gt; FVL → <b>success</b>"],
         ["Steepening twist (L yield up, S down, M fixed)","PVA falls below PVL (long bond loses more)","Risk — may still work if portfolio IRR rises enough"],
         ["Flattening twist (L down, S up)","PVA rises above PVL","Risk — portfolio IRR may fall too far"],
         ["Positive butterfly (S and L up, M down)","PVA ↓, PVL ↑","<b>Significant</b> structural risk"],
         ["Negative butterfly (S and L down, M up)","PVA ↑, PVL ↓","Favourable, not guaranteed (IRR may drop)"]]) +
      K("<b>Structural risk</b>: assets' durations spread out (S, L) while liability sits at one point (M)",
        "Immunisation = <b>zero replication</b>: success if portfolio IRR tracks the yield of the replicating zero",
        "Parallel shifts are <b>sufficient but not necessary</b> for success",
        "Not buy-and-hold: coupon bond duration falls slower than the liability's (which falls one year per year) → rebalance"))
    sub("Rules for immunising a single liability; money duration", 5,
      F("1. PV assets ≥ PV liability (exceptions if portfolio IRR ≠ liability discount rate)\n2. Portfolio <b>Macaulay duration = liability due date</b>\n3. <b>Minimise convexity</b> (least dispersion of asset cash flows around the liability)\n4. Rebalance regularly (trade-off: transaction costs vs duration drift)") +
      F("Money duration (BPV, PVBP, 'value of an 01') = MD × Value × 0.0001\nMatching BPVs combines rules 1 and 2") +
      K("Lower dispersion → lower convexity → less structural risk; dispersion 0 = a zero-coupon bond = perfect match") +
      TRAP("+C is good for price, but immunisation is about reaching the <b>future value</b> → minimise convexity (quiz: match Macaulay duration to due date = A)."))
    sub("Multiple liabilities: cash-flow matching, duration matching, contingent immunisation", 5,
      T(["Method","How","Notes"],
        [["Cash-flow matching (dedication)","Zero or coupon bonds whose flows match each payment","Simple; govt bond portfolio allows legal <b>defeasance</b> (assets and debt off balance sheet); expensive"],
         ["Duration matching","Match <b>BPV</b> of assets and liabilities","Flexible, cheaper; structural risk; BPV handles different sizes and discount rates"],
         ["Contingent immunisation","Active management while surplus &gt; 0; immunise before surplus hits 0","Needs significant surplus; hybrid active/passive"]]) +
      F("Multiple-liability rules:\n1. PVA ≥ PVL  2. BPV_A = BPV_L\n3. Asset dispersion &amp; convexity <b>greater</b> than liabilities' (but not by much)\n4. Rebalance to keep BPVs matched") +
      F("UK company retiring bonds: tender too costly (bonds held by buy-and-hold investors); defeasance with gilts costs GBP475m (too high)\n→ duration-matching portfolio of high-quality corporates (cheaper, no defeasance, may help rating)\nChoose <b>Portfolio B</b>: BPV closely matches + convexity slightly above liabilities\nExpect very large parallel shifts → <b>Portfolio C</b> (much higher convexity, weaker BPV match)") +
      TRAP("Single liability: minimise convexity. Multiple: convexity must <b>exceed</b> liabilities', then be minimised."))
    sub("Closing a duration gap with futures (derivatives overlay)", 5,
      P("<b>In plain words:</b> instead of selling and buying bonds, add bond futures to raise or lower asset BPV. Buying futures adds duration.") +
      K("Treasury futures on 2-, 5-, 10-yr notes and 30-yr bond; seller delivers 100,000 par of a deliverable bond — the <b>cheapest-to-deliver (CTD)</b>; buyer pays futures price × conversion factor",
        "CTD's duration sets the contract's BPV; <b>Ultra 10-year</b> narrows deliverables to durations near 10 years") +
      F("Futures BPV ≈ BPV_CTD ÷ CF_CTD\nN_f = (BPV_L − BPV_A) ÷ BPV_futures   (+ = buy, − = sell)\nUK revised: gap opened from 13 to 218,517 − 203,456 = 15,061 after a positive butterfly\n5-yr: 48.1650 / 0.9237 = 52.1436 → buy <b>289</b>\n10-yr: 86.7001 / 0.9169 = 94.5579 → buy <b>159</b>\nLiability duration 8.99 → 10-yr contract = closer match → less structural risk") +
      K("PVA = PVL need not hold after initiation; success if value tracks the replicating zero",
        "Overfunding is common; big surplus → contingent immunisation"))
    sub("Contingent immunisation in practice", 4,
      T(["Way to use the surplus","Comment"],
        [["Invest whole portfolio in stocks","Most active; must liquidate fast if surplus shrinks"],
         ["Only surplus in stocks / long options; rest immunised","Safer — only the surplus at risk"],
         ["Active bond management: over/underhedge","Expect rates ↑ → underhedge (&lt;100%); expect rates ↓ → overhedge (&gt;100%)"]]) +
      F("Each 1/32 price move on 100,000 par = (1/32) × (100,000/100) = <b>$31.25</b> per contract") +
      K("Liquidity risk: must convert to immunised portfolio quickly; short options and futures can lose more than the surplus",
        "Success → surplus grows, cost below immunising; failure → must immunise at a higher cost") +
      TRAP("Contingent immunisation = active management while PVA &gt; PVL (quiz C)."))
    sub("Defined benefit pensions: liabilities and a futures hedge", 5,
      K("Liability model inputs: years of service G, wage W₀, wage growth w, multiplier m, years to retirement T, discount rate r (high-quality corporate), payout years Z",
        "<b>ABO</b> (legal liability if plan closed now, lower) vs <b>PBO</b> (expected payout of ongoing plan, higher, usually more realistic)",
        "Effective duration from PV₋ and PV₊ with equal up/down curve shifts; equity duration assumed <b>zero</b>") +
      F("PBO $2.57bn, effective duration 9.35 → BPV_L = 2.57bn × 9.35 × 0.0001 = <b>2,402,950</b>\nAssets $3.07bn: 60% equity, 40% bond ladder (1–5 yr) duration 2.85\nBPV_A = 1.228bn × 2.85 × 0.0001 = <b>349,980</b> → gap 2,052,970\nCTD BPV 128.98, duration 13.53, CF 0.9436 → contract BPV 136.69\n100% hedge: buy 2,052,970 / 136.69 ≈ <b>15,019</b>\nRates expected ↓ (110%): ≈ 16,521 ; rates expected ↑ (90%): ≈ 13,517") +
      K("Daily margin: gains/losses on ~15,000 contracts paid in cash, while liability changes are unrealised → 100% hedges are rare; partial hedges common",
        "One 1/32 move ≈ only 0.2 bp of yield on duration 13.53 → large margin flows"))
    sub("Closing the gap with interest rate swaps", 5,
      P("<b>In plain words:</b> a receive-fixed swap acts like owning a fixed bond financed by floating debt → adds duration. Pay-fixed removes duration. Swaps are OTC, so traditionally no daily margin.") +
      F("Swap BPV per 100 NP = (D_fixed − D_floating) × 100 × 0.0001\nNP = BPV gap ÷ (swap BPV per 100 ÷ 100)\nPension: (9.18 − 0.25) → 0.0918 − 0.0025 = 0.0893 → NP = 2,052,970 / 0.000893 ≈ <b>$2.30bn</b> receive-fixed\nMandate 30–70%, 50% neutral\nExpect rates ↑ → 30%: 0.3 × 2.30 = <b>$0.69bn</b>\nThen expect rates ↓ → 70%: 0.7 × 2.30 = $1.61bn → add <b>$0.92bn</b> receive-fixed\nQuiz: gap $300,000; (8.25 − 0.5) × 0.01 = 0.0775 → NP = 300,000 / 0.000775 = <b>$387m</b>") +
      K("Many swaps are now marked to market and margined → less counterparty risk, but same cash-flow issues as futures",
        "Quiz note: the quiz did not say which BPV is larger → size known, direction not"))
    sub("Swaptions for the duration gap (worked)", 5,
      T(["Swaption (named for the <b>buyer's</b> fixed leg)","Right to","Valuable when new swap fixed rate (SFR)…","Effect"],
        [["Receiver swaption","Receive fixed at strike","Falls below strike","Adds duration when rates fall"],
         ["Payer swaption","Pay fixed at strike","Rises above strike","Removes duration when rates rise"]]) +
      F("US plan: gap 450,000 (assets short); swap BPV 0.2571 per 100\n1. 50% hedge: 450,000 × 0.5 / 0.002571 = <b>$87.515m</b> receive-fixed\n2. Want 35% if rates rise → buy <b>payer</b> swaption on 15%: 450,000 × 0.15 / 0.002571 = $26.254m\n   Premium 55 bp → 26.254m × 0.0055 = <b>$144,397</b>\n3. Exercise if new SFR &gt; 2.7% strike (pay 2.7% when market pays more)") +
      K("Capture value: exercise and receive higher floating, or exercise and enter a new receive-fixed swap at the higher SFR and pocket the difference",
        "Premium is a <b>sunk cost</b> — it does not affect the exercise decision",
        "Swaption cost is limited to the premium; a swap can keep losing",
        "<b>Swaption collar</b>: buy receiver + sell payer → cuts premium but gives away gains if rates rise above the payer strike"))
    sub("Choosing the optimal swap hedge (rate scenarios)", 5,
      P("<b>In plain words:</b> all three hedges cut risk. Which is <b>best</b> depends on where you think swap rates will go. Plan needs more asset duration; must hedge.") +
      T(["Hedge","Optimal if new SFR is…","Why"],
        [["Receive-fixed swap at 2.5%","<b>≤ 2.5%</b>","Like owning 2.5% bonds; gains as rates fall; no premium"],
         ["Zero-cost collar: buy 2.3% receiver + sell 3.3% payer","<b>Between 2.5% and 3.3%</b>","Both options worthless → zero value; swap would lose, receiver cost premium"],
         ["Buy 2.3% receiver swaption","<b>Well above 3.3%</b>","Loss capped at premium; swap and collar (short payer) keep losing"]]) +
      K("Breakeven above 3.3% where the receiver beats the collar is <b>not</b> covered") +
      TRAP("Seller of a payer swaption loses when rates rise above its strike."))
    sub("Risks of liability-driven investing", 5,
      T(["Risk","Meaning"],
        [["Convexity ignored","Duration-only hedges miss large-rate-move effects"],
         ["Parallel-shift assumption","Duration assumes parallel moves"],
         ["Structural risk","Curve twists; set asset convexity somewhat above liabilities but limit dispersion"],
         ["Model risk","Many assumptions to model DB liabilities, effective duration, BPV"],
         ["Measurement error","Weighted averages instead of cash-flow-based statistics"],
         ["CTD can change","Futures duration and BPV change; accrued interest adjustment"],
         ["<b>Spread risk</b>","Asset and liability rates differ (govt/swap vs corporate); Treasuries more volatile → non-parallel moves; swaps reflect MRR"],
         ["Counterparty risk","OTC derivatives; collateral reduces it"],
         ["Cash-flow (collateral) risk","Posting margin or collateral for futures and swaps"],
         ["Asset liquidity risk","Cannot adjust positions quickly at fair cost"]]) +
      TRAP("'Liability rate = corporate, asset rate = government' → <b>spread risk</b> (quiz C). 'Cannot adjust at reasonable cost' → liquidity risk."))
    sub("Bond indexing: why it is harder than equity", 5,
      P("<b>In plain words:</b> bond index funds give cheap diversification and aim for minimal tracking error. <b>Pure indexing</b> (full replication) holds every bond; <b>enhanced indexing</b> matches the index's risk factors, not every holding.") +
      T(["Challenge","Detail"],
        [["Size and variety","Far more issues, very different features → full replication impractical"],
         ["Many issues per issuer","Different liquidity → concentrate in liquid issues"],
         ["OTC dealer market","Post-2008 capital rules → smaller dealer inventories, wider spreads → less liquidity"],
         ["Rare trading","Most bonds don't trade in a year; trades often unreported → <b>matrix / evaluated pricing</b> (infer yield from similar traded bonds); unusual features = hard"],
         ["Index changes","New issues, maturities, rating changes alter composition quickly"]]))
    sub("Matching the primary risk factors", 5,
      T(["Match","Controls tracking error from"],
        [["Modified duration (effective if options)","<b>Parallel</b> shifts"],
         ["<b>Key rate durations</b>","<b>Non-parallel</b> shifts (quiz B)"],
         ["Sector and quality weights; spread duration","Spread changes vs government bonds"],
         ["Sector/coupon/maturity cell weights; callable and MBS weights","Convexity and option exposure (e.g. 1.7% in A-rated corporates of duration 2–3)"],
         ["Issuer exposure","Issuer event risk (bankruptcy)"]]) +
      F("Effective duration = (PV₋ − PV₊) / (2 × Δcurve × PV₀)\nKey rate duration = −(1/PV) × ΔPV / Δr_k\nSpread duration: %Δ relative value ≈ −spread duration × Δspread") +
      F("PV distribution of cash flows: 3-yr 4% semiannual bond at par (2% per period)\nt: 1–5 coupons 2, t6 = 102 → PVs 1.961, 1.922, 1.885, 1.848, 1.811, 90.573 (sum 100)\nw = PV/100 → 0.0196 … 0.9057 ; Σ t × w = 5.713 periods = <b>2.86 years</b>\nEach t × w = contribution to duration = a key rate duration\nMatch portfolio w to index w → matches KRDs, duration and convexity"))
    sub("Enhanced indexing: stratified sampling, ESG and adding value", 4,
      K("<b>Stratified sampling (cell matching)</b>: split index into cells (e.g. 3 duration bands × 3 sectors = 9 cells); hold the same weight per cell (e.g. 5.1% in 1–5 duration Treasuries) with fewer bonds",
        "Can add <b>ESG</b> rules (exclude high-carbon issuers, include clean energy) while matching cell weights",
        "Add value or cut cost: lower expenses and trading costs · overweight cheap / underweight rich securities, sectors, curve points (avoid spread widening, favour narrowing) · overweight callables when rate volatility expected <b>low</b>, underweight when high"))
    sub("Passive bond exposure: other vehicles", 5,
      T(["Vehicle","Pros","Cons"],
        [["Separately managed (full / enhanced)","Control, customisation","Higher setup cost"],
         ["Index mutual fund (open-end)","Small investors; diversification; scale economies; buy/sell at NAV daily","Management fees, front/back loads; never matures; holdings and income change"],
         ["ETF","Trades all day; <b>authorised participants</b> create/redeem in kind → arbitrage keeps price near NAV","Arbitrage weaker for illiquid bonds"],
         ["Total return swap (TRS)","Receive index total return, pay MRR + spread = index bought with borrowed money; cheap entry","Not fully collateralised → leveraged; no ownership; <b>counterparty risk</b>; receiver pays negative index returns"]]) +
      K("Indirect methods avoid big upfront trading costs but bring ongoing costs and other risks (quiz: TRS = A)"))
    sub("Selecting a bond benchmark", 4,
      K("Start with client objectives and constraints → strategic asset allocation → index that matches (tactical discretion possible)",
        "Static bond portfolio: duration <b>falls</b> as bonds age (quiz: 'stays the same' is false)",
        "New issuance shifts index duration (issuers move shorter or longer) → index may stop fitting",
        "Custom index from desired duration and sectors, e.g. 50% 5–10-yr Treasuries + 50% 1–3-yr IG corporates",
        "<b>Smart beta / credit barbell</b>: long-term Treasuries supply duration (no spread risk); short-term corporates add spread return and suffer less if spreads widen"))
