from summary_lib import *

def add(chap, sub):
    chap(13, "Basics of Derivatives", "10", 5)
    sub("Meaning of a derivative & underlying assets", 5,
      KV([("Derivative","Contract/product whose value is derived from an underlying asset"),
          ("Underlyings","Metals (gold, silver, aluminium, copper, zinc, nickel, tin, lead) · energy (crude &amp; products, cracks, coal, electricity, natural gas) · agri (wheat, sugar, coffee, cotton, pulses) · financial (shares, bonds, forex)")]) +
      T(["Ind AS 109 criterion","Meaning"],
        [["1. Value linked to underlying","Price set by underlying (raw material → finished product), not by derivative's demand-supply"],
         ["2. Settled on a 'future' date","Later than underlying's settlement (underlying T+2 → derivative after T+2)"],
         ["3. No full cash outlay on trade date","Gives <b>leverage</b> — buy without full payment / sell without immediate delivery"]]))
    sub("World history of derivatives", 3,
      T(["When","Milestone"],
        [["12th century","European trade fairs: contracts for future delivery"],
        ["13th century","English Cistercian monasteries sold wool up to 20 yrs in advance"],
        ["1634–1637","Tulip Mania in Holland (tulip futures bust)"],
        ["Late 17th century","Dojima (near Osaka), Japan: rice futures"],
        ["1848","CBOT facilitated forward contracts on commodities"],
        ["1865","CBOT listed first exchange-traded 'futures contracts' in US"],
        ["1919","Chicago Butter and Egg Board reorganised → later CME"],
        ["1972","CME's International Monetary Market (IMM): currency futures"],
        ["1973","CBOE: first market for listed options"],
        ["1975","CBOT T-bill futures — first successful pure interest rate futures"],
        ["1977","CBOT T-bond futures"],["1982","CME Eurodollar futures; Kansas City Board of Trade: first stock index futures"],
        ["1983","CBOE options on S&amp;P 100 (OEX) and S&amp;P 500 (SPX)"]]) +
      K("Growth drivers: more price volatility · global market integration · technology cuts costs · better understanding of risk tools · frequent innovation"))
    sub("Indian derivatives market history", 5,
      T(["Date","Event"],
        [["18 Nov 1996","SEBI's 24-member <b>L.C. Gupta Committee</b> for regulatory framework"],
         ["17 Mar 1998","Report: declare derivatives 'securities'"],
         ["Jun 1998 → Oct 1998","<b>J.R. Varma</b> group: risk containment — margining system, initial margin method, membership &amp; net worth, deposits, real-time position monitoring"],
         ["1999","SCRA amended (Securities Laws (Second Amendment) Act 1999): derivatives = securities"],
         ["Mar 2000","Govt repealed three-decade-old ban on forward trading in securities"],
         ["Jun 2000","BSE &amp; NSE equity derivatives; <b>index futures</b> on Nifty and Sensex"],
         ["Jun 2001","Index options"],["Jul 2001","Stock options"],["Nov 2001","Stock futures"],
         ["Feb 2013","MSEI started derivatives"]]) +
      KV([("SCRA definition","(a) security derived from debt instrument, share, loan, risk instrument, contract for differences (b) contract deriving value from prices/index of prices of securities (c) commodity derivatives (d) others declared by Central Govt"),
          ("Section 18A","Derivative contracts legal and valid if traded on a recognised stock exchange, settled on its clearing house per its rules, and between parties/terms notified by Central Govt")]))
    sub("Four generic derivatives", 5,
      T(["Derivative","Key feature","Market"],
        [["Forward","Buy/sell underlying for cash on a future date; customised; both parties obliged","OTC"],
         ["Futures","Same but standardised (lot, maturity) — 'exchange-traded forwards'","Exchange"],
         ["Swap","Exchange cash flows/returns by formula; a series of forwards; manage rate, FX, commodity risk","Mainly OTC"],
         ["Option","Right, not obligation, to buy/sell on/before a date at a price; buyer pays premium, writer receives it and is obliged","OTC and exchange"]]))
    sub("Market participants", 5,
      T(["Participant","Role"],
        [["Hedgers","Face price risk; use derivatives to reduce it (corporations, institutions, banks — rates, shares, bonds, FX, commodities)"],
         ["Speculators / traders","Take positions on price views; prefer derivatives for leverage, lower cost, faster execution in size"],
         ["Arbitrageurs","Profit from price differences across markets — buy cheap, sell dear simultaneously; gaps close quickly"]]) +
      K("One individual may play different roles at different times"))
    sub("OTC vs exchange-traded derivatives", 5,
      T(["OTC features","Exchange-traded (ETD)"],
        [["Tailor-made contracts","Standardised"],["Counterparty risk managed by each institution","Clearing corporation guarantees settlement"],
         ["No central limits on positions, leverage, margining","Margins, limits"],["No formal market-stability rules","Risk management rules"],
         ["Private, little disclosure","Transparent anonymous auction"],["Banks, FIs, hedge funds, corporates, HNIs; less regulated","Open access, low cost, credit agnostic"]]) +
      K("OTC = network of broker-dealers, a way of doing business, not a place",
        "ETD limitations: standardisation → imperfect hedge; cash settlement may not help actual hedgers; daily MTM &amp; margins → operational issues",
        "Convergence: exchanges offer customised contracts via RFQ and Exchange-for-Physical (EFP); OTC offers 'vanilla' and 'exotic'; e-trading platforms; CCP clearing",
        "India: <b>CCIL</b> provides CCP with trade guarantee for OTC currency and interest rate derivatives; OTC adopts margining &amp; MTM"))
    sub("Significance of derivatives", 5,
      T(["Function","Point"],
        [["Hedging","Contract moves opposite to owned asset → offsets losses"],
         ["Price discovery","Futures/forward prices show expected future spot prices"],
         ["Market efficiency","Payoffs replicable → underlying and derivative stay in equilibrium (no arbitrage)"],
         ["Access to unavailable assets/markets","e.g. interest rate swap to get better rate than direct borrowing"],
         ["Price stability","Central banks (incl. RBI) use derivatives for currency stability"],
         ["Higher underlying volumes","More players join due to risk transfer"],
         ["Speculation","Not the only or most important use; risky if misused; tool for calculated risks"],
         ["Organised speculation","Shifts speculation from unorganised to organised market with surveillance"]]))
    sub("Risks in derivatives trading", 5,
      T(["Risk","Meaning"],
        [["Counterparty","Default by counterparty"],["Price","Loss from price move"],["Liquidity","Can't exit position"],
         ["Legal / regulatory","Enforceability of contracts"],["Operational","Fraud, poor documentation, improper execution (e.g. inadequate disaster planning)"]]) +
      K("Leveraged — may not suit limited resources, limited experience or low risk tolerance","Read the <b>Model Risk Disclosure Document</b> given by broker at agreement (issued by exchange members; covers equities and F&amp;O)"))
