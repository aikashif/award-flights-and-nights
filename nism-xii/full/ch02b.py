from summary_lib import *

def add(chap, sub):
    sub("DR issue process & IDRs", 4,
      L("<b>Sponsored issue</b>: existing shareholders offer shares for conversion into DRs; or company issues <b>fresh</b> shares (funds repatriated to India within set time)",
        "Steps: meet foreign exchange listing rules → appoint depository bank → deliver shares to its local custodian → each DR = set number of shares → DRs issued to brokers",
        "<b>Two-way fungibility</b> (if allowed): shares ↔ DRs",
        "DR holders get dividends and appreciation but <b>no voting rights</b>",
        "IDRs: limit on money raised, lock-in on conversion; only <b>resident Indians</b>, not FPIs"))
    sub("FCCBs", 5,
      T(["Rule","Detail"],
        [["What","Foreign-currency (usually USD) debt convertible into equity before maturity; interest and principal in foreign currency"],
         ["Conversion price","Usually at a <b>premium</b> to market price"],["Benefit","Cheaper, quicker debt abroad"],
         ["Eligibility","Not eligible for domestic equity → not eligible for FCCB; unlisted issuers must list in India within set time"],
         ["Regulation","RBI under <b>FEMA</b>; Issue of FCCBs and Ordinary Shares (Through Depository Receipt Mechanism) Scheme <b>1993</b>; within RBI limits"],
         ["Placement","Public via international lead manager; private to banks, FIs, foreign collaborators"],
         ["Maturity","Not less than <b>5 years</b>"],["Expenses","Max <b>4%</b> of issue (public), <b>2%</b> (private placement)"]]))
    sub("Warrants", 5,
      L("Company-issued option to subscribe to shares at set price on/after set date; longer life than exchange stock options (1–3 months)",
        "Pay <b>25%</b> upfront; balance on exercise; not exercised → amount <b>forfeited</b>",
        "Company gains if exercise price &gt; current price (captures expected rise); investor locks future price for 25%") +
      F("ABC at ₹180; 4,00,000 warrants at ₹220; upfront = 25% × 4,00,000 × 220 = <b>₹2.20 crore</b>"))
    sub("Commodities as an asset class", 4,
      T(["Category","Examples"],[["Soft / agri","Sugar, tea, coffee, cocoa, corn, wheat, soya bean"],["Bullion","Gold, silver"],["Base metals","Copper, zinc, aluminium, nickel"],["Energy","Crude oil, natural gas"]]) +
      K("'Real' assets, react directly to macro conditions","Physical holding: storage &amp; insurance costs; needs knowledge of weather, inventories, preferences",
        "Roles: <b>inflation hedge</b> · <b>low correlation</b> with equity and debt → diversification",
        "Shares of commodity producers are not a pure play (company risk: debt, imports, policy); direct route = commodity ETFs, MFs, derivatives"))
    sub("Derivatives — features & roles", 5,
      L("Value derived from underlying; OTC and exchange; exchange-traded in India = futures and options",
        "Call = right to buy; put = right to sell; strike/exercise price; expiry date → short shelf life",
        "Contracts designed by exchanges, approved by regulator (size, quote unit, tick, grade, hours, cycle, expiry, delivery, price limits)",
        "<b>Under-funded</b> (margin only) · <b>leveraged</b> · often more liquid than cash market · risky") +
      F("ABC ₹100, margin 10% → ₹100 margin controls 10 shares (₹1,000) → <b>10× leverage</b>") +
      K("Roles: price discovery · risk transfer (hedging) · diversification into currencies and commodities"))
    sub("Derivative segments in India", 5,
      T(["Segment","Key facts"],
        [["Equity","F&amp;O on indices (Nifty, Bank Nifty) and eligible stocks; index = <b>cash</b> settled; stock F&amp;O = <b>physical delivery</b>; hedge systematic risk"],
         ["Currency","INR pairs: USDINR, EURINR, GBPINR, JPYINR; cross: EURUSD, GBPUSD, USDJPY; all cash-settled in INR"],
         ["Commodity","Options are on <b>futures</b>, not spot (futures regulated by SEBI, spot by state govts); expiry → futures position"],
         ["Interest rate","IRF on G-secs, T-bills, MIBOR; IRO on G-secs; cash-settled"]]))
    sub("Asset allocation & diversification", 5,
      T(["Objective","Suitable investment"],
        [["Growth","Equity shares &amp; funds, real estate, gold"],["Regular income","Deposits, debt instruments &amp; funds, real estate"],
         ["Liquidity","Cash, bank deposits, short-term MF schemes"],["Capital preservation","Cash, bank deposits, ultra-short-term funds"]]) +
      T(["Investor","Problem from concentration"],
        [["Jayesh — only real estate","Can't sell or borrow fast (liquidity)"],["Kamal — savings account","Too little growth"],["Latika — all equity","Value fluctuates"],
         ["Harmeet — gold jewellery","No regular income"],["Gayatri — bank FDs","Fixed interest, rising expenses (inflation)"]]) +
      K("Asset allocation: split across assets so a fall in one is cushioned; near retirement → more debt; young high earner → more equity",
        "Diversification level 1: across asset classes; level 2: within class (different industries)","Works only if investments don't move together"))
    sub("Investment process factors", 4,
      K("Manage return and risk (MFs diversify with small sums)","Match horizon: young with no liquidity need → more equity","Portfolio focus shifts: growth while saving for retirement → income after",
        "Ease of periodic investing and exit","Flexibility: e.g. MIP growth option for low-risk investor who needs no income","Regular information and updates"))
    sub("Price vs intrinsic value", 5,
      L("Intrinsic value = <b>discounted value of future benefits</b> (future earnings); price = market quote",
        "Intrinsic &gt; price → <b>undervalued</b>; intrinsic &lt; price → <b>overvalued</b>",
        "Markets not perfectly efficient; investing = exploiting inefficiency, not a formula",
        "Equity process: security selection · market timing (cycles: steel/construction slow more than FMCG) · sector &amp; segment weighting"))
    sub("PE, PBV, dividend yield", 5,
      F("PE = market price ÷ EPS ; EPS = PAT ÷ shares outstanding\nPBV = market price ÷ book value per share (net worth per share)\nDividend yield = DPS ÷ market price\n40% dividend on FV ₹10 = ₹4 ; price ₹200 → yield 2%") +
      T(["Measure","Signal"],
        [["Market PE ≥ 22×","Overvalued zone"],["Market PE ≤ 12×","Undervalued zone"],["PBV &lt; 1","May be undervalued"],
         ["Falling dividend yield","Bull market"],["Rising dividend yield","Bear market"]]) +
      K("Look at <b>prospective</b> PE when growth is expected","Large known firms command higher PE than small risky peers","Book value at cost less depreciation, not inflation-adjusted",
        "Dividend declared as % of <b>face value</b>; yield inversely related to price; PSU banks tend to have high yields"))
    sub("Equity research, analysis & valuation", 4,
      T(["","Buy-side","Sell-side"],[["Who","Institutional investors","Broking houses"],["Analysts","Generalists; question models, downside risk","Sector specialists; build models, meet management, arrange meetings"]]) +
      T(["Approach","Meaning"],
        [["Fundamental analysis","Financial statements → earning potential → intrinsic value; EIC framework"],["Technical analysis","Price &amp; volume charts, support/resistance, trends, indicators"],
         ["Top-down","Macro → sector → stock"],["Bottom-up","Stock → confirm with industry and macro"],
         ["DCF valuation","Cash flow estimates + discount rate (risk); rigorous; estimates vary between analysts"],
         ["Relative valuation","Compare with peers/sector averages; easy, finds over/undervalued; can carry market errors"]]) +
      K("Sources: audited statements · analyst meets, plant visits · industry reports · govt/regulatory publications"))
    sub("Time value of money & bond pricing", 5,
      F("₹1,000 at 8% simple for 2 yrs → ₹1,160 → today's money worth more\nCompound today's money forward; discount future money back\nAmit: 5-yr bond, FV 100, 10% annual, yield 8%\nDF: 0.9259 / 0.8573 / 0.7938 / 0.7350 / 0.6806\nPV: 9.26 + 8.57 + 7.94 + 7.35 + 74.86 = <b>₹107.98</b>") +
      K("Later cash flow → lower PV","Higher yield → lower PV",
        "4 steps: coupons → redemption value → discount each at market yield → add"))
    sub("Yield, current yield, YTM", 5,
      L("Price, coupon, yield: know two → find third; price is what's quoted",
        "Bought below FV → yield &gt; coupon; above FV → yield &lt; coupon",
        "Yield and price move <b>inversely</b>",
        "<b>YTM</b> = rate equating PV of cash flows to price; standard debt quote") +
      F("Current yield = coupon ÷ market price ; 12% bond at ₹109.50 → 10.95%"))
    sub("Debt investing process", 4,
      L("Macro knowledge matters more than in equity",
        "Selection: retail → bank FDs, postal certificates, money market &amp; short-term debt funds; institutions → money market, G-secs (liquidity), corporate bonds (return)",
        "Timing: buy long G-secs when interest rate cycle <b>peaks</b> (lock high yields)",
        "Credit spread narrow in boom, <b>widens in recession</b> → chance to buy highly rated bonds at good yields",
        "Weights (via MFs): ~20% in liquid funds; at rate peak more in <b>gilt funds</b>; least in credit risk funds in recession; non-experts → <b>dynamic bond funds</b>"))
    sub("Workbook sample answers", 3,
      K("Ranked last for profit and liquidation = equity shareholders","Reserves belong to equity shareholders","Intrinsic ₹50, price ₹35 → undervalued",
        "Rates rise after issue → bond quotes below face value","Top-down starts with macro = True"))
