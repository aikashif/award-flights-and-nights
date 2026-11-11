from summary_lib import *
from helpers import P

def add(chap, sub):
    chap(3, "P3 Active Equity Investing: Portfolio Construction", "11% of PM", 4)
    sub("Sources of active return & the building blocks", 5,
      P("<b>In plain words:</b> active return = portfolio return − benchmark return. It is positive if you overweight the winners. It comes from three places: different exposure to rewarded factors, true skill (alpha), and plain luck from concentrated bets.") +
      F("Active return = Σ(βₚᵢ − βᵦᵢ) × Factor return ᵢ   +   α (skill)   +   ε (idiosyncratic = luck)") +
      T(["Building block","Meaning","Link to return source"],
        [["1. Factor weightings","Over/underweight rewarded factors (market, size, value, momentum, liquidity) vs benchmark; static exposure no longer counts as alpha","Long-term factor exposure"],
         ["2. Alpha skills","Factor timing (rewarded or unrewarded: sectors, regions, commodities), security selection","Mispricing → alpha"],
         ["3. Position sizing","Balance conviction vs idiosyncratic risk; more, smaller positions → lower risk","Mostly idiosyncratic risk"],
         ["4. Breadth of expertise","Ties them together — more independent decisions","Consistency"]]))
    sub("Fundamental law of active management", 5,
      F("E(R_A) = IC × √BR × σ_A × TC\nIC = information coefficient (skill), BR = breadth (independent decisions per year),\nσ_A = active risk, TC = transfer coefficient (how well insights reach the portfolio)\nExample: 10 decisions/month → BR = 120; IC 0.1, σ_A 5%, TC 0.5\nE(R_A) = 0.1 × √120 × 5% × 0.5 = <b>2.74%</b>") +
      K("One factor, one metric → decisions not independent → low breadth","Shorting / fewer constraints raise TC → higher IR") +
      TRAP("Convert breadth to <b>annual</b>: 10 a month = 120 a year."))
    sub("Approaches, objectives and constraints", 4,
      T(["Approach","Typical use of building blocks"],
        [["Systematic (rules)","Diversified factor exposures, optimisation, many positions"],
         ["Discretionary (judgment)","More factor timing, concentrated, less formal optimisation"],
         ["Bottom-up / top-down","Security information vs macro information; factor timing mostly <b>discretionary top-down</b>"]]) +
      T(["","Absolute","Relative to benchmark"],
        [["Objective","Maximise Sharpe ratio","Maximise information ratio"],["Constraint","Max volatility","Max active risk / tracking error"]]) +
      K("Other objectives: minimise volatility/downside/drawdown · maximise rewarded-factor exposure · maximise custom traits (deep value) · heuristic ranking (e.g. by low P/B)"))
    sub("Active Share vs active risk", 5,
      F("Active Share = ½ Σ |wₚᵢ − wᵦᵢ|        0 = index; 1 = no overlap\n1 − Active Share = overlap with benchmark\nActive risk (tracking error) = SD of (Rₚ − Rᵦ)\nActive risk² = active factor risk (β differences) + active idiosyncratic risk (incl. alpha)") +
      T(["","Active Share","Active risk"],
        [["Measures","Holdings difference from benchmark","Volatility of active returns"],["Correlation matters?","No","Yes"],
         ["Manager control","<b>Full</b> (sets weights)","Partial (depends on estimated variances/correlations)"],
         ["Swap pharma A for similar pharma B","↑","Barely ↑"],["Swap pharma for consumer stock","↑","↑"]]) +
      K("Fewer, more concentrated stocks → higher Active Share","Active Share of 0.2 at the same fee as 0.5 = expensive (closet indexing)",
        "High net factor exposure → high active risk; no factor exposure → active risk all from Active Share (falls as number of stocks rises)") +
      T(["Manager type","Active Share","Active risk"],
        [["Closet indexer","Low","Low"],["Diversified multi-factor","Moderate","Moderate"],["Sector rotator","Moderate","High (large sector deviations)"],["Concentrated stock picker","High","High (large single-stock deviations, sector-neutral possible)"]]) +
      TRAP("Factor bets always raise Active Share, but high Active Share need not mean factor bets (two stocks with identical factor exposures)."))
    sub("Risk budgeting: absolute risk", 5,
      P("<b>In plain words:</b> a risk budget hands out the total risk you are willing to take across positions or factors, like a spending budget.") +
      F("4 steps: choose measure (absolute for total-return mandates, relative for index-beating) → understand risk sources → set budget → allocate\nContribution of asset i to variance: CVᵢ = Σⱼ wᵢ wⱼ Cov(i,j) = wᵢ × Cov(i, portfolio)\nAsset A (w 0.20, var 0.05): 0.2×0.2×0.05 + 0.2×0.3×0.0067 + 0.2×0.5×0.0013 = <b>0.002532</b>\nPortfolio variance = 0.002532 + 0.001998 + 0.002880 = 0.00741 → A's share = <b>34.2%</b>\nFactor contribution: Σⱼ βᵢ βⱼ Cov(Fᵢ,Fⱼ); market: 0.892²×0.00178 + 0.892×(−0.283)×0.00042 = 0.00131\nTotal variance 0.0374² = 0.0013988 → market explains <b>93.7%</b>; size −0.00007 → unexplained = 0.00016 = <b>11.4%</b>") +
      K("Contribution of a sector/country = its weight × covariance with the <b>portfolio</b>","Shares can exceed 100% when a factor contributes negatively"))
    sub("Risk budgeting: relative (active) risk", 4,
      F("Contribution of asset i to active variance: CAVᵢ = (wₚᵢ − wᵦᵢ) × Σⱼ (wₚⱼ − wᵦⱼ) × Cov(active returns i, j)") +
      K("Driven by active weight and active risk, not absolute SD","50/50 benchmark of two indexes + cash in portfolio: cash's active risk is high (low correlation) → cash = 100% of active variance; the two indexes' active returns correlate −1"))
    sub("Choosing the level of risk", 4,
      L("Implementation constraints (short/leverage limits, liquidity costs) → IR degrades as active risk rises",
        "Limited diversification at high risk → Sharpe falls (concave frontier)",
        "Leverage: R_g ≈ R_a − σ²/2 → too much leverage lowers compounded return (−20% then +20% = 0.96)"))
    sub("Heuristic vs formal risk constraints", 4,
      T(["Type","Examples","Needs return forecasts?"],
        [["Heuristic","Position, sector, region limits; leverage, liquidity, turnover limits","No"],
         ["Formal","Volatility, active risk, skewness, drawdown, VaR, <b>CVaR</b> (expected loss beyond VaR), <b>IVaR</b> (VaR change from adding a position), <b>MVaR</b> (VaR change from a tiny position change)","<b>Yes</b> → estimation error"]]) +
      K("Leverage magnifies estimation errors; tail events force sales","Absolute-return managers watch drawdown; market-neutral managers target absolute volatility","Concentrated portfolios → larger estimation error"))
    sub("AUM, liquidity, turnover and market impact", 5,
      F("Small cap $5bn, 1% trades daily → ADV $50m; limit 10% of ADV → max $5m\nIn a $1bn fund → max weight 0.5%\nScale example: $20tn index, min index weight 0.02% → smallest stock $4bn; ADV 1.5% → $60m\nMax 5% of ADV → $3m; max weight = min(10 × 0.02%, 0.02% + 1%) = 0.2%\nStrategy impaired when AUM &gt; $3m / 0.002 = <b>$1.5bn</b>") +
      K("Impact cost ↑ with: higher AUM vs market cap · smaller caps · higher turnover · shorter horizon · information-rich trades",
        "<b>Slippage</b> = execution price − midquote when order entered: usually &gt; explicit costs · higher for small caps · not necessarily higher in emerging markets · much higher in volatile markets",
        "Small-cap managers: close fund, diversify, cut turnover or change trading; beware track records that can't scale"))
    sub("The well-constructed portfolio", 4,
      K("Clear philosophy, consistent process · promised risk characteristics · efficient exposures · reasonable costs",
        "Same exposures with fewer positions → more risk-efficient","Same factors → prefer lower absolute and active risk",
        "Same risks, costs, skill → prefer <b>higher Active Share</b>","Combine managers to fill missing factor exposures"))
    sub("Long-only, long/short, long extension, market-neutral", 5,
      F("Gross exposure = longs + |shorts| ; net = longs − shorts (as % of capital)\n$100m capital, $80m long, $30m short → gross 110%, net 50%, cash $50m ($20m + $30m short proceeds)\n130/30 long extension: net 100%, gross 160%\nMarket-neutral: $200m long β 0.9 (=180) vs $150m short β 1.2 (=180) → net beta 0") +
      T(["Long-only merits","Long/short benefits","Long/short drawbacks"],
        [["Earns long-term risk premiums","Express negative views fully (long-only can at most not hold) → higher TC/IR","Unlimited loss on shorts; gives up market premium"],
         ["Higher capacity (liquidity vs borrow availability)","Use short proceeds to gear into best longs","Leverage magnifies losses"],
         ["Limited liability — loss capped","Remove market risk → diversifier","Borrow costs can spike"],
         ["No short-sale bans, simpler (no prime broker, collateral, recall risk)","Better control of factor exposures","Collateral calls, <b>short squeeze</b>, lender recalls"],
         ["Lower fees and costs; ideology",""," "]]) +
      K("Market-neutral built via pairs trading (quant = stat arb); low volatility, low correlation, mostly for diversification; hard to hold beta at zero"))
