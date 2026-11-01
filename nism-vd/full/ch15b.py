from summary_lib import *

def add(chap, sub):
    sub("Cash-and-carry vs reverse cash-and-carry", 5,
      T(["Situation","Arbitrage","Effect"],
        [["Futures &gt; fair price","<b>Cash and carry</b>: buy spot (borrowed money), sell futures, deliver at expiry","Spot ↑, futures ↓ until aligned"],
         ["Futures &lt; fair price","<b>Reverse cash and carry</b>: buy futures, sell spot (borrowed asset), earn interest on sale proceeds, return asset after futures delivery","Spot ↓, futures ↑ until aligned"]]))
    sub("Transaction costs & no-arbitrage bounds", 4,
      L("Margins, commissions, taxes create <b>no-arbitrage bounds</b> around fair price — no arbitrage inside them",
        "Every carrying-cost component widens the bounds; wider bounds = further from equilibrium",
        "Efficient markets need low operating costs → narrow bounds",
        "Different participants have different costs → different fair values and bounds → continuous trading"))
    sub("Cost of carry with income (dividend yield)", 5,
      F("Fair futures = Spot + Cost of carry − Inflows\nF = S × (1 + r − q)^T        Continuous: F = S × e^((r − q)T)\nIndex 17,500, financing 12%, index yield 4%, 90 days:\n  17,500 × (1.08)^(90/365) = 17,835.26 ; continuous 17,500 × e^(0.08 × 90/365) = 17,848.63\nFutures above 17,848.63 → buy index stocks, sell index futures") +
      K("Costs, taxes, margins ignored in fair price"))
    sub("Pricing with known dividends", 5,
      F("F = (S − PV of dividends) × e^(rT)\nS ₹200, T 0.5 yr, dividend ₹5 at 0.25 yr, r 6%\nPV = 5 × e^(−0.06 × 0.25) = 5 × e^(−0.015) ≈ 4.93\nF = (200 − 4.93) × e^(0.03) = 195.07 × e^0.03 ≈ 201.01"))
    sub("Assumptions of the cost of carry model", 4,
      L("Underlying abundant in cash market","Demand-supply not seasonal","Easy to hold/store","Can be sold short","No transaction costs","No taxes","No margins") +
      K("Fails for seasonal commodities (prices fall when new crop arrives), non-storable assets, assets that can't be shorted",
        "Ignores margins → better suited to <b>forwards</b> than futures","Can be adjusted for costs and taxes"))
    sub("Convenience yield", 4,
      L("Intangible inflow — comfort of holding the asset (e.g. hoarding grains, heating oil during floods)",
        "Subjective, differs by person and over time, hard to price",
        "If convenience yield dominates cost of carry → futures at <b>discount</b> to spot; reverse arbitrage impossible (no one lends the asset) → model breaks down",
        "Arises with scarcity / low inventory — <b>consumption assets (commodities)</b>, not financial assets"))
    sub("Expectations model", 5,
      L("Relationship of <b>expected spot</b> and futures prices moves market (esp. assets that can't be shorted or stored)",
        "Futures price = expected future spot price; futures may trade at premium or discount",
        "Futures &gt; spot → expected rise → '<b>contango</b> market'; futures &lt; spot → expected fall → '<b>backwardation</b> market'"))
    sub("Price discovery & convergence", 5,
      L("May 2024 index futures at 22,308.70 on 14 May → market expects spot to settle there at close of last trading day (30 May 2024)",
        "All participants predict the spot at one point in time → price discovery",
        "Futures and spot <b>converge at maturity</b> — futures settle at underlying cash price"))
    sub("Hedgers, traders, arbitrageurs in futures", 5,
      T(["Participant","Futures use"],
        [["Hedgers","Farmer sells futures to lock crop price; food processor buys; diversified investor sells index futures against correction"],
         ["Traders (speculators)","Cheaper to create positions; e.g. buy stock futures before good results; leverage is a double-edged sword — riskier than the underlying"],
         ["Arbitrageurs","Risk-free profit from mispricing; link markets"]]) +
      L("Traders take naked positions and give hedgers a counterparty — market depth depends on them",
        "Farmer fearing wheat price fall sells 3-month futures; buyer may be flour mill/bakery or a trader with the opposite view",
        "Arbitrageurs lock in profits (unlike traders)") +
      F("Spot ₹100, May futures ₹110, lot 50 → buy spot, sell futures → lock ₹10/share\nExpiry 108: cash +8, futures +2 = ₹10 × 50 = ₹500\nExpiry 95: cash −5, futures +15 = ₹10 × 50 = ₹500  (ignores costs)") +
      K("Arbitrage risks: time lag between legs; illiquid leg → only one leg executes → naked exposure; non-cash-settled markets need reversal",
        "Traders &amp; arbitrageurs bring liquidity → better price discovery, lower cost, less manipulation"))
    sub("Systematic vs unsystematic risk & beta", 5,
      T(["Risk","Examples","Managed by"],
        [["Unsystematic (specific)","Factory strike, key manager leaves, strong competitor","Diversification; single stock futures hedge total risk of a stock"],
         ["Systematic (market)","Monetary/fiscal policy change, currency depreciation, war","Index futures"]]) +
      L("Total price risk = systematic + unsystematic",
        "Stock futures vs cash: difference is deferred settlement",
        "Beta = sensitivity to index (historical): β 2 → stock moved 20% when index moved 10%",
        "β &gt; 1 = aggressive; β &lt; 1 = conservative",
        "Beta info from newspapers, Bloomberg, Reuters") +
      F("Portfolio beta = Σ weight × beta\nBetas 0.5, 1.1, 1.3, 0.9 with weights 35%, 15%, 20%, 30% → β = 0.87"))
    sub("Hedge ratio", 5,
      L("Single stock futures: <b>1:1</b> hedge (e.g. 550 HDFC Bank shares = 1 futures contract of 550)",
        "Index futures for a portfolio: not 1:1 (different composition and beta)") +
      F("Contracts = Vp × βp ÷ Vi    (Vi = futures index level × multiplier; futures beta vs spot index = 1)\nPortfolio ₹50,00,000, β 1.3 → hedge value ₹65,00,000\nNifty futures 23,900 × 65 = ₹15,53,500 → 65,00,000 ÷ 15,53,500 = 4.18 lots\n4 lots → under-hedged; 5 lots → slightly over-hedged → perfect hedge not always possible") +
      K("Hedge ratio changes with the index used; assumes past beta continues"))
    sub("Long hedge, short hedge, cross hedge, hedge month", 5,
      T(["Term","Meaning"],
        [["Long hedge","Go long futures to hedge a future purchase (expected inflow; fear of rising market); also lets you invest gradually and unwind futures"],
         ["Short hedge","Short futures to protect a portfolio you'll sell soon (fear of fall)"],
         ["Cross hedge","Use futures of a closely related asset (jet fuel hedged with crude/heating oil/gasoline); index futures on a portfolio is broadly a cross hedge"],
         ["Hedge contract month","Choose contract expiring <b>just after</b> the unwind date (sell portfolio on 20 June → short June futures, not May)"]]))
    sub("Trading: naked & spread positions", 4,
      L("Naked long when expecting rise (Sensex futures at 61,000, expect settlement higher); naked short when expecting fall; loss if wrong",
        "Spread = two opposite positions: same maturity, different products = <b>inter-commodity / inter-product</b> spread; same product, different maturities = <b>calendar / time / horizontal</b> spread",
        "Equity derivatives: only calendar spreads tradable; inter-commodity spreads (gold–silver, soybean complex) in commodity segment",
        "Calendar spread counted vs near month: short 3 one-month + long 2 two-month + long 3 three-month = 2 spreads (1st–2nd) + 1 spread (1st–3rd) + 2 naked three-month",
        "Spread becomes naked when near month expires or a leg is closed",
        "Spreads = conservatively speculative positions; <b>lower margin than two independent legs</b>"))
    sub("Arbitrage types & formulas", 5,
      T(["Type","Positions"],
        [["Cash and carry","Long cash + short futures"],["Reverse cash and carry","Long futures + short cash"],
         ["Inter-exchange","Same contract on two exchanges (Aug futures of Z at ₹101 NSE, ₹100 BSE → buy BSE, sell NSE; reverse when gap shrinks)"]]) +
      F("F = S + C   ·   F = S(1 + r)^T   ·   F = S × e^(rT)\nFutures > fair → cash and carry; futures < fair → reverse cash and carry\nDo it only if net inflow after costs, brokerage, margins") +
      K("Futures = quick, cheap tools to add or reduce portfolio risk — risk management and restructuring tools"))
    sub("Workbook sample numericals", 4,
      F("Sold 1 XYZ futures at 278, lot 1,200, bought back at 265 → profit (278 − 265) × 1,200 = +₹15,600\nShort 1 June XYZ (multiplier 50) at 3,400; profit ₹10,000 → closed by BUYING at 3,200") +
      K("Margins in futures: paid by both buyer and seller","When near leg of a calendar spread expires, far leg becomes a regular open position (True)"))
