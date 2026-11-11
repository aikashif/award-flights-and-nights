from summary_lib import *
from helpers import P

def add(chap, sub):
    chap(6, "P6 Fixed-Income Active Management: Credit Strategies", "19% of PM", 5)
    sub("What this reading is about", 3,
      P("<b>In plain words:</b> P5 used the risk-free government curve; P6 adds <b>credit risk</b> — bonds that may not pay. Learn: what spreads pay for, every spread measure (and why OAS is best), spread duration, DTS and excess spread, bottom-up and top-down credit strategies, liquidity and tail risk, CDS trades, credit curve strategies, global/EM credit, structured credit and analytics. This is the <b>biggest</b> PM reading.") +
      T(["LOS","Topic"],[["P6.a","Risk considerations for spread portfolios"],["P6.b","Spread measures; why OAS is best"],["P6.c","Bottom-up credit strategies"],
        ["P6.d","Top-down, factor and ESG credit strategies"],["P6.e","Liquidity risk"],["P6.f","Tail risk"],["P6.g","CDS strategies"],
        ["P6.h","Credit spread curve positioning"],["P6.i","International / EM credit"],["P6.j","Structured credit"],["P6.k","Fixed-income analytics"]]))
    sub("Credit risk: POD, LGD, CVA and the fair spread", 5,
      P("<b>In plain words:</b> a spread is the extra yield over a comparable government bond. It pays for <b>credit risk</b> (issuer may not pay) and <b>liquidity risk</b> (you may not be able to sell at a fair price).") +
      T(["Term","Meaning"],
        [["Probability of default (POD)","Chance the issuer misses a payment, usually annual"],
         ["Loss given default (LGD) / loss severity","Share lost if default = 1 − recovery rate"],
         ["Expected loss","Σ POD × LGD × expected exposure"],
         ["Credit valuation adjustment (CVA)","PV of expected losses → risky bond = risk-free bond − CVA"],
         ["Credit loss rate","Historical realised % lost to default (starting point)"]]) +
      F("Fair spread ≈ POD × LGD\nFirst lien spread 1.5%, recovery 50% → POD = 1.5% / 0.5 = 3%\nSecond lien recovery 40% → spread = 3% × 0.6 = <b>1.8%</b>") +
      K("'Lien' = ranking of claim on collateral",
        "IG = BBB and above: defaults very rare, main risk = <b>credit migration</b> (downgrade). HY = BB and below: default risk dominates"))
    sub("Credit spread curve and the credit cycle", 5,
      P("<b>In plain words:</b> the credit spread curve plots spread against maturity. Upward = default more likely later; flat = equal over time. Its shape follows the credit (economic) cycle.") +
      T(["Phase","Spreads","Curve shape"],
        [["Recovery / early expansion","Falling from wide levels as defaults drop","Upward sloping, steepening"],
         ["Expansion","Low and stable","Upward sloping"],
         ["Peak (late cycle)","<b>Rising</b> (leverage, inflation fears, future defaults priced in)","<b>Upward sloping</b> (quiz A)"],
         ["Contraction","Widen sharply","IG flattens; <b>HY inverts</b> (near-term default risk) — quiz C"]]) +
      K("HY curves change level and slope more sharply than IG over the cycle"))
    sub("Rates vs spreads: empirical vs analytical duration", 5,
      P("<b>In plain words:</b> risk-free rates and spreads usually move in <b>opposite</b> directions (good economy: rates up, spreads down; bad economy: rates down, spreads up). So a low-quality bond's price reacts less to rate changes than its modified duration says.") +
      F("HY 5-yr bond yields 6%; Treasury 2% → spread 4%; MD 4.4\nFlight to quality: Treasury → 1%, spread → 5% → bond yield still 6% → price unchanged\nModified duration predicted +4.4%; observed sensitivity ≈ 0") +
      K("<b>Empirical duration</b> = regression of actual bond returns on benchmark rate changes",
        "Low-quality bonds: empirical duration <b>&lt;</b> analytical (modified) duration (quiz A)"))
    sub("Fixed-rate spread measures", 5,
      T(["Measure","Definition","Pros / notes"],
        [["Yield (benchmark) spread","Bond YTM − YTM of nearest-maturity on-the-run govt","Simplest; maturity mismatch"],
         ["G-spread","Bond YTM − <b>interpolated</b> govt YTM at the exact maturity","Upward curve → g-spread &lt; yield spread (quiz C)"],
         ["I-spread (interpolated spread)","Bond YTM − interpolated <b>swap fixed rate</b>","Swap is tradeable → hedge duration, measure carry"],
         ["Asset swap spread (ASW)","Bond <b>coupon</b> − interpolated swap rate","Spread over MRR from bond + pay-fixed swap: 6% coupon, 4% swap → MRR + 2%. Bond below par → i-spread &gt; ASW (quiz C)"],
         ["Z-spread (zero-volatility)","Single spread over govt <b>spot</b> curve that prices the bond (trial and error)","Respects term structure"],
         ["CDS basis","CDS spread − z-spread","Gap from bond away from par, accrued interest, CDS features"],
         ["<b>Option-adjusted spread (OAS)</b>","Spread added to every node of a rate tree (with volatility) after adjusting cash flows for option exercise","<b>Only</b> valid measure for bonds with options; best for comparing all bonds; an 'option-removed' spread"]]) +
      K("YTM and swap rates are non-simple averages of spot/expected rates → ignore term structure; z-spread fixes this",
        "A bond whose OAS differs a lot from its other spreads has an embedded option → compare on OAS",
        "Portfolio OAS = market-value weights incl. accrued interest: X 102 + 1.0 AI, OAS 120; Y 94 + 1.5 AI, OAS 140 → weights 0.519 / 0.481 → <b>129.6 bp</b> (below 130)"))
    sub("Worked: interpolation, yield spread, g-spread, i-spread, ASW", 5,
      F("Weight on longer bond = (M − S) / (L − S)\n12-yr corporate: YTM 4.5%, coupon 4.3%, MD 11.1 ; govt 10-yr 3.0%, 20-yr 5.0%\nYield spread = 4.5 − 3.0 = <b>1.5%</b>\nWeight 20-yr = (12 − 10)/(20 − 10) = 0.2 → 0.8×3% + 0.2×5% = 3.4% → g-spread = <b>1.1%</b>\nScenario: 20-yr falls 10 bp, spread fixed\nYield spread view: no change. G-spread view: 0.8×3% + 0.2×4.9% = 3.38% → yield 4.48% (−2 bp) → price +11.1 × 0.02% = <b>+0.222%</b>\nSwap spreads 20 bp (10-yr) and 30 bp (20-yr) → swap rates 3.2% and 5.3%\nInterpolated 12-yr swap = 0.8×3.2 + 0.2×5.3 = 3.62%\ni-spread = 4.50 − 3.62 = <b>0.88%</b> ; ASW = 4.30 − 3.62 = <b>0.68%</b>"))
    sub("Floating-rate note spreads: QM, DM, Z-DM", 5,
      P("<b>In plain words:</b> an FRN pays MRR + a fixed <b>quoted margin (QM)</b>. Its coupon follows rates, so <b>rate duration is low</b>. But the QM is fixed, so if credit worsens the FRN falls → <b>spread duration</b> is much higher. The <b>discount margin (DM)</b> is the margin investors now require — it plays the role of yield; QM plays the role of coupon.") +
      F("DM &gt; QM → below par ; DM &lt; QM → above par ; DM = QM → about par\nEffRateDur = (PV₋ − PV₊) / (2 × ΔMRR × PV₀)\nEffSpreadDur = (PV₋ − PV₊) / (2 × ΔDM × PV₀)\n1-yr FRN, quarterly: MRR 0.55%, QM 1.25%, DM 1.55% → <b>below par</b>\nCoupon (0.55 + 1.25)/4 = 0.45% → $4,500 per $1m ; discount rate (0.55 + 1.55)/4 = 0.525%\nValue = Σ 4,500/1.00525^t (t = 1–4) + 1,000,000/1.00525⁴ ≈ <b>$997,040</b>") +
      K("DM assumes MRR stays flat (ignores term structure)",
        "<b>Zero-discount margin (Z-DM)</b>: coupons from forward MRR + QM, discounting at spot MRR + Z-DM — like the z-spread for FRNs",
        "Upward MRR curve (e.g. recovery) → <b>Z-DM &lt; DM</b> (quiz A)"))
    sub("Spreads in the return decomposition; spread duration and convexity", 5,
      K("Steps 1–3 (coupon, rolldown, rate change) also help explain corporate vs government excess return: corporate bonds roll down a <b>credit</b> curve too (excess rolling yield)") +
      F("EffSpreadDur = (PV₋ − PV₊) / (2 × Δspread × PV₀)\nEffSpreadCon = (PV₋ + PV₊ − 2PV₀) / (Δspread² × PV₀)\n%Δprice ≈ −EffSpreadDur × Δspread + ½ × EffSpreadCon × Δspread²   (Δspread usually = ΔOAS)") +
      K("Spread changes tend to be <b>proportional</b> to spread level — wide spreads move more"))
    sub("Duration times spread (DTS)", 5,
      F("DTS ≈ EffSpreadDur × spread\nExpected bp change in value ≈ −DTS × % change in index OAS\nA-rated: 9.0 × 180 = 1,620 ; C-rated: 9.5 × 400 = 3,800\nPortfolio 70/30 → 0.7×1,620 + 0.3×3,800 = <b>2,274</b>\nIndex OAS 200 → +20 bp = +10% → value falls 2,274 × 0.10 = <b>227.4 bp</b>") +
      K("DTS assumes each bond's spread moves by the same <b>percentage</b> as the index"))
    sub("Expected excess spread", 5,
      P("<b>In plain words:</b> what you expect to earn above fair compensation for credit losses — after spread-widening losses and expected defaults. Positive = undervalued; negative = overvalued.") +
      F("Expected excess spread ≈ spread − (EffSpreadDur × Δspread) − (POD × LGD)   (all for the holding period)\nSpread 250 bp, dur 4.5, POD 1.5%/yr, LGD 55%, spread → 270 bp in 6 months\n= 0.025/2 − 4.5 × 0.0020 − 0.015 × 0.55 / 2 = 0.0125 − 0.0090 − 0.004125 = <b>−0.000625</b> → <b>overvalued</b>\nQuiz (spreads +15%): A-rated 0.015 − 6 × 0.00225 − 0.0025 × 0.6 = <b>0%</b>\nB-rated 0.03 − 8 × 0.0045 − 0.03 × 0.6 = <b>−2.4%</b> → A more attractive") +
      TRAP("De-annualise spread and POD × LGD for the holding period. Use decimals for every input."))
    sub("Bottom-up credit: process and credit risk models", 5,
      P("<b>In plain words:</b> bottom-up = pick the best issuers and bonds. Define the universe, split into sectors (industry, region), then find relative mispricing inside each sector.") +
      K("Credit analysis: ability to pay principal and interest — operating history, competitive position, profitability (EBITDA/total assets), leverage (debt/equity), coverage (EBITDA/interest)") +
      T(["Model","Idea","Examples"],
        [["Structural ('distance to default')","Default when asset value falls below the default threshold; asset volatility from equity market cap and volatility","Moody's EDF, Bloomberg DRSK (daily POD and fair spread)"],
         ["Reduced form","Link macro conditions and firm ratios to <b>default intensity</b> (periodic POD); with LGD → fair spread","Altman z-score"]]) +
      F("z = 1.2A + 1.4B + 3.3C + 0.6D + 1.0E\nA = WC/TA, B = RE/TA, C = EBIT/TA, D = MV equity/TL, E = sales/TA\n&gt; 3 low risk · 1.8–3 some risk · &lt; 1.8 default likely\nQuiz: 2,100/3,500 = 0.60 ; 1,900/3,500 = 0.54 ; 600/3,500 = 0.17 ; 3,000/1,200 = 2.5 ; 2,000/3,500 = 0.57\nz = 0.72 + 0.76 + 0.57 + 1.50 + 0.57 = <b>4.11</b> → low default risk") +
      K("Formula is usually given — focus on using and interpreting it",
        "Structural: <b>lower</b> equity volatility → farther from default → lower POD; lower coverage or higher leverage → higher POD (quiz B)"))
    sub("Bottom-up relative value", 5,
      K("Highest expected excess spread under your scenario = best relative value",
        "Check structure (options, seniority), liquidity, M&amp;A and other corporate events") +
      F("New 10-yr issue = interpolated credit spread + 5 bp new-issue premium\n5-yr corporate 1.5% − govt 0.8% = 0.7%\n15-yr govt: weight 30-yr = (15 − 10)/(30 − 10) = 0.25 → 0.75×2% + 0.25×4% = 2.5% → 15-yr spread 3.5 − 2.5 = 1.0%\n10-yr: weight 15-yr = (10 − 5)/(15 − 5) = 0.5 → 0.5×0.7 + 0.5×1.0 + 0.05 = <b>0.90%</b>"))
    sub("Top-down credit strategies", 5,
      K("Macro drivers: economic growth and corporate profits. Stronger → spreads narrow → move <b>down</b> in quality (more HY). Weaker → move up",
        "Also pick sectors likely to improve or worsen (can guide bottom-up analysts)",
        "Growth and default rates are negatively correlated; defaults and spreads highly correlated → high HY spread alone is <b>not</b> an opportunity (it pays for high losses); you need to foresee improvement before consensus",
        "Average rating: linear scale (AAA = 1, AA+ = 2…) <b>understates</b> credit risk; non-linear (Moody's 1, 10, 20, 40…) shows risk rising faster as ratings fall",
        "Portfolio OAS and spread duration are market-value weighted; use <b>DTS</b> because wider spreads move more",
        "Excess spread can be applied to a rating band or sector; can also form views on a sector's curve shape"))
    sub("Factor and ESG credit strategies", 4,
      T(["Credit factor","Meaning"],
        [["Carry","Return if nothing changes — measured by OAS"],
         ["Defensive","Lower-risk (e.g. short duration) bonds earn better risk-adjusted returns (quiz B)"],
         ["Momentum","Recent winners keep winning, losers keep losing"],
         ["Value","Low market value vs fundamental value (high excess spread)"]]) +
      K("Similar to equity factors; diversify equity and credit premiums",
        "ESG: negative <b>screening</b> · <b>ESG ratings</b> (more varied than credit ratings but positively related: poor ESG → more distress; agencies add ESG) · <b>direct funding</b>, e.g. <b>green bonds</b> (pollution, recycling, remediation, sustainable buildings)"))
    sub("Liquidity risk in credit", 5,
      K("Liquidity: very high for large on-the-run DM sovereigns; very low for small off-the-run corporates (may not trade for days) → <b>matrix (evaluated) pricing</b>",
        "Historically an OTC dealer market; electronic trading and ETFs growing",
        "Transaction cost = <b>effective spread</b> (pay above mid when buying, receive below mid when selling); US corporate trades reported on <b>TRACE</b>") +
      T(["How to manage liquidity","Detail"],
        [["Match liquidity to horizon","Liquid on-the-run bonds for short-term trades; illiquid for long-term"],
         ["Liquid alternatives","CDS; bond <b>ETFs</b> (authorised participants create/redeem; ETFs never mature and duration doesn't drift, except target-maturity ETFs)"],
         ["Asset swap hedge","Selling a big illiquid fixed bond slowly → enter <b>pay-fixed</b> swap now, unwind it <b>as</b> the bond is sold (quiz A)"]]))
    sub("Tail risk: VaR and its extensions", 5,
      P("<b>In plain words:</b> VaR = the minimum loss expected over a period with a given probability. '1% daily VaR = $7m' → 1% chance of losing $7m <b>or more</b> in a day. It marks where the tail starts.") +
      T(["Method","How","Pro","Con"],
        [["Parametric","Assume normal: 5% = 1.65σ, 1% = 2.33σ","Simple","Bad for non-normal (options)"],
         ["Historical simulation","Apply past risk-factor moves to today's portfolio","Real data; non-normal OK","Depends on sample"],
         ["Monte Carlo","Random draws from a user model","Flexible, non-normal","High model risk"]]) +
      F("$100m 15-yr bond (2% coupon, 3% yield), MD 12, yield vol 1.5% a year\nMonthly vol = 1.5% / √12 = 0.433% ; 1% tail → 2.33 × 0.433% = 100.89 bp\nLoss = 12 × 1.0089% = 12.107% → 1-month 1% VaR = <b>$12.107m</b>") +
      T(["VaR weakness","Extension"],
        [["Tails more frequent and severe than forecast","Stress tests"],["Misses correlation and liquidity changes in stress","Scenario analysis"],
         ["Says nothing about loss size in the tail","<b>CVaR</b> = average loss given you are in the tail"],
         ["—","<b>Incremental (partial) VaR</b> = VaR change from adding/removing a position (quiz B)"],
         ["—","<b>Relative VaR</b> = VaR of returns vs benchmark (minimum underperformance)"]]) +
      K("Rate volatility from swaption implied vol; spread volatility from CDS and equity prices",
        "Consider consequences: margin calls for leveraged funds, extra DB contributions, bank regulatory reserves"))
    sub("Credit default swaps: mechanics and pricing", 5,
      P("<b>In plain words:</b> a CDS is insurance on an issuer. The protection <b>buyer</b> pays a regular coupon and is paid if a credit event occurs → 'short risk' (like shorting the bond). The protection <b>seller</b> receives the coupon and pays on default → 'long risk' (like owning the bond).") +
      F("Standard coupon: 1% IG, 5% HY (not the fair price)\nCDS spread = fair premium; difference paid upfront\nUpfront premium (buyer pays) ≈ (CDS spread − fixed coupon) × EffSpreadDur\nCDS price ≈ 1 + (fixed coupon − CDS spread) × EffSpreadDur\nΔprice ≈ −ΔCDS spread × EffSpreadDur\nHY, spread 5.5%, dur 4.5 → upfront 0.5% × 4.5 = 2.25% (buyer pays) → price <b>97.75</b>\nSpread → 5.4%: price +0.45% → protection <b>buyer loses 0.45%</b>\nQuiz: HY 4.7%, dur 4.5, $10m → (0.05 − 0.047) × 4.5 × 10m = <b>$135,000</b> paid to the <b>buyer</b>") +
      K("Spread above coupon → price below par (lower quality); below coupon → above par",
        "Single-name or index (Markit CDX NA IG = 125 equal-weighted names)",
        "<b>Payer</b> CDS option = right to <b>buy</b> protection → profits if spread &gt; strike; <b>receiver</b> = right to sell protection → profits if spread &lt; strike") +
      TRAP("For P&amp;L, treat a <b>long-risk</b> (sold protection) position like a long bond: gains when spreads fall and price rises."))
    sub("CDS long/short and curve trades", 5,
      F("Long/short: increase XYZ, decrease ABC → <b>sell</b> XYZ protection, <b>buy</b> ABC protection, $15m each\nABC +15 bp: 15m × 0.0015 × 4.59 = $103,275 ; XYZ −20 bp: 15m × 0.0020 × 4.62 = $138,600\nTotal = <b>$241,875</b>") +
      F("Curve flattener (HY index, duration-neutral): buy 5-yr protection, sell 10-yr\n5-yr BPV = 5m × 4.78 × 0.0001 = $2,390 → 10-yr notional = 2,390 / (9.18 × 0.0001) = <b>$2,603,486</b>\n5-yr −5 bp → −5 × 2,390 = −$11,950 ; 10-yr −20 bp → +20 × 2,390 = +$47,800\nTotal = <b>+$35,850</b>") +
      K("Long/short: buy protection where spreads will widen relative; sell where they will narrow",
        "Curve trade: buy protection at maturities whose spreads will rise relative to others; sell where they will fall"))
    sub("Static credit curve strategies", 5,
      P("<b>In plain words:</b> if you expect the credit curve to stay the same, take more credit risk: lower average rating, or longer spread duration (buy and hold longer bonds). With CDS: sell protection on lower quality or longer tenors.") +
      F("Cash: overweight $10m 15-yr corporate vs 10-yr for 6 months\nExtra coupon $35,000 ; of which govt part (1.1% − 0.8%)/2 × 10m = $15,000 → credit $20,000\nRolldown (interpolate 9.5- and 14.5-yr yields, weights 0.9/0.1):\n10-yr: 2.27% → 100.8888 → 101.1053 = $21,650 (all from govt yield)\n15-yr: 2.84% → 102.4187 → 103.0726 = $65,390 (half govt, half g-spread: $32,695 each)\nExtra rolldown $43,740 → total <b>$78,740</b> ; from credit $20,000 + $32,695 = <b>$52,695</b>") +
      F("CDS: sell $50m 10-yr HY protection; 5-yr 450 bp, 10-yr 550 bp\nIn 1 year it is a 9-yr: weight 10-yr = (9 − 5)/(10 − 5) = 0.8 → 0.8×550 + 0.2×450 = 530 bp\nPrice now 0.9555 → later 1 + (0.05 − 0.053) × 8.1 = 0.9757 → +$1,010,000\nCoupon 5% × 50m = $2,500,000 → total <b>$3.51m</b>") +
      TRAP("Stable curve: buying short-dated protection is <b>least</b> likely (quiz B)."))
    sub("Dynamic credit curve strategies (slowdown vs recovery)", 5,
      T(["Expected","Spreads / curves","Cash bonds","CDS"],
        [["Economic slowdown","HY widens more than IG; curves flatten or invert","Buy IG, sell HY (flight to quality); raise quality","Buy HY protection, sell IG protection; buy short-dated, sell long-dated protection"],
         ["Economic recovery","HY narrows more; curves steepen","Buy HY, sell IG; lower quality","Sell HY protection, buy IG; <b>sell short-dated, buy long-dated</b> protection (quiz B)"]]) +
      F("Cash slowdown: long 100% A-rated, short 100% BB-rated; compute excess spread with OAS and expected loss +40% (IG) and +80% (HY)\nCDS slowdown: sell IG protection + buy HY protection, $50m each; spreads +40% IG, +80% HY; durations later 3.85 / 3.82\nNet coupon paid = 50m × (5% − 1%) = −$2m\nHY leg: price 1.0191 → 1.11575 → buyer gains 50m × 0.09665 = <b>+$4,832,500</b>\nIG leg (long risk) = −$770,000 → price total $4,062,500 → net <b>+$2,062,500</b>") +
      F("Quiz: overweight IG name → sell protection $10m; spread 150 → 120 bp, dur 4.5 → 3.5\nPrice 1 + (0.01 − 0.015) × 4.5 = 0.9775 → 1 + (0.01 − 0.012) × 3.5 = 0.993 → +$155,000\nCoupon 1% × 10m = $100,000 → total <b>$255,000</b>"))
    sub("Global credit strategies", 4,
      K("EM reliant on one industry/commodity → sectors move together → little diversification",
        "Sector mix differs even between DMs (US has far more MBS/ABS)",
        "Accounting differences distort liquidity, profitability, solvency ratios",
        "Credit cycles differ in timing and size → opportunities in yields, FX, credit curves") +
      F("R_DC = (1 + R_FC)(1 + R_FX) − 1\nUS manager expects European recovery → sell protection on European HY index: spread 4.5%, dur 4.55\nPrice 1 + (0.05 − 0.045) × 4.55 = 1.02275 → spreads −20% → 1 + (0.05 − 0.036) × 4.55 = 1.0637\nR_FC = 4% ; EUR +2% → 1.04 × 1.02 − 1 = <b>6.08%</b>"))
    sub("Emerging market sovereign and corporate credit", 4,
      T(["Sovereign factor","What to check"],
        [["Institutional","Property rights, contract law, political stability, geopolitics (trade wars, conflicts), ESG"],
         ["Economic","Tax revenue; debt/GDP; deficit/GDP — <b>fiscal stability = lowest deficit/GDP</b> (quiz A)"],
         ["Exchange rate regime","Fixed regimes limit monetary policy; high <b>external debt/GDP</b> → distress risk; low <b>reserves/GDP</b> → liquidity risk"]]) +
      K("EM corporates: government influence; <b>sovereign ceiling</b> (firms rarely rated above their sovereign); few bonds trade → liquidity premium; currency risk — high yields may signal depreciation (UIRP), but UIRP often fails → carry"))
    sub("Structured credit", 4,
      T(["Reason","Instruments"],
        [["Tranching creates risk profiles you can't get directly (losses hit junior tranches first; senior tranches rated highest)","<b>CDOs</b> (general debt), <b>CLOs</b> (leveraged loans to non-IG firms)"],
         ["Access to collateral you can't buy directly","<b>MBS</b> (mortgages), <b>ABS</b> (cards, autos), <b>covered bonds</b>"]]) +
      K("Covered bonds: senior bank debt backed by a loan pool <b>on the bank's balance sheet</b>; recourse to the bank; bad loans replaced → lower risk than SPV-issued products",
        "Expect recovery + housing rebound → <b>sell AA MBS tranche, buy BB MBS tranche</b> (quiz C)"))
    sub("Fixed-income analytics", 4,
      T(["Part","Contents"],
        [["Inputs","Positions; market data (prices, yields, FX, volatilities); credit and ESG ratings; index data"],
         ["User-defined parameters","Term-structure, risk (VaR) and scenario models; filters (sector, ESG); time horizon; objective (total return vs liability-driven)"],
         ["Outputs","Positions and risk vs benchmark; security selection and construction tools; risk and scenario analysis; trading and cash management"]]) +
      K("Check input accuracy, model assumptions, and fit of outputs with objectives",
        "MBS hold a <b>short</b> prepayment option → a <b>lower</b> volatility input raises their value vs option-free bonds (quiz C)"))
