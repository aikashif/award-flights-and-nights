"""Series XII quiz part E: Ch6 Derivatives Markets."""

def add(Q, inr, num):
    C = 6
    S = lambda *a: Q(C, "S", *a)
    H = lambda *a: Q(C, "H", *a)
    S("In a Nifty 50 futures contract, the underlying is:",
      "The value of the Nifty 50 index", "Workbook sample answer.",
      ("Top traded Nifty stocks", "No."),
      ("Average price of Nifty stocks", "No."),
      ("Market cap of the index", "No."))
    S("Counterparty risk of forwards is reduced in futures mainly by:",
      "The clearing corporation", "CC is counterparty; margins.",
      ("Collateral by both parties directly", "No."),
      ("Gross settlement", "No."),
      ("Position limits", "Supporting tool only."))
    S("The daily settlement price for futures MTM is:",
      "Weighted average price of the last 30 minutes", "Workbook.",
      ("Last traded price", "No."),
      ("Average of high, low, close", "No."),
      ("Average of last 60 minutes", "No."))
    S("An option exercisable any time before expiry is:",
      "American", "India trades only European.",
      ("European", "Only on expiry."),
      ("At the money", "Moneyness."),
      ("Bermudan", "Specific dates."))
    S("Indian exchange-traded options are:",
      "European style", "CE / PE.",
      ("American style", "No."),
      ("Bermudan style", "No."),
      ("Both European and American", "No."))
    S("Forward at ₹30,000 for 10 g gold. In a year gold is ₹35,000. Who gains?",
      "The buyer", "Pays 30,000 for gold worth 35,000.",
      ("The seller", "Loses."),
      ("Both", "Zero sum."),
      ("Neither", "No."))
    S("Forward at ₹30,000; gold falls to ₹25,000. Who gains?",
      "The seller", "Gets 30,000 vs market 25,000.",
      ("The buyer", "Loses."),
      ("Both", "No."),
      ("Neither", "No."))
    S("A farmer's contract paying off on rainfall is a:",
      "Weather derivative", "Workbook.",
      ("Currency derivative", "No."),
      ("Index derivative", "No."),
      ("Interest rate swap", "No."))
    S("Paying fixed and receiving floating to convert a floating loan to fixed is a/an:",
      "Interest rate swap", "Workbook.",
      ("Currency forward", "No."),
      ("Call option", "No."),
      ("Index future", "No."))
    S("An importer locking the USD/INR rate for a future payment uses a:",
      "Currency derivative", "Workbook.",
      ("Weather derivative", "No."),
      ("Index derivative", "No."),
      ("Equity option", "No."))
    S("The net economic value of all derivative positions is:",
      "Zero", "Zero-sum: every long has a short.",
      ("Positive", "No."),
      ("Equal to underlying value", "No."),
      ("Negative", "No."))
    S("Since October 2019, stock F&O open at expiry are settled by:",
      "Physical delivery", "Index F&O stay cash.",
      ("Cash", "Index."),
      ("Rollover", "No."),
      ("Auction", "No."))
    S("Forwards are ___ and futures are ___.",
      "OTC; exchange-traded", "Workbook.",
      ("Exchange-traded; OTC", "Reversed."),
      ("Both OTC", "No."),
      ("Both exchange-traded", "No."))
    S("Prices of the same good in two markets differ only by transaction costs. This is the:",
      "Law of one price", "Arbitrage keeps it.",
      ("Law of demand", "No."),
      ("Efficient market hypothesis", "No."),
      ("Zero sum rule", "No."))
    S("The option buyer pays the seller an upfront:",
      "Premium", "Price of the option.",
      ("Margin", "Seller pays margin."),
      ("Strike price", "Paid only if exercised."),
      ("Brokerage", "No."))
    S("Arvind's Nifty 10,000 call; Nifty at expiry 10,200. The option is:",
      "In-the-money", "Spot > strike for a call.",
      ("Out-of-the-money", "Spot < strike."),
      ("At-the-money", "Spot = strike."),
      ("Expired worthless", "No."))
    S("If Nifty ends at 9,800, Salim (call writer):",
      "Keeps the ₹100 premium", "Arvind won't exercise.",
      ("Pays ₹200", "No."),
      ("Loses ₹100", "No."),
      ("Must buy Nifty", "No."))
    S("Equity index futures were introduced in India in:",
      "June 2000", "Options and stock futures in 2001.",
      ("2001", "Options/stock futures."),
      ("2008", "SLBM."),
      ("1995", "No."))
    S("Index options, stock options and stock futures were introduced in:",
      "2001", "Workbook.",
      ("2000", "Index futures."),
      ("2003", "No."),
      ("2019", "Physical settlement."))
    S("The tick size for equity futures is:",
      "₹0.05", "e.g. 5610.50 → 5610.55.",
      ("₹0.01", "No."),
      ("₹0.0025", "IRF."),
      ("₹1", "No."))
    S("Per the XII workbook, the trading lot value at introduction is at least:",
      "₹5 lakh", "XII figure.",
      ("₹15 lakh", "V-D newer figure."),
      ("₹2 lakh", "IRF."),
      ("₹1 lakh", "No."))
    S("NSE equity derivatives normal market hours (as stated in this workbook) are:",
      "9:15 am to 3:40 pm", "Trade modification till 4:15 pm.",
      ("9:15 am to 3:30 pm", "Equity cash."),
      ("9:00 am to 5:00 pm", "Debt/IRF."),
      ("10:00 am to 3:30 pm", "No."))
    S("A professional clearing member is:",
      "A bank or custodian that clears but doesn't trade", "Workbook.",
      ("A trading member clearing its own trades only", "SCM."),
      ("A member that trades and clears for others", "TM-CM."),
      ("A SEBI official", "No."))
    S("A self-clearing member clears:",
      "Only its own trades", "Workbook.",
      ("Trades of all members", "No."),
      ("Only client trades of others", "No."),
      ("No trades", "No."))
    S("Daily MTM for derivatives is settled on:",
      "T+1", "Workbook.",
      ("T+0", "No."),
      ("T+2", "No."),
      ("At expiry only", "Final settlement."))
    S("Bought Nifty futures at 10,000; settlement price 9,900; lot 50. MTM pay-in is:",
      "₹5,000", "100 × 50.",
      ("₹100", "Per unit."),
      ("₹50,000", "No."),
      ("₹9,900", "No."))
    S("Final settlement of futures is at:",
      "Closing price of the underlying in the cash market on expiry", "Workbook.",
      ("Opening price on expiry", "No."),
      ("Average of the month", "No."),
      ("The original traded price", "No."))
    S("Initial margin in futures estimates risk over:",
      "A 2-day horizon", "Workbook.",
      ("1 week", "No."),
      ("1 month", "No."),
      ("Intraday only", "No."))
    S("Exposure margin is collected as a percentage of:",
      "Notional value of the open position", "Workbook.",
      ("Premium", "Option initial margin."),
      ("Brokerage", "No."),
      ("Net worth", "No."))
    S("Open interest is:",
      "Outstanding contracts counted one side", "Not volume.",
      ("Total contracts traded today", "Volume."),
      ("Buyers plus sellers count", "Double counting."),
      ("Margin collected", "No."))
    H("In options, exposure margin is collected from:",
      "Option sellers (short positions) only", "Workbook.",
      ("Option buyers only", "No."),
      ("Both buyers and sellers", "No."),
      ("Nobody", "No."))
    H("Premium margin in options is levied:",
      "Until pay-in of the premium is complete", "Assignment margin until exercise pay-in.",
      ("Until expiry", "No."),
      ("Only on exercise", "Assignment margin."),
      ("Never", "No."))
    H("Assignment margin covers:",
      "The final exercise settlement obligation", "Workbook.",
      ("Daily premium", "Premium margin."),
      ("Notional exposure", "Exposure margin."),
      ("Brokerage", "No."))
    H("A sold B a future; later A buys from C to square off. Market open interest:",
      "Stays the same (B short vs C long)", "Workbook example.",
      ("Falls by one", "No."),
      ("Rises by one", "No."),
      ("Becomes zero", "No."))
    H("Higher open interest relative to volume indicates:",
      "Greater liquidity", "Workbook.",
      ("Lower liquidity", "No."),
      ("Market crash", "No."),
      ("Lower margins", "No."))
    H("PCR = 0.8 means:",
      "More calls outstanding than puts", "Below one.",
      ("More puts than calls", "Above one."),
      ("Equal puts and calls", "PCR = 1."),
      ("Market is closed", "No."))
    H("Option base price at introduction is computed using:",
      "Theoretical price with MIBOR as interest rate", "Workbook.",
      ("Previous day close of underlying", "No."),
      ("Repo rate", "No."),
      ("Fixed ₹1", "No."))
    H("Option price bands are:",
      "Computed by the exchange and announced daily, not a fixed %", "Workbook.",
      ("Fixed at 10%", "No."),
      ("Same as futures", "No."),
      ("Not applicable", "No."))
    H("Option premium is settled daily to the seller on:",
      "T+1", "Workbook.",
      ("T+0", "No."),
      ("At expiry", "No."),
      ("T+2", "No."))
    H("SEBI's January 2023 study found individual F&O traders making net losses were:",
      "9 out of 10", "Workbook footnote.",
      ("5 out of 10", "No."),
      ("7 out of 10", "No."),
      ("1 out of 10", "No."))
    H("Which is TRUE of weekly index options per the workbook?",
      "Seven weekly expiries excluding the monthly expiry week", "Workbook.",
      ("Four weekly expiries", "No."),
      ("Every stock has weekly options", "No."),
      ("Weekly options settle physically", "No."))
    H("Per SEBI (26 May 2025), an exchange's equity derivatives expire on:",
      "Either Tuesday or Thursday, uniformly for all its contracts", "NSE Tuesday, BSE Thursday.",
      ("Any day the exchange chooses per contract", "No."),
      ("Always Thursday", "No."),
      ("Always the last Friday", "No."))
    H("Long-dated contracts include 3 quarterly and ___ semi-annual (Jun/Dec) months.",
      "8", "Workbook.",
      ("4", "No."),
      ("2", "No."),
      ("12", "No."))
    H("A spread order executes when:",
      "The price difference between two positions hits a set level", "Workbook.",
      ("Bid-ask spread narrows", "No."),
      ("Market opens", "No."),
      ("Volume crosses a limit", "No."))
    H("When open positions near position limits, the exchange:",
      "Sends alerts, blocks fresh positions and allows only squaring off", "Terminal deactivated if hit.",
      ("Raises the limit", "No."),
      ("Cancels all trades", "No."),
      ("Ignores it", "No."))
    H("Liquid net worth of a member is:",
      "Part of net worth and margins held in cash and cash equivalents", "Rest is base capital.",
      ("Total assets minus liabilities", "Net worth."),
      ("Brokerage income", "No."),
      ("Value of client securities", "No."))
    H("Arbitrageurs exploit a futures–cash gap only if:",
      "The gap exceeds the cost of borrowing", "Gain less interest is locked.",
      ("The market rises", "Direction irrelevant."),
      ("Volatility is high", "No."),
      ("They own the stock already", "Not required."))
    H("Speculating with long futures costs the trader mainly:",
      "The margin", "No underlying position.",
      ("The full contract value", "No."),
      ("The premium", "Options."),
      ("Nothing", "No."))
    H("MCX wheat futures per the workbook are settled by:",
      "Physical delivery only, at exchange-approved warehouses", "Delivery on 20th.",
      ("Cash only", "No."),
      ("Either", "No."),
      ("Rollover", "No."))
    H("A cost of derivatives noted in the workbook is:",
      "OTC and poorly regulated markets caused liquidity crises and counterparty failures", "Workbook.",
      ("They always reduce liquidity", "They enhance it."),
      ("They increase trading costs in cash market", "They reduce them."),
      ("They stop price discovery", "They help it."))
    H("Trading members settle their derivative trades through:",
      "Clearing members", "Workbook.",
      ("Depositories directly", "No."),
      ("SEBI", "No."),
      ("Their clients", "No."))
