from summary_lib import *
from helpers import P

def add(chap, sub):
    chap(3, "P3 Active Equity Investing: Portfolio Construction", "11% of PM", 4)
    sub("What this reading is about", 3,
      P("<b>In plain words:</b> P2 was about <b>finding</b> ideas; P3 is about <b>turning ideas into a portfolio</b>: how big each bet is, how far to move from the benchmark (Active Share, active risk), how to spend a risk budget, how size and trading costs limit a strategy, and when to use shorts.") +
      T(["LOS","Topic"],[["P3.a","Investment philosophy: sources of active return, building blocks, fundamental law"],["P3.b","Approaches; objectives and constraints"],
        ["P3.c","Active Share vs active risk"],["P3.d","Risk budgeting (absolute and relative)"],["P3.e","Heuristic vs formal risk constraints"],
        ["P3.f","AUM, position size, liquidity, turnover"],["P3.g","The well-constructed portfolio"],["P3.h","Long-only, long extension, long/short, market-neutral"]]))
    sub("Active return and its three sources", 5,
      P("<b>In plain words:</b> active return = portfolio return − benchmark return. It is positive if you overweight winners and underweight losers. Active portfolios aim to beat the benchmark <b>after all costs</b>.") +
      F("R_A = Σ (wₚᵢ − wᵦᵢ) × Rᵢ\nEx post: R_A = Σ (βₚₖ − βᵦₖ) × F_k   +   α   +   ε\n              (factor exposure)    (skill)   (idiosyncratic = luck)") +
      T(["Source","What it is"],
        [["1. Rewarded factor exposure","Long-term exposures that differ from the benchmark to factors with positive risk premiums: market (beta), size, value, liquidity, momentum"],
         ["2. Alpha","Tactical bets on mispriced securities, sectors, factors — return not explained by factor exposure = <b>skill</b>"],
         ["3. Idiosyncratic risk","Return from concentrated positions not due to factors or skill = <b>luck</b>"]]))
    sub("The building blocks of portfolio construction", 5,
      T(["Block","Meaning","Main link"],
        [["1. Factor weightings","Over/underweight rewarded factors vs benchmark. Now cheap via rules-based index products → static factor exposure is <b>no longer alpha</b>","Source 1"],
         ["2. Alpha skills","<b>Factor timing</b> of rewarded factors (value vs growth) or unrewarded ones (countries, sectors, commodities, single stocks — 'thematic' for discretionary managers)","Source 2"],
         ["3. Position sizing","Balance conviction against idiosyncratic risk. Affects all three sources, most of all idiosyncratic. Many small positions → lower volatility","Source 3"],
         ["4. Breadth of expertise","Integrates the three; broader expertise → more consistent active return","All"]]) +
      K("Factor-oriented manager: many assets → little idiosyncratic risk. Stock picker: concentrated → takes idiosyncratic risk on purpose"))
    sub("Fundamental law of active management", 5,
      P("<b>In plain words:</b> expected outperformance grows with skill (IC), with the number of independent bets (breadth), with risk taken, and with how freely insights reach the portfolio (TC).") +
      F("E(R_A) = IC × √BR × σ_A × TC\nIC = information coefficient (skill) ; BR = breadth (independent decisions per year)\nσ_A = active risk ; TC = transfer coefficient (0–1)\nQuiz: 10 decisions per month → BR = 120 ; IC 0.1, σ_A 5%, TC 0.5\nE(R_A) = 0.1 × √120 × 5% × 0.5 = <b>2.74%</b> (answer C)") +
      K("Single factor, single metric → decisions not independent → low breadth","Several factors, several metrics each → more independent decisions → higher breadth",
        "Fewer constraints (e.g. allowing shorts) → higher TC → higher information ratio") +
      TRAP("Breadth must be <b>annual</b> — multiply monthly decisions by 12."))
    sub("Approaches to portfolio construction", 4,
      T(["Approach","Factor weightings","Alpha skills (timing)","Position sizing","Optimisation"],
        [["Systematic bottom-up","Diversified rewarded factors","Rule-based signals","Many small positions","Formal optimiser common"],
         ["Systematic top-down","Factor/macro rules","Some rule-based timing","Diversified","Formal"],
         ["Discretionary bottom-up","Implicit via stock choice","Security selection","Concentrated","Less formal"],
         ["Discretionary top-down","Macro/thematic bets","<b>Most factor timing</b>","Concentrated in themes","Less formal"]]) +
      K("Systematic = rules; discretionary = judgment. Bottom-up = stock data; top-down = macro data",
        "Discretionary managers: more factor timing, more concentrated, less formal optimisation",
        "Quiz: factor timing most likely by <b>discretionary top-down</b>"))
    sub("Objectives and constraints", 4,
      P("<b>In plain words:</b> building a portfolio is an optimisation: one goal (objective) plus limits (constraints), stated in absolute or benchmark-relative terms.") +
      T(["","Absolute","Relative"],
        [["Objective","Maximise Sharpe ratio","Maximise information ratio"],
         ["Constraint","Maximum volatility","Maximum active risk (tracking error)"]]) +
      K("Other objectives: minimise volatility, downside risk or drawdowns",
        "Maximise exposure to rewarded factors (size, value, momentum)",
        "Maximise a custom trait set by a discretionary manager (e.g. a deep-value metric)",
        "<b>Heuristic</b> weighting: rank stocks by a trait (e.g. low P/B) — less scientific"))
    sub("Active Share", 5,
      P("<b>In plain words:</b> Active Share measures how different your <b>holdings</b> are from the benchmark's. 0 = identical; 1 = no stock in common. Benchmark-aware managers keep it low; benchmark-agnostic managers let it be high.") +
      F("Active Share = ½ × Σ |wₚᵢ − wᵦᵢ|  (= total overweights = total underweights)\nOverlap with benchmark = 1 − Active Share\nBenchmark: A, B, C, D 25% each (universe A–F)\nPortfolio = benchmark → 0 ; portfolio only in E, F → ½ × (4 × 25% + 100%) = 1\nPortfolio B 10%, C 25%, D 25%, E 40% → ½ × (25 + 15 + 0 + 0 + 40)% = <b>0.40</b> → overlap 0.1 + 0.25 + 0.25 = 0.60") +
      K("Only benchmark stocks, same benchmark → <b>fewer</b> stocks = more concentrated = <b>higher</b> Active Share",
        "Fee check: Active Share 0.2 at same fee as 0.5 → expensive (closet indexing)",
        "Manager <b>fully controls</b> Active Share (sets weights)"))
    sub("Active risk & how it differs from Active Share", 5,
      P("<b>In plain words:</b> active risk (tracking error) = how much active return jumps around from period to period. It depends on <b>correlations</b>, so the manager cannot fully control it.") +
      F("Active risk σ_A = SD(Rₚ − Rᵦ)\nσ²_A = active factor risk (variance from βₚ − βᵦ) + active idiosyncratic risk (incl. alpha)") +
      T(["","Active Share","Active risk"],
        [["Measures","Holdings difference","Volatility of active return"],["Uses correlations?","No","Yes"],
         ["Realised vs predicted","—","Realised (history) and predicted (needs forecasts)"],["Control","Full","Partial"],
         ["Swap pharma A → similar pharma B","Up","Hardly up (quiz A)"],["Swap pharma → consumer discretionary","Up","Up"]]) +
      K("High net factor exposure → high active risk","No net factor exposure → active risk comes only from Active Share",
        "Active risk from Active Share falls as the number of stocks rises (inversely proportional)","Active risk rises with factor and idiosyncratic risk") +
      TRAP("Factor bets <b>always</b> raise Active Share; high Active Share does <b>not</b> always mean factor bets (stock A for stock B with the same exposures)."))
    sub("Classifying managers with Active Share and active risk", 5,
      T(["Manager","Active Share","Active risk","Typical limits"],
        [["Pure indexer","~0","~0","None"],["Closet indexer","Low","Low","Small deviations allowed"],
         ["Diversified multi-factor","Moderate","Moderate","Moderate sector deviation; low single-stock risk (many positions)"],
         ["Sector rotator","Moderate","<b>High</b>","Large sector deviations allowed"],
         ["Concentrated stock picker","<b>High</b>","High","Large single-stock deviations; may have sector weights fixed"]]) +
      K("Worked example: A = sector rotator (large sector deviations) · D = concentrated stock picker (large security risk, no sector deviation) · C = closet indexer (low target active risk) · B = diversified multi-factor (moderate everything, low single-stock risk)",
        "Tip: start with the most obvious manager, then eliminate"))
    sub("Risk budgeting: the four steps", 4,
      P("<b>In plain words:</b> a risk budget shares out the total risk you accept among positions or factors, like a spending budget shares out money.") +
      F("1. Choose the measure: <b>absolute</b> (total-return mandate, e.g. long/short vs cash + margin) or <b>relative</b> (beat an index)\n2. Understand what drives risk (rewarded factors? sectors? single stocks?)\n3. Set the overall risk level\n4. Allocate risk to positions/factors efficiently"))
    sub("Absolute risk: contribution of an asset and of a factor", 5,
      F("Contribution of asset i to variance: CVᵢ = Σⱼ wᵢ wⱼ Cov(i,j) = wᵢ × Cov(rᵢ, rₚ)\nσₚ² = Σ CVᵢ\nWorked: wA 0.20, wB 0.30, wC 0.50 ; Var(A) 0.05, Cov(A,B) 0.0067, Cov(A,C) 0.0013\nCV_A = 0.2×0.2×0.05 + 0.2×0.3×0.0067 + 0.2×0.5×0.0013 = <b>0.002532</b>\nσₚ² = 0.002532 + 0.001998 + 0.002880 = 0.00741 → A's share = <b>34.2%</b>") +
      F("Contribution of factor i: CVᶠᵢ = Σⱼ βᵢ βⱼ Cov(Fᵢ, Fⱼ) ; σₚ² = Σ CVᶠ + unexplained\nMarket β 0.892, size β −0.283 ; Var(M) 0.00178, Cov(M,S) 0.00042 ; σₚ = 3.74%\nMarket: 0.892×0.892×0.00178 + 0.892×(−0.283)×0.00042 = 0.00131\nσₚ² = 0.0374² = 0.0013988 → market explains <b>93.7%</b>\nSize −0.00007 → explained 0.00124 → unexplained 0.00016 = <b>11.4%</b>") +
      K("Country or sector contribution = its weight × covariance with the <b>portfolio</b> (quiz C — not with the global market, not correlation)",
        "Shares can add to over 100% when a factor contributes negatively",
        "Multi-factor manager: most risk explained by rewarded factors, little unexplained"))
    sub("Relative (active) risk contribution", 4,
      F("CAVᵢ = (wₚᵢ − wᵦᵢ) × Σⱼ (wₚⱼ − wᵦⱼ) × Cov(RAᵢ, RAⱼ)\nΣ CAVᵢ = active variance AVₚ") +
      K("Same idea as absolute, but uses <b>active weights</b> and covariances of <b>active returns</b>",
        "Example: benchmark 50% index A + 50% index B; portfolio holds A, B and cash. CAV_A 0.000233, CAV_B −0.000233, CAV_cash 0.001296 → cash = <b>100%</b> of active variance (calculation not tested)",
        "Cash has low SD but <b>high active risk</b> (twice the indexes') because it has low correlation with the benchmark",
        "Active returns of A and B correlate −1: when one beats the 50/50 benchmark the other must lag",
        "Can be done by country, sector or factor; split into active factor variance + unexplained") +
      T(["Manager","Main risk sources"],
        [["Factor diversified","Balanced rewarded factor exposures; low idiosyncratic and sector risk"],
         ["Sector rotator","Concentrated <b>sector</b> and <b>cash</b> bets dominate"]]))
    sub("Choosing the right level of risk", 4,
      T(["Issue","Why it limits risk"],
        [["Implementation constraints","Short/leverage limits stop full over/underweights; liquidity costs rise with active risk → <b>information ratio falls</b>"],
         ["Limited diversification","Concave efficient frontier: high-risk targets run out of good ideas → <b>Sharpe ratio falls</b>"],
         ["Leverage","Moves you up the straight capital allocation line for one period, but too much lowers compounded return"]]) +
      F("R_g ≈ R_a − σ²/2   (σ is squared, so leverage eventually lowers geometric return)\n−2% then +2%: 0.98 × 1.02 = 0.9996 ; −20% then +20%: 0.8 × 1.2 = <b>0.96</b>"))
    sub("Heuristic vs formal risk constraints", 5,
      T(["Type","Examples","Needs return-distribution forecast?"],
        [["Heuristic (experience, good practice)","Limits on single positions, sectors, regions; leverage; illiquidity; turnover","No"],
         ["Formal (statistical)","Volatility, active risk, skewness, drawdown, VaR family","<b>Yes</b> → estimation error (quiz B)"]]) +
      T(["VaR measure","Meaning"],
        [["CVaR (expected shortfall / expected tail loss)","Expected loss <b>given</b> VaR is exceeded"],
         ["Incremental VaR (IVaR)","Change in VaR from <b>adding a new</b> position"],
         ["Marginal VaR (MVaR)","Change in VaR from a <b>very small</b> change in a position"]]) +
      K("Leverage magnifies wrong risk estimates; tail events (early 2000s, 2008) force sales at bad prices",
        "Volatility spikes → managers tighten risk controls",
        "Benchmark-agnostic absolute-return manager → watches <b>drawdown</b>, not active risk; market-neutral manager → keeps <b>absolute volatility</b> in a range",
        "Few positions → higher estimation error → formal measures harder to use"))
    sub("AUM, liquidity, turnover and market impact", 5,
      P("<b>In plain words:</b> big trades move prices against you (market impact). This hidden cost eats alpha and grows with fund size, small caps, turnover and 'informative' trades.") +
      K("Impact ↑ with: higher AUM vs stock market cap · smaller caps · higher turnover · shorter horizon · trades that carry information",
        "<b>Slippage</b> = execution price − bid/ask midpoint when the order was entered",
        "Slippage facts: 1. usually &gt; explicit costs · 2. higher for small caps · 3. <b>not necessarily</b> higher in emerging markets · 4. much higher in volatile markets",
        "Small-cap manager as AUM grows: close to new money, tell investors the strategy may change, limit AUM, diversify, cut turnover, change trading",
        "Beware new funds raised on a track record that cannot scale; large-cap funds can hold more AUM") +
      F("Small cap $5bn, 1% traded daily → ADV $50m; limit 10% of ADV → max $5m\n$1bn fund → max weight 0.5% (maybe too small for a concentrated strategy)") +
      F("Scale: $200m fund, 350 stocks, index $20tn, 1,000 stocks, small ones trade 1.5% a day\nRule 1 no stock with index weight &lt; 0.02% → smallest stock = 0.0002 × 20tn = $4bn\nADV = 0.015 × 4bn = $60m ; Rule 3 max 5% of ADV → $3m\nRule 2 max weight = lesser of 10 × 0.02% = 0.2% and 0.02% + 1% = 1.02% → 0.2%\nImpaired when AUM &gt; 3m / 0.002 = <b>$1.5bn</b>") +
      TRAP("Higher market impact comes with <b>higher</b> AUM and turnover, and <b>smaller</b> caps (quiz C)."))
    sub("The well-constructed portfolio", 4,
      K("Clear philosophy + consistent process","Risk and structure as promised to investors","Desired exposures achieved efficiently","Reasonably low operating costs",
        "Same exposures with <b>fewer</b> positions → more risk-efficient (more risk-management focus; no return guarantee)",
        "Similar factor exposures → prefer lower absolute volatility and lower active risk",
        "Similar risks, costs and skill → prefer <b>higher Active Share</b> (leverages alpha skill) — quiz B",
        "Multi-manager equity sleeve: combine managers so a missing factor exposure is filled by a specialist"))
    sub("Long-only vs long/short: factors in the choice", 5,
      P("<b>In plain words:</b> short selling = borrow a stock, sell it, buy back later cheaper. It lets a manager act on <b>negative</b> views. Any portfolio that can short is 'long/short'.") +
      T(["Factor","Favours long-only because…"],
        [["Long-term risk premiums","Premiums are earned by being net <b>long</b>; long-term shorts lose (short horizons may want shorts)"],
         ["Capacity and scalability","Long capacity set by liquidity; short capacity set by <b>stock available to borrow</b> → lower"],
         ["Limited legal liability","Long loss capped at price paid; short loss <b>unlimited</b>"],
         ["Regulations","Some countries ban short selling"],
         ["Transactional complexity","Shorts need borrowing, collateral, recall risk, <b>prime broker</b> (extra counterparty risk)"],
         ["Costs","Higher fees and operating costs for long/short"],
         ["Personal ideology","Moral objection; doubt managers can short well; dislike leverage"]]))
    sub("Long/short structures: gross, net, 130/30, market-neutral", 5,
      F("Gross exposure = long + |short| (% of capital) ; Net = long − short\n$100m capital, $80m long, $30m short → gross <b>110%</b>, net <b>50%</b>\nCash $50m = $20m uninvested + $30m short-sale proceeds\n130/30 long extension: long 130%, short 30% → net 100%, gross 160%\nMarket-neutral: long $200m × β 0.9 = 180 ; short $150m × β 1.2 = 180 → net β = 0\nEqual long and short size → gross = 2 × long, net = 0") +
      K("<b>Long extension</b>: net fixed at 100%; manager has no discretion over gross/net; for investors wanting full market exposure plus some shorting",
        "<b>Market-neutral</b>: removes market risk where the manager has no edge; low volatility, low correlation → used for <b>diversification</b>; zero beta hard to hold as correlations change",
        "Built via <b>pairs trading</b>; quantitative pairs trading = stat arb"))
    sub("Long/short: benefits and drawbacks", 5,
      T(["Benefits","Drawbacks"],
        [["Express negative views fully (long-only max underweight = benchmark weight) → higher TC → higher IR","Losses unlimited (prices have no ceiling); <b>reduces exposure to market risk premium</b>"],
         ["Use short proceeds to <b>gear into high-conviction longs</b> (quiz A)","Leverage magnifies losses as well as gains"],
         ["Remove market risk → diversifier","Borrow costs can become very high (hard-to-borrow stocks)"],
         ["Better control of factor exposures (factors are long/short by nature)","Collateral calls force sales; <b>short squeeze</b>; lenders recall shares"]]) +
      TRAP("High leverage is <b>both</b> a benefit and a drawback — not the best answer for 'benefit'."))
