from summary_lib import *

def add(chap, sub):
    sub("Reading the order book (worked)", 5,
      T(["Buy qty","Bid","Ask","Sell qty"],
        [["4","131.95","132.05","1,437"],["8,169","131.90","132.10","4,046"],["6,180","131.85","132.15","4,885"],["6,698","131.80","132.20","10,997"],["9,201","131.75","132.25","32,151"]]) +
      K("Highest bid on top (picked first); lowest ask on top","Bid-ask now <b>131.95 – 132.05</b>; trade needs a higher bid or lower ask",
        "Buy limit at 131 or sell at 132 unlikely to match","Unmatched order stays till day end or cancellation",
        "Trade confirmation slip: trade no., price, quantity, time, order no.; a market order may fill at several prices"))
    sub("Active vs passive orders; DMA", 5,
      T(["","Active","Passive"],
        [["What","At market price; match at once (market orders)","Rest in book away from market (limit orders); LTP 105.10 → buy 102.45 / sell 107.70"],
         ["Liquidity","<b>Drains</b> — 'reactive'","<b>Adds</b> depth — 'proactive'"]]) +
      L("<b>Direct Market Access</b> since <b>2008</b> for institutional clients: orders go straight to exchange book, bypassing broker server (after broker authorisation, due diligence, KYC)",
        "Benefits: lower latency, faster execution, fewer manual errors, lower cost"))
    sub("Bulk deals vs block deals", 5,
      T(["","Bulk deal","Block deal"],
        [["Size","&gt; <b>0.50%</b> of listed shares (one or many trades in a day)","Min <b>₹25 crore</b>, single transaction"],
         ["Window","Normal market, visible to all","Special window: <b>8:45–9:00 am</b> and <b>2:05–2:20 pm</b>; not visible in normal window"],
         ["Price","Market","Within ±<b>3%</b> of reference: morning = previous close; afternoon = VWAP 1:45–2:00 pm"],
         ["Reporting","Broker reports immediately; exchange discloses same day after hours","Disclosed same day after hours"],
         ["Settlement","Normal","<b>Delivery only</b>, no square-off or reversal"]]) +
      K("Block deals are negotiated outside, executed on exchange to avoid moving the price and keep confidentiality (block deal framework reviewed 8 Oct 2025)"))
    sub("Circuit breakers & price bands", 5,
      L("Automatic trading halt on rapid move in index or stock — time to reassess, avoid panic and settlement crises",
        "Stock price bands: <b>2%, 5%, 10% or 20%</b> by liquidity, volatility; exchange may narrow",
        "F&amp;O stocks have <b>no price band</b> (operating range against errors); index stocks without derivatives get suitable bands",
        "Market-wide breaker: Sensex <b>or</b> Nifty 50, whichever first; halts equity and equity derivatives; limits from previous close; reopens with pre-open call auction") +
      T(["Index move","When","Halt","Pre-open after"],
        [["10%","Before 1 pm","45 min","15 min"],["10%","1:00 – 2:30 pm","15 min","15 min"],["10%","After 2:30 pm","No halt","—"],
         ["15%","Before 1 pm","1 hr 45 min","15 min"],["15%","1:00 – 2:00 pm","45 min","15 min"],["15%","2 pm or later","Rest of day","—"],
         ["20%","Any time","Rest of day","—"]]))
    sub("Contract note", 5,
      L("Confirmation of the day's trades; proof in disputes; shows trade, settlement, brokerage, STT, GST",
        "Valid if: signed by authorised signatory · SEBI/exchange format · client UCC &amp; PAN · broker name, address, SEBI reg. no. · order no., trade no., time, security, qty, price, brokerage, settlement no., STT, GST, penalties · trade price and charges shown separately · <b>arbitration clause</b>",
        "Issued within <b>24 hours</b>; two copies — client signs and returns broker's copy",
        "<b>ECN</b> by email only with client consent; digitally signed, tamper-proof, password-protected; also on broker website",
        "Client checks against trade confirmation slip; reports discrepancies"))
    sub("Cost of trading — user charges & statutory levies", 5,
      L("Three types: <b>user charges</b> (brokerage, exchange transaction charges, DP charges) · <b>statutory levies</b> · <b>spread &amp; impact cost</b>",
        "Max brokerage set by exchange regulations; intraday cheaper than delivery; big clients negotiate") +
      T(["STT — equity segment","Rate","Paid by"],
        [["Delivery purchase of equity share","0.100%","Buyer"],["Delivery sale of equity share","0.100%","Seller"],
         ["Delivery sale of equity fund unit","0.001%","Seller"],["Non-delivery (intraday) sale of share / equity fund / business trust unit","0.025%","Seller"]]) +
      T(["STT — derivatives","Rate","Paid by"],
        [["Sale of option","0.15% of premium","Seller"],["Option exercised","0.15% of intrinsic value","Buyer"],["Sale of futures","0.05% of traded price","Seller"]]) +
      K("GST <b>18% on brokerage</b>; STT and GST go to <b>Central Govt</b>",
        "Stamp duty: uniform national rates (from 1 Jul 2020); collected for <b>state govts</b> by exchanges/CCs/depositories (also CCIL, RTAs), who keep a small share",
        "SEBI turnover fee: <b>0.0001%</b> (₹10 per crore) non-debt; <b>0.000025%</b> (₹2.5 per crore) debt"))
    sub("Bid-ask spread & impact cost (worked)", 5,
      T(["Buy qty","Bid","Ask","Sell qty"],[["1,000","350","400","2,000"],["1,000","340","405","1,000"],["2,000","340","420","500"],["1,000","330","425","100"]]) +
      F("Buy 1,000 at 400, sell at 350 → spread ₹50\nIdeal price = (350 + 400) ÷ 2 = 375\nImpact cost = 25 ÷ 375 = <b>6.67%</b>") +
      K("Illiquid → wider spread","Lower impact cost = more liquid, cheaper (BSE June 2019: Cipla 0.03%, Bank of India 0.05%, SKF 0.12%, Reliance Power 0.15%)"))
    sub("Total trading cost (worked, ₹1 lakh)", 4,
      T(["Item","Rate","₹"],
        [["Brokerage","0.3%","300"],["DP charges","0.02%","20"],["STT","0.1%","100"],["GST","18% of brokerage","54"],["Stamp duty","0.015%","15"],["SEBI turnover tax","0.0001%","0.10"],["<b>Total</b>","<b>0.4891%</b>","<b>489.10</b>"]]) +
      K("Institutions usually pay less brokerage; rates differ for equity, debt, derivatives","Some exchange/regulator charges are borne by brokers"))
    sub("Delivery vs square-off; T+1", 5,
      L("Rolling settlement: trades of day T settled on <b>T+1</b> = delivery trades ('inter-day')",
        "T+1 phased from <b>Feb 2022</b>; all equity, ETFs, bonds in equity segment on T+1 since <b>27 Jan 2023</b>",
        "Square-off: buy and sell same stock same day (or sell then buy back) → net nil = <b>intraday / day trading</b>; lower brokerage and levies"))
    sub("Settlement obligations & netting", 5,
      L("Settlement cycle = T to completion; each has a settlement number",
        "Institutions, FPIs, NRIs, PMS clients settle through <b>custodians</b>",
        "Netting at client level, then member level across all securities") +
      T(["Trades in cycle","Net result"],
        [["Buy 100, sell 50 XYZ","Receive 50 XYZ, pay"],["Buy 100 MNO","Receive 100 MNO, pay"],["Buy 50, sell 150 DEF","Deliver 100 DEF, receive funds"]]) +
      K("Only net positions settled = <b>net settlement</b> (vs gross)",
        "Steps: obligation identified &amp; confirmed → <b>pay-in</b> (securities/funds to CC) → <b>pay-out</b> (CC to members)",
        "Not delivered → <b>auction</b>; delivered but rejected by depository (wrong signature/details) = <b>bad delivery</b>"))
    sub("Margins in the cash market", 5,
      F("Buy 100 X at ₹100 on 3 Jul → pay ₹10,000 by 4 Jul; margin 17% → ₹1,700 upfront\nPrice falls to ₹80 same day → notional loss ₹2,000 → default temptation") +
      T(["Margin","Rule"],
        [["VaR margin","Multiple of volatility, % of price; updated ≥ <b>5 times</b> a day"],["Extreme Loss Margin","<b>3.5%</b> for any stock"],
         ["Mark-to-market","Transaction vs closing price; payable at start of next day"]]) +
      K("Both buyers and sellers pay margin; brokers collect at order, exchanges at execution","More volatile stock → higher margin",
        "Upfront VaR + ELM collection mandatory; no short-collection penalty if broker collects ≥ <b>20%</b> upfront"))
    sub("Cross-margining", 5,
      L("Lower margin when cash and derivatives positions offset (long MNO shares + short MNO futures)",
        "Spread margin = <b>25%</b> of applicable upfront margin on offsetting positions; normal margin on the rest",
        "Highly correlated equity indices: spread margin <b>30%</b>",
        "Benefit = margin on total portfolio − margin excluding offsets − spread margin") +
      K("Eligible: index futures vs constituent stock futures · index futures vs constituent cash stocks · cash stock vs its futures · ETF vs constituents · ETF vs constituent futures · ETF vs index futures",
        "Helps arbitrageurs and hedgers"))
    sub("Short delivery & funds shortage", 4,
      L("Short delivery or bad delivery → CC <b>auctions</b> shares for buyer; member pays shortage × last closing price on settlement day + any auction difference",
        "Funds shortage → penal charge daily until paid; trading/clearing facility withdrawn; repeat defaulters keep 'funds shortage collateral'"))
    sub("Corporate actions & price adjustment", 5,
      L("Stock benefits: bonus, rights, split, merger, warrants; cash benefit: dividend",
        "<b>Record date</b>: holders on record get the benefit (1:1 bonus → one extra share each)",
        "<b>Cum</b> = price includes benefit; <b>ex</b> = buyer no longer gets it (price drops by dividend)",
        "Exchange adjusts prices after close on last cum day so position value is unchanged") +
      F("Split FV ₹10 → ₹2, price ₹500 → 5 shares at ₹100 each"))
