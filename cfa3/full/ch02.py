from summary_lib import *
from helpers import P

def add(chap, sub):
    chap(2, "P2 Active Equity Investing: Strategies", "12% of PM", 4)
    sub("Fundamental vs quantitative approaches", 5,
      P("<b>In plain words:</b> both try to beat a benchmark. A <b>fundamental</b> manager decides by <b>judgment</b> after studying companies. A <b>quantitative</b> manager decides by <b>rules</b> built from data. The difference is how the buy decision is made, not the tools used.") +
      T(["","Fundamental","Quantitative"],
        [["Style","Subjective, analyst discretion","Objective, systematic rules from data"],["Focus","Company: business model, management, valuation","Factors across many stocks"],
         ["Portfolio","Fewer, larger, high-conviction positions","Many small positions; optimiser maximises alpha / IR"],
         ["Main risk","Company level: intrinsic value wrong, or mispricing never corrects","Portfolio level: factors stop working"],
         ["Rebalancing","Continuous, by opinion","Fixed intervals (monthly, quarterly), by rules"]]) +
      TRAP("Screening for low P/B can be used by <b>both</b> types. What matters is how the final decision is made."))
    sub("Bottom-up strategies: value & growth sub-styles", 5,
      T(["Value sub-style","Looks for"],
        [["Relative value","Low P/E or P/B vs peers, without good reason"],["Contrarian","Against sentiment — depressed cyclicals with low/negative earnings"],
         ["High-quality value","Value + financial strength + good management + profitability ('Warren Buffett')"],["Income","High dividend yield, dividend growth"],
         ["Deep value","Very low value vs assets (low P/B), often distressed"],["Restructuring &amp; distressed debt","Before/during bankruptcy — value released by restructuring or liquidation"],
         ["Special situations","Mispricing from divestitures, spin-offs, mergers"]]) +
      T(["Growth sub-style","Looks for"],[["Consistent growth","Long-term steady growth"],["Earnings momentum","Short-term earnings acceleration"],["GARP","Growth at reasonable price; <b>PEG = P/E ÷ growth %</b>"]]) +
      F("Matching example: lowest P/B 0.75 → deep value · lowest PEG (15/10 = 1.5) → GARP\nLowest P/E vs sector (20 vs 30 = 0.67) → relative value · highest yield (1.08/12 = 9%) → income") +
      K("Fundamental bottom-up: strong business model, brand, competitive advantage, management, governance",
        "Undervalued vs liquidation value → <b>distressed debt</b>, not deep value"))
    sub("Top-down strategies", 4,
      L("Macro, policy and market-level views; implement with broad ETFs and derivatives",
        "Dimensions: <b>country/geography · industry sector · volatility</b> (VIX futures, variance swaps, straddles) · <b>thematic</b> (cloud, blockchain, clean energy; or short-term like a political vote)",
        "Blend: top-down sets country/sector weights, bottom-up picks stocks; or bottom-up portfolio + top-down derivatives overlay to remove unintended macro bets",
        "'Smart beta' = rotating into factors expected to outperform — a top-down idea") +
      TRAP("A manager hunting GARP among individual S&amp;P 500 stocks is <b>bottom-up</b>, even if the universe is an index."))
    sub("Factor-based active strategies & the hedged portfolio", 5,
      P("<b>In plain words:</b> a factor is a stock trait linked to returns (small size, cheapness). To measure a factor, rank stocks by it, buy the best slice and short the worst slice, and track that long/short portfolio.") +
      F("Hedged portfolio (Fama–French): rank universe by factor → split into quantiles (deciles/quintiles)\n→ long best quantile, short worst → track return = factor return\nValue factor: long HIGH book-to-market (cheap), short LOW book-to-market (expensive)") +
      T(["Drawback of hedged portfolio approach",""],
        [["1","Ignores middle quantiles"],["2","Assumes a linear factor–return link"],["3","Correlated factors give less diversification than it seems"],
         ["4","Needs short selling"],["5","Not 'pure' — has exposures to other factors"]]) +
      K("Rewarded factors = persistent premium; avoid unrewarded ones; factor must make intuitive sense (else data-mined)",
        "<b>Factor-mimicking portfolio</b>: dollar-neutral, exposure 1 to one factor, 0 to others — hard to build (liquidity, shorting)",
        "Long-only investors tilt toward factors; small tilts = enhanced indexing",
        "Factor timing / <b>style rotation</b>: regress factor returns on drivers (e.g. rate surprises)") +
      F("Rate-surprise regression: current month beta coefficient −0.5 (high beta underperforms after upward surprise)\nNext month: size −1.0 (small caps underperform), value negative, beta ≈ +0.7 → timing of the beta effect needs study") +
      TRAP("Using quartiles instead of deciles is <b>not</b> an error. Buying low book-to-market and shorting high <b>is</b> the error."))
    sub("Activist strategies", 5,
      F("Process: screen → buy stake (usually &lt; 10% of votes) → public proposal (open letter) → threaten proxy contest → launch proxy contest / keep negotiating") +
      T(["Activist tactics","Management defences"],
        [["Seek board seats; open letters; rally shareholders","Multi-class shares (founder super-votes)"],
         ["Proposals at AGM","<b>Poison pill</b> (holders buy cheap shares, diluting activist)"],
         ["Higher dividends, buybacks; cut excessive pay","<b>Staggered board</b> (partial re-election each year)"],
         ["Lawsuits for breach of fiduciary duty; media campaigns; break up conglomerates",""]]) +
      K("Roots: 1970s–80s corporate raiders; activist AUM more than doubled 2007–2015, campaigns ×4",
        "Targets: slow growth, negative momentum, weak governance; may be ESG-driven",
        "Impact: better growth, profitability, governance — but <b>higher debt</b>; Sharpe slightly above market; prices rise into and on announcement day",
        "Activists do <b>not</b> take majority stakes") +
      F("Case: Formby (cash-rich, no dividend, slowing growth) → <b>activist</b> (push payouts/buybacks)"))
    sub("Statistical arbitrage & event-driven strategies", 5,
      T(["Strategy","How","Risk"],
        [["Pairs trading (stat arb)","Two historically correlated stocks; buy the laggard, short the leader; spread = ln(price ratio); sell spread &gt; +2 SD of moving average, buy &lt; −2 SD","Relationship broke for good → no mean reversion"],
         ["Market microstructure arbitrage","Millisecond order-book imbalances; needs HFT","Technology/latency"],
         ["Event-driven","Mispricing around M&amp;A, earnings, restructuring, buybacks, special dividends, spin-offs (no activism)","Event outcome"],
         ["Risk (merger) arbitrage","Cash deal: buy target below deal price. Stock deal: long target + short acquirer at exchange ratio","Deal fails → large loss; skill = estimating failure probability, timing, annualised premium"]]) +
      F("Case: Parmeon (1-for-1 share deal, regulatory doubt) → <b>event-driven</b>: buy target, short Parmeon 1:1\nBaron (profit warnings, new management, debt doubts, correlation broke) → <b>distressed debt</b>, NOT pairs trade"))
    sub("Building a fundamental strategy & its pitfalls", 4,
      F("1. Define universe per mandate + investment thesis\n2. Prescreen (e.g. drop high P/E)\n3. Analyse industry, competitive position, financials\n4. Forecast cash flows / earnings\n5. Convert forecasts to valuations\n6. Construct portfolio with desired risk (add top-down views)\n7. Rebalance; sell disciplines: target prices, stop-losses") +
      K("Biases: confirmation, illusion of control, availability, loss aversion, overconfidence, regret aversion",
        "<b>Value trap</b>: cheap for a reason — fundamentals deteriorating; need a catalyst",
        "<b>Growth trap</b>: growth already in the price (priced for 15%, delivers 12% → P/E collapses)"))
    sub("Building a quantitative strategy; information coefficient", 5,
      F("1. Define market opportunity  2. Acquire &amp; process data (most time-consuming)  3. Backtest  4. Evaluate (out-of-sample, VaR, drawdown)  5. Construct portfolio (risk model + trading costs)\nStandardised factor score = (value − mean) / SD   e.g. E/P 7%, mean 3%, SD 5% → 0.8\nPearson IC = correlation(factor score, SUBSEQUENT return); 5–6% monthly = very strong\nSpearman rank IC = correlation of ranks → robust to outliers") +
      F("9-stock example: Pearson IC −0.99% (distorted by outlier stock A); Spearman +40% → E/P predictive\nLong top 3 (G, H, I) = (3.02 + 3.05 + 5.20)/3 = 3.76% ; short bottom 3 (A, B, C) = 2.99% → L/S = 0.77%\nSmall sample → retest on more data") +
      K("Data types: company mapping · fundamentals · survey (estimates, sentiment, flows) · unconventional (satellite, news sentiment, supply chains)",
        "Pitfalls: <b>survivorship</b> bias · <b>look-ahead</b> bias (Dec accounts used in Jan) · data mining / overfitting · turnover · stock not available to borrow · transaction costs",
        "<b>Quant overcrowding</b>: everyone exits together (August 2007); warning sign = high correlation of short interest and momentum",
        "Correlated factors add little in a multi-factor model") +
      TRAP("IC must use <b>subsequent</b> returns, not contemporaneous. Worried about outliers → Spearman rank IC."))
    sub("Style classification: holdings-based vs returns-based", 5,
      L("Styles should be highly correlated within, low correlated between",
        "<b>Holdings-based</b> (Morningstar style box): size (large ≈ top 70% of cap, mid next 20%, small rest) × value/blend/growth; each stock gets value and growth scores 0–100; net = growth − value: strongly negative → value, positive → growth, near zero → core (stock) / blend (fund)",
        "<b>Returns-based</b> (Sharpe): regress fund returns on style indexes, coefficients sum to 1 = style allocation (e.g. large value 0.85, small value 0.15, growth 0)",
        "<b>Self-identification</b>: check against both; long/short, market-neutral, short-bias funds rely on prospectus") +
      T(["","Holdings-based","Returns-based"],
        [["Pros","Shows <b>current</b> exposure; precise; spots drift","Little data needed; captures <b>average</b> exposure over time; picks up derivatives overlays"],
         ["Cons","Needs frequent holdings data; misses undisclosed <b>derivatives overlays</b>; data-intensive","Needs long history; results depend on chosen indexes; shows past, not current, style"]]) +
      TRAP("Derivatives overlays with limited disclosure hurt <b>holdings-based</b> analysis only."))
