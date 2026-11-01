from summary_lib import *

def add(chap, sub):
    chap(2, "Concept & Role of a Mutual Fund", "4", 3)
    sub("Concept of a mutual fund", 4,
      KV([("Definition","Professionally managed investment vehicle (a <b>trust</b>) that mobilises money from investors and invests per stated objectives"),
          ("Correct phrase","Invest <b>through</b> mutual funds (not 'in') — a different <b>way</b> of investing, not a different product"),
          ("Gives access to","Equities, bonds, money market and other securities otherwise unavailable + professional management by AMC"),
          ("Difference","Professional investing, diversification, regulated vehicle")]))
    sub("Role of mutual funds", 3,
      L("Primary: help investors earn income / build wealth via securities markets",
        "'Fund' and 'scheme' used interchangeably; the offering entity = 'mutual fund' / 'the fund'",
        "Money raised funds govts &amp; companies → projects → jobs → demand → economic development",
        "As large investors, check investee companies' operations, corporate governance, ethics",
        "Livelihood for MF employees, distributors, registrars, service providers",
        "Higher output → more tax revenue → nation-building",
        "<b>Market stabiliser</b>: in 2022 and 2025 FPIs sold heavily; MF inflows provided counterforce"))
    sub("Investment objectives (Table 2.1)", 4,
      T(["Objective (from SIDs)","Category"],
        [["Reasonable income + high liquidity; only debt &amp; money market securities up to 91 days","Liquid fund"],
         ["Capital appreciation/income from portfolio predominantly in equity","Equity fund"],
         ["Long-term capital appreciation via mix: equity, debt, InvITs, commodities","Hybrid fund"],
         ["Goal-based investing, reduce risk over time via pre-determined maturity + glide path","Life Cycle Fund"]]) +
      K("Objectives stem from safety, liquidity, returns","Each pool = a scheme with pre-announced objective","Classification by objective ≈ by investment universe",
        "Profits/losses belong only to unitholders; all others earn fees/commission"))
    sub("Investment policy", 3,
      KV([("Investment policy","Asset allocation + investment style (to achieve the objective)"),
          ("Asset allocation","Disclosed in SID (e.g. liquidity → money market; long-term growth → equity)"),
          ("Style","Growth or value; concentration: focused vs diversified")]))
    sub("Key concepts: units, face value, unit capital, expenses, NAV, AUM, MTM", 5,
      T(["Term","Meaning"],
        [["Units","Investment translated into units of the scheme"],
         ["Face value","Typically ₹10 (can be ₹100); relevant for accounting"],
         ["Unit capital","Units issued × face value"],
         ["Recurring expenses","Fees/commissions to constituents; % of AUM; deducted in NAV → higher expense = lower NAV; SEBI limits"],
         ["NAV","True worth of a unit; net realisable value per unit if scheme liquidated"],
         ["AUM","Scheme size = NAV × units outstanding; AMC size judged by AUM; rises with performance/inflows, falls with IDCW/redemptions"],
         ["IDCW","Dividend option now called Income Distribution cum Capital Withdrawal"],
         ["Mark to market (MTM)","Valuing each security at current market value, daily, for NAV → daily NAV fluctuation"]]))
    sub("Advantages of mutual funds", 5,
      T(["Advantage","Workbook points"],
        [["Professional management","Objective-based, research-based, prudent processes; avoids multiple accounts (broking, demat); handles corporate benefits (interest, dividends, rights, buybacks); daily NAV = daily accounting; low cost, even smallest investments"],
         ["Affordable diversification","Proportionate ownership of diversified portfolio for as little as ₹500; 'eggs not in one basket'; same diversification directly needs several lakhs"],
         ["Economies of scale","Afford professional managers; research/office costs spread; better terms with brokers, bankers; IDCW/growth options to structure returns"],
         ["Transparency","3 sources: scheme documents (SID, SAI, KIM), portfolio disclosures (factsheet), NAV — available even to prospective investors"],
         ["Liquidity","Recover value from the fund (anytime / intervals / closure); bond market wholesale — MF gives small-ticket access; close-ended compulsorily listed; timely 'material' info + liquidity enhances safety"],
         ["Tax deferral","MFs don't pay tax on income; growth options defer investor's tax"],
         ["Tax benefits","ELSS: deduction up to ₹1,50,000 per FY u/s 80C (Old Tax Regime)"],
         ["Convenient options","Options suit liquidity/tax; partial withdrawal, additional investment, systematic transactions"],
         ["Investment comfort","Further purchases need very little documentation"],
         ["Regulatory comfort","SEBI checks and balances"],
         ["Systematic approach","SIP, SWP, STP → investment discipline"]]))
    sub("Limitations of mutual funds", 4,
      T(["Limitation","Points"],
        [["Lack of portfolio customisation","PMS gives large investors control/customised portfolio; MF unitholder is one of thousands, can't influence securities"],
         ["Choice overload","Many schemes/options; handled by information, advisers/MFDs; SEBI categorisation brings uniformity"],
         ["No control over costs","Costs shared in proportion; SEBI limits; market forces push costs below limits (advantage)"],
         ["No guaranteed returns","Pass-through vehicle; deciding factors: market movement, individual securities, team's skill — only skill is in manager's control"]]))
    sub("Classification by structure", 5,
      T(["Type","Features"],
        [["Open-ended","Perpetual purchase &amp; repurchase after NFO; no closing time-frame; unit capital keeps changing (units created on purchase, cancelled on redemption)"],
         ["Close-ended","Fixed maturity; buy from fund only in NFO; wound up at maturity; <b>listing compulsory</b> (every close-ended scheme other than ELSS); unit capital stable; trades usually at <b>discount</b> to NAV (buyer has better bargaining position)"],
         ["Interval","Largely close-ended, open at pre-specified intervals (e.g. Jan 1–5, Jul 1–5); compulsorily listed; <b>transaction period ≥ 2 working days</b>; <b>interval period ≥ 15 days</b>; redemption only in transaction period"]]) +
      K("SIF close-ended/interval strategies must also be listed","Listed close-ended/interval units: poor liquidity, discount to NAV","NFO = New Fund Offer (first offer to public)"))
    sub("Exchange Traded Funds (Box 2.1)", 4,
      L("Traded on exchange like a stock; usually track an index → passive",
        "Open-ended fund: single end-of-day NAV; ETF: multiple prices through the day",
        "Extra liquidity, benefit from intraday price changes; downside: price may fluctuate and gap from NAV",
        "Buy like a stock, small minimum; needs demat; wide variety of indices",
        "Market price tracks NAV closely (solves close-ended liquidity issue)",
        "Silver ETF introduced by SEBI (invests primarily in silver/silver-related instruments), like Gold ETF"))
    sub("Classification by portfolio management; MF Lite", 4,
      KV([("Active funds","Manager chooses portfolio within objective; higher expenses; expected to beat market"),
          ("Passive / index funds","Track an index (e.g. S&amp;P BSE Sensex) in same weights; mirror index; not designed to beat market; manager has no role; low running costs"),
          ("MF Lite (from 31 Dec 2024)","Framework for passively managed schemes: a mutual fund having only index funds, ETFs, FoFs or other specified schemes; <b>Chapter X of SEBI MF Regulations 2026</b>"),
          ("MF Lite scheme","Any scheme launched by an MF Lite or other eligible passive scheme specified by SEBI")]))
    sub("Classification by investment universe", 2,
      K("Equity, fixed income, money market, gold, international funds","Narrower: large cap, mid cap; G-sec funds, corporate debt funds"))
    sub("SEBI categorisation 2026 — five broad categories", 5,
      KV([("Circular","Categorisation and Rationalisation of MF Schemes, 2026 (SEBI circular dated 26 Feb 2026)"),
          ("Objective","Uniformity across fund houses; objective evaluation"),
          ("A. Equity","13 sub-categories"),("B. Debt","17 sub-categories"),("C. Hybrid","7 sub-categories"),
          ("D. Life Cycle Funds","(new)"),("E. Other","2 sub-categories")]))
    sub("Market-cap definitions (Box 2.2)", 5,
      T(["Category","Rank by full market capitalisation"],[["Large cap","1st – 100th"],["Mid cap","101st – 250th"],["Small cap","251st onwards"]]))
    sub("A. Equity schemes (13)", 5,
      T(["#","Category","Rule"],
        [["1","Multi Cap","Min <b>75%</b> equity: min 25% each in large, mid, small"],
         ["2","Large Cap","Min 80% in large cap"],
         ["3","Large &amp; Mid Cap","Min 35% large + min 35% mid"],
         ["4","Mid Cap","Min 65% mid cap"],
         ["5","Small Cap","Min 65% small cap"],
         ["6","Dividend Yield","Predominantly dividend-yielding stocks; min <b>80%</b> equity"],
         ["7","Value","Value strategy; min 80% equity"],
         ["8","Contra","Contrarian strategy; min 80% equity"],
         ["9","Focused","Max 30 stocks; must state focus (multi/large/mid/small cap); min 80% equity"],
         ["10","Sectoral","Specific sector (bank, power…); min 80% in sector"],
         ["11","Thematic","Theme (e.g. infrastructure: construction, cement, steel, telecom, power); min 80%"],
         ["12","ELSS – Tax Saver","Statutory 3-yr lock-in + tax benefit; min 80% equity (ELSS 2005 notified by MoF)"],
         ["13","Flexi Cap","Min 65% equity; dynamic across large/mid/small"]]) +
      K("Value AND Contra both allowed if portfolio overlap ≤ 50%","Sectoral/thematic: overlap ≤ 50% with other sectoral/thematic and other equity schemes except large cap",
        "Existing scheme can convert to Flexi Cap (fundamental attribute change rules)","Residual portion: equity, money market, liquid, gold &amp; silver instruments, InvITs (within limits)",
        "ESG = sub-category under thematic"))
    sub("B. Debt schemes (17)", 5,
      T(["#","Category","Rule"],
        [["1","Overnight","Overnight securities, 1-day maturity; may put ≤5% in G-secs/T-bills ≤30 days residual maturity as margin/collateral"],
         ["2","Liquid","Debt &amp; money market up to 91 days maturity"],
         ["3","Ultra-Short-Term","Macaulay duration 3–6 months"],
         ["4","Ultra Short to Short Term","Macaulay duration 6–12 months (low duration)"],
         ["5","Money Market","Money market instruments, maturity up to 1 yr"],
         ["6","Short Term","Macaulay duration 1–3 yrs"],
         ["7","Medium Term","3–4 yrs; under adverse situation 1–4 yrs"],
         ["8","Medium to Long Term","4–7 yrs; under adverse situation 1–7 yrs"],
         ["9","Long Term","&gt; 7 yrs"],
         ["10","Dynamic Term","Across duration"],
         ["11","Corporate Bond","Min 80% in AA+ and above corporate bonds"],
         ["12","Credit Risk","Min 65% in AA (excl. AA+) and below corporate bonds"],
         ["13","Banking &amp; PSU Debt","Min 80% in banks, PSUs, PFIs, municipal bonds"],
         ["14","Gilt","Min 80% G-secs across maturity"],
         ["15","10-yr Constant Maturity Gilt","Min 80% G-secs; Macaulay duration = 10 yrs"],
         ["16","Floating Interest Rates","Min 65% floating (incl. fixed converted via swaps/derivatives)"],
         ["17","Sectoral (debt)","Min 80% in one sector, AA+ and above, across duration; sectors: Financial Services, Energy, Infrastructure, Housing, Real Estate"]]) +
      TRAP("Scheme names can't stress only returns (e.g. 'credit opportunities', 'high yield', 'credit advantage') — SEBI circular 6 Oct 2017."))
    sub("C. Hybrid schemes (7)", 5,
      T(["#","Category","Rule"],
        [["1","Conservative Hybrid","Debt 75–90%, equity 10–25%"],
         ["2","Balanced Hybrid","Equity 40–60%, debt 40–60%; <b>no arbitrage</b>"],
         ["3","Aggressive Hybrid","Equity 65–80%, debt 20–35%"],
         ["4","Dynamic Asset Allocation / Balanced Advantage","Equity/debt managed dynamically"],
         ["5","Multi Asset Allocation","≥3 asset classes, ≥10% each; foreign securities NOT a separate asset class"],
         ["6","Arbitrage","Min 65% equity (arbitrage); debt limited to G-secs &lt;1 yr maturity + repo of govt bonds"],
         ["7","Equity Savings","Min 65% equity, min 10% debt; <b>net equity 15–40%</b>; min hedged/unhedged stated in SID"]]) +
      K("Residual in hybrid: InvITs (not arbitrage funds), ETCDs, Gold ETFs, Silver ETFs","Balanced and Aggressive listed together (one AMC offers either)"))
    sub("D. Life Cycle Funds (new)", 5,
      KV([("Strategy","Glide path across equity, debt, InvITs, ETCDs, gold &amp; silver ETFs; risk falls as maturity nears (equity ↓, debt ↑)"),
          ("Tenure","Min 5 yrs, max 30 yrs; multiples of 5"),
          ("Limit","Max <b>6</b> life cycle funds open for subscription per MF at a time"),
          ("Name","Must include maturity date (e.g. Life Cycle Fund 2045, 2055)")]) +
      T(["If AMC keeps…","It may not launch","May launch"],
        [["Children's Fund","20-yr life cycle fund","Any of remaining 5"],["Retirement Fund","30-yr life cycle fund","Any of remaining 5"],
         ["Both","20 &amp; 30-yr","Only 5, 10, 15, 25-yr (4 funds)"],["Neither (discontinues both; merged per Board approval)","—","All 6"]]))
    sub("E. Other schemes; one scheme per category rule", 5,
      T(["Category","Rule"],[["Index Funds / ETFs","Min 95% in index securities"],["Fund of Funds (overseas/domestic)","Min 95% in underlying fund"]]) +
      K("Only ONE scheme per category, except: (1) index funds/ETFs on different indices (2) FoFs with different underlying (3) sector/thematic funds in different sectors/themes"))
    sub("Other categories: FMP, TMF, capital protection, IDF, REMF", 4,
      T(["Type","Points"],
        [["Fixed Maturity Plan (FMP)","Close-ended debt; portfolio duration aligned to scheme maturity; pre-identified investments; no money post-NFO; clarity on likely returns (no guarantee)"],
         ["Target Maturity Fund (TMF)","Debt fund maturing on a specific date (typically 2–14 yrs); bonds with matching maturity → low reinvestment risk, predictable returns; listed for exit; low credit risk, tax efficiency, liquidity"],
         ["Capital Protection Oriented","Close-ended hybrid; equity via derivatives; e.g. ₹90 in debt for 3 yrs grows to ₹100; rest in equity derivatives"],
         ["Infrastructure Debt Fund (IDF)","Sponsored by banks/NBFCs; trust-based IDF = MF (SEBI); company-based = NBFC (RBI). IDF-MF: close-ended, min <b>90%</b> in debt/securitised debt of infra companies/projects/SPVs or bank loans of completed revenue-generating projects. IDF-NBFC sponsors: only banks &amp; Infrastructure Finance Companies"],
         ["Real Estate MF (REMF)","Real estate assets in cities per SEBI circular 2 May 2008; close-ended; must be listed"]]))
    sub("ESG investing", 3,
      K("Separate sub-category under thematic equity","Strategies: Exclusion · Integration · Best-in-class &amp; Positive Screening · Impact investing · Sustainable objectives · Transition / transition-related"))
    sub("REITs & InvITs (box)", 4,
      T(["","REIT","InvIT"],
        [["Registered with","SEBI (trust)","SEBI (trust)"],["Invests in","Commercial real estate","Infrastructure"],
         ["Asset value (initial offer)","≥ ₹500 crore","≥ ₹500 crore"],["Min offer size","≥ ₹250 crore","≥ ₹250 crore"],
         ["Min subscription","₹10,000–15,000 (earlier ₹50,000)","₹10,000–15,000 (earlier ₹1 lakh)"],["Listing / lot","Listed; trading lot 1 unit","Listed; trading lot 1 unit"]]) +
      K("SM REITs (small &amp; medium): asset value ≥ ₹50 crore, capped at ₹500 crore","REITs/InvITs are NOT mutual fund schemes","REIT raises later via follow-on, rights, institutional placements"))
    sub("New types of funds", 3,
      T(["Fund","Idea"],
        [["Factor-based","Factors: value (inexpensive), size (smaller cos), momentum (recent winners), low volatility, quality (strong fundamentals), dividend yield; factors rotate; often via ETFs"],
         ["Smart beta","Extension of index/ETF; less market-cap weighting (e.g. equal weight); aim: better returns, diversification, lower risk"],
         ["Quant","Machine/data-driven models from past data; removes human element"],
         ["International REITs","Exposure to overseas REITs: international + commercial real estate"]]))
    sub("Specialized Investment Fund (SIF) — strategies", 5,
      KV([("Why","Gap between MFs and PMS in portfolio flexibility; regulation gets more flexible MF → PMS → AIF"),
          ("What","New product line under MF regulations"),
          ("Minimum","₹10 lakh per investor across all strategies of the same AMC"),
          ("Proliferation","Only ONE strategy per category")]) +
      T(["Strategy","Rules","Structure / redemption"],
        [["Equity Long-Short","Min 80% equity; unhedged short ≤ 25%","Open-ended/interval; daily or less frequent"],
         ["Equity Ex-Top 100 Long-Short","Min 65% of NAV in stocks excluding top 100; short (non-large cap) ≤ 25%","Open-ended/interval; daily or less"],
         ["Sector Rotation Long-Short","Min 80% equity; max 4 sectors; short at sector level (all stocks of sector); short ≤ 25%","Open-ended/interval; daily or less"],
         ["Debt Long-Short","Debt across duration; unhedged short via exchange-traded debt derivatives","Interval; redemption once a week or less"],
         ["Sectoral Debt Long-Short","Min 2 sectors; max 75% per sector; short across all instruments of a sector; short ≤ 25%","Interval; once a week or less"],
         ["Active Asset Allocator Long-Short","Equity, debt, equity/debt/commodity derivatives, REITs, InvITs; short ≤ 25%","Interval; twice a week or less"],
         ["Hybrid Long-Short","Min 25% equity + min 25% debt; short ≤ 25%","Interval; twice a week or less"]]))
    sub("Growth of the MF industry in India", 3,
      T(["Metric","Data"],
        [["AUM","₹12.33 lakh crore (Mar 2016) → ₹79.46 lakh crore (Mar 2026); 10-yr CAGR 20.48%"],
         ["Folios","4.8 crore (Mar 2010) → 27.39 crore (Mar 2026)"],
         ["MF share in financial investments","10% (Mar 2016) → 12% (2017) → 14% (2018); bank deposits 71% → 69% → 65%"],
         ["India's share of world MF industry","0.33% (2008) → 0.60% (2018)"],
         ["Monthly SIP contribution","₹8,055 crore (Mar 2019) → ₹32,087 crore (Mar 2026)"],
         ["SIP AUM","₹15.11 lakh crore (Mar 2026)"]]))
