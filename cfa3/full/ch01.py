from summary_lib import *
from helpers import P

def add(chap, sub):
    chap(1, "P1 Index-Based Equity Strategies", "4% of PM", 3)
    sub("Factor-based vs market-cap indexing", 4,
      P("<b>In plain words:</b> a normal index fund buys every stock in proportion to its size (market cap). A <b>factor-based</b> fund instead tilts toward stocks with a chosen trait — cheap, small, high momentum — because the investor believes that trait will earn more.") +
      K("CAPM = one factor (market beta); multifactor models = several",
        "Fama–French (2015) five factors: market risk premium · size · book-to-market (value) · operating profitability · investment intensity (asset growth)",
        "Common factors: growth, value, size, yield, momentum, quality, volatility") +
      T(["Type","Examples"],
        [["Return-oriented","Dividend yield, momentum, <b>fundamentally weighted</b> (dividends, sales, income)"],
         ["Risk-oriented","Volatility weighting (weights = 1/volatility), minimum-variance (Markowitz with constraints)"],
         ["Diversification-oriented","Equal weighting, maximum diversification (max ratio of weighted-average stock volatility to portfolio volatility)"]]) +
      K("Factor funds are rules-based, transparent → 'passive', but tilting is a form of active management",
        "Cheaper than active management, dearer than cap-weighted index funds","Transparency lets others copy → may erode the extra return",
        "Multiple benchmarks (factor + cap-weighted) can raise tracking error",
        "Risk-oriented: simple, reduce risk, but rely on past data") +
      TRAP("A small-cap, high-P/E (growth) strategy is <b>return-oriented</b>, not risk-oriented."))
    sub("Ways to get index exposure", 4,
      T(["Approach","Pros","Cons"],
        [["Pooled: open-end mutual fund","Low transaction cost, convenient","Must sell stocks to meet redemptions → taxable gains"],
         ["Pooled: ETF","Trades intraday; in-kind redemptions → no forced sales, fewer taxable gains","Commissions, bid-ask spread, some ETFs illiquid"],
         ["Derivatives (futures, options, swaps)","Quick, cheap exposure change; liquid; easy leverage","Expire → must roll; position limits; may not fit special needs; OTC counterparty risk; basis risk → tracking error"],
         ["Separately managed portfolio","Full control","Needs index data, trading &amp; accounting systems, broker relationships (program trading), compliance systems"]]) +
      T(["Overlay","Purpose"],[["Completion overlay","Bring portfolio back to index risk (e.g. match beta)"],["Rebalancing overlay","Cheaply match index reconstitution"],["Currency overlay","Adjust FX risk of foreign holdings"]]))
    sub("Full replication, stratified sampling, optimisation", 5,
      T(["Method","How","Best for / drawbacks"],
        [["Full replication","Hold every index stock at index weight","Closest match before costs; costly for many/illiquid stocks; best for <b>few, liquid, similar</b> stocks"],
         ["Stratified sampling","Split index into mutually exclusive, exhaustive strata (size, sector, country, yield…); sample within each to match factor exposures","More criteria → lower tracking error"],
         ["Optimisation","Mean-variance: minimise tracking error subject to constraints","Accounts for covariances; lower TE than sampling; but based on history, costly to maintain, may not be mean-variance efficient"],
         ["Blended","Replicate large liquid names, sample/optimise the thin tail","Broad indexes like Wilshire 5000"]]) +
      TRAP("As you add stocks, tracking error <b>first falls, then rises</b>: the later, less liquid stocks add trading costs."))
    sub("Tracking error: causes, control, attribution", 4,
      P("<b>In plain words:</b> tracking error is how much the fund's return wobbles around the index return (SD of the return differences). For an index fund, low tracking error — not high excess return — shows skill.") +
      K("Causes: management fees · commissions · sampling · intraday trading (index uses closing prices) · <b>cash drag</b>",
        "Control: trade-off between replication cost and sampling error; use <b>index futures</b> to equitise cash",
        "Attribution analysis finds the sources of tracking error",
        "<b>Securities lending</b> income offsets fees → lowers tracking error",
        "Index managers still owe a fiduciary duty to vote proxies; many use proxy-voting services"))
