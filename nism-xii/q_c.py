"""Series XII quiz part C: Ch4 Secondary Markets (+2 Ch3 top-ups)."""

def add(Q, inr, num):
    Q(3, "H", "Which is TRUE of a private placement offer?",
      "It is made by name to identified persons and filed with the RoC; no advertising", "Companies Act 2013.",
      ("It must be approved by SEBI before launch", "SEBI public-issue rules don't apply."),
      ("It may be advertised in newspapers", "Not allowed."),
      ("Only listed companies can make it", "Any company."))
    Q(3, "H", "A rights issue letter of offer is filed in draft with:",
      "SEBI", "Abridged letter sent to all holders; record date fixed.",
      ("RBI", "No."),
      ("RoC only", "No."),
      ("Depositories", "No."))
    C = 4
    S = lambda *a: Q(C, "S", *a)
    H = lambda *a: Q(C, "H", *a)
    S("The primary function of the secondary market is to:",
      "Provide liquidity for securities issued", "Workbook sample answer.",
      ("Provide a platform for public issues", "Primary market."),
      ("Provide information about companies", "Secondary role."),
      ("Give greater disclosures", "No."))
    S("The document confirming a trade on the exchange is the:",
      "Contract note", "Issued within 24 hours.",
      ("Confirmation slip", "Shows trade but isn't the legal document."),
      ("Delivery instruction slip", "DP instruction."),
      ("Allotment advice", "Primary market."))
    S("Exchanges control default risk from trading mainly by:",
      "Imposing margins", "Workbook sample answer.",
      ("Imposing circuit filters", "Volatility control."),
      ("Restricting investors", "No."),
      ("Blocking high value trades", "No."))
    S("A trade squared off during the day:",
      "Does not require delivery of shares", "Net position nil.",
      ("Is not guaranteed by the exchange", "It is."),
      ("Is cancelled by the exchange", "No."),
      ("Isn't counted in volumes", "It is."))
    S("Market capitalisation of a stock changes with:",
      "Its share price", "Shares × price.",
      ("The market index", "Not directly."),
      ("Trading volume", "No."),
      ("Market liquidity", "No."))
    S("The three national stock exchanges in India are:",
      "BSE, NSE and MSEI", "Workbook.",
      ("BSE, NSE and MCX", "MCX is commodities."),
      ("NSE, NSE IX and India INX", "IFSC exchanges."),
      ("BSE, NSE and CCIL", "CCIL is clearing."))
    S("Trades done directly between investors outside the exchange are:",
      "Off-market trades without exchange protections", "No regulatory redressal.",
      ("Block deals", "On exchange window."),
      ("Bulk deals", "On exchange."),
      ("Proprietary trades", "Broker's own trades."))
    S("After KYC with a broker, each investor gets a:",
      "Unique Client Code (UCC)", "Used on every order.",
      ("ISIN", "Security identifier."),
      ("Folio number", "Mutual funds."),
      ("ARN", "MF distributor code."))
    S("The current equity settlement cycle in India is:",
      "T+1 (with optional T+0)", "T+1 for all since 27 Jan 2023.",
      ("T+2", "Old."),
      ("T+3", "Old."),
      ("T+5", "No."))
    S("Clearing corporations are usually:",
      "Wholly owned subsidiaries of stock exchanges", "Separate legal entities.",
      ("Departments of SEBI", "No."),
      ("Owned by RBI", "No."),
      ("Owned by brokers", "No."))
    S("The two depositories in India are:",
      "NSDL and CDSL", "Workbook.",
      ("NSDL and CCIL", "CCIL clears."),
      ("CDSL and ICCL", "ICCL clears."),
      ("BSE and NSE", "Exchanges."))
    S("Secondary markets are regulated under SCRA 1956 and:",
      "SCR Rules 1957", "SEBI implements.",
      ("Companies Act 2013", "No."),
      ("FEMA 1999", "No."),
      ("RBI Act 1934", "No."))
    S("India's first IFSC is at:",
      "GIFT City, Gandhinagar", "Workbook.",
      ("BKC, Mumbai", "No."),
      ("Noida", "No."),
      ("Bengaluru", "No."))
    S("Since July 2023, SGX Nifty derivatives trade exclusively on:",
      "NSE IX", "SGX Nifty delisted.",
      ("India INX", "BSE's IFSC exchange."),
      ("NSE F&O segment", "No."),
      ("Singapore Exchange", "Moved away."))
    S("India INX at GIFT City was set up by:",
      "BSE", "NSE IX by NSE.",
      ("NSE", "NSE IX."),
      ("MSEI", "No."),
      ("RBI", "No."))
    S("Bullion imports for domestic use are routed through:",
      "India International Bullion Exchange (IIBX)", "Workbook.",
      ("MCX", "No."),
      ("NSE IX", "No."),
      ("RBI vaults", "No."))
    S("The Gandhi Committee on MII governance reported in:",
      "March 2018", "Chaired by R. Gandhi.",
      ("December 2012", "SEBI earlier norms."),
      ("June 2019", "Interoperability implemented."),
      ("July 2020", "No."))
    S("MII committees are chaired by:",
      "Public Interest Directors", "Workbook.",
      ("SEBI officials", "No."),
      ("Shareholder directors", "No."),
      ("Managing Directors", "No."))
    S("A broker must issue a contract note within:",
      "24 hours of execution", "Workbook.",
      ("48 hours", "No."),
      ("T+1", "No."),
      ("7 days", "No."))
    S("A broker must pay/deliver to the client within ___ of pay-out.",
      "24 hours", "Workbook.",
      ("48 hours", "No."),
      ("3 working days", "No."),
      ("7 days", "No."))
    S("Which document is NOT given by a broker at account opening?",
      "Scheme Information Document", "That's for MFs.",
      ("Risk Disclosure Document", "Given."),
      ("Rights and Obligations", "Given."),
      ("Tariff sheet", "Given."))
    S("PoA misuse led SEBI to introduce:",
      "DDPI (Demat Debit and Pledge Instruction)", "Limited purposes; revocable.",
      ("ASBA", "Primary market."),
      ("UCC", "Client code."),
      ("ECN", "Electronic contract note."))
    S("DDPI can be used by a broker only for:",
      "Securities pay-in and pledging for margins", "Limited purposes.",
      ("Any trade the broker wants", "No."),
      ("Withdrawing client funds", "No."),
      ("Opening new accounts", "No."))
    S("NSE's trading system is called:",
      "NEAT", "BSE: BOLT; MSEI: TWS.",
      ("BOLT", "BSE."),
      ("TWS", "MSEI."),
      ("NDS-OM", "G-secs."))
    S("BOLT is the trading system of:",
      "BSE", "BSE On-Line Trading.",
      ("NSE", "NEAT."),
      ("MSEI", "TWS."),
      ("MCX", "No."))
    S("ISIN is a unique identifier of:",
      "12 characters for each security in the depository system", "e.g. INE038A01020.",
      ("10 digits for each investor", "No."),
      ("8 digits for each broker", "No."),
      ("6 digits for each trade", "No."))
    S("A limit buy order at ₹2,500 when the price is ₹2,600 will execute:",
      "Only at ₹2,500 or lower", "Limit price or better.",
      ("Immediately at ₹2,600", "Market order."),
      ("At ₹2,500 or higher", "Sell logic."),
      ("Never", "Can execute if price falls."))
    S("An order cancelled if not filled immediately is:",
      "Immediate or Cancel (IOC)", "Unfilled part cancelled at once.",
      ("Day order", "Valid all day."),
      ("Stop-loss", "Trigger based."),
      ("Disclosed quantity", "Hides size."))
    S("A buyer at ₹1,000 places a stop-loss sell at ₹990. If price falls to ₹990:",
      "The sell order triggers to close the position", "Limits loss.",
      ("The buy order is cancelled", "Already executed."),
      ("Nothing happens until day end", "No."),
      ("The exchange halts trading", "No."))
    S("Indian exchanges allow orders valid:",
      "For the day only (no GTC)", "Brokers may re-enter next day.",
      ("Good till cancelled", "Not permitted."),
      ("For one week", "No."),
      ("Till expiry", "No."))
    S("NSE equity regular trading hours are:",
      "9:15 am to 3:30 pm", "Pre-open 9:00–9:15.",
      ("9:00 am to 5:00 pm", "Debt."),
      ("9:15 am to 3:40 pm", "Equity derivatives (workbook)."),
      ("10:00 am to 3:30 pm", "No."))
    S("The NSE pre-open session runs from:",
      "9:00 am to 9:15 am", "Entry, matching, buffer.",
      ("8:45 am to 9:00 am", "Block deal window."),
      ("9:15 am to 9:30 am", "No."),
      ("9:00 am to 9:30 am", "No."))
    S("Order matching follows:",
      "Price-time priority", "Best price first, then earliest.",
      ("Size priority", "No."),
      ("Broker priority", "No."),
      ("Random allocation", "No."))
    S("Orders resting away from the market that add depth are:",
      "Passive orders", "Limit orders; add liquidity.",
      ("Active orders", "Drain liquidity."),
      ("Market orders", "Active."),
      ("IOC orders", "Active."))
    S("A bulk deal is a deal exceeding ___ of listed shares in a day.",
      "0.50%", "Disclosed same day after hours.",
      ("5%", "No."),
      ("1%", "No."),
      ("0.05%", "No."))
    S("Minimum size of a block deal is:",
      "₹25 crore", "Single transaction in special window.",
      ("₹5 crore", "No."),
      ("₹10 crore", "No."),
      ("₹50 crore", "No."))
    S("Block deals must be settled by:",
      "Delivery only — no square-off or reversal", "Workbook.",
      ("Cash difference", "No."),
      ("T+5 settlement", "No."),
      ("Either, by choice", "No."))
    S("Daily price bands for individual stocks can be:",
      "2%, 5%, 10% or 20%", "Based on liquidity, volatility.",
      ("1%, 3%, 5%", "No."),
      ("10%, 15%, 20%", "Market-wide breaker levels."),
      ("Unlimited", "No."))
    S("Stocks in the F&O segment have:",
      "No price band (only an operating range)", "Workbook.",
      ("A 2% band", "No."),
      ("A 20% band", "No."),
      ("Trading only in pre-open", "No."))
    S("A market-wide circuit breaker is triggered by:",
      "Sensex or Nifty 50, whichever breaches first", "Halts equity and equity derivatives.",
      ("Nifty Bank", "No."),
      ("India VIX", "No."),
      ("Sensex only", "No."))
    S("A 20% index move at any time during market hours halts trading for:",
      "The rest of the day", "Workbook table.",
      ("1 hour 45 minutes", "15% before 1 pm."),
      ("45 minutes", "10% before 1 pm."),
      ("15 minutes", "No."))
    S("GST on brokerage is:",
      "18%", "Goes to Central Government.",
      ("12%", "No."),
      ("5%", "No."),
      ("28%", "No."))
    S("STT on delivery purchase of equity shares is:",
      "0.1% paid by the buyer", "Also 0.1% for seller.",
      ("0.025% by seller", "Intraday."),
      ("0.001% by seller", "Equity fund units."),
      ("Nil", "No."))
    S("SEBI turnover fee on non-debt securities is:",
      "₹10 per crore (0.0001%)", "Debt ₹2.5 per crore.",
      ("₹2.5 per crore", "Debt."),
      ("₹100 per crore", "No."),
      ("0.01%", "No."))
    S("Stamp duty on securities transfers is collected for:",
      "State governments", "By exchanges, CCs, depositories.",
      ("Central Government", "STT and GST."),
      ("SEBI", "No."),
      ("RBI", "No."))
    S("Higher impact cost indicates:",
      "Lower liquidity and higher trading cost", "Lower impact cost = more liquid.",
      ("Higher liquidity", "Reversed."),
      ("Lower brokerage", "No."),
      ("Lower volatility", "No."))
    S("Selling and buying the same quantity of a stock on the same day is:",
      "Squaring off (intraday trading)", "No delivery.",
      ("Rolling settlement", "Delivery."),
      ("Block deal", "No."),
      ("Netting across members", "No."))
    S("When securities sold are not delivered on settlement day, the CC:",
      "Conducts an auction to buy and deliver them", "Short delivery.",
      ("Cancels the trade", "No."),
      ("Pays the buyer interest only", "No."),
      ("Asks SEBI to intervene", "No."))
    S("Delivered shares rejected by the depository for technical reasons are a:",
      "Bad delivery", "Must be rectified.",
      ("Short delivery", "Not delivered at all."),
      ("Auction delivery", "No."),
      ("Off-market delivery", "No."))
    S("Extreme Loss Margin for any stock is:",
      "3.5%", "SEBI Feb 2020.",
      ("5%", "No."),
      ("10%", "No."),
      ("1.5%", "No."))
    S("Mark-to-market margin in the cash market is payable:",
      "At the start of the next trading day", "Computed at day end.",
      ("At order placement", "VaR/ELM."),
      ("Weekly", "No."),
      ("At settlement only", "No."))
    S("VaR margin rates are updated at least:",
      "5 times a trading day", "Workbook.",
      ("Once a day", "No."),
      ("Once a week", "No."),
      ("Every minute", "No."))
    S("The record date determines:",
      "Who receives the corporate action benefit", "Holders on record.",
      ("When the company was listed", "No."),
      ("When trading stops", "No."),
      ("The face value", "No."))
    S("A ₹10 FV share at ₹500 splits to FV ₹2. Ex-date price becomes about:",
      "₹100", "5 shares × ₹100.",
      ("₹500", "No."),
      ("₹250", "No."),
      ("₹50", "No."))
    S("Interoperability of clearing corporations was implemented in:",
      "June 2019", "Framework 2018.",
      ("January 2023", "T+1."),
      ("July 2023", "SGX Nifty move."),
      ("October 2019", "Physical settlement."))
    S("SLBM was introduced on Indian exchanges in:",
      "2008", "Exchange platform, not OTC.",
      ("2001", "No."),
      ("2013", "No."),
      ("2019", "No."))
    S("SLB contracts are available on securities that are:",
      "In the F&O segment", "Monthly and yearly contracts.",
      ("In the SME segment", "No."),
      ("Unlisted", "No."),
      ("G-secs only", "No."))
    S("Sensex consists of:",
      "30 stocks", "Base 100 on 1 April 1979.",
      ("50 stocks", "Nifty 50."),
      ("40 stocks", "SX40."),
      ("100 stocks", "No."))
    S("Nifty 50's base value and date are:",
      "1,000 on 3 November 1995", "Workbook.",
      ("100 on 1 April 1979", "Sensex."),
      ("10,000 on 31 March 2010", "SX40."),
      ("1,000 on 1 January 1986", "No."))
    S("SCORES complaints must be resolved by the entity within:",
      "21 days", "Upload Action Taken Report.",
      ("30 days", "No."),
      ("7 days", "No."),
      ("15 days", "No."))
    S("The Investor Protection Fund of an exchange is administered by:",
      "A trust", "Pays when defaulter's assets fall short.",
      ("SEBI directly", "No."),
      ("The clearing corporation", "No."),
      ("The defaulting broker", "No."))
    H("A broker doing both proprietary and client trading without algo must keep BMC of:",
      "₹25 lakh", "10 (prop) / 15 (client) / 25 (both) / 50 (algo).",
      ("₹10 lakh", "Prop only."),
      ("₹15 lakh", "Client only."),
      ("₹50 lakh", "Algo."))
    H("A trading member using algorithmic trading must keep BMC of:",
      "₹50 lakh", "Workbook.",
      ("₹25 lakh", "No."),
      ("₹1 crore", "No."),
      ("₹10 lakh", "No."))
    H("At least what share of BMC must be in cash or cash equivalents?",
      "50%", "No exposure allowed against BMC.",
      ("25%", "No."),
      ("100%", "No."),
      ("75%", "No."))
    H("A 10% index fall at 1:30 pm causes a halt of:",
      "15 minutes, then 15-minute pre-open", "1:00–2:30 pm slot.",
      ("45 minutes", "Before 1 pm."),
      ("No halt", "After 2:30 pm."),
      ("Rest of day", "No."))
    H("A 15% index fall at 2:15 pm leads to:",
      "Halt for the rest of the day", "On or after 2 pm.",
      ("45-minute halt", "1–2 pm."),
      ("1 hr 45 min halt", "Before 1 pm."),
      ("No halt", "No."))
    H("A 10% index fall at 2:45 pm leads to:",
      "No halt", "At or after 2:30 pm.",
      ("15-minute halt", "1–2:30 pm."),
      ("Rest of day halt", "No."),
      ("45-minute halt", "No."))
    H("The afternoon block deal window's reference price is:",
      "VWAP of trades between 1:45 pm and 2:00 pm", "Morning: previous close.",
      ("Previous day close", "Morning window."),
      ("Opening price", "No."),
      ("Last traded price at 2:05 pm", "No."))
    H("Block deal order price must be within ___ of the reference price.",
      "±3%", "Workbook.",
      ("±1%", "No."),
      ("±5%", "No."),
      ("±10%", "No."))
    H("Block deal windows are:",
      "8:45–9:00 am and 2:05–2:20 pm", "Workbook (Oct 2025 review).",
      ("9:00–9:15 am and 3:15–3:30 pm", "No."),
      ("9:15–9:30 am and 2:00–2:15 pm", "No."),
      ("After market close only", "No."))
    H("Order book: best bid 350, best ask 400. Impact cost of buying is:",
      "6.67%", "Ideal 375; 25/375.",
      ("14.29%", "50/350."),
      ("12.5%", "50/400."),
      ("13.33%", "50/375."))
    H("Total trading cost on ₹1 lakh in the workbook example is:",
      "₹489.10 (0.4891%)", "Brokerage 300 + DP 20 + STT 100 + GST 54 + stamp 15 + SEBI 0.10.",
      ("₹300", "Brokerage only."),
      ("₹454", "No."),
      ("₹1,000", "No."))
    H("STT when an option is exercised is 0.15% paid by:",
      "The purchaser, on intrinsic value", "Sale of option: seller on premium.",
      ("The seller, on premium", "Sale of option."),
      ("The seller, on strike", "No."),
      ("The exchange", "No."))
    H("STT on sale of futures is:",
      "0.05% by seller on traded price", "Workbook.",
      ("0.15% by seller on premium", "Options."),
      ("0.1% by buyer", "Delivery equity."),
      ("0.025% by buyer", "No."))
    H("STT on intraday (non-delivery) sale of equity shares is:",
      "0.025% by the seller", "Workbook.",
      ("0.1% by buyer and seller", "Delivery."),
      ("0.001%", "Equity fund unit delivery sale."),
      ("0.05%", "Futures."))
    H("Netting: buy 100 XYZ, sell 50 XYZ, buy 100 MNO, buy 50 DEF, sell 150 DEF. Net result:",
      "Receive 50 XYZ and 100 MNO; deliver 100 DEF", "Net settlement.",
      ("Receive 150 XYZ", "No."),
      ("Deliver 150 DEF", "Gross."),
      ("Receive 50 DEF", "No."))
    H("A broker collecting at least ___ upfront margin avoids short-collection penalty in cash segment.",
      "20%", "In lieu of VaR + ELM.",
      ("10%", "No."),
      ("50%", "No."),
      ("100%", "No."))
    H("Spread margin on offsetting cash–futures positions under cross-margining is:",
      "25% of applicable upfront margin", "Highly correlated indices: 30%.",
      ("30%", "Correlated indices."),
      ("50%", "No."),
      ("Nil", "No."))
    H("Which is NOT eligible for cross-margin benefit?",
      "Long stock A in cash vs short futures on unrelated stock B", "Must be offsetting positions.",
      ("Index futures vs constituent stock futures", "Eligible."),
      ("Cash stock vs its own futures", "Eligible."),
      ("ETF vs its constituent stocks", "Eligible."))
    H("Interoperability covers all segments EXCEPT:",
      "Commodity derivatives", "Also excludes IFSC CCs.",
      ("Currency derivatives", "Covered."),
      ("Debt segment", "Covered."),
      ("Equity derivatives", "Covered."))
    H("A client is long 10 lots XYZ Sep futures on NSE and short 6 lots on BSE. Under interoperability, margin is on:",
      "Long 4 lots", "Netted across exchanges.",
      ("Long 10 + short 6 = 16 lots", "No."),
      ("Short 6 lots", "No."),
      ("Long 10 lots", "No."))
    H("Arbitrator's award must be issued within ___ of appointment.",
      "30 days (extendable by 30 days)", "Workbook.",
      ("15 days", "No."),
      ("60 days fixed", "No."),
      ("90 days", "No."))
    H("Appeal against an arbitrator's award to the appellate panel must be made within:",
      "7 days of receiving the award", "Then High Court.",
      ("30 days", "No."),
      ("15 days", "No."),
      ("3 months", "No."))
    H("A party unhappy with the appellate arbitration decision can approach:",
      "The High Court", "Workbook.",
      ("SEBI", "No."),
      ("SCORES", "No."),
      ("The stock exchange board", "No."))
    H("Which claim will the exchange NOT resolve through grievance redressal?",
      "Compensation for mental agony", "Also notional/opportunity loss.",
      ("Non-receipt of funds from broker", "Handled."),
      ("Non-receipt of contract note", "Handled."),
      ("Wrong trade in client's UCC", "Handled."))
    H("IPEF restitution claims can be made up to ___ from SEBI inviting claims.",
      "7 years", "Workbook.",
      ("3 years", "No."),
      ("10 years", "No."),
      ("1 year", "No."))
    H("Order of escalation under the ODR framework is:",
      "Market participant → SCORES → ODR portal", "ODR also directly if unresolved/pending.",
      ("ODR → SCORES → SEBI", "No."),
      ("SEBI → court → ODR", "No."),
      ("Exchange → RBI → ODR", "No."))
    H("Which SEBI circular created the common ODR portal?",
      "31 July 2023", "Online Resolution of Disputes.",
      ("30 May 2022", "Arbitration for RTA disputes."),
      ("4 July 2022", "Hybrid arbitration."),
      ("26 May 2025", "Expiry day."))
    H("Arbitration can now cover disputes between shareholders and listed companies/RTAs about:",
      "Transfer, transmission, demat/remat, duplicate shares, corporate benefits", "30 May 2022 SOP.",
      ("Share price falls", "No."),
      ("Dividend policy", "No."),
      ("IPO pricing", "No."))
    H("Which is TRUE of DMA (Direct Market Access)?",
      "Institutional orders go straight to the exchange bypassing the broker's server", "Allowed since 2008.",
      ("It is open to all retail clients", "Institutions."),
      ("It removes KYC need", "Broker does due diligence."),
      ("It bypasses the exchange", "No."))
    H("HFT is characterised by:",
      "Very high order-to-trade ratios and no significant overnight positions", "SEC features.",
      ("Long holding periods", "No."),
      ("Manual order entry", "No."),
      ("Low technology spend", "No."))
    H("Latency in trading means:",
      "Time between sending an order and its receipt by the exchange", "Co-location reduces it.",
      ("Delay in settlement", "No."),
      ("Gap between bid and ask", "Spread."),
      ("Time to get contract note", "No."))
    H("A buy order at 102.45 when LTP is 105.10 is a:",
      "Passive order", "Below market.",
      ("Active order", "No."),
      ("Market order", "No."),
      ("Stop-loss order", "No."))
    H("Which exchange action forces delivery in a volatile scrip?",
      "Shifting it to the trade-to-trade segment", "No intraday netting.",
      ("Raising the circuit band", "No."),
      ("Removing it from indices", "No."),
      ("Suspending SLB", "No."))
    H("Exchanges inspect trading members' books at least:",
      "Once a year", "Workbook.",
      ("Once a quarter", "No."),
      ("Every 3 years", "No."),
      ("Only on complaint", "No."))
    H("Residual default risk beyond margins is covered by the:",
      "Core Settlement Guarantee Fund", "Workbook.",
      ("Investor Protection Fund", "Pays investors for broker default."),
      ("IPEF", "SEBI fund."),
      ("BMC", "Member capital."))
    H("CCIL was set up in:",
      "2001", "Runs NDS-OM; guarantees G-sec settlement.",
      ("2005", "NDS-OM start / call market change."),
      ("1995", "No."),
      ("2008", "No."))
    H("OTC corporate bond trades must be reported on exchange platforms within:",
      "15 minutes", "Workbook.",
      ("30 minutes", "OTC derivatives to trade repository."),
      ("1 hour", "No."),
      ("End of day", "No."))
    H("The institutional platform of the exchange debt segment has a minimum lot of:",
      "₹1 crore", "Retail platform for publicly issued bonds.",
      ("₹10 lakh", "No."),
      ("₹1 lakh", "Private placement face value (Ch 18 V-D)."),
      ("₹5 crore", "Wholesale cash lot."))
    H("SEBI made clearing of OTC corporate bond trades through exchange CCs compulsory in:",
      "2009", "Reporting 2007; debt segment 2013.",
      ("2007", "Reporting platforms."),
      ("2013", "Debt segment."),
      ("2015", "NSE negotiated platform."))
    H("The trading facility using UPI block in the cash segment is offered by:",
      "Qualified Stock Brokers (from 1 Feb 2025)", "Or 3-in-1 account.",
      ("All mutual funds", "No."),
      ("RBI Retail Direct", "No."),
      ("Depositories", "No."))
    H("Which describes the SLB reverse leg?",
      "Borrower returns the security to the lender", "First leg: lender delivers.",
      ("Lender delivers to borrower", "First leg."),
      ("CC sells the security", "No."),
      ("Fee is refunded", "No."))
    H("Which is NOT a strategy SLBM enables?",
      "Guaranteed capital protection", "Enables short-selling, reverse cash-and-carry, pairs trading.",
      ("Short-selling", "Enabled."),
      ("Reverse cash-and-carry arbitrage", "Enabled."),
      ("Pairs trading", "Enabled."))
