from summary_lib import *
from helpers import P

def add(chap, sub):
    chap(6, "P6 Fixed-Income Active Management: Credit Strategies", "19% of PM", 5)
    sub("Credit risk, spreads and the credit cycle", 5,
      P("<b>In plain words:</b> a credit spread is the extra yield a risky bond pays over a safe government bond. It pays you for two risks: the issuer may not pay (<b>credit risk</b>) and you may not be able to sell easily (<b>liquidity risk</b>).") +
      F("Expected loss = POD × LGD ; LGD = 1 − recovery rate\nCVA = PV of Σ(POD × LGD × expected exposure) → risky bond = risk-free bond − CVA\nSimple fair spread ≈ POD × LGD\nFirst lien spread 1.5%, recovery 50% → POD = 1.5%/0.5 = 3%\nSecond lien recovery 40% → spread = 3% × 0.6 = <b>1.8%</b>") +
      K("IG = BBB and above (main risk = <b>credit migration</b>/downgrade); HY = BB and below (main risk = default)",
        "Credit spread curve = spread vs maturity; upward = defaults more likely later",
        "Cycle: peak → spreads rising, curve upward sloping; recession → IG flattens, <b>HY inverts</b> (near-term default risk); HY moves more sharply",
        "Rates and spreads move oppositely → HY bond price reacts less to rate changes: <b>empirical duration &lt; analytical duration</b>") +
      F("HY 6% vs Treasury 2% (spread 4%), MD 4.4: Treasury falls to 1%, spread widens to 5% → yield still 6% → price unchanged (empirical duration ≈ 0)"))
    sub("Fixed-rate spread measures", 5,
      T(["Measure","Definition","Note"],
        [["Yield (benchmark) spread","Bond YTM − nearest on-the-run govt YTM","Simplest; maturity mismatch"],
         ["G-spread","Bond YTM − <b>interpolated</b> govt YTM","Upward curve → g-spread &lt; yield spread"],
         ["I-spread","Bond YTM − interpolated <b>swap</b> rate","Tradeable hedge; carry"],
         ["Asset swap spread (ASW)","Bond <b>coupon</b> − swap rate","Spread over MRR via bond + pay-fixed swap; bond below par → i-spread &gt; ASW"],
         ["Z-spread","Constant spread over the govt <b>spot</b> curve that prices the bond","Respects term structure"],
         ["CDS basis","CDS spread − z-spread","Technical differences"],
         ["<b>OAS</b>","Spread over an interest-rate tree after removing the option","<b>Only</b> valid measure for bonds with options — best for comparisons"]]) +
      F("Interpolation weight on longer bond = (M − S)/(L − S)\n12-yr corporate 4.5% (coupon 4.3%, MD 11.1); govt 10-yr 3.0%, 20-yr 5.0%\nYield spread = 4.5 − 3.0 = 1.5% ; weight on 20-yr = 2/10 = 0.2 → interpolated 3.4% → g-spread = <b>1.1%</b>\n20-yr falls 10 bp → interpolated 3.38% → corporate yield 4.48% → price +11.1 × 0.02% = +0.222%\nSwap rates 3.2% / 5.3% → interpolated 3.62% → i-spread = <b>0.88%</b>, ASW = 4.30 − 3.62 = <b>0.68%</b>") +
      TRAP("A bond whose OAS is very different from its other spreads has an embedded option — compare it using <b>OAS</b>."))
    sub("Floating-rate note spreads", 4,
      F("Coupon = MRR + quoted margin (QM) ; required margin = discount margin (DM)\nDM &gt; QM → below par ; DM &lt; QM → above par ; DM = QM → par\n1-yr FRN: MRR 0.55%, QM 1.25%, DM 1.55% → below par\nQuarterly coupon (0.55 + 1.25)/4 = 0.45% → $4,500 ; discount (0.55 + 1.55)/4 = 0.525%\nValue of $1m ≈ <b>$997,040</b>") +
      K("FRNs: low rate duration, but spread duration ≈ like a fixed bond (QM fixed)",
        "DM assumes flat MRR; <b>Z-DM</b> uses forward MRR + spot discounting; upward MRR curve (recovery) → Z-DM &lt; DM"))
    sub("Spread duration, DTS and excess spread", 5,
      F("Spread return ≈ −EffSpreadDur × ΔSpread + ½ × EffSpreadCon × ΔSpread²   (Δspread = ΔOAS)\nDTS = EffSpreadDur × spread\nPortfolio: 70% A bond (9.0 × 180 = 1,620) + 30% C bond (9.5 × 400 = 3,800) → DTS = 2,274\nIndex OAS 200 → +20 bp = +10% → portfolio falls 2,274 × 0.1 = <b>227.4 bp</b>\nExpected excess spread = spread × t − EffSpreadDur × ΔSpread − POD × LGD × t\nSpread 250 bp, dur 4.5, POD 1.5%, LGD 55%, spread → 270 in 6 months:\n0.0125 − 4.5 × 0.0020 − 0.015 × 0.55 × 0.5 = <b>−0.0625%</b> → overvalued") +
      K("Spread changes are proportional to spread level → use DTS","Portfolio OAS is market-value weighted (include accrued interest)") +
      TRAP("De-annualise spread and POD × LGD for the holding period, and work in decimals."))
    sub("Bottom-up credit: models & relative value", 5,
      T(["Model","How","Examples"],
        [["Structural","Default when asset value falls below liabilities ('distance to default'); asset volatility from equity data","Moody's EDF, Bloomberg DRSK"],
         ["Reduced form","Default intensity from macro + firm ratios","<b>Altman z-score</b>"]]) +
      F("z = 1.2 × WC/TA + 1.4 × RE/TA + 3.3 × EBIT/TA + 0.6 × MVE/TL + 1.0 × Sales/TA\n&gt; 3 low risk · 1.8–3 some risk · &lt; 1.8 default likely\nExample: 0.6, 0.54, 0.17, 2.5, 0.57 → z = <b>4.11</b> → low risk") +
      F("New 10-yr issue: 5-yr spread 1.5 − 0.8 = 0.7% ; 15-yr govt interpolated 0.75×2% + 0.25×4% = 2.5% → 15-yr spread 1.0%\n10-yr spread = 0.5×0.7 + 0.5×1.0 + 0.05 premium = <b>0.90%</b>") +
      K("Bottom-up: universe → sectors → best relative value; operating history, profitability, leverage, coverage ratios",
        "Lower equity volatility → farther from default → lower POD","Watch structure (options, seniority), liquidity, M&amp;A"))
    sub("Top-down, factor and ESG credit strategies", 4,
      L("Macro: strong growth → spreads narrow → move <b>down</b> in quality (more HY); weak growth → move up",
        "High spreads alone are not an opportunity — only if you foresee improvement before others",
        "Average rating: linear scale (1,2,3…) <b>understates</b> credit risk; non-linear (Moody's 1, 10, 20, 40…) is better; use DTS",
        "Credit factors: <b>carry</b> (OAS), <b>defensive</b> (low-risk/short duration earns better risk-adjusted), <b>momentum</b>, <b>value</b>",
        "ESG: negative screening · ESG ratings (correlated with credit ratings) · direct funding e.g. <b>green bonds</b>"))
    sub("Liquidity risk & tail risk (VaR)", 5,
      K("On-the-run sovereigns very liquid; small off-the-run corporates may not trade → matrix pricing; TRACE for US corporate trade data",
        "Manage liquidity: liquid bonds for short-term strategies · CDS and ETFs (APs create/redeem) · <b>pay-fixed asset swap</b> while slowly selling a big illiquid bond, unwinding as you sell") +
      T(["VaR method","Pro","Con"],
        [["Parametric (normal; 5% = 1.65σ, 1% = 2.33σ)","Simple","Poor for non-normal (options)"],["Historical simulation","Real data, non-normal OK","Depends on the sample"],["Monte Carlo","Flexible","Model risk"]]) +
      F("$100m bond, MD 12, annual yield vol 1.5% → monthly 1.5%/√12 = 0.433%\n1% VaR yield move = 2.33 × 0.433% = 100.89 bp → loss 12 × 1.0089% = 12.107% → <b>$12.1m</b>") +
      K("VaR flaws: tails worse than forecast, ignores correlation/liquidity shifts, no tail-size info",
        "<b>CVaR</b> = average loss in the tail · <b>IVaR</b> = VaR change from adding/removing a position · <b>Relative VaR</b> vs benchmark",
        "Stress the consequences: margin calls, sponsor contributions, bank reserves"))
    sub("Credit default swaps: pricing", 5,
      P("<b>In plain words:</b> a CDS is insurance on a bond. The <b>buyer</b> of protection pays a fee and gets paid if the issuer defaults — he is 'short risk', like being short the bond. The <b>seller</b> is 'long risk', like owning the bond.") +
      F("Standard coupon: 1% IG, 5% HY\nUpfront premium (paid by buyer) ≈ (CDS spread − fixed coupon) × EffSpreadDur\nCDS price ≈ 1 + (fixed coupon − CDS spread) × EffSpreadDur\nHY, spread 5.5%, dur 4.5 → upfront 2.25% ; price 97.75\nSpread falls to 5.4% → +0.45% price → buyer loses 0.45%\nQuiz: HY 4.7%, dur 4.5, $10m → seller pays buyer (0.05 − 0.047) × 4.5 × 10m = <b>$135,000</b>") +
      K("Single-name or index (CDX NA IG = 125 names); payer CDS option = right to buy protection (profits if spreads above strike); receiver = right to sell protection",
        "Long risk position behaves like a long bond: profits when spreads fall and CDS price rises"))
    sub("CDS long/short and curve trades", 5,
      F("Long XYZ / short ABC: sell XYZ protection, buy ABC protection, $15m each\nABC +15 bp: 15m × 0.0015 × 4.59 = $103,275 ; XYZ −20 bp: 15m × 0.002 × 4.62 = $138,600 → <b>$241,875</b>\nFlattener (HY index): buy 5-yr protection $5m (dur 4.78 → BPV $2,390), sell 10-yr protection $2,390/(9.18×0.0001) = <b>$2,603,486</b>\n5-yr −5 bp → −$11,950 ; 10-yr −20 bp → +$47,800 → <b>+$35,850</b>") +
      K("Buy protection where spreads will widen; sell where they will narrow","Curve trade: buy protection at maturities expected to rise relative to others"))
    sub("Static & dynamic credit curve strategies", 5,
      T(["View","Cash bonds","CDS"],
        [["Static curve","Lower average rating or extend spread duration (buy and hold longer)","Sell protection on lower quality or longer tenors"],
         ["Economic slowdown (HY widens more; curves flatten/invert)","Buy IG, sell HY (flight to quality)","Buy HY protection, sell IG; buy short-dated, sell long-dated protection"],
         ["Economic recovery (HY narrows more; curves steepen)","Buy HY, sell IG","Sell HY protection, buy IG; sell short-dated, buy long-dated protection"]]) +
      F("Static, cash: overweight $10m 15-yr corporate vs 10-yr for 6 months\nExtra coupon $35,000 (govt part $15,000, credit $20,000)\nRolldown: 10-yr → 100.8888 to 101.1053 = $21,650 ; 15-yr → 102.4187 to 103.0726 = $65,390 → extra $43,740\nTotal <b>$78,740</b>; from credit = $20,000 + $32,695 = <b>$52,695</b>") +
      F("Static, CDS: sell $50m 10-yr HY protection; 5-yr 450 bp, 10-yr 550 bp → 9-yr 530 bp\nPrice 0.9555 → 1 + (0.05 − 0.053) × 8.1 = 0.9757 → +$1,010,000 + coupon $2,500,000 = <b>$3.51m</b>\nSlowdown: sell IG protection + buy HY protection, $50m each, spreads +40% / +80%\nNet coupon −$2m ; HY leg +$4,832,500 ; IG leg −$770,000 → <b>+$2,062,500</b>") +
      F("Quiz: sell IG protection $10m, spread 150 → 120 bp, dur 4.5 → 3.5\nPrice 0.9775 → 0.993 = $155,000 + coupon $100,000 = <b>$255,000</b>"))
    sub("Global credit, emerging markets", 4,
      K("One-industry/commodity EM economies give little sector diversification","Sector mix differs (US has far more MBS/ABS)","Accounting differences distort ratios","Credit cycles differ in timing → opportunities") +
      F("Recovery view, buy European HY credit via CDS (sell protection): spread 4.5%, dur 4.55\nPrice 1 + (0.05 − 0.045) × 4.55 = 1.02275 → spreads −20% → 1 + (0.05 − 0.036) × 4.55 = 1.0637 → +4%\nEUR +2% → 1.04 × 1.02 − 1 = <b>6.08%</b>") +
      K("Sovereign analysis: institutions (property rights, politics, geopolitics, ESG) · economy (tax base, debt/GDP, deficit/GDP — fiscal stability) · FX regime (external debt/GDP = distress risk; reserves/GDP = liquidity)",
        "EM corporates: government influence, <b>sovereign ceiling</b>, liquidity premium, currency risk (UIRP often fails)"))
    sub("Structured credit & fixed-income analytics", 4,
      T(["Reason to use","Instruments"],
        [["Tranching creates new risk profiles (losses hit junior first)","CDOs (general debt), CLOs (leveraged loans)"],
         ["Access collateral you can't buy directly","MBS, ABS (cards, autos), <b>covered bonds</b> (on bank's balance sheet, recourse to the bank, bad loans substituted → lower risk)"]]) +
      K("Recovery + housing rebound → sell AA MBS tranche, buy BB MBS tranche",
        "Analytics = inputs (positions, market data, credit/ESG ratings, index data) + user parameters (term-structure, VaR, scenario models, filters, horizon, objective) + outputs (exposures vs benchmark, construction, risk/scenario, trading &amp; cash tools)",
        "MBS hold a short prepayment option → <b>lower</b> volatility assumption raises their value"))
