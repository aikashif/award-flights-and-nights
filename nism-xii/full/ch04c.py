from summary_lib import *

def add(chap, sub):
    sub("Interoperability of clearing corporations", 5,
      L("Each exchange must have its own CC (separate legal entity); earlier brokers needed membership and margins at every CC → costly",
        "SEBI framework <b>2018</b>; implemented <b>June 2019</b>; covers cash, equity derivatives, currency derivatives, debt — <b>not commodity derivatives</b>") +
      K("One CC for margins and capital → cheaper","Positions netted across exchanges: long 10 lots XYZ Sep futures on NSE + short 6 on BSE → margin on <b>long 4</b>","Competition among CCs improves pricing and service"))
    sub("Investor's trading & settlement journey", 4,
      L("3-in-1 account; keep funds in bank and <b>allocate</b> them for trading (blocked); <b>de-allocate</b> unblocked funds to withdraw",
        "Orders: market, limit, Good-till-Date… modifiable until executed; immediate online confirmation; trade book (executed) and order book (status); daily email of orders",
        "Digital contract notes within 24 hours",
        "Short sale allowed in broker's Margin segment — must be squared off same day, no overnight short",
        "Purchase money debited on trade date; shares credited at pay-out; short delivery → auction → delay of a few days") +
      K("New facility: <b>trading supported by blocked amount</b> via UPI block in cash segment, offered by Qualified Stock Brokers (from 1 Feb 2025) — or 3-in-1; investor chooses"))
    sub("Securities Lending & Borrowing Mechanism (SLBM)", 5,
      L("Borrow securities temporarily for a fee; on <b>exchange platform</b> in India since <b>2008</b> (OTC abroad)",
        "Monthly and yearly contracts on all <b>F&amp;O</b> securities; demat only; fee set by demand and supply",
        "Two legs: lender delivers → <b>reverse leg</b> returns; early repay/recall allowed; settlement <b>guaranteed by CC</b>",
        "Uses: short selling · reverse cash-and-carry arbitrage · pairs trading · meeting delivery shortages",
        "Lender benefits: risk-free income, ownership rights kept, CC guarantee, better portfolio return",
        "Lenders: MFs, insurers, HNIs") +
      F("Mr A bearish on ABC at ₹180 (target ₹85 in 2 months): borrow on SLB, sell in cash market, buy back lower, return shares"))
    sub("Market cap, turnover, delivery %", 5,
      F("Market cap = shares outstanding × market price\nMarket turnover ratio = turnover (₹) ÷ market cap\nMarket cap ÷ GDP = size of a country's market") +
      T(["Category","Traits"],[["Large cap / blue chip","Largest, most liquid, less volatile, stable"],["Mid cap","Good liquidity, medium size; rise more in bull, fall more in bear — momentum"],["Small cap","Small, less liquid"]]) +
      K("Turnover by value or volume; higher = more liquid","Delivery % shows how much was investor buying vs trading"))
    sub("Market indices", 5,
      T(["Index","Facts"],
        [["S&amp;P BSE Sensex","<b>30</b> stocks, market-cap weighted; computed since <b>Jan 1986</b>; base <b>100</b> on <b>1 Apr 1979</b>; India's oldest"],
         ["Nifty 50","<b>50</b> NSE stocks; base date <b>3 Nov 1995</b>, base value <b>1,000</b>; chosen on liquidity, float, market cap"],
         ["SX40 (MSEI)","<b>40</b> large-cap liquid stocks, free float; base <b>31 Mar 2010</b> = <b>10,000</b>"]]) +
      K("Most indices market-cap weighted; liquid members → cheap replication; reviewed periodically",
        "Others: Nifty Next 50, Nifty 100, Nifty 500, Nifty MidCap 150, Nifty SmallCap 250, S&amp;P BSE 100, BSE 500, BSE MidCap, BSE SmallCap + sector indices",
        "Uses: widely reported real-time data · leading indicator of economy/sector · <b>performance benchmark</b> for funds",
        "Ticker: last traded price + change vs previous close (green up, red down)"))
    sub("Listing agreement obligations", 4,
      L("Signed under company's <b>common seal</b>; breach → suspension or delisting",
        "Prompt transfer, registration, sub-division, consolidation · notice of book closure and record dates · full annual reports to exchange · periodic shareholding pattern and results · prompt disclosure of price-sensitive events (insider trading, takeover rules) · corporate governance",
        "Exchange listing department monitors fees, results, shareholding, quarterly governance reports"))
    sub("Exchange risk management", 5,
      T(["Category of trading member","Base Minimum Capital"],
        [["Proprietary only, no algo","₹<b>10 lakh</b>"],["Clients only, no algo","₹<b>15 lakh</b>"],["Proprietary + clients, no algo","₹<b>25 lakh</b>"],["Any member with algo","₹<b>50 lakh</b>"]]) +
      K("≥ <b>50%</b> of BMC in cash/cash equivalents; <b>no exposure</b> against BMC; exchanges may ask more",
        "Liquid assets must cover MTM, VaR, ELM and BMC: cash, FDs, bank guarantees, G-secs, exchange-traded securities",
        "Margin shortfall → terminals <b>deactivated</b> at once; margins returned after pay-in",
        "Pay-in shortfall → trading withdrawn, securities pay-out withheld, daily penalty",
        "<b>Core Settlement Guarantee Fund</b> covers residual risk beyond margins",
        "Online monitoring alerts on abnormal positions; CC can cut open positions; surveillance on news-driven moves",
        "Price actions: <b>special margins</b> · narrower circuit filters · shift to <b>trade-to-trade</b> segment (forced delivery)",
        "Inspection of member books ≥ <b>once a year</b>"))
    sub("Investor rights & obligations", 4,
      T(["Rights","Obligations"],
        [["UCC; copy of KYC &amp; documents","Execute KYC with documents"],["Trades only in own UCC; best price","Understand voluntary terms, member rights, Risk Disclosure Document"],
         ["Contract note; know charges","Understand product, process, deadlines"],["Funds &amp; securities on time; statement; settlement of accounts","Pay margins, funds and securities on time"],
         ["Complain against member or listed company","Verify trades, bank and DP movements, contract notes, statements"],
         ["Arbitration; challenge award in court","Complain in time with documents; join dispute meetings"]]) +
      K("SEBI Investor Charters explain intermediaries' roles and investors' rights"))
    sub("Grievance redressal & arbitration", 5,
      L("Exchange <b>Investors Grievance Division (IGD)</b> handles complaints vs members and listed companies",
        "Not resolved by exchange: notional/opportunity loss, off-exchange trades, mental agony claims",
        "<b>Arbitration</b>: quasi-judicial; once started, no other exchange panels; single arbitrator or panel by claim size",
        "Award within <b>30 days</b> of appointment (+30 extension); hybrid hearings since <b>July 2022</b>",
        "Appeal to appellate panel within <b>7 days</b> of award → then <b>High Court</b>",
        "Arbitration extended to shareholder vs listed company / RTA disputes (transfer, transmission, demat/remat, duplicates, corporate benefits) — 30 May 2022",
        "Exchanges may release <b>interim relief</b> in phases"))
    sub("SCORES, ODR, investor protection funds", 5,
      T(["Mechanism","Key facts"],
        [["SCORES","SEBI online system for complaints vs all regulated entities and intermediaries; instant acknowledgement + unique number; entity uploads <b>Action Taken Report</b>; resolve within <b>21 days</b>"],
         ["ODR (31 Jul 2023)","Complain to entity → SCORES → ODR portal; or ODR directly if unresolved/pending; entity may start ODR after notice; common MII portal; ODR institutions provide online conciliation &amp; arbitration for a fee"],
         ["Investor Protection Fund (IPF)","Each exchange, run by a <b>trust</b>; pays investors when defaulting broker's assets fall short; max per investor set by exchange; also funds education"],
         ["IPEF (SEBI)","SEBI contributions, govt grants, <b>disgorged</b> amounts; restitution claims within <b>7 years</b> of SEBI inviting claims; rest for education"]]))
    sub("Debt secondary market & reporting", 5,
      L("G-secs &amp; T-bills: <b>NDS-OM</b> (RBI-owned, CCIL-run, anonymous); phone deals must be reported on NDS-OM; also on exchanges",
        "SEBI brokers access NDS-OM via a <b>Separate Business Unit</b> (RBI 7 Feb 2025, SEBI 11 Feb 2025); <b>RBI Retail Direct</b> for retail primary + secondary",
        "Corporate bonds: mostly OTC, bilateral; smaller, shallower market") +
      T(["Year","SEBI step"],
        [["2007","Exchange reporting platforms for OTC corporate bond trades; later mandatory within <b>15 minutes</b>"],
         ["2009","OTC corporate bond trades cleared &amp; settled via exchange CCs"],
         ["2013","Dedicated <b>debt segment</b>: retail platform (public issues) and institutional platform (private placements, min lot <b>₹1 crore</b>)"],
         ["2015","NSE web-based negotiated trade platform"]]) +
      K("Centralised corporate bond database by NSDL &amp; CDSL",
        "<b>RFQ</b>: electronic request-for-quote, pre-trade transparency; MFs and PMS must route a share of trades; extended to debt-segment brokers, AIFs, FPIs"))
    sub("Workbook sample answers", 3,
      K("Primary function = liquidity","Trade confirmation document = contract note","Default risk controlled by margins","Squared-off trade needs no delivery","Market cap changes with stock price"))
