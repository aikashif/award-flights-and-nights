from summary_lib import *
from helpers import P

def add(chap, sub):
    chap(2, "P2 Active Equity Investing: Strategies", "12% of PM", 4)
    sub("What this reading is about", 3,
      P("<b>In plain words:</b> active managers try to <b>beat</b> a benchmark. This reading lists the ways they do it (fundamental vs quantitative; bottom-up vs top-down; factor, activist, stat arb, event-driven), how each strategy is built, its traps, and how to classify a manager's <b>style</b>. Learn the vocabulary, the steps, and the pros and cons.") +
      T(["LOS","Topic"],[["P2.a","Fundamental vs quantitative"],["P2.b / c","Bottom-up and top-down strategies"],["P2.d","Factor-based active strategies"],["P2.e","Activist strategies"],
        ["P2.f","Statistical arbitrage &amp; market microstructure (plus event-driven)"],["P2.g","Building a fundamental strategy"],["P2.h","Building a quantitative strategy"],["P2.i","Style classification"]]))
    sub("Fundamental vs quantitative approaches", 5,
      P("<b>In plain words:</b> a fundamental manager decides by <b>opinion</b> (judgment after research). A quant manager decides by <b>rules</b> found in historical data. Both may use the same data and tools — the difference is how the final buy/sell decision is made.") +
      T(["","Fundamental","Quantitative"],
        [["Style","Subjective, discretionary","Objective, systematic (rules)"],
         ["Decision based on","Analyst's research and judgment","Model of past data"],
         ["Focus","Company: financials, business model, management, industry position → intrinsic value","Factors that predict returns across many stocks (P/E, size, D/E, sector, momentum)"],
         ["Forecast","Intrinsic value and return of each firm","Expected return from factor exposures"],
         ["Portfolio","Fewer, larger positions; size by conviction within mandate limits","Many smaller positions; optimiser maximises alpha or information ratio"],
         ["Main risk","<b>Company</b> level: value wrongly estimated, or market never corrects the mispricing","<b>Portfolio</b> level: factors fail to perform as the model predicts"],
         ["Rebalancing","Continuous, whenever opinion changes","Automatic, at set intervals (monthly, quarterly)"]]) +
      K("Fundamental managers may use screens, DCF and regression; quants may use financial-statement data",
        "Quiz: screening for low P/B can be used by <b>both</b> types (answer C)"))
    sub("Bottom-up vs top-down", 5,
      T(["","Bottom-up","Top-down"],
        [["Information used","Single companies (profitability, momentum, brand, moat, management, governance)","Macro, policy, demographics — variables that affect many companies"],
         ["Selects","Best individual stocks","Best countries, sectors, styles, themes"],
         ["Tools","Stock purchases","Broad ETFs, index derivatives"]]) +
      K("Blends: top-down strategist sets country/sector weights → bottom-up managers pick stocks inside them",
        "Or: bottom-up picks stocks, then a top-down <b>derivatives overlay</b> removes unintended macro exposures",
        "Quant bottom-up: measurable links between firm data (P/E) and return. Fundamental bottom-up: also qualitative traits (brand, competitive advantage, management, governance)"))
    sub("Bottom-up value sub-styles", 5,
      P("<b>In plain words:</b> value investors buy stocks priced <b>below</b> their estimated intrinsic value.") +
      T(["Sub-style","Looks for"],
        [["Relative value","Low P/E, P/B vs peers/industry with no clear reason"],
         ["Contrarian","Going against sentiment, e.g. depressed cyclical stocks with low or negative earnings"],
         ["High-quality value","Value <b>plus</b> financial strength, good management, proven profitability ('Warren Buffett' style)"],
         ["Income investing","High dividend yield and dividend growth"],
         ["Deep value","Extremely low value vs assets (low P/B), often due to distress"],
         ["Restructuring &amp; distressed debt","Buy before or during expected bankruptcy; value released via restructuring or liquidation"],
         ["Special situations","Mispricing from corporate events: divestitures, spin-offs, mergers"]]) +
      TRAP("Undervalued vs <b>bankruptcy liquidation value</b> = restructuring/distressed debt (quiz B), not deep value."))
    sub("Bottom-up growth sub-styles & worked selection example", 5,
      P("<b>In plain words:</b> growth investors buy firms whose sales, earnings or cash flows will grow faster than the industry or market. They care less about high multiples and more about the source and persistence of growth.") +
      K("Consistent long-term growth","Short-term earnings momentum","<b>GARP</b> (growth at a reasonable price) — uses the PEG ratio") +
      F("PEG = P/E ÷ expected EPS growth (in % terms, e.g. 15 ÷ 10 = 1.5)\nExample (match each stock to one strategy, each used once):\nTW — lowest P/B 0.75 (only stock below 1) → <b>deep value</b>\nNB — lowest PEG 15/10 = 1.5 → <b>GARP</b>\nSO — P/E 20 vs sector 30 = 0.67 → <b>relative value</b> (TW's 1.5/8 is lower, but TW is needed for deep value)\nTO — dividend yield 1.08/12 = 9% → <b>income investing</b>"))
    sub("Top-down strategies & smart beta", 4,
      T(["Dimension","How"],
        [["Country / geography","Overweight attractive markets via ETFs, futures"],
         ["Industry sector","Overweight / underweight sectors"],
         ["Volatility","VIX futures, variance swaps, straddles (e.g. GARCH forecast: buy options when implied vol low, sell when high)"],
         ["Thematic","New technologies, regulation, economic cycles; long-term (cloud, blockchain, clean energy) or short-term (currency effect of a vote)"],
         ["Equity style rotation","Rotate into styles (factors) expected to outperform"]]) +
      K("Country/sector views can be checked bottom-up by adding up company values",
        "<b>Smart beta</b>: rotate exposures into factors (betas) expected to earn more — a top-down idea; made easy by focused ETFs and structured products",
        "Quiz: GARP on S&amp;P 500 stocks = <b>bottom-up</b>, not top-down"))
    sub("Factor-based strategies: rewarded factors & hedged portfolio", 5,
      P("<b>In plain words:</b> a factor is a stock trait linked to returns (e.g. small size, high book-to-market). <b>Rewarded</b> factors earn a long-term risk premium; <b>unrewarded</b> ones do not. A factor must make intuitive sense — otherwise heavy backtesting finds false patterns.") +
      F("Hedged portfolio approach (Fama-French):\n1. Rank universe by the factor (size → market cap)\n2. Split into quantiles (deciles 10%, quintiles 20%, quartiles 25%)\n3. Long best quantile, short worst (size: long smallest 10%, short largest 10%)\n4. Track the long/short return = the factor's return") +
      T(["Drawback","Meaning"],
        [["Middle quantiles ignored","Best stocks may sit in the middle"],["Assumes linear factor–return link","Non-linear effects missed"],
         ["False diversification","Several highly correlated factors"],["Needs short selling","Not always allowed"],
         ["Not a pure factor","Has exposures to other factors"]]) +
      K("<b>Factor-mimicking portfolio</b>: theoretical, dollar-neutral, exposure of 1 to the chosen factor and 0 to others; hard to build (liquidity, shorting)",
        "Long-only investors <b>tilt</b> toward factors; modest tilts = low tracking error = enhanced indexing",
        "Real value added = finding factors that predict the future") +
      TRAP("Value factor: go <b>long high</b> book-to-market (cheap), short low B/M. Using quartiles instead of deciles is <b>not</b> an error (quiz C)."))
    sub("Factor timing (style rotation) worked example", 4,
      P("<b>In plain words:</b> some factors work better in some conditions. Regress factor returns on a suspected driver to find when to hold each factor.") +
      F("Driver: ISurprise = actual central bank rate − rate priced in Eurodollar futures the day before (high = hawkish surprise)\nCurrent month: beta (market) coefficient −0.5 → high-beta stocks lose on upward surprise; size and value no signal\nNext month: size −1.0 (small caps underperform after hawkish surprise); value also negative; beta ≈ +0.7\nIssue: beta sign flips (− now, + next month) → need to know how long the effect lasts before trading on it"))
    sub("Activist strategies", 5,
      P("<b>In plain words:</b> activists buy a minority stake and push management for changes (strategy, capital structure, ESG, governance) to raise the share price. Example: Carl Icahn.") +
      F("Process: screen → buy stake (usually &lt; 10% of votes) → public proposal (open letter) → threaten proxy contest → launch proxy contest → keep negotiating") +
      T(["Activist tactics","Management defences"],
        [["Seek board seats (then change management)","Multi-class shares (founders hold extra votes)"],
         ["Open letters, meetings, rally other shareholders","<b>Poison pill</b>: existing holders buy shares at a discount → dilutes activist"],
         ["Proposals at the AGM","<b>Staggered board</b>: only part re-elected each year"],
         ["Financial restructuring: more dividends, buybacks",""],["Cut excessive pay; sue for breach of fiduciary duty",""],
         ["Media campaign; break up an inefficient conglomerate",""]]) +
      K("Roots: 1970s–80s corporate raiders; activist AUM more than doubled 2007–2015; campaigns rose four-fold",
        "<b>Targets</b>: slower growth than market, negative price momentum, weak governance",
        "<b>Impact</b>: better growth, profitability, governance, but <b>higher debt</b>; Sharpe ratios only slightly above market; prices rise before, most on the announcement day, modestly over the next month") +
      TRAP("Activists do <b>not</b> buy a majority stake (quiz A)."))
    sub("Statistical arbitrage & market microstructure", 5,
      P("<b>In plain words:</b> stat arb uses price and volume data to profit when related prices drift apart and then come back (mean reversion).") +
      F("Pairs trading: two historically correlated stocks in one industry\nSpread = ln(P_A / P_B)  (log gives a more stable signal)\nSpread &gt; moving average + 2 SD → SELL the spread (short A, long B)\nSpread &lt; moving average − 2 SD → BUY the spread\nProfit if the gap closes; risk = relationship broken for good") +
      K("<b>Market microstructure</b> arbitrage: supply/demand imbalances lasting milliseconds; needs limit order book analysis and <b>high-frequency trading</b> (quiz B)",
        "Stat arb and event-driven are usually quantitative but may include judgment"))
    sub("Event-driven strategies & risk arbitrage", 5,
      P("<b>In plain words:</b> event-driven managers profit from mispricing around corporate events: M&amp;A, earnings, restructuring, buybacks, special dividends, spin-offs. Unlike activists, they do <b>not</b> cause the event.") +
      T(["Merger type","Risk arb trade","Profit / risk"],
        [["Cash deal","Buy target after announcement (trades just below deal price)","Earn the gap when deal closes; big loss if deal fails"],
         ["Share-for-share","Buy target, short acquirer in the exchange ratio","Same"]]) +
      K("Key skill: estimate probability of failure, deal length and annualised premium") +
      F("Case: Formby (cash-rich tech, slowing growth, no dividend) → <b>activist</b>: push for dividends/buybacks\nParmeon (1-for-1 share deal, regulatory risk) → <b>event-driven</b>: buy target, short Parmeon 1:1\nBaron (distressed commodity trader) → <b>distressed debt</b>: buy bonds if market too pessimistic\nNOT a pairs trade for Baron — correlation broke for fundamental reasons, no mean reversion"))
    sub("Creating a fundamental strategy & its pitfalls", 5,
      F("1. Define universe per mandate; state the market opportunity (thesis)\n2. Prescreen to a manageable list (value manager drops high P/E)\n3. Analyse industry, competitive position, financial reports\n4. Forecast (cash flows or earnings)\n5. Convert forecasts to valuations\n6. Build portfolio with desired risk; add top-down views/constraints\n7. Rebalance; sell disciplines: target prices (take profit) and stop-losses") +
      T(["Pitfall","Meaning"],
        [["Behavioural biases","Confirmation, illusion of control, availability, loss aversion, overconfidence, regret aversion"],
         ["<b>Value trap</b>","Low multiple <b>justified</b> by deteriorating business → price keeps falling. Need a trigger for revaluation"],
         ["<b>Growth trap</b>","Growth already in (or over) the price: price assumes 15%, firm delivers 12% → P/E and price fall"]]) +
      K("Sell disciplines and stop-losses fight the bias to hold losers"))
    sub("Creating a quantitative strategy: steps & data", 5,
      F("1. Define market opportunity (thesis)\n2. Acquire and process data (most time-consuming)\n3. Backtest\n4. Evaluate (out-of-sample)\n5. Construct portfolio") +
      T(["Data type","Content"],
        [["Company mapping","Track firms over time and across vendors (mergers, bankruptcies, identifiers)"],
         ["Company fundamentals","Demographic, price, financial data (e.g. Bloomberg)"],
         ["Survey data","Earnings forecasts, macro, sentiment, fund flows"],
         ["Unconventional data","Satellite images, news sentiment, supply chains, events — machine learning helps"]]))
    sub("Backtesting: factor scores and information coefficient (IC)", 5,
      P("<b>In plain words:</b> the IC is the correlation between today's factor scores and <b>next period's</b> returns across stocks. Positive and significant = the factor predicts.") +
      F("Standardised factor score (z) = (stock value − mean) / SD\nE/P 7%, mean 3%, SD 5% → (7 − 3)/5 = 0.8\nPearson IC = correlation(factor score, subsequent return) — monthly 5–6% is very strong; hurt by outliers\nSpearman Rank IC = correlation of the <b>ranks</b> → robust to outliers") +
      F("9-stock example: Pearson IC −0.99% (distorted by stock A: negative score, +10.06% return)\nSpearman Rank IC +40% → high E/P does predict\nLong top 3 (G, H, I): (3.02 + 3.05 + 5.20)/3 = 3.76%\nShort bottom 3 (A, B, C): (10.06 − 0.6 − 0.5)/3 = 2.99%\nLong/short = <b>0.77%</b>; sample too small → test more data and periods") +
      K("Multifactor model: weight factors by judgment or mean-variance optimisation; a factor adds little if correlated with others",
        "Evaluate: <b>out-of-sample</b> tests; returns plus VaR and maximum drawdown",
        "Portfolio construction: commercial <b>risk models</b> (variances, correlations) and <b>trading costs</b> (explicit + market impact) — same return → choose lower cost") +
      TRAP("Predictive power uses <b>subsequent</b> returns, not contemporaneous. Outliers → <b>Spearman</b> (quiz B)."))
    sub("Pitfalls in quantitative investing", 5,
      T(["Pitfall","Meaning"],
        [["Survivorship bias","Test only on firms still alive → results look too good"],
         ["Look-ahead bias","Using data before it was available (December accounts to trade in January)"],
         ["Data mining / overfitting","Search until something works — not real proof"],
         ["Turnover","Limits stop the strategy being followed"],
         ["Stock not available to borrow","Shorts cannot be placed"],
         ["Transaction costs","Erode backtested returns"],
         ["<b>Quant crowding</b>","Many quants hold the same trades → mass exit, margin calls, fire sales (August 2007 quant meltdown in a calm market). Warning sign: high correlation of short interest and price momentum"]]))
    sub("Style classification: holdings-based (Morningstar style box)", 5,
      P("<b>In plain words:</b> style analysis says what kind of manager someone really is (large value, small growth…). Good style groups have high correlation inside and low correlation between groups.") +
      T(["Size","Value","Blend (core)","Growth"],[["Large (top 70% of market cap)","","",""],["Mid (next 20%)","","",""],["Small (rest)","","",""]]) +
      T(["Value score (weight)","Growth score (weight)"],
        [["Forward P/E 50%","Long-term projected EPS growth 50%"],["P/B 12.5%","Historical EPS growth 12.5%"],["P/S 12.5%","Sales growth 12.5%"],
         ["P/CF 12.5%","Cash flow growth 12.5%"],["Dividend yield 12.5%","Book value growth 12.5%"]]) +
      K("Each stock gets value and growth scores 0–100; net style = growth − value: strongly negative → value; strongly positive → growth; near 0 → core",
        "Morningstar: a <b>stock</b> with no bias = <b>core</b>; a <b>fund</b> with no bias = <b>blend</b>",
        "Columns hold about equal numbers of stocks; a stock can be part value, part growth (e.g. 60% to value index, 40% to growth)"))
    sub("Returns-based style analysis, self-identification, pros & cons", 5,
      F("Regress fund returns on passive style indexes, slopes sum to 1 (and ≥ 0)\nR_fund = b1 LargeGrowth + b2 SmallGrowth + b3 SmallValue + b4 LargeValue\nb1 = b2 = 0, b3 = 0.15, b4 = 0.85 → <b>value manager</b>, mostly large-cap value") +
      T(["","Holdings-based","Returns-based"],
        [["Shows","<b>Current</b> exposure (if holdings up to date)","<b>Average</b> exposure over the period"],
         ["Data","Detailed holdings; costly; needs history for averages","Only returns; cheap, quick"],
         ["Weakness","Misses derivatives overlays unless disclosed; holdings may be stale/window-dressed","Lags style changes; wrong index choice; collinear indexes; black box"],
         ["Strength","Precise, explains each stock","Captures effect of derivatives and all positions"]]) +
      K("<b>Self-identification</b>: manager's stated style — compare with both analyses; for long/short, market-neutral, short bias the prospectus is the key source") +
      TRAP("Undisclosed derivatives overlays mislead <b>holdings-based</b> analysis only (quiz A)."))
