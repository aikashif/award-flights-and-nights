from summary_lib import *

def add(chap, sub):
    chap(1, "Investment Landscape", "5", 3)
    sub("Why invest: examples & financial goals", 3,
      T(["Workbook example","Goal type"],
        [["Shalini (8 yrs) — wants to be a space scientist","Child's higher education (~10 yrs away)"],
         ["Rabindra (45, engineer, no pension)","Retirement (works ~15 more yrs)"],
         ["Surinder Singh (transferred to big city)","Buy a house (next couple of years)"],
         ["Mrs. D'Souza (just retired, lump sum)","Regular income for life (immediate + long, uncertain period)"]]) +
      KV([("Financial objective","A need (education, house, retirement…)"),
          ("Financial goal","Objective + <b>amount</b> + <b>timeline</b>"),
          ("Common goals","Child's education, child's marriage, retirement lifestyle, vehicle, buy/renovate house, big vacation"),
          ("Not-so-common","Start own business, sabbatical to fund higher education"),
          ("Why invest","Goal needs money that current income (salary/fees) can't fund at that time")]) +
      K("Start with WHY (Simon Sinek)","Questions about 'best fund' focus on investments, not the investor"))
    sub("Goal-setting steps", 4,
      F("1. Identify life events (desirable/planned vs undesirable surprises)\n2. Assign priorities (responsibilities vs good-to-have)\n3. Assign timeline + amount needed at that time\n4. Classify goals by horizon and importance") +
      K("Undesirable events (death, hospitalisation, accident, theft, fire) → can't plan via investments → emergency fund + insurance",
        "Retirement / children's education = responsibilities","Grand vacation = good-to-have","Only the individual/family decides priorities; MFD/adviser only guides"))
    sub("Short-term needs vs long-term goals; goal matrix", 3,
      T(["Horizon ↓ / Importance →","Critically important (responsibilities/needs)","Dreams","Good-to-have"],
        [["Immediate term","","",""],["Near term","","",""],["Medium term","","",""],["Long term","","",""]]) +
      K("Retirement goal = 2 parts: accumulate corpus + draw income from it","Mrs. D'Souza: income needed now AND for life"))
    sub("Covey's time management matrix", 2,
      T(["","Urgent","Not urgent"],[["Important","I","II"],["Not important","III","IV"]]) +
      K("Source: 'The Seven Habits of Highly Effective People' — Stephen R. Covey","Focus only on Quadrant I (urgent + important) → it grows and dominates",
        "Plan for important-but-not-urgent goals early, else they become urgent","Many struggle financially because they don't plan the important, not-urgent events"))
    sub("Goals, horizon & inflation; the pool approach", 4,
      KV([("Inflation (goal value)","Rise in the cost of a goal over time; must adjust goal values"),
          ("Fast-rising costs","Education and healthcare (impact retirement years)"),
          ("Pool approach","Meet all needs from one pool of savings — drawback: horizon of investments unknown"),
          ("Long-term goals","Inflation impact big → must factor in"),("Immediate / near-term","Little impact of price change")]) +
      F("Case: Shalini's education ₹50 lakh today, 10 yrs, 8% inflation → ≈ ₹1,07,94,625\nHousehold ₹30,000/month at 6% → ₹31,800 next year · ₹53,725 after 10 yrs · ₹96,214 after 20 yrs\nCommon to all goals: mismatch of cash flows (expenses > income, or no income)"))
    sub("Saving vs investing", 4,
      KV([("'Saving'","Same root as 'safe' — safety of money; reduce consumption so money is saved"),
          ("'Investing'","Primary objective: earn profits; risk–return trade-off"),
          ("Relationship","Two steps of the same process: <b>saving precedes investing</b>")]))
    sub("Factors to evaluate investments", 5,
      "<p class='sub'>Three most important: <b>safety, liquidity, returns</b>. Plus convenience, ticket size, taxability, tax deduction.</p>" +
      T(["Factor","Workbook points"],
        [["Safety","Safety of capital + degree of surety of income; understand the risks"],
         ["Liquidity","Ease of converting to cash; product nature or features (lock-in, exit penalty). Penalty doesn't hamper liquidity — only lowers return. <b>Divisibility</b>: can you sell part?"],
         ["Returns","Current income (periodic, without selling) + capital appreciation (only on sale). Exit charges = liquidity vs return trade-off"],
         ["Convenience","Ease of investing, withdrawing (full/part), checking value, receiving income"],
         ["Ticket size","Min amount: from ₹50/₹100 to &gt;₹1 lakh or &gt;₹1 crore; don't choose just because affordable"],
         ["Taxability of income","Post-tax return matters; don't view tax in isolation; some products tax-efficient only if held to maturity/min period"],
         ["Tax deduction","Raises effective return (on net amount invested); often comes with lock-in → liquidity vs deduction trade-off"]]) +
      TRAP("No factor in isolation; consider the investor's situation."))
    sub("Four asset classes", 5,
      T(["Asset class","Key traits (workbook)"],
        [["Real estate","Location = most important factor · illiquid · not divisible · physical or financial form · rent (current income) + appreciation · high transaction costs (brokerage, registration) · maintenance &amp; taxes reduce return · self-occupied house = expense, not investment · sub-types: residential, land, commercial"],
         ["Commodities","Most can't be invested (perishable/storage). Commodity derivatives not 'investments': leveraged + short-term. Gold &amp; silver = investment commodities; prices in sync globally (adjust for FX, costs); gold = safe haven; gold standard abandoned decades ago but central banks still hold gold; <b>no current income</b> — only appreciation; purity hard to judge"],
         ["Fixed income","Borrowing via bonds/debentures (used interchangeably); issuers: companies, Union/State govts, municipal corps, banks, FIs, PSUs; regular interest; held from issue to maturity → usually no capital gain; secondary trades → gains/losses; safer than equity, not risk-free; classify by issuer (govt/corporate) or maturity (short: liquidity; long: income)"],
         ["Equity","Owner's capital / risk capital; returns beat inflation historically; Sensex 100 (base 1979) → 82,269 (30 Jan 2026) ≈ 15.4% p.a. before dividends; dividends from profits; prices fluctuate often without regard to fundamentals but follow profits long-term"]]) +
      T(["Comparison","Equity","Bonds","Real estate","Commodities"],
        [["Form","Financial only","Financial only","Physical or financial","Physical or financial"],
         ["Consumption use?","No","No","Yes (self-use)","Yes (jewellery)"],
         ["Intermittent cash flow","Dividends (no guarantee)","Interest","Rent","<b>None</b>"],
         ["Investor is","Owner","Lender","Owner","Owner"],
         ["Cash flows known?","No","Agreed at issue","No","No"]]) +
      K("Ownership assets = uncertain returns","Lending assets (bonds, FDs) = agreed receipts","Tangible feels safer to many","International assets add currency exposure (e.g. LSE share → GBP/INR risk)") )
    sub("Table 1.1 — avenues by asset category", 4,
      T(["Equity","Fixed income","Real estate / infra","Commodities","Hybrid / others"],
        [["Blue-chip, mid-sized, small-sized, unlisted, foreign stocks; equity MFs; ETFs; index funds",
          "Bank FD &amp; RD; endowment &amp; money-back policies; PPF; SSY; SCSS; PO MIS; PO RD; company FD; debentures/bonds; debt MFs",
          "Physical: residential/commercial. Financial: REMF, REIT, InvIT",
          "Gold, silver, gold funds, commodity ETFs",
          "Hybrid/multi-asset MFs · Others: rare coins, art, rare stamps"]]) +
      TRAP("Endowment and money-back policies are listed under FIXED INCOME. InvIT is under real estate/infrastructure."))
    sub("Investment risks", 5,
      T(["Risk","Workbook points"],
        [["Inflation risk","Erodes purchasing power; hits hard over long periods. Nominal rate = return without inflation; <b>real rate</b> = inflation-adjusted. Safety + anytime liquidity usually earns below inflation (e.g. FD 7% vs inflation 8%)"],
         ["Liquidity risk","Promised return only if held to maturity (FD premature penalty; PPF no/partial liquidity); real estate takes weeks/months; listed equity liquid but volatile → unsuitable for short-term needs"],
         ["Credit risk","Delay or default of interest/principal. 3 outcomes: pays on time / pays late / doesn't pay. Causes: <b>ability</b> (business stability, profitability) or <b>intention</b>. Own-country government bonds safest → lowest rates"],
         ["Market &amp; price risk","Volatility from opinion changes. Market-wide (e.g. war fear) vs company-specific (product sales fall) vs industry-specific (policy, technology — pager industry vanished). Specific risk reduced by diversification; market-wide not"],
         ["Interest rate risk","Value changes with rates; affects bonds more than stocks; <b>inverse</b> relation; longer maturity → bigger price swings; market-wide"]]) +
      T(["Inflation 8% p.a. — money needed to buy ₹10,000 of goods today","Amount"],
        [["After 5 years","₹14,693"],["After 10 years","₹21,589"],["After 20 years","₹46,610"],["After 30 years","₹1,00,627"]]) +
      F("FV = P × (1 + r)^n\n100 units for ₹10,000 today → only 68 units after 5 yrs, 46 units after 10 yrs (8% inflation)\nBond ₹1,000 at 8%; new bonds offer 8.5% → old bond sells at a discount"))
    sub("Risk management strategies & risk measures", 4,
      T(["Strategy","Meaning"],
        [["Avoid","Skip products whose risk you don't want; experts: avoid what you don't understand (but lose the opportunity)"],
         ["Take a position","Act on an expected event (e.g. expect rates ↓ → sell short-maturity, buy long-maturity bonds); needs superior knowledge; not for most investors"],
         ["Diversify","Prudent for lay investors; spreads risk of loss"]]) +
      T(["Measure","For"],[["Credit rating, credit spreads","Credit risk"],["Variance, standard deviation, beta, modified duration","Volatility / return fluctuation (Ch 10)"]]))
    sub("Systematic vs unsystematic classification", 5,
      T(["Risk","Type"],
        [["Credit risk","Mostly unsystematic (issuer-specific)"],["Liquidity risk","Unsystematic most of the time (except market-wide crisis, e.g. GFC)"],
         ["Inflation risk","Systematic"],["Interest rate risk","Systematic (lower for short maturity, but exists)"],
         ["Market risk (market-wide volatility)","Systematic"],["Price risk of individual security","Unsystematic"]]) +
      K("Unsystematic = specific risk → reduced by diversification","Systematic = market-wide risk → cannot be diversified"))
    sub("Behavioural biases", 5,
      K("Dominant emotions: fear, greed, hope") +
      T(["Bias","Meaning"],
        [["Availability heuristic","Rely on examples that come to mind immediately → too little research, miss risks"],
         ["Confirmation bias","Seek info confirming existing views; decide first, then find data"],
         ["Familiarity bias","Prefer familiar ('known devil better than unknown angel') → concentration, poor diversification"],
         ["Herd mentality","Follow the group ('man is a social animal'); going against the herd often most profitable"],
         ["Loss aversion","Avoiding ₹5,000 loss preferred over ₹5,000 gain; identified by Kahneman &amp; Tversky (Kahneman: Nobel in Economics)"],
         ["Overconfidence","Overrate own ability → lower guard, take unassessed risks"],
         ["Recency bias","Extrapolate recent events; bear market → prefer safe assets, bull market → over-allocate risky assets"],
         ["Behaviour patterns","Personality (spender/saver/investor) drives saving; behavioural tests help"],
         ["Interest of the investors","Choose by interest, not suitability (IT employee holding only tech stocks) → concentration"],
         ["Ethical standards &amp; boundaries","Ethical people more disciplined; shortcuts derail long-term wealth"]]) +
      K("List not exhaustive","Remedy: detailed analysis; take a third person's opinion — RIA or MFD"))
    sub("Risk profiling", 5,
      KV([("Purpose","Don't sell schemes riskier than the investor can handle"),
          ("Need to take risk","Need higher returns to reach goals"),
          ("Ability to take risk","Financial ability + investment horizon"),
          ("Willingness to take risk","Psychological capacity"),
          ("Distributor's job","Evaluate all three; strike a balance when they conflict"),
          ("Method","Distributor free to choose/design own tools")]))
    sub("Asset allocation: SAA, TAA", 5,
      KV([("Definition","A <b>process</b> of allocating money across asset categories in line with a stated <b>objective</b>"),
          ("Strategic (SAA)","Aligned to goals; uses required return, horizon, risk profile; maintains a <b>target</b> % allocation"),
          ("Tactical (TAA)","Dynamically changes allocation to exploit opportunities; primary aim: improve <b>risk-adjusted return</b>; also called <b>dynamic asset allocation</b>; suits seasoned investors with large investible surplus"),
          ("Workbook example","Two-asset portfolio (equity + debt)")]))
    sub("Rebalancing", 5,
      F("Target 50:50 in A and B; ₹1,000 each\nA +20% → ₹1,200 ; B −5% → ₹950 ; total ₹2,150 → 55.81% : 44.19%\nRestore 50:50 → sell ₹125 of A, buy ₹125 of B  (buy low, sell high automatically)") +
      K("Needed for both SAA and TAA","Also when investor's situation / risk appetite changes") +
      KV([("SEBI passive-breach rebalancing","Deviation from SID asset allocation due to passive breach (not AMC's act/omission): <b>30 business days</b> for all schemes except index funds &amp; ETFs"),
          ("Not applicable","Overnight funds")]))
    sub("Do-it-yourself vs professional help", 3,
      T(["Question","Point"],
        [["Can one do it?","Ability (skills/knowledge) + time (history teacher can't teach higher maths)"],
         ["Does one want to?","May not enjoy research/admin/accounting; prefer profession, family, hobbies"],
         ["Can one afford to outsource?","MF costs capped by SEBI; compare with hidden costs of DIY: value of time + emotional mistakes"]]) +
      F("Example: DIY 12% vs fund 10% net (2% cost) on ₹10 lakh → ~₹20,000/yr saved — worth the time?\nValue of time may be higher for wealthier people") +
      K("MF = outsourcing the investing job to an AMC, not a different asset","For most investors MF is the better option"))
