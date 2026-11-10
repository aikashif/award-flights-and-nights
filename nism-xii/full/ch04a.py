from summary_lib import *

def add(chap, sub):
    chap(4, "Secondary Markets", "20", 5)
    sub("Role of the secondary market", 5,
      L("Trades between investors; issuer gets <b>no new capital</b>; instruments include listed issues, privately placed securities, derivatives") +
      T(["Role","Point"],
        [["Liquidity","Exit/entry for perpetual, risky, long-term securities at low cost, quickly"],
         ["Price discovery","Rising demand signals good prospects; FV ₹10 share at ₹100 → new issue priced near ₹100"],
         ["Information signalling","Prices monitor issuers continuously; efficient market = prices reflect all information"],
         ["Economic barometer","Indices (S&amp;P BSE Sensex, NSE Nifty 50): sustained rise = growing economy"],
         ["Market for corporate control","Underperformers become cheap takeover targets; threat alone improves governance"]]) +
      K("Bull market: optimism, expansion → overshoots intrinsic value, rising costs → crash",
        "Bear market: stress, falling prices below intrinsic value → value buyers, lower rates → next bull cycle"))
    sub("Secondary markets by asset", 5,
      T(["Market","Key facts"],
        [["Equity","Stock exchanges (MIIs, SEBI); clearing corporation = <b>central counterparty</b>, guarantees settlement; <b>interoperability</b> lets trades clear at another exchange's CC; intra-day and EOD data published"],
         ["Debt — G-secs","RBI; pre-2005 OTC by phone, SGL form + cheque; <b>CCIL</b> set up <b>2001</b>; runs <b>NDS-OM</b> (anonymous, order-driven, owned by RBI); guaranteed settlement; NDS-OM for institutions, retail on exchanges"],
         ["Debt — corporate","SEBI: OTC trades reported on exchanges, central database, clearing via exchange CCs, dedicated debt segment"],
         ["Commodity spot","State govts; APMC mandis (licensed traders); <b>e-NAM 2016</b> — 'One Nation, One Market', online bidding, e-payment, assaying"]]))
    sub("Participants & stock exchanges", 5,
      L("Participants: exchanges · clearing corporations · investors · issuers · intermediaries · regulator",
        "National exchanges: <b>BSE, NSE, MSEI</b>",
        "Trade only through <b>members</b> (brokers) and their APs; members meet capital, qualification, net worth tests; may be trading and/or clearing members",
        "Investors trading directly among themselves = '<b>off-market</b>' — no regulatory protection or redressal",
        "Investor completes KYC with broker → gets <b>Unique Client Code (UCC)</b>",
        "Listed securities: equity, corporate bonds, debentures, G-secs, T-bills; listing criteria on size, public holding, rating, ownership; listing fee + disclosure"))
    sub("Trading, clearing, settlement", 5,
      L("Trading = buy/sell on exchange (electronic order matching); then buyer owes money, seller owes shares",
        "<b>Clearing</b> = working out what each party owes; <b>settlement</b> = discharging it",
        "Settlement cycle: T+2 → <b>T+1</b>; optional <b>T+0</b> added alongside T+1",
        "Risk management: member capital + margins → high liquidity and <b>guaranteed settlement</b>"))
    sub("Clearing corporation, depositories, custodians", 5,
      T(["Entity","Role"],
        [["Clearing corporation","Wholly owned subsidiary of exchange; counterparty to every trade; buyers pay CC, sellers deliver to CC; via clearing members"],
         ["Interoperability","Consolidate clearing at one CC whatever the exchange; all recognised CCs except IFSC; all products except <b>commodity derivatives</b> (27 Nov 2018)"],
         ["CCs","NSE Clearing Ltd · Indian Clearing Corporation Ltd (ICCL) · Metropolitan Clearing Corporation of India Ltd (MCCIL)"],
         ["Depositories","<b>NSDL</b> and <b>CDSL</b>; securities must be demat to trade"],
         ["DPs","Banks, brokers; demat account ≈ bank account for securities; DP tells depository of ownership change; money via clearing banks"],
         ["Custodians","Hold funds &amp; securities for banks, insurers, MFs, FPIs; settle their trades; many are also clearing members/banks"]]))
    sub("Regulator & IFSC", 5,
      L("SCRA 1956 + <b>SCR Rules 1957</b>; SEBI implements, delegates trading, membership, listing administration to exchanges") +
      T(["IFSC item","Fact"],
        [["What","Finance to/from offshore customers; global IFSCs: London, New York, Singapore, Dubai, Shanghai"],
         ["India's first","<b>GIFT City</b>, Gandhinagar; regulator IFSCA"],
         ["Exchanges","<b>NSE IX</b> (NSE) and <b>India INX</b> (BSE): foreign shares, DRs, debt, FX, rate &amp; commodity derivatives; Indian index/stock F&amp;O in <b>USD</b>; IOSCO/FATF compliant"],
         ["Tax","Exempt from STT, CTT, capital gains tax, income tax"],
         ["IIBX","India International Bullion Exchange: bullion spot and bullion DRs; bullion imports routed through it"],
         ["SGX Nifty","Since <b>July 2023</b> traded only on NSE IX; SGX Nifty delisted"]]))
    sub("MII governance — Gandhi Committee", 4,
      L("MIIs = exchanges, clearing corporations, depositories; SEBI norms Dec 2012",
        "<b>R. Gandhi</b> (ex-RBI Deputy Governor) committee report <b>March 2018</b>: widely held ownership · MD renewal after board review · unrelated activities need SEBI approval · KMP identified by NRC/board, pay aligned with global principles · transparent KMP pay · fewer overlapping committees",
        "Functional committees: Member · Grievance Redressal · Nomination &amp; Remuneration · Oversight",
        "Oversight committees: Standing Committee on Technology · Advisory · Regulatory Oversight · Risk Management",
        "<b>Public Interest Directors</b> chair each committee; every MII needs a <b>BCP</b> and <b>Disaster Recovery Site</b>"))
    sub("Brokers & authorised persons", 5,
      L("Broker = SEBI-registered exchange member trading on screen; AP = broker's agent (ex sub-broker), registered with exchange",
        "Can be individuals, firms, companies (incl. bank subsidiaries); must display membership details",
        "Own-account trades = <b>proprietary</b>",
        "SEBI registration: exchange eligibility, office, equipment, staff, experience; <b>base minimum capital</b> with exchange; exposure capped at a multiple of it",
        "Brokerage: maximum set by each exchange") +
      T(["Broker duty","Timeline"],
        [["Separate client and proprietary accounts; client funds separate",""],["Contract note","Within <b>24 hours</b> of execution"],
         ["Collect funds/securities","Before pay-in day"],["Pay or deliver to client","Within <b>24 hours</b> of pay-out"],["Compliance officer","Monitors rules and grievances"]]))
    sub("Client acquisition & documents", 5,
      K("KYC + <b>in-person verification (IPV)</b> before account opening",
        "KYC: personal (name, gender, marital status, PAN, residential status, UID) + proof · address + proof · income, occupation, net worth · bank &amp; demat details · regulatory action in last <b>3 years</b>",
        "Documents given: Rights &amp; Obligations (incl. internet/wireless trading) · Uniform <b>Risk Disclosure Document</b> · Do's &amp; Don'ts guidance note · index of documents · <b>tariff sheet</b> · contacts of senior officials and exchange grievance cell",
        "Policies published: inactive accounts · exposure limits · brokerage · delayed payment charges · right to sell securities / close positions without notice for non-payment · shortages from internal netting · when positions may be refused/closed · suspension at client request · deregistration",
        "Secure client access (user ID, password) to positions and statements"))
    sub("3-in-1 account; PoA → DDPI", 5,
      L("3-in-1 = savings + demat + trading; bank-led (broking via subsidiary) or broker-led (bank elsewhere); single form, common KYC",
        "Bank/demat accounts can't be used through it except to settle trades",
        "Benefits: less paperwork, convenience, real-time efficient trading") +
      T(["","Power of Attorney (old)","DDPI (now)"],
        [["Status","Voluntary but needed for online 3-in-1; brokers forced and misused it","Separate system by exchanges, CCs, depositories"],
         ["Permitted use","Transfer securities for pay-in; pledge/re-pledge for margins","Same limited purposes only"],
         ["Revocation","—","Client may revoke any time"]]) +
      K("After DDPI, PoA can no longer be executed for these purposes"))
    sub("Trading systems", 5,
      T(["System","Exchange"],[["BOLT","BSE On-Line Trading"],["NEAT","National Exchange Automated Trading (NSE)"],["TWS","Trader Work Station (MSEI)"]]) +
      T(["Mode","Points"],
        [["Open outcry","Physical floor shouting — replaced in India by screen trading"],
         ["Mobile trading","Easy, live alerts; preferred by young investors; problems: connectivity, small screen, speed"],
         ["Algo trading","Rule-based program (e.g. buy above 10-day moving average); splits large orders; speed, accuracy, no emotion; risk = design errors (exchanges require testing)"],
         ["HFT","Subset of algo; huge tech spend; holding seconds/minutes; very high order-to-trade ratio; flat by end of day; uses co-location"],
         ["Co-location","Broker servers at exchange premises → lower <b>latency</b> (order sent to received); fee-earning for exchanges"]]) +
      K("Sequence: place order → broker routes → displayed → matched → confirmed → <b>contract note</b>"))
    sub("Orders & identifiers", 5,
      L("Order must state company, buy/sell, quantity; price optional; identified by <b>UCC</b>",
        "<b>ISIN</b> = unique <b>12-character</b> code in depository system (Hindalco: symbol HINDALCO, ISIN INE038A01020)") +
      T(["Order","How it works"],
        [["Limit","Price set; buy at limit or lower (buy ABC Bank 2,500 when at 2,600); sell at limit or higher; lapses end of day"],
         ["Market","Any current price; immediate; rarely unfilled"],
         ["Immediate or Cancel (IOC)","Fill at once; unfilled part cancelled immediately"],
         ["Stop-loss","With a buy/sell; opposite limit order fires at <b>trigger</b> (buy 1,000 XYZ at 1,000, stop sell at 990; sell at 1,000, stop buy at 1,010); kept in stop-loss book; mainly intraday; unexecuted cancelled at day end"],
         ["Disclosed quantity","Shows only part of a large order; only broker knows the split"],
         ["Day vs GTC","Indian exchanges allow <b>day orders only</b>; brokers may re-enter 'GTC' orders next day"],
         ["Modification","Until matched; none after"]]))
    sub("Trading hours & pre-open", 5,
      T(["Segment (NSE)","Hours"],
        [["Equity","<b>9:15 am – 3:30 pm</b>"],["Equity derivatives","9:15 am – <b>3:40 pm</b> (as stated in this workbook)"],["Debt","9:00 am – 5:00 pm"],
         ["Pre-open","<b>9:00 – 9:15 am</b>: order entry 9:00–9:10 (random close in last 2 min) · matching 9:10–9:12 · buffer 9:12–9:15"]]) +
      K("Monday–Friday except holidays","Pre-open sets opening price and spreads out the opening rush","Brokers may use their own front-end software linked to exchange"))
    sub("Electronic order matching", 5,
      L("Buy order = <b>bid</b>; sell order = <b>ask</b>; buyer gets ≤ bid, seller ≥ ask",
        "<b>Order-driven</b> (computer matches) · <b>transparent</b> (all quotes visible) · <b>anonymous</b>",
        "<b>Price-time priority</b>: best price first (₹285 bid before ₹280); same price → earlier order first",
        "Unique order numbers → full audit trail for disputes"))
