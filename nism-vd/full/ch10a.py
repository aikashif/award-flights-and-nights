from summary_lib import *

def add(chap, sub):
    chap(10, "Risk, Return & Performance of Funds", "5", 4)
    sub("Standard vs specific risk factors (SID)", 4,
      KV([("Standard / general","Risks all MF investments face"),("Specific","Risks of particular asset categories (credit &amp; interest rate → debt; currency → foreign securities)"),
          ("Who manages","Fund manager manages some; MF structure controls some; some remain with investor"),
          ("SID","Lists risks + risk mitigation strategies")]))
    sub("General risk factors", 5,
      L("Trading volumes, settlement, liquidity, default — incl. possible loss of principal",
        "NAV moves with markets, interest rates, currency, govt policy, tax, politics, economy, volatility",
        "Past performance of sponsor/AMC/MF doesn't guarantee future",
        "Scheme <b>name</b> doesn't indicate quality or prospects",
        "Sponsor not liable beyond initial contribution to set up the MF") +
      T(["Risk","Workbook points"],
        [["Liquidity","Trading volumes, settlement periods, transfer procedures; settlement delays → uninvested cash or missed opportunities; money market lacks developed secondary market; liquidity premium changes; G-secs more liquid but can freeze in extreme volatility; adverse RBI guidelines"],
         ["Interest rate","Rates ↑ → prices ↓; extent depends on coupon, maturity, yield level; derivatives too"],
         ["Re-investment","Interim cash flows reinvested at lower rate than assumed ('interest on interest')"],
         ["Political","Central/state/local politics, unrest, external tensions, policy delays"],
         ["Economic","Slowdown, fiscal deficits"],
         ["Foreign currency","INR vs FPI's home currency; AMC does NOT manage FPIs' currency risk; sponsor/fund/trustees/AMC not liable"],
         ["Settlement (counterparty)","Floating asset created via swap: counterparty may default"],
         ["Exchange transactions","Allotment/redemption depend on BSE/NSE and clearing corporations"]]))
    sub("Specific risk factors — equity, short selling, mid/small cap, dividend", 4,
      T(["Risk","Points"],
        [["Equity","Daily volatility; liquidity limited by volume &amp; settlement; affected by rates, FX, law, tax, politics"],
         ["Securities lending","Lend via approved intermediary; borrower returns equivalent securities + corporate benefits; risk: counterparty failure, loss of collateral rights / corporate benefits"],
         ["Short selling","Sell borrowed securities, buy back later; counterparty risk + liquidity risk (cover at much higher price)"],
         ["Mid &amp; small cap","Faster earnings growth expected but may fail; volatility and liquidity risk rise down the cap spectrum (large 1–100, mid 101–250, small 251+)"],
         ["Dividend","Due only when declared; past record no assurance"]]))
    sub("Derivative risks", 5,
      K("Highly leveraged — small margin, big gain/loss","Need understanding of derivative + underlying") +
      T(["Risk","Meaning"],
        [["Counterparty","Counterparty fails → renegotiate at unfavourable price; exchange-traded: exchange guarantees but you take exchange's performance risk"],
         ["Market liquidity","Can't trade due to low volumes or big price impact"],["Model","Mis-pricing / improper valuation"],
         ["Basis","Derivative moves differently from hedged security"],["Execution","Insufficient bids, trading suspension, circuit breakers"],
         ["Index futures","Same risk as the index portfolio"],["Strategy","Depends on manager's ability; no assurance"],["Fixed income derivatives","Interest rate + liquidity risk"]]))
    sub("Debt fund risks", 5,
      T(["Risk","Meaning"],
        [["Reinvestment","Rates on coupon/maturity dates may differ from original coupon"],
         ["Rating migration","Downgrade (AAA → AA+) hurts price; upgrade helps"],
         ["Term structure of interest rates","Rates ↓ → value ↑; rates ↑ → value ↓"],
         ["Credit","Issuer can't pay; managed by in-house credit analysis; corporate &gt; G-sec risk; AAA &lt; AA risk; derivative credit risk small (no principal exchanged)"],
         ["Floating rate — spread risk","Spread over benchmark widens → value falls even if benchmark unchanged"],
         ["Floating rate — basis risk","Benchmark becomes inactive/ceases → doesn't capture rate moves"],
         ["Repo in corporate bonds","Counterparty may not repurchase; collateral sold — loss only if sale price &lt; repo amount; mitigated by <b>over-collateralisation</b>"],
         ["Segregated portfolio","Can't liquidate till recovery; may realise nothing; listing doesn't ensure liquidity; may trade far below NAV"]]) +
      K("SEBI credit-risk-based single issuer limits for actively managed schemes"))
    sub("Securitised assets", 4,
      KV([("Structure","Originator (bank, NBFC, HFC, company) sells receivables to SPV (trust) → investors get rated <b>Pass-Through Certificates (PTCs)</b> → paid from loan collections; credit enhancement per rating agency")]) +
      T(["Risk factor","Points"],
        [["Asset class","CV, auto, credit card, home loans; macro, collateral, documentation, borrower intent"],
         ["Loan size","Small loans diversify but tiny tickets = costly recovery"],
         ["Loan to Value (LTV)","Lower is better: truck ₹20 lakh with ₹10 lakh own equity safer than ₹2 lakh own equity"],
         ["Seasoning","Pool that repaid 80% of instalments beats one that repaid 10%"],
         ["Default distribution","Current, 0–30, 30–60, 60–90 DPD (days past due); 60–90 riskier"],
         ["Credit rating &amp; enhancement","Can reach rating above originator's; non-recourse; schemes mostly buy AA and above; no assurance rating stays"],
         ["Liquidity &amp; price","Thin secondary market; may sell at discount"],
         ["Limited recourse / delinquency","Enhancement is limited loss cover; no recourse to issuer/originator; repossession delays"],
         ["Prepayment","Early repayment, repurchase for misrepresentation, repossession → tenor &amp; yield change"],
         ["Bankruptcy of originator","If not a 'true sale' → losses/delays; legal opinion obtained"],
         ["Bankruptcy of investor's agent","Assets must be held as agent/trustee"],
         ["Co-mingling","Servicer's collections mixed with own funds before deposit; servicer with highest rating"]]))
    sub("REITs/InvITs risks & risk mitigation strategies", 3,
      K("REIT/InvIT: price, interest rate, credit, liquidity, reinvestment risk + lower-than-expected distributions (depend on net cash flows)") +
      T(["Risk","How managed"],
        [["Market liquidity","Portfolio with liquidity access; liquid G-secs, high-quality PSU bonds; cash first"],
         ["Credit","Good credit profiles; in-house analysis; issuer limits on amount &amp; tenor (except GoI); periodic review"],
         ["Term structure","Active duration management; mostly short duration"],["Rating migration","High-grade securities; periodic review"],
         ["Reinvestment","Short duration → small impact"],["Equity market","Own research, management meetings, conferences; financials, governance, brand, market share etc."],
         ["Floating rate","Very low liquidity → limited investment"],["Equity tax status","Monitor equity exposure of equity-oriented schemes"]]))
    sub("Systematic vs unsystematic risk", 5,
      T(["","Systematic","Unsystematic"],
        [["Also called","Market risk, non-diversifiable","Company-/firm-specific, diversifiable"],
         ["Example","Rise in inflation","Labour strike at a plant"],["Reduced by","Only staying out of market (cash, within SEBI limits)","Diversification"]]) +
      K("Finance theory: rewarded only for non-diversifiable risk","Active managers take unsystematic risk to beat benchmark","Some managers stay fully invested (investor chose the risk)"))
    sub("'Subject to market risks' — meaning", 4,
      L("MF = pass-through; investor is owner and bears investment risk",
        "Company FD promises fixed return → depositor bears credit risk only",
        "Diversification protects against credit/security-specific risk, not market-wide price fluctuation",
        "Equity growth funds: big NAV swings; overnight funds: stable NAV",
        "Risk lies in underlying investments; MFs pass on some, reduce others"))
    sub("Drivers of equity scheme returns", 4,
      K("Portfolio = main driver: asset class, sectors, style, strategy","Equity returns linked to business earnings","To beat benchmark, portfolio must differ from it",
        "<b>Security selection</b> (pick winners, avoid losers) vs <b>market timing</b> (time entry/exit)") +
      T(["","Fundamental analysis","Technical analysis"],
        [["Studies","Business, financial statements, management, competition","Price-volume charts ('chartists'): support, resistance, breakouts"],
         ["Best for","Long-term, security selection","Short-term, intra-day, timing"]]))
    sub("Fundamental ratios", 5,
      T(["Ratio","Formula / reading"],
        [["EPS","Net profit after tax ÷ number of equity shares"],
         ["P/E","Market price ÷ EPS; forward P/E on projected EPS; low P/E ≠ cheap automatically"],
         ["PEG","P/E ÷ expected earnings growth: = 1 fair, &lt; 1 undervalued, &gt; 1 overvalued"],
         ["Book value per share","Net worth ÷ number of shares (historical, accounting-based)"],
         ["Price to book","Market price ÷ book value per share"],
         ["Dividend yield","Dividend per share ÷ market price; conservative investors; high yield may mean fewer growth prospects; falls in bull markets, rises in bear markets"]]))
    sub("Growth vs value; top-down vs bottom-up", 5,
      T(["Style","Features"],
        [["Growth","Faster-growing companies; high valuations; fall more in corrections; high P/E &amp; PEG, low dividend yield; do well early in bull runs"],
         ["Value","Priced below intrinsic value; needs longer horizon; winners offset failures; safer when markets heat up"]]) +
      K("High valuation ≠ high share price (₹100 share can be cheap; ₹5 share can be over-valued)","Blend possible") +
      T(["Approach","Order"],
        [["EIC framework","Economy (inflation, rates, GDP, fiscal/monetary policy, BoP) → Industry (regulation, competition, inputs, cycles) → Company (management, financials, products)"],
         ["Top-down","Economy → industries → companies; avoids big exposure to a poor sector"],
         ["Bottom-up","Company → industry → economy; sector allocation results from stock picks; good stock even in a cold sector"]]))
    sub("Drivers of debt scheme returns", 5,
      KV([("Two main risks","Interest rate risk and credit risk — yields rise with maturity and with credit risk"),
          ("Tenor / redemption","Pre-specified period; repaying at maturity = redemption"),
          ("Money market securities","Mature within a year"),
          ("Yield / YTM","Total return; YTM = return if held to maturity"),
          ("Holding period return (HPR)","Interest + capital gain/loss vs purchase price"),
          ("Credit spread","Yield on non-govt debt − yield on gilt of same tenor"),
          ("Rating agencies","CRISIL, ICRA, CARE, Fitch (India Ratings); AAA = highest safety"),
          ("Floaters","Base + spread, e.g. 5-yr G-sec + 2%")]) +
      T(["Instrument","Issuer / tenor"],
        [["G-sec / gilt","Government; no credit risk; lowest yield for a tenor"],["T-bills","RBI on behalf of GoI, short term"],
         ["CD","Banks 7 days–1 yr; FIs 1–3 yrs"],["CP","Companies, up to 1 yr"],["Bonds / debentures","&gt; 1 yr; govt/PSUs issue bonds, private cos debentures"]]) +
      F("Bought at 8% yield; market yields rise to 9% → value falls (inverse)\nCompany X 5-yr 9.5% AAA debenture; after 2 yrs, 3-yr AAA rate = 8.5% → trades at a PREMIUM\nLonger maturity → bigger price swings"))
