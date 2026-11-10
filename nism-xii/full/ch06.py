from summary_lib import *

def add(chap, sub):
    chap(6, "Derivatives Markets", "10", 4)
    sub("Derivative & forward (gold example)", 5,
      L("Derivative = value derived from an <b>underlying</b>; risk management tool for unknown future values",
        "Buyer fears price rise, seller fears fall → agree price now = <b>forward</b>; they are <b>counterparties</b>; one's loss is the other's gain") +
      T(["Gold in 1 year (forward at ₹30,000 for 10 g)","Buyer","Seller"],
        [["₹30,000","No gain/loss","No gain/loss"],["₹35,000","<b>Gains</b>","Loses"],["₹25,000","Loses","<b>Gains</b>"]]))
    sub("Structuring derivatives — examples", 4,
      K("Main purpose: <b>transfer risk</b>; payoff can be two-way (forward) or one-way") +
      T(["Risk","Derivative"],
        [["Farmer: monsoon failure","<b>Weather</b> derivative (payoff on rainfall)"],["Borrower: floating rate, wants fixed","<b>Interest rate swap</b> (receive floating, pay fixed)"],
         ["Importer: rupee falls vs USD","<b>Currency</b> derivative fixing future rate"],["Portfolio manager: market falls","<b>Index</b> derivative paying on index fall"]]))
    sub("Zero sum, settlement, OTC vs exchange, arbitrage", 5,
      L("Every long has a matching short → net economic value of all positions = <b>zero</b>; no new asset created",
        "Cash settlement = pay price difference, no delivery",
        "Since <b>October 2019</b>: all <b>stock</b> F&amp;O open at expiry settled by <b>physical delivery</b>; <b>index</b> F&amp;O stay <b>cash-settled</b>",
        "OTC: mutually agreed, non-standard, rely on trust, between institutions; exchange-traded: standard, via clearing corporation with margins, anonymous",
        "Forwards = OTC; futures = exchange-traded",
        "<b>Law of one price</b>: identical goods can differ across markets only by transaction costs (transport, storage, insurance, interest); arbitrageurs close gaps",
        "Derivative price differs from cash price by costs such as warehousing and interest"))
    sub("Forwards, futures, options, swaps", 5,
      T(["Product","Key points"],
        [["Forward","OTC, custom terms; cash or delivery; <b>counterparty risk</b>; relies on trust (community/regional commodity forwards)"],
         ["Futures","Exchange-traded forwards; exchange sets terms; <b>clearing corporation</b> is counterparty; margins remove counterparty risk"],
         ["Option","Right, not obligation; buyer/holder (long) pays premium; seller/writer (short) obliged if exercised; call = right to buy, put = right to sell"],
         ["Swap","Exchange of payments on future dates; common in rates and currencies; OTC but governed by swap dealer association rules"]]) +
      F("MCX wheat futures: unit 10 MT · min order 500 MT · max position 5,000 MT per individual · standard mill quality · starts 21st · delivery 20th · physical only · approved warehouses") +
      F("Swap: borrower pays T-bill + spread quarterly → pays fixed to dealer, receives T-bill + spread → net = fixed rate; only interest on agreed principal exchanged"))
    sub("Option terminology (Arvind–Salim)", 5,
      L("Arvind buys Nifty call from Salim: strike <b>10,000</b>, 3 months, premium <b>₹100</b>",
        "Arvind = buyer; Salim = writer; strike/exercise price = 10,000; premium = price of option",
        "Nifty 10,200 at settlement → <b>in-the-money</b>; Arvind exercises; Salim keeps ₹100 but must sell at 10,000",
        "Nifty 9,800 → <b>out-of-the-money</b>; Arvind lets it lapse; Salim keeps ₹100"))
    sub("Indian derivatives market structure", 5,
      K("On exchanges: equity index options &amp; futures · stock options &amp; futures · currency F&amp;O on select pairs · interest rate futures &amp; options · commodity F&amp;O",
        "OTC: agricultural forwards, interest rate swaps",
        "Index futures on BSE &amp; NSE from <b>June 2000</b>; index options, stock options, stock futures from <b>2001</b>; India among few markets with single-stock futures",
        "Derivative volumes far above cash market volumes",
        "Fully automated, nationwide, anonymous screen trading; CC settles; guaranteed via capital norms, intraday position and margin monitoring",
        "Trade via exchange members; trading members settle through clearing members",
        "Transaction charges on contract value (futures) or premium (options), possibly from both sides; <b>STT</b> payable",
        "Eligible indices/stocks (e.g. Nifty 50, Nifty Bank, Sensex) chosen on size and volume per SEBI criteria; exchanges may be stricter"))
    sub("Equity futures contract specifications", 5,
      T(["Spec","Rule (this workbook)"],
        [["Expiry","Last <b>Tuesday or Thursday</b> of month as chosen by the exchange; all its equity derivatives on the same day (SEBI 26 May 2025); holiday → previous trading day"],
         ["Contracts","Near, next and far month; plus 3 quarterly (Mar/Jun/Sep/Dec) and 8 semi-annual (Jun/Dec); weekly index options: 7 weekly expiries excluding monthly expiry week"],
         ["Lot size","Value ≥ <b>₹5 lakh</b> at introduction"],
         ["Base price","Day 1: theoretical futures price (underlying + interest to expiry); later: daily settlement price"],
         ["Tick","<b>₹0.05</b> (5610.50 → 5610.55 or 5610.45, not 5610.52)"],
         ["Price &amp; quantity freeze","Orders outside range need member confirmation; may be refused if over exposure or contract illiquid"],
         ["Hours (NSE)","9:15 am – <b>3:40 pm</b>; trade modification till <b>4:15 pm</b>"]]) +
      TRAP("The XII workbook still gives the old ₹5 lakh minimum lot value. The V-D (Sept 2026) workbook gives ₹15–20 lakh for index contracts and ₹5–10 lakh for stocks. For the XII exam, answer ₹5 lakh."))
    sub("Order types in F&O", 4,
      T(["Order","Rule"],
        [["Regular lot","Market or limit; unmatched (even partly) cancelled at day end"],["Stop loss","Triggers at set price to protect an executed position"],
         ["Immediate or cancel","Cancelled if not executed at once"],["Day order","Valid that day"],
         ["Spread order","Executes when the gap between two positions hits a set level"]]) +
      K("Orders time-stamped by exchange; different books by type","Corporate-action price adjustment after close on last cum day (position value unchanged)"))
    sub("Clearing members & settlement", 5,
      T(["Clearing member","Role"],
        [["TM-CM","Trades and clears own + other members' trades"],["Professional CM (PCM)","Not a trading member — banks/custodians, clearing only"],["Self-clearing member (SCM)","Clears only own trades"]]) +
      L("Daily MTM settlement on <b>T+1</b>: traded price vs daily settlement price = <b>weighted average of last 30 minutes</b>",
        "Final settlement on expiry at underlying's <b>closing price</b> in cash market",
        "<b>Clearing bank</b>: empanelled by CC; clearing account used only for settlement") +
      F("Buy Nifty futures 10,000; settlement price 9,900 → loss ₹100 × lot 50 = <b>₹5,000 pay-in</b>"))
    sub("Options trading & settlement", 5,
      L("Same indices/stocks as futures; expiry last Tuesday (NSE) or Thursday (BSE)",
        "India trades only <b>European</b> options: <b>CE</b> = call European, <b>PE</b> = put European; market trades the premium for each strike",
        "Lot ≥ ₹5 lakh at introduction; tick ₹0.05; base = theoretical price using <b>MIBOR</b>",
        "Price band computed and announced daily (not a fixed %)",
        "Daily settlement of <b>premium</b> on T+1 to seller",
        "On expiry, exercised ITM options settled at close; long positions assigned to shorts, aggregated client → TM → CM"))
    sub("Risk management in derivatives", 5,
      K("Tools: capital adequacy · stringent margins · position limits by capital · online monitoring · automatic disablement on breach",
        "SEBI study (25 Jan 2023): <b>9 of 10</b> individual F&amp;O traders made net losses",
        "<b>Liquid net worth</b> = liquid part of net worth and margins (cash &amp; equivalents); rest = base capital; CC may use them to settle member dues; collateral release via electronic interface") +
      T(["Margin","Futures","Options"],
        [["Initial","Risk over a <b>2-day</b> horizon","On premium value of open positions"],["Exposure","% of notional value","Notional value; <b>short positions only</b>"],
         ["Premium margin","—","Premium due, till premium pay-in"],["Assignment margin","—","Final exercise obligation, till exercise pay-in"]]) +
      K("Margins paid upfront; flow client → TM → CM → CC","Non-payment: trading suspended, disciplinary action, positions closed","CMs report margins due and collected daily (upfront collection framework 20 Jul 2020)"))
    sub("Position limits", 4,
      L("CM open position = aggregate of its TMs, clients, custodial participants; proprietary and client positions grossed separately (sells set off against buys within each)",
        "Limits as % of market-wide position limit or contract value",
        "Near limit → alerts, no fresh positions, only squaring off; terminal deactivated when hit; penalties for breaches",
        "Real-time monitoring; CMs may need more base capital and liquid net worth"))
    sub("Uses: hedging, speculation, arbitrage", 5,
      T(["Use","Meaning"],
        [["Hedging","Protect an existing position from adverse price moves"],["Speculation","No underlying position; implement a price view cheaply — cost of long futures = margin"],
         ["Arbitrage","Price gap &gt; borrowing cost → borrow, buy cheap, sell dear; settle both legs at expiry → locked gain less interest"]]) +
      K("Benefits: symmetrical and asymmetrical payoffs for hedging · more liquidity, lower costs, better price discovery",
        "Costs: OTC and poorly regulated markets caused liquidity crises and counterparty failures when big positions were unwound"))
    sub("Open interest & put-call ratio", 5,
      L("Open interest = all outstanding contracts, counted <b>one side</b>",
        "A sells to B (OI 1); A later buys from C to square off → A out, but B short vs C long → OI unchanged",
        "OI ≠ volume; higher OI relative to volume → more liquidity; rising OI = fresh money") +
      F("PCR = put options outstanding ÷ call options outstanding\nMore calls → PCR &lt; 1 ; more puts → PCR &gt; 1") +
      K("Traders read PCR as bullish or bearish in different ways"))
    sub("Workbook sample answers", 3,
      K("Nifty 50 futures underlying = value of the Nifty 50 index","Futures cut counterparty risk through the clearing corporation",
        "MTM settlement price = weighted average of last 30 minutes","Exercisable any time before expiry = American option"))
