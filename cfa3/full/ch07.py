from summary_lib import *
from helpers import P

def add(chap, sub):
    chap(7, "P7 Trade Strategy and Execution", "12% of PM", 4)
    sub("Why managers trade", 5,
      T(["Motivation","Key points"],
        [["Profit seeking","<b>Alpha decay</b> → urgency (news traders high, fundamental low); avoid <b>information leakage</b> using several venues incl. <b>dark pools</b> (ATS in US; MTF / systematic internaliser in Europe) vs <b>lit</b> exchanges"],
         ["Risk management / hedging","Rebalance to target exposure (duration, FX hedge); derivatives if liquid and allowed; watch leverage"],
         ["Cash flows","Subscriptions/redemptions; <b>cash drag</b> → equitise with ETFs/futures; redemptions at NAV → trade at <b>close</b>; weigh liquidity and tax when choosing what to sell"],
         ["Corporate actions, margin calls, index reconstitution","Reinvest income; urgent sales for margin calls; reconstitution → trade at close to cut tracking error"]]))
    sub("Inputs to trading strategy & the trader's dilemma", 5,
      T(["Input","Effect"],
        [["Order: side, absolute size, size vs ADV","Buying into rising market costlier; one-sided lists carry more market risk; bigger orders → more impact"],
         ["Security: type, short-term alpha, volatility, liquidity","Fast alpha decay → urgent; high volatility → <b>execution risk</b>; liquidity (tight spreads, depth) lowers both costs"],
         ["Market conditions","Crises: volatility up, liquidity down (2008; quant crowding Aug 2007)"],
         ["Risk aversion","More averse → trades faster"]]) +
      K("<b>Trader's dilemma</b>: trade fast → market impact &amp; leakage; trade slow → execution risk",
        "Longer horizon lowers market impact but raises execution risk","Higher liquidity lowers <b>both</b>"))
    sub("Reference price benchmarks", 5,
      T(["Type","Benchmark","Used by"],
        [["Pre-trade","Decision price","Ideal measure of the PM's decision"],["","Previous close","Quant managers (proxy for decision)"],
         ["","Opening price","Fundamental long-term managers (ignores overnight news); not if trading in the opening auction"],
         ["","Arrival price (when order reaches market)","Alpha-seeking active managers"],
         ["Intraday","VWAP","Passive over the day, rebalancing (sells fund buys)"],
         ["","TWAP","Ignore volume outliers; erratic volume"],
         ["Post-trade","Closing price","Index funds, NAV-based redemptions; can't judge during trading"],
         ["Price target","Manager's fair value","Short-term alpha: buy all you can below target"]]) +
      K("Short-term alpha trade: high urgency, price target + arrival price, algorithm","Long-term alpha in illiquid bonds: low urgency, sell gradually over weeks","Index reconstitution, low TE mandate → <b>market on close</b>"))
    sub("Execution methods & algorithms", 5,
      T(["Method","Description"],
        [["High-touch principal (broker risk)","Dealer takes risk, priced into spread; OTC, RFQ markets; very large/illiquid/urgent"],
         ["High-touch agency","Broker finds the other side; risk stays with manager"],
         ["Electronic / DMA","Order-driven limit order book; buy side accesses exchange through broker's technology"],
         ["Profit-seeking algos","Market makers, quants, HFT"]]) +
      T(["Execution algorithm","Best for"],
        [["Scheduled: POV (participation), VWAP, TWAP","Small orders, liquid markets, low urgency, minimise impact (rebalancing)"],
         ["Liquidity-seeking (opportunistic)","Large orders, illiquid, higher urgency, fear of leakage, sporadic liquidity; lit + dark"],
         ["Arrival price","Small orders, liquid; prices expected to move against you; risk-averse to execution risk"],
         ["Dark strategies / liquidity aggregators","Large orders, illiquid, need not fill immediately"],
         ["Smart order router (SOR)","Small market or limit orders across many venues"]]) +
      K("POV: uses liquidity when it appears but trades at any price and may not finish","VWAP/TWAP: finish on time but may force trades in thin periods",
        "100% of ADV → high-touch principal; big + urgent + illiquid → liquidity-seeking; small, low urgency → scheduled",
        "New: <b>clustering</b> (ML groups trades to pick algos) · high-frequency forecasting with <b>LASSO</b> to cut variables"))
    sub("Trading by market", 4,
      T(["Market","How it trades"],
        [["Equities","Lit exchanges + dark pools; electronic; algos common"],
         ["Fixed income","Many heterogeneous issues, low liquidity, big tickets → dealer quote-driven, high-touch, electronic <b>RFQ</b>; algos only for on-the-run Treasuries &amp; futures; urgent → principal, else agency"],
         ["Exchange-traded derivatives","Electronic, DMA; algos less common (more futures than options)"],
         ["OTC derivatives","Dealer, high-touch; post-2008 central clearing push (Dodd-Frank 2010)"],
         ["Spot FX","OTC tiers: interbank, interdealer, bank-to-client; large urgent → RFQ; large non-urgent → scheduled algos or agency; small → DMA"]]) +
      K("Example: small urgent futures → DMA · agency MBS → high-touch broker · large non-urgent equity → scheduled algorithm"))
    sub("Implementation shortfall (worked)", 5,
      F("IS = paper return − actual return  (paper = all shares at decision price, no costs)\nBuy 50,000 SJB, decision $20.00, arrival $20.10, filled 40,000 at $20.34, commission $0.02, close $20.55\nPaper = 50,000 × 0.55 = 27,500 ; actual = 40,000 × 0.21 − 800 = 7,600 → IS = $19,900 = <b>199 bp</b>\nDelay = 40,000 × (20.10 − 20.00) = 4,000 (40 bp)\nTrading = 40,000 × (20.34 − 20.10) = 9,600 (96 bp)\nOpportunity = 10,000 × (20.55 − 20.00) = 5,500 (55 bp)\nFixed fees = 800 (8 bp)") +
      F("Sell 100,000 FTRB, decision £2.56, arrival £2.59, sold 70,000 at £2.60, fee £400, close £2.54\nPaper = 100,000 × 0.02 = 2,000 ; actual = 70,000 × 0.06 − 400 = 3,800 → IS = −£1,800 = <b>−70.3 bp</b> (benefit)\nDelay −82.0 · trading −27.3 · opportunity +23.4 · fees +15.6\nQuiz: sell 10,000 at $32.50, 4,000 filled at $32.65, $0.03/sh, close $32.35 → paper 1,500, actual 1,080 → <b>12.92 bp</b>") +
      K("Delay cost ↓ with faster pre-trade analysis","Opportunity-cost analysis → redeploy unfilled cash into the next idea","Negative cost = trader added value") +
      TRAP("For sells, flip the signs: a higher sale price is a gain."))
    sub("Evaluating execution: arrival, market-adjusted, added value", 5,
      F("Cost (bp) = Side × (execution price − benchmark) / benchmark × 10,000   (Side +1 buy, −1 sell)\nIndex cost (bp) = Side × (index VWAP − index arrival) / index arrival\nMarket-adjusted cost = arrival cost − β × index cost\nAdded value = arrival cost − estimated pre-trade cost\nBuy at $25.50 vs close $25.60 → −39.1 bp (benefit)\nBuy: arrival €10 → €10.15 = 150 bp ; index 3,500 → 3,507 = 20 bp ; β 1.5 → 150 − 30 = <b>120 bp</b>\nPre-trade estimate 160 → added value −10 bp (good)\nQuiz sell: 8.40 → 8.38 = 23.8 bp ; index cost −1 × 50/3000 = −166.7 ; β 1.3 → <b>240.5 bp</b>") +
      K("Market-adjusted cost stops traders being blamed or credited for market moves"))
    sub("Trade governance & best execution", 5,
      T(["Trade policy area","Contents"],
        [["1. Meaning of best execution","Best <b>result</b>, not just best price: price, costs, speed, likelihood of execution &amp; settlement, size, nature of trade (block sale at a discount can be best execution)"],
         ["2. Factors for optimal approach","Urgency, size, liquidity, security type, venues, strategy horizon, reason; regulations — <b>MiFID II</b> effectively bans soft dollars in Europe"],
         ["3. Approved brokers &amp; venues","Kept by a <b>Best Execution Monitoring Committee</b> (execution, compliance, risk); criteria: execution quality, financial stability, ethics, settlement, costs, willingness to commit capital"],
         ["4. Monitoring","Reputation, errors, crimes, solvency; remove failing brokers; keep records for clients and regulators"]]) +
      TRAP("'Use the lowest-cost broker' and 'traders alone decide governance' are both <b>not</b> best practice."))
