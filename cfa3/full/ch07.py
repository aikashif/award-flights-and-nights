from summary_lib import *
from helpers import P

def add(chap, sub):
    chap(7, "P7 Trade Strategy and Execution", "12% of PM", 4)
    sub("What this reading is about", 3,
      P("<b>In plain words:</b> once a PM decides to buy or sell, the trade must be done well. This reading covers why managers trade, what drives the choice of trading strategy, which benchmark price to judge against, which execution method or algorithm to use, how markets differ, how to <b>measure trading cost (implementation shortfall)</b>, how to judge execution, and what a firm's trade policy must contain.") +
      T(["LOS","Topic"],[["P7.a","Motivations to trade"],["P7.b","Inputs to trading strategy"],["P7.c","Benchmarks for trade execution"],["P7.d","Recommend a trading strategy"],
        ["P7.e","Choosing an algorithm class"],["P7.f","Characteristics of key markets"],["P7.g","Measuring trade cost (IS)"],["P7.h","Evaluating execution"],["P7.i","Trade governance"]]))
    sub("Four motivations to trade", 5,
      T(["Motivation","Key points"],
        [["1. Profit seeking","Act on mispricing before others. <b>Alpha decay</b> = loss of alpha after the decision: news traders high (urgent), fundamental long-term low. Avoid <b>information leakage</b>: split across venues incl. <b>dark pools</b> (no pre-trade transparency; but you can't see the other side → unknown fill chance). US: ATS; Europe: MTF (many parties) or systematic internaliser (single dealer). <b>Lit</b> venue = high pre-trade transparency (exchanges)"],
         ["2. Risk management / hedging","Rebalance to target risk (e.g. fixed duration), hedge FX. Derivatives if liquid contracts exist and mandate allows; otherwise trade securities. Leverage → monitor closely"],
         ["3. Cash flow needs","Subscriptions/redemptions; urgency depends on flow, fund liquidity, promised liquidity terms (daily vs one-month notice). Illiquid funds → <b>cash drag</b> → <b>equitise</b> with ETFs/derivatives. Redemptions at NAV (closing prices) → sell at the <b>close</b> (quiz C); weigh liquidity and tax"],
         ["4. Corporate actions, margin calls, index reconstitution","Mergers, spin-offs; reinvest dividends/coupons or sell for distributions; margin calls → urgent sales; reconstitution → trade at close to cut tracking error"]]))
    sub("Inputs to the trading strategy & the trader's dilemma", 5,
      T(["Input","Detail","Effect"],
        [["Order: side","Buy, sell, short sell, cover","Buying into a rising market costs more; all-buy or all-sell lists carry more market risk than mixed lists"],
         ["Order: absolute size","Number of shares","Bigger → more market impact → trade less urgently"],
         ["Order: relative size","% of average daily volume (ADV)","Higher % → more impact"],
         ["Security: type","Stocks, ETFs, ADRs, GDRs, derivatives, FX","Different markets, costs, rules, liquidity"],
         ["Security: short-term alpha","Fast alpha decay","More urgency; also when buying into a rising / selling into a falling market"],
         ["Security: price volatility","—","High → high <b>execution risk</b> (adverse move during trading)"],
         ["Security: liquidity","Narrow spreads, market depth","Lowers <b>both</b> execution risk and impact (quiz C)"],
         ["Market conditions","Volatility and liquidity, which change; crises (2008), quant crowding (Aug 2007)","Low liquidity → longer horizon; high volatility → trade faster"],
         ["Individual risk aversion","—","More averse → more urgency"]]) +
      K("<b>Trader's dilemma</b>: trade fast → market impact and information leakage; trade slow → execution risk",
        "Example: larger order → more impact; higher liquidity → less impact; faster alpha decay → trade fast → more impact",
        "'Longer horizon lowers market impact' = true; 'longer horizon lowers execution risk' = false"))
    sub("Reference price benchmarks", 5,
      T(["Type","Benchmark","Used by / notes"],
        [["Pre-trade (known before trading)","Decision price","Price when PM decided — the ideal"],
         ["","Previous close","Quant, rules-based managers (proxy for decision price)"],
         ["","Opening price","Fundamental long-term managers (ignores overnight news); not valid if you trade in the opening auction"],
         ["","Arrival price","Price when the order reaches the market — alpha-seeking active managers"],
         ["Intraday","VWAP (volume-weighted)","Trade passively with volume over the day; rebalancing (sells fund buys)"],
         ["","TWAP (time-weighted, ignores volume)","Remove outliers (big trades at highs/lows); erratic volume (quiz A)"],
         ["Post-trade","Closing price","Cut tracking error (index funds, NAV); can't judge performance during the day"],
         ["Price target","Manager's fair value","Short-term alpha: buy all you can below e.g. $10.50 fair value"]]))
    sub("Recommending a trading strategy by trade type", 5,
      P("<b>In plain words:</b> balance expected cost, risk and alpha decay against the manager's objective and risk aversion.") +
      T(["Trade type","Urgency","Benchmark","Execution"],
        [["Short-term alpha (news overreaction, liquid stock)","High","Price target + arrival price","Algorithm (arrival price / liquidity-seeking)"],
         ["Long-term alpha (sell illiquid bonds before credit worsens)","Low","Hard to use in practice","Sell gradually over weeks in small parts (avoid leakage, dealer pressure)"],
         ["Risk rebalance","Low–moderate","VWAP / arrival","Scheduled algorithm; sells fund buys"],
         ["Client redemption / cash flow","Finish by close","Closing price (NAV)","Market-on-close / scheduled"],
         ["New mandate / cash to invest","Low","Arrival / VWAP","Equitise with futures/ETFs, then buy securities over time"],
         ["Index reconstitution, low-TE fund","Close","Closing price","<b>Market on close</b> (quiz C)"]]))
    sub("Execution methods", 5,
      T(["Method","How it works","Use"],
        [["High-touch <b>principal</b> (broker risk) trade","Dealer takes all or some risk, priced into spread; quote-driven, OTC, off-exchange; <b>RFQ</b> markets quote only on request","Large blocks, illiquid, urgent"],
         ["High-touch <b>agency</b> trade","Broker finds the other side; risk stays with the manager","Large, less urgent"],
         ["Electronic trading","Order-driven central <b>limit order book</b> (limit = price or better)","Liquid markets"],
         ["Direct market access (DMA)","Buy side enters orders on the exchange through the broker's systems","Small, liquid, fast"],
         ["Algorithmic trading","Programmed rules: <b>profit-seeking</b> (market makers, quants, HFT) or <b>execution</b> algorithms","—"]]))
    sub("Execution algorithms and how to choose one", 5,
      T(["Algorithm","How","Best for"],
        [["Scheduled: POV (participation)","Trade e.g. 5% of volume","Uses extra liquidity; but trades at any price and may not finish"],
         ["Scheduled: VWAP / TWAP (time-slicing)","VWAP follows historical intraday volume (more at open and close); TWAP equal shares per period","Finishes on time; may force trades when thin or under-trade when busy"],
         ["<b>Scheduled (general)</b>","—","Small orders, liquid, low urgency, minimise impact (risk rebalancing)"],
         ["Liquidity-seeking (opportunistic)","Waits for the other side, then hits it; lit + dark","<b>Large</b> orders, illiquid, higher urgency, fear of leakage, sporadic liquidity"],
         ["Arrival price","Trades aggressively near the arrival price","Small orders, liquid, prices expected to move against you; risk-averse to execution risk (quiz STU)"],
         ["Dark strategies / liquidity aggregators","Trade across dark pools","Large orders, illiquid; can wait (lower fill chance)"],
         ["Smart order router (SOR)","Routes to best lit/dark venue","Small market orders (best price) or small limit orders (best fill chance) across many venues"]]) +
      F("Example (each used once):\nSFDL — large, illiquid, high urgency → <b>liquidity-seeking</b>\nTWEL — small, liquid, low urgency → <b>scheduled</b> (POV/VWAP/TWAP)\nUDSL — 100% of ADV → <b>high-touch principal</b> (algo would leak and move price)") +
      K("New: <b>clustering</b> — machine learning groups trades with similar features (e.g. size/ADV) and tests which algorithm works best, finding factors humans missed",
        "<b>High-frequency market forecasting</b> — models short-term direction; <b>LASSO</b> cuts many variables to a few significant ones"))
    sub("Trading characteristics of key markets", 5,
      T(["Market","How it trades"],
        [["Equities","Lit exchanges + dark pools; most advanced; mostly electronic; algorithms common"],
         ["Fixed income","Many heterogeneous issues, low liquidity, large orders → dealer quote-driven; electronic <b>RFQ</b> growing (quiz B); algorithms only for most liquid on-the-run Treasuries and futures; elsewhere high-touch: urgent → principal, less urgent → agency"],
         ["Exchange-traded derivatives","Electronic; algos less common than equities (more futures than options); buy side uses DMA"],
         ["OTC derivatives","Dealer quote-driven, high-touch; post-2008 push for transparency and central clearing (Dodd-Frank 2010)"],
         ["Spot FX","OTC, electronic + high-touch; tiers: interbank → interdealer → bank-to-client (smaller trades, wider spreads); large urgent → RFQ with brokers; large non-urgent → scheduled algos or agency; small → DMA"]]) +
      F("Example (each used once):\nSmall urgent futures order → <b>DMA</b>\nAgency MBS order → <b>high-touch broker risk</b>\nLarge non-urgent equity order → <b>scheduled algorithm</b>"))
    sub("Implementation shortfall: definition and worked buy", 5,
      P("<b>In plain words:</b> IS compares a 'paper' portfolio (all shares bought at the decision price, no costs) with what really happened. The gap is the full cost of trading — explicit (commissions) and implicit (impact, delay, missed shares).") +
      F("IS = paper return − actual return   (in bp of paper portfolio cost)\nBuy 50,000 SJB; decision $20.00 (9:00); arrival $20.10 (9:30); limit $20.50\nFilled 40,000 at $20.34; commission $0.02/share; close $20.55\nPaper = 50,000 × (20.55 − 20.00) = $27,500\nActual = 40,000 × (20.55 − 20.34) − 800 = $7,600\nIS = $19,900 / $1,000,000 = <b>199 bp</b>") +
      T(["Component","Formula","SJB"],
        [["Delay cost","Filled shares × (arrival − decision)","40,000 × 0.10 = $4,000 = 40 bp"],
         ["Trading cost","Filled × (execution − arrival)","40,000 × 0.24 = $9,600 = 96 bp"],
         ["Opportunity cost","Unfilled × (close − decision)","10,000 × 0.55 = $5,500 = 55 bp"],
         ["Fixed fees","Commissions, fees","$800 = 8 bp"]]) +
      K("Execution cost = delay + trading cost",
        "Cut <b>delay</b> with fast pre-/post-trade analysis",
        "Study <b>opportunity cost</b> → if only 80% will fill, put the other 20% in the next-best idea (avoid cash drag)",
        "Study <b>trading cost</b> → set benchmarks and urgency"))
    sub("Implementation shortfall: worked sell & quiz", 5,
      F("Sell 100,000 FTRB; decision £2.56 (1:05); high-touch agency, limit £2.50; arrival £2.59 (1:13)\nSold 70,000 at £2.60; commission £400; close £2.54\nPaper = 100,000 × (2.56 − 2.54) = £2,000 ; actual = 70,000 × (2.60 − 2.54) − 400 = £3,800\nIS = −£1,800 / £256,000 = <b>−70.3 bp</b> (a benefit)\nDelay 70,000 × (2.56 − 2.59) = −£2,100 = −82.0 bp\nTrading 70,000 × (2.59 − 2.60) = −£700 = −27.3 bp\nOpportunity 30,000 × (2.56 − 2.54) = £600 = 23.4 bp ; fees £400 = 15.6 bp") +
      F("Quiz: sell 10,000 STU; decision $32.50; arrival $32.60; 4,000 sold at $32.65; $0.03/share; close $32.35\nPaper 10,000 × 0.15 = 1,500 ; actual 4,000 × 0.30 − 120 = 1,080 → IS 420 / 325,000 = <b>12.92 bp</b>") +
      TRAP("For sells, a <b>higher</b> price is good: cost terms flip sign. A negative cost = value added."))
    sub("Evaluating trade execution: cost vs benchmark", 5,
      F("Cost (per share) = Side × (execution price − benchmark price)   Side +1 buy, −1 sell\nCost (bp) = Side × (P_exec − P_bench) / P_bench × 10,000\nBuy at $25.50, MOC benchmark $25.60 → +1 × (−0.10)/25.60 = <b>−39.1 bp</b> (benefit)") +
      F("Index cost (bp) = Side × (index VWAP − index arrival) / index arrival × 10,000\nMarket-adjusted cost = arrival cost − β × index cost\nBuy: arrival €10.00 → avg €10.15 = 150 bp ; index 3,500 → VWAP 3,507 = 20 bp ; β 1.5\nMarket-adjusted = 150 − 1.5 × 20 = <b>120 bp</b>\nQuiz sell: 8.40 → 8.38 → −1 × (−0.02)/8.40 = 23.8 bp ; index −1 × 50/3,000 = −166.7 bp ; β 1.3\n23.8 − 1.3 × (−166.7) = <b>240.5 bp</b>") +
      F("Added value (bp) = arrival cost − estimated pre-trade cost\n150 − 160 = <b>−10 bp</b> → trader added value") +
      K("Benchmarks: arrival, VWAP, TWAP, close — may use several",
        "Buying in a rising market / selling in a falling market creates cost regardless of skill → market-adjusted cost removes it",
        "Pre-trade cost model uses order size, market liquidity, etc."))
    sub("Trade governance: the trade policy", 5,
      T(["Area","Contents"],
        [["1. Meaning of best execution","Best <b>result</b> for clients, not just best price or lowest cost: price, trading costs, speed and likelihood of execution and settlement, size and liquidity, nature (urgency). Example: block sale at a discount to a trusted dealer before an expected bankruptcy can be best execution (avoids execution risk and leakage)"],
         ["2. Factors for the optimal approach","Urgency, size, liquidity (ADV), standard vs custom security, venue features, strategy horizon, reason for trade; reflect regulation and conventions — <b>MiFID II</b> effectively bans soft-dollar arrangements in Europe; equities/ETDs more algorithmic than fixed income"],
         ["3. Approved brokers and venues","List kept by a <b>Best Execution Monitoring Committee (BEMC)</b> — execution, compliance, risk staff. Criteria: service quality (price, speed, capacity), financial stability, ethical reputation, settlement facilities, competitive explicit costs, willingness to commit capital. OTC needs extra due diligence"],
         ["4. Monitoring","Watch reputation, error frequency, crimes, solvency; remove failing brokers promptly; monitor execution quality; keep records for clients and regulators (executions, allocations)"]]) +
      K("Soft dollars = paying for goods/services with commission rebates — may harm best execution") +
      TRAP("'Traders alone set governance' and 'best execution = lowest-cost broker' are <b>both</b> wrong (quiz: zero statements correct)."))
