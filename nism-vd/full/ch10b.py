from summary_lib import *

def add(chap, sub):
    sub("Debt fund management: duration, floaters, credit spreads", 5,
      L("Higher <b>modified duration</b> → more price volatility for a rate change",
        "Floaters reset coupon with market → hold value when yields change",
        "Expect rates ↑ → more floaters / shorter fixed-rate paper (low MD); expect rates ↓ → longer fixed-rate paper (high MD)",
        "Debt fund returns hinge on interest-rate calls (equity: sector &amp; stock calls)",
        "Rating upgrade → lower credit spread accepted → price ↑",
        "Accrual focus: money market, liquid, ultra short, floating rate funds (short maturities, low MD)",
        "Accrual + gains: mix of short and long; more long → more volatility",
        "<b>Duration management</b>: lengthen if rates expected to fall; risk = view goes wrong",
        "Credit plays: buy papers expected to be upgraded; risk = default if upgrade doesn't happen",
        "Tight SEBI mandate (e.g. overnight: only overnight securities) leaves little room; ultra-short may take credit risk (only maturity defined)",
        "Dynamic bond fund: manager positions portfolio on rate view"))
    sub("Gold fund performance", 4,
      L("No current income — gain only from price rise; demand-supply drives price",
        "Truly international asset, objectively measurable quality",
        "Indian price = international price (foreign currency) × exchange rate + import duties",
        "Global price: safe haven — rises in political/economic turmoil; central banks &amp; IMF hold gold; their selling weakens price, big countries' buying lifts it",
        "<b>Stronger rupee → lower returns</b>; weaker rupee → higher returns",
        "Gold funds are passive — no fund-manager decision risk"))
    sub("Real estate fund performance", 3,
      L("Local, immovable asset; local factors drive value",
        "Economy: uncertainty/recession → purchases postponed, prices weaken",
        "Infrastructure development → values rise",
        "Interest rates: cheap money → prices up; rate rise softens market",
        "Varies by type: residential, commercial, industrial, infrastructure, warehouse, hotel, retail",
        "Returns: rent (regular) + capital appreciation (hard to determine short-term)",
        "SEBI mandates neutral valuation agencies; currently <b>no MF schemes invest in real estate</b>; REITs gaining popularity"))
    sub("Simple, annualised and compounded return", 5,
      F("Simple return = (Later − Initial) ÷ Initial          NAV 12 → 15 = 25%\nAnnualised = Simple return × 12 ÷ months (or 365 ÷ days)\n   5% in 6 months → 10% ; 3% in 4 months → 9%\nCompounded = (Later ÷ Initial)^(1/n) − 1, n in years (days ÷ 365)\n   ₹1,000 → ₹4,000 in 2 yrs → 100%\nCompounding: ₹10,000 at 10% for 3 yrs → ₹13,310 (simple ₹13,000)") +
      K("These three ignore IDCW — valid only for growth options or IDCW options with no payout in the period"))
    sub("CAGR with IDCW reinvested (SEBI method)", 5,
      F("₹10,000 at ₹10 on 30 Jun 2019 → 1,000 units\n1 Jan 2020: IDCW ₹1 → ₹1,000 ÷ ex-NAV 12.50 = 80 units → 1,080\n1 Jan 2021: IDCW ₹1 → ₹1,080 ÷ ex-NAV 15 = 72 units → 1,152 units × ₹15 = ₹17,280\nn = 551 days ÷ 365 = 1.51 yrs → CAGR = (17,280 ÷ 10,000)^(1/1.51) − 1 = 43.65% (pre-tax)") +
      K("Assumes IDCW reinvested at ex-dividend NAV"))
    sub("Scheme returns vs investor returns", 4,
      L("Loads drag investor return below scheme return: exit load 1% → receive ₹14.85 not ₹15; old 2% entry load → paid ₹10.20",
        "Use amount actually paid (NAV + entry load) and actually received (NAV − exit load); taxes reduce further",
        "Additional purchases/partial redemptions also change investor return",
        "Advertised returns ignore loads",
        "Holding-period returns: CAGR if &gt; 1 year, simple absolute if &lt; 1 year; distorted by unusual start/end values",
        "<b>Rolling returns</b>: average annualised return over many consecutive periods (e.g. all 1-yr returns in 3 yrs, daily/weekly/monthly roll)",
        "Don't judge on returns alone: consistency, benchmark, peers; active fund should rise well and fall less; consider volatility"))
    sub("Assured returns", 3,
      K("MFs can't promise returns unless an assured-return scheme","Assured return needs a guarantor named in SID who pays any shortfall","So far no assured/guaranteed product — only capital protection-oriented funds"))
    sub("Risks from the investor's view", 5,
      T(["Fund","Investor risk"],
        [["Equity","Price, business and liquidity risk rise large → mid → small; higher in focused funds; goal may fail; invest per risk profile; keep liquid funds to avoid selling equity in downturns"],
         ["Debt","NAV moves with rates and credit migration; IDCW not guaranteed (schemes have skipped IDCW); liquid/ultra-short/low duration may give partial liquidity if gating or segregation; without segregation, staying investors' bad-paper exposure rises (5% → 10% after 50% redemptions); 2018–19 credit events hit even liquid funds — <b>'low risk' ≠ 'zero risk'</b>"],
         ["Hybrid — arbitrage","Not always pure arbitrage: debt, paired arbitrage, alpha hedging, merger arbitrage = directional views → losses/low returns possible"],
         ["Gold","Transparent, hard to manipulate; does well in turmoil, war, weak currency; know if Gold Sector Fund or Gold ETF; loses if gold price falls"],
         ["Real estate","Subjective valuation, illiquid, unorganised agents, high stamp duty/registration, regulatory &amp; litigation risk, low transparency, family-run groups with poor governance — high risk but less than direct real estate"]]) +
      K("Listing mandatory: every close-ended scheme (except ELSS) and segregated portfolio units (SEBI 28 Dec 2018)","Schemes being wound up (Clause 37(d)) listed for exit"))
    sub("Variance & standard deviation", 5,
      T(["Month","Scheme 1","Scheme 2"],
        [["1","5","5"],["2","4","−5"],["3","5","10"],["4","6","5"],["Average","5","3.75"],["Variance","0.67","39.58"]]) +
      L("Risk = fluctuation of periodic returns vs average (up or down)",
        "Variance: Excel =VAR(range); relevant for debt and equity",
        "Standard deviation = √variance = <b>total risk</b>; Excel =STDEV(range); compare with benchmark &amp; peers; historic → limited for prediction",
        "≥ 30 observations for accuracy",
        "Annualise: weekly × √52 (0.65 × √52 ≈ 4.70%); monthly × √12; daily × √252 (trading days)"))
    sub("Beta, modified duration, WAM, credit rating", 5,
      T(["Measure","Points"],
        [["Beta","From CAPM; systematic risk only; scheme vs diversified index (index β = 1); β 0.8 moves 8% when market moves 10%; β 1.2 moves 12%; <b>only for equity schemes</b>"],
         ["Modified duration","Sensitivity of debt value to interest rates; professionals' preferred measure"],
         ["Weighted average maturity","70% in 4-yr + 30% in 1-yr = 3.1 yrs; simpler, used with lay investors; longer → more fluctuation"],
         ["Credit rating","Default risk; G-secs and cash have none; higher rating → lower spread; downgrade (AAA → AA) → yield ↑, value ↓; anticipating upgrades can pay"]]))
    sub("Credit events & the redemption spiral", 4,
      F("Credit risk = default, delayed payment or downgrade (a 'credit event')\n₹10,000 cr scheme, 8% (₹800 cr) in debenture M; M downgraded; 20% redeemed\n→ other papers sold → corpus ₹8,000 cr → M = 10%; another halving → 20%\nRegulatory cap: max 10% in a single issuer") +
      K("Market-wide illiquidity can block redemptions even in good portfolios","SEBI's two tools: gating (restriction on redemption) and segregated portfolios"))
    sub("Gating — restriction on redemption", 5,
      L("Only for <b>systemic</b> crises affecting almost all securities, not issuer-specific problems",
        "Triggers: (a) market-wide liquidity issues — not to manage a scheme's own liquidity or a bad investment (b) market failure / exchange closure (political, economic, military, monetary emergencies) (c) operational issues — force majeure, technical failure (e.g. blackout) despite diligence",
        "Max <b>10 working days in any 90-day period</b>",
        "Needs approval of <b>AMC Board and Trustees</b>; SEBI informed immediately",
        "Requests up to <b>₹2 lakh</b> not restricted; above ₹2 lakh → first ₹2 lakh paid, excess restricted",
        "Possibility disclosed prominently in scheme documents"))
    sub("Segregated portfolio (side pocketing)", 5,
      KV([("Permitted","December 2018 — fair treatment in credit events + liquidity risk"),
          ("Definitions","Segregated portfolio = debt/money market instrument hit by credit event, separated; main portfolio = rest"),
          ("Trigger","Credit event at issuer level = downgrade by a SEBI-registered CRA; optional, AMC's discretion"),
          ("Unrated debt (7 Nov 2019)","For issuer with no rated debt — only on <b>actual default</b> of interest or principal; AMC informs AMFI immediately → AMFI informs all AMCs"),
          ("New schemes","All launched after 7 Nov 2019 must have enabling provisions in SID"),
          ("Policy","Written policy approved by trustees")]) +
      L("After trustee approval: effective from day of credit event; immediate press release; NAV of both portfolios from that day",
        "Existing investors get equal units in segregated portfolio",
        "No subscription/redemption in segregated portfolio; listed within <b>10 working days</b>; transfers enabled",
        "Redeeming investors keep segregated units; new subscribers get only main portfolio units",
        "If trustees don't approve → transactions at NAV of total portfolio"))
    sub("Segregated portfolio: TER, NAV, risks", 4,
      L("No investment &amp; advisory fee; other TER pro-rata only upon recovery, capped at simple average of daily non-management expenses of main portfolio while segregated portfolio existed",
        "Legal recovery costs charged in proportion to recovery, within main portfolio's TER limit; excess borne by AMC",
        "Costs never charged to main portfolio",
        "NAV declared daily; disclosed in scheme documents, monthly/half-yearly portfolios, annual report",
        "Risks: can't liquidate till recovery; may realise nothing; listing ≠ liquidity; may trade well below NAV"))
    sub("Segregated portfolio illustration", 4,
      F("30 Sep 2019: 8% XYZ Ltd NCD downgraded A- → C, marked down 50% (₹99.105 → ₹49.552)\nTotal net assets ₹1,00,01,227 ; 10,000 units ; NAV ₹1,000.1227\nMain portfolio (B+C+D+cash) = ₹87,62,427 → NAV ₹876.2427\nSegregated (XYZ) = ₹12,38,800 → NAV ₹123.88\n876.2427 + 123.88 = 1,000.1227 per unit (unchanged in total)"))
    sub("Risk mitigation for investors", 4,
      K("Equity: longer holding period narrows return range — 1 yr: extremes; 5 yrs: mostly positive/moderate; 10 yrs: negative returns next to nil",
        "Debt credit risk: check portfolio ratings; G-sec funds, TMFs, corporate bond funds hold better quality",
        "Debt interest rate risk: match holding period to portfolio maturity"))
