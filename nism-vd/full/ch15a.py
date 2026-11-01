from summary_lib import *

def add(chap, sub):
    chap(15, "Introduction to Forwards & Futures", "15", 5)
    sub("Forward contracts", 5,
      KV([("Definition","Agreement directly between two parties to buy/sell an asset on a future date at terms fixed today (commodities, FX, equity, interest rates)"),
          ("Example","Gold spot ₹62,130/10 g on 11 May 2024 = cash/spot transaction; 1-month forward ₹62,337 → you are 'long forward', goldsmith 'short forward'; no money/gold exchanged now"),
          ("Features","Bilateral; all terms (price, quantity, quality, delivery place, settlement) fixed on contract day; OTC; changes only if both agree"),
          ("Purpose","Fix the price → avoid price risk")]) +
      F("After 1 month spot ₹62,700 → buy at 62,337, sell 62,700 → profit ₹363 per 10 g\nSpot ₹62,100 → loss ₹237 per 10 g"))
    sub("Limitations of forwards", 5,
      T(["Limitation","Meaning"],
        [["Liquidity risk","Tailor-made, not exchange-listed → hard for others to access; hard to exit before maturity"],
         ["Counterparty (default / credit) risk","A buys 100 kg rice at ₹40 from B in 6 months: price ₹50 → B may refuse; price ₹35 → A may buy from market instead"],
         ["Others","Lack of transparency, settlement complications"]]) +
      K("Solution: centralised trading platform → futures"))
    sub("Futures contracts: features & limitations", 5,
      L("Agreement through an organised exchange to buy/sell a fixed amount of an asset on a future date at an agreed price — <b>standardised forwards</b>",
        "Clearing corporation guarantees settlement",
        "Buyer = long, seller = short (figurative — nothing changes hands at origination)",
        "Exchange fixes all terms except price",
        "Contract via exchange · centralised platform · price discovery · <b>margins by both parties</b> · standardised quality and quantity") +
      K("Limitations: limited maturities, limited underlyings, no design flexibility, admin costs of MTM"))
    sub("Contract specifications — Nifty futures example", 4,
      T(["Field (3 Oct 2025)","Value"],
        [["Instrument","Index futures"],["Underlying","Nifty 50"],["Expiry","28 Oct 2025"],["Open / High / Low","24,950.40 / 25,020 / 24,878.60"],
         ["Close (futures)","25,006.60"],["Underlying (spot)","24,894.25"]]) +
      F("Lot size (example) = 65 → contract value = 65 × 24,894.25 = ₹16,18,126.25"))
    sub("Lot size rules (SEBI Master Circular 30 Dec 2024)", 5,
      T(["Rule","Index derivatives","Stock derivatives"],
        [["Value at introduction","≥ <b>₹15 lakh</b>","≥ <b>₹5 lakh</b>"],
         ["Value at review","₹15–20 lakh","₹5–10 lakh"],
         ["Lot size","Multiple of 5, not less than 10","Multiple of 25, not less than 50; if &gt; ₹10 lakh at 50 → multiple of 5, min 10; if still &gt; ₹10 lakh at 10 → lot of 5"],
         ["Review","Every 6 months, average close of last 1 month; 2 weeks' notice","Same; lot same across exchanges"],
         ["Higher revised lot","Only for new contracts","Only for new contracts"]]) +
      K("Futures and options on the same underlying have the same contract size"))
    sub("Contract cycle, expiry day & rollover", 5,
      L("Max maturity <b>12 months</b> (monthly 1–12); exchanges generally run a <b>3-month cycle</b>: near (Oct), mid (Nov), far (Dec)",
        "Expiry day = last trading day; all open contracts compulsorily settled; to continue, <b>roll over</b> (long: sell expiring, buy next) simultaneously",
        "New contract introduced on the trading day after near-month expiry") +
      KV([("SEBI 26 May 2025","All equity derivative expiries of an exchange on either <b>Tuesday or Thursday</b>; one weekly benchmark index option per exchange; all other contracts (index futures, non-benchmark index F&amp;O, stock F&amp;O) min 1-month tenor, expiring last Tuesday/Thursday of the month; changing settlement day needs SEBI prior approval"),
          ("NSE","Nifty 50, Bank Nifty, stock futures &amp; Nifty Financial Services monthly futures: <b>last Tuesday</b> (previous day if holiday)"),
          ("BSE","Index &amp; stock futures: <b>last Thursday</b> (previous day if holiday)")]))
    sub("Other contract terms", 4,
      T(["Term","Rule"],
        [["Quantity freeze","Orders above freeze quantity rejected"],["Price quotation","In rupees"],
         ["Tick size","Minimum price move; NSE index futures by index level, stock futures = cash-market tick; BSE stock futures 5 paise"],
         ["Daily settlement price","VWAP of last 30 minutes (across exchanges if more than one; else that exchange's); if not traded in last half hour → theoretical price; differs per expiry"],
         ["Final settlement price","Closing price of the underlying index on expiry (from constituents' closes); stocks: volume-weighted average of closing prices across exchanges (Closing Auction Session SOP)"],
         ["Pre-open session (SEBI 29 May 2025)","Near-month stock &amp; index futures (also next month in last 5 trading days); call auction 9:00–9:15 am; order entry 9:00–9:10 with random closure in last 2 min"],
         ["Trading hours","9:15 am – 3:30 pm, Mon–Fri"],
         ["Holidays","Trading holiday: exchange closed; clearing holiday: trading possible but no clearing/settlement (banks closed)"]]) +
      T(["BSE Sensex futures","Spec"],
        [["Underlying","BSE Sensex"],["Contract size","20"],["Tick size","₹0.05"],["Cycle","3 serial monthly contracts"],
         ["Trading hours","9:15 am – 3:40 pm (as stated)"],["Expiry","Last Thursday"],["Final settlement","Cash, closing index value on expiry"]]))
    sub("Basis", 5,
      F("Basis = Spot − Futures\n3 Oct 2025: 24,894.25 − 25,006.60 = −112.35 (negative)") +
      L("Futures &gt; spot → negative basis → upward expectations → <b>contango</b>",
        "Spot &gt; futures → positive basis → downward expectations → <b>backwardation</b>",
        "Basis differs for 1-, 2-, 3-month contracts; difference between 1- and 2-month basis = cost of carry between months",
        "Basis becomes <b>zero at expiry</b> (final settlement at underlying close)"))
    sub("Cost of carry", 5,
      F("Cost of carry = Storage (commodities) + Interest − Income\nEquity: interest paid − dividend earned\nEx: ABC at ₹100, borrow at 6%, dividend 200% on FV ₹1 = ₹2 → net carry ₹4 → break-even futures ₹104") +
      T(["Component","Effect on futures price"],
        [["Financing cost (interest) — usually biggest","Increases"],["Storage (warehousing, refrigeration, security; insurance) — not for equities","Increases"],
         ["Income (dividends, interest)","Decreases"]]) +
      K("Cost of carry may differ across participants"))
    sub("Margins & MTM", 5,
      KV([("Who","Exchange/CC charges brokers; brokers charge clients — protection against default"),
          ("Initial margin","Deposit when entering; both buyer and seller; higher for volatile assets"),
          ("Extreme Loss Margin (ELM)","Covers losses beyond initial margin scenarios; paid upfront"),
          ("MTM settlement","Profits/losses settled daily; collected from losers, paid to gainers")]) +
      F("Long Nifty futures (May 2024) at 22,250, lot 25 → contract value ₹5,56,250\nInitial margin 10% = ₹55,625\nClose 22,308.70 → MTM gain = 58.70 × 25 = ₹1,468 credited; next day starts from 22,308.70"))
    sub("Open interest vs volume", 5,
      L("OI = total contracts outstanding; longs = shorts = OI (count one side); shows market depth",
        "Volume = contracts traded over a period (day, week, month, life)") +
      T(["Date","Trades","OI","Volume"],
        [["Mar 1","A shorts 50, B longs 50","50","50"],["Mar 2","C longs 100, D shorts 100","150","100"],
         ["Mar 3","A buys back 50, E shorts 50 (replaces A)","150","50"],["Mar 4","C sells 100, D buys back 100 (both close)","50","100"]]))
    sub("Price band & base price", 4,
      L("Price band: daily range around previous close/base (₹100 with 10% → ₹90–110)",
        "Currently <b>no daily price range for futures</b>; a % band only to prevent erroneous orders (dynamic band — next chapter)",
        "Base price: day 1 = theoretical price; later = close or theoretical price"))
    sub("Positions: long, short, open, naked, calendar spread", 4,
      T(["Term","Meaning"],
        [["Long","Outstanding buy position"],["Short","Outstanding sell position"],
         ["Open position","Outstanding long/short (short 5 Infosys + buy 2 later → short 3)"],
         ["Naked","Futures position without position in the underlying"],
         ["Calendar spread","Long one maturity + short another, same underlying; computed vs near month; becomes open when near month expires or a leg is closed"],
         ["Opening / closing","Increases / reduces open position"]]))
    sub("Forwards vs futures", 5,
      T(["Feature","Forwards","Futures"],
        [["Mechanism","Not exchange-traded","Exchange-traded"],["Specs","Tailor-made","Standardised except price"],
         ["Counterparty risk","Exists (maybe reduced by guarantor)","Clearing agency is counterparty"],["Liquidity","Low","High"],
         ["Price discovery","Not efficient (scattered)","Efficient (common order book)"],["Information","Poor, slow","Quickly disseminated nationwide"]]))
    sub("Futures payoffs", 5,
      PO(payoff("Long futures at 100","5,65 115,5","Expiry 150 → +50; 70 → −30"),
         payoff("Short futures at 100","5,5 115,65","Expiry 60 → +40; 150 → −50")) +
      K("Payoff = profit/loss at expiry vs underlying price (x-axis: price, y-axis: P&amp;L; no negative prices)","Both long and short: unlimited profit/loss → <b>linear</b>"))
    sub("Cost of carry (no-arbitrage) model", 5,
      L("Assumes efficient markets → arbitrage can't persist",
        "Futures position = buy futures OR buy stock in cash and carry it (synthetic futures)",
        "<b>Fair futures price = spot + cost of carrying</b> (transaction, custodial, financing; for commodities warehousing, insurance)") +
      F("Gold spot ₹62,130; carry for 3 months ₹100 → fair ₹62,230\n3-month futures at ₹62,280 → buy spot (borrowed), sell futures, deliver at expiry → riskless ₹50\nArbitrage pushes spot up and futures down until aligned"))
