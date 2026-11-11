from summary_lib import *
from helpers import P

def add(chap, sub):
    chap(1, "P1 Index-Based Equity Strategies", "4% of PM", 3)
    sub("What this reading is about", 3,
      P("<b>In plain words:</b> an index fund tries to earn exactly what an index (e.g. the S&amp;P 500) earns — no more, no less. This reading covers: (1) factor-based indexes, (2) ways to get index exposure (funds, derivatives, own portfolio), (3) how to build the portfolio (full replication, sampling, optimisation), and (4) tracking error and its causes.") +
      T(["LOS","Topic"],[["P1.a","Factor-based vs market-cap-weighted indexing"],["P1.b/c","Approaches to index-based investing (pooled, derivatives, separately managed)"],
        ["P1.d","Full replication vs stratified sampling vs optimisation"],["P1.e","Causes and control of tracking error"],["P1.f","Sources of return and risk (attribution, securities lending, proxy voting)"]]))
    sub("Single-factor vs multifactor models (Fama-French five)", 4,
      P("<b>In plain words:</b> a 'factor' is a common driver of stock returns. CAPM says only one factor matters — the market (measured by beta). Multifactor models say returns depend on exposure to several factors.") +
      T(["Fama-French (2015) factor","How it is measured"],
        [["1. Market risk premium","Beta (standardised covariance with market return)"],
         ["2. Firm size","Market value of equity"],
         ["3. Book-to-market","Shareholders' equity ÷ market value of equity"],
         ["4. Operating profitability","Operating income ÷ beginning shareholders' equity"],
         ["5. Investment intensity","Growth rate of total assets"]]) +
      K("Other common factors: growth, value, size, yield, momentum, quality, volatility",
        "Factor indexes let investors <b>add to or replace</b> a cap-weighted index based on their view of future factor returns",
        "Usually packaged as <b>ETFs</b>"))
    sub("Factor-based strategies: passive or active?", 4,
      K("<b>Passive</b> side: rules-based, transparent, replicable",
        "<b>Active</b> side: choosing to emphasise some factors over the market portfolio is an active decision; managers may exploit out-of-favour factors",
        "Costs: <b>lower</b> than traditional active funds, <b>higher</b> than large cap-weighted index funds (higher fees and commissions)",
        "Transparency lets others copy the strategy → their buying moves prices → extra factor return can shrink or disappear",
        "Managers often use several benchmarks (factor + cap-weighted) → can raise tracking error") +
      TRAP("A factor index fund is passive in <b>implementation</b> but active in <b>factor choice</b>."))
    sub("Three types of factor-based strategy", 5,
      T(["Type","Examples","Notes"],
        [["Return-oriented","Dividend yield (high yield or dividend growth); momentum (overweight recent winners vs benchmark); fundamentally weighted (dividends, sales, income)","Focus on factors that explained past return differences"],
         ["Risk-oriented","Volatility weighting (weight = 1 ÷ price volatility); minimum-variance (Markowitz, with sector/country limits)","Simple, reduce risk — but rely on <b>past</b> data"],
         ["Diversification-oriented","Equal weighting; maximum diversification (maximise weighted-average stock volatility ÷ portfolio volatility)","Spread risk widely"]]) +
      K("Quiz: a <b>small-cap, high P/E</b> strategy → <b>return-oriented</b>") +
      TRAP("Minimum-variance is <b>risk</b>-oriented, not diversification-oriented. Equal weight is <b>diversification</b>-oriented."))
    sub("Three ways to get index exposure", 5,
      T(["Approach","Advantages","Disadvantages"],
        [["Pooled: open-end mutual fund","Low transaction costs, convenient structure","Must sell stocks to meet redemptions → taxable gains passed to all holders; traded only at close"],
         ["Pooled: ETF","Trades intraday; redemptions met <b>in kind</b> by authorised participants → no forced sales, fewer taxable gains","Commissions + bid-ask spread; some ETFs illiquid in secondary market"],
         ["Derivatives (futures, options, swaps)","Quick, cheap change of factor exposure; liquid markets; easy leverage","Expire → must roll; position limits; specialty needs may not exist; OTC counterparty risk; <b>basis risk</b> → tracking error"],
         ["Separately managed portfolio","Full control, customised","Needs updated index data, trading &amp; accounting systems, broker relationships for program trading, compliance systems"]]) +
      T(["Overlay type","Use"],
        [["Completion overlay","Return portfolio to index risk (e.g. match index beta)"],
         ["Rebalancing overlay","Cheaply match index reconstitution (adds/deletes)"],
         ["Currency overlay","Adjust FX risk of foreign holdings"]]))
    sub("Building the portfolio: replication, sampling, optimisation", 5,
      T(["Method","How","Pros","Cons / best for"],
        [["Full replication","Hold every index stock at index weight","Closest match to index (before costs)","Costly with many / illiquid stocks; must reconstitute and rebalance. Best: <b>few, liquid, similar</b> stocks"],
         ["Stratified sampling (cell matching)","Split index into strata (cells) by size, sector, country, dividend yield, momentum…; sample stocks in each cell; weight to match index exposures","Cheaper; keeps factor exposures","Strata must be <b>mutually exclusive and exhaustive</b>; more criteria → lower tracking error"],
         ["Optimisation","Mean-variance model minimises tracking error subject to constraints (min stocks, style tilt, min cap)","Lower tracking error than sampling; uses <b>covariances</b> directly","Based on historical relationships that change; costly to maintain; result may not be mean-variance efficient"],
         ["Blended","Replicate large liquid stocks; sample/optimise thin small caps","Best of both","E.g. Wilshire 5000"]]) +
      K("Optimisation can be run inside each stratum (combined with sampling)",
        "Many heterogeneous, thinly traded small caps → sampling or optimisation") +
      TRAP("Tracking error vs sample size: <b>first falls, then rises</b> — the last stocks added are illiquid and costly (quiz answer C)."))
    sub("Tracking error: causes and control", 5,
      P("<b>In plain words:</b> tracking error = standard deviation of (portfolio return − index return). For an index manager, low tracking error is the skill — the goal is to match, not beat.") +
      F("Tracking error = SD(R_portfolio − R_index)") +
      T(["Cause","Why"],
        [["Management fees","Index has no fees"],["Trade commissions","Index trades for free"],["Sampling","Not all stocks held"],
         ["Intraday trading","Index uses closing prices"],
         ["Cash drag","Cash held for flows; lowers return in rising markets, helps in falling markets"]]) +
      K("Control = trade-off: full replication's higher trading costs vs sampling's tracking error",
        "Must still trade for inflows, outflows and dividend reinvestment",
        "<b>Index futures</b> on idle cash reduce cash drag",
        "Quiz: tracking error is a better skill measure than excess return because the goal is to <b>match</b> the index"))
    sub("Sources of return and risk", 4,
      T(["Item","Point"],
        [["Attribution analysis","Finds sources of tracking error so the manager can reduce them (details in core Performance Evaluation reading)"],
         ["Securities lending","Lend stocks for fee income (or return on collateral) → offsets fees → <b>lowers</b> tracking error"],
         ["Proxy voting","Index managers still have a fiduciary duty to vote; good governance can raise index returns; costly across many firms → many use <b>proxy-voting services</b>"]]) +
      K("Corporate governance and investor activism matter for index managers too"))
