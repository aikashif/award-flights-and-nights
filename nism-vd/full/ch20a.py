from summary_lib import *

def add(chap, sub):
    chap(20, "Exchange Traded Interest Rate Futures", "10", 5)
    sub("Futures basics", 4,
      L("Futures fix the limits of forwards: standardised, exchange-traded, clearing corporation guarantees",
        "Buyer = long, seller = short; 'buy/sell' figurative — no money or asset changes hands at trade",
        "Exchange sets every term except price") +
      K("Two parties via exchange · centralised platform · price discovery · <b>margins from both sides</b> · expiry fixed · lot size fixed"))
    sub("History of IRF in India", 5,
      T(["Year","Attempt","Result"],
        [["Jun 2003","91-day T-bill, 6% 10Y notional bond, zero-coupon 10Y notional bond futures","Failed, withdrawn"],
         ["Aug 2009","Notional 7% 10Y GOI bond futures — <b>cheapest-to-deliver</b>, physical","Not adopted"],
         ["Mar 2011","91-day T-bill futures; then 2Y and 5Y bond futures","Limited"],
         ["Dec 2013","<b>Cash-settled single-bond futures on on-the-run 10-yr GOI</b> (SEBI + RBI)","Success"],
         ["Jun 2015","6-year and 13-year GOI futures permitted",""],
         ["10 Jan 2023","SEBI: futures on <b>corporate bond indices</b>",""]]) +
      K("Pre-Dec 2013 failures: cheapest-to-deliver, physical settlement, zero-coupon yield curve","IRDs took off only on the <b>third attempt, 2014</b>; OTC OIS very successful","Exchange derivatives more successful in equity &amp; currency than rates"))
    sub("Futures terminology", 5,
      T(["Term","Meaning"],
        [["Underlying","Rate (overnight MIBOR), G-sec, index (8–13 yr G-sec, corporate bond index) or notional security (10Y)"],
         ["Quantity freeze","Max lots per single order — prevents fat-finger errors"],
         ["Contract cycle","Monthly (near, mid, far), quarterly, some weekly; up to 1 yr; single-bond G-sec: 3 serial monthly + 3 quarterly (Mar/Jun/Sep/Dec)"],
         ["Expiry","Last trading day; single-bond G-sec: <b>last Thursday</b>; holiday → previous trading day"],
         ["Tick size","₹0.0025 for single-bond futures (99.9975, 100.0000, 100.0025)"],
         ["Contract value","Price × lot size"],
         ["Base price","Day 1 = theoretical futures price; later = daily settlement price"],
         ["Price band","± % of base; where none, dummy operating range relaxed in direction of move"],
         ["MTM","Daily vs settlement price; losers pay, gainers receive"],
         ["Daily settlement price","VWAP of last <b>30 minutes</b>; else theoretical"],
         ["Final settlement price","From underlying market; cash (P&amp;L only) or physical delivery"],
         ["Open interest","Contracts outstanding; count one side only (longs = shorts); shows depth"]]))
    sub("Positions & rollover", 4,
      L("Long = outstanding buy; short = outstanding sell; open position = all unsettled longs/shorts",
        "Opening increases open position; closing reduces it (sell what you bought / buy what you sold)",
        "Example: short 5 bond futures + long 3 T-bill futures; next day sell 2 T-bill → short 5 + long 1",
        "Rollover = close current month + open next month; % of positions; compared with trailing 3-month average; low → uncertainty, high → strong sentiment") +
      K("All open positions MTM'd · square off by opposite trade · trader alone responsible for margins · <b>zero-sum</b> · unlimited profit and loss"))
    sub("Futures payoffs", 5,
      F("Long at ₹100: expiry 101 → +1 ; 99 → −1 ; 98 → −2 ; 102 → +2\nShort at ₹100: expiry 99 → +1 ; 101 → −1\nCash-settled → only P&amp;L paid/received") +
      K("Linear, symmetrical payoff; X-axis = price at expiry (never below 0), Y-axis = P&amp;L") +
      PO(payoff("Long futures","5,65 115,5","Gains as price rises"), payoff("Short futures","5,5 115,65","Gains as price falls")))
    sub("Cash-settled GOI bond futures (6/10/13-yr) specs", 5,
      T(["Spec","Rule"],
        [["Underlying","Single GOI dated security, residual maturity <b>4–8 / 8–11 / 11–15 years</b>; chosen by exchanges with FIMMDA (e.g. 6.33% GS 2035)"],
         ["Lot","FV <b>₹2 lakh</b> = 2,000 bonds"],["Quote","Clean price per ₹100 FV"],["Contract value","Price × 2,000"],["Tick","₹0.0025"],
         ["Price band","±3% of base; may widen by 0.5% after 30 minutes, max 2 times a day"],
         ["Hours","Mon–Fri <b>9:00 am – 5:00 pm</b> (aligned with NDS-OM)"],
         ["Cycle","3 serial monthly + 3 quarterly (Mar/Jun/Sep/Dec)"],["Expiry","Last Thursday (holiday → previous day)"],["Settlement","Cash"],
         ["Final settlement price","Weighted average price on NDS-OM in <b>last 2 hours</b>; &lt; 5 trades → FIMMDA/FBIL price"],
         ["Daily settlement price","VWAP of last half hour across exchanges, or theoretical"],
         ["MTM &amp; final settlement","T+1"]]) +
      K("FBIL = independent benchmark administrator for interest rates and FX"))
    sub("91-day T-bill futures specs", 5,
      T(["Spec","Rule"],
        [["Underlying","91-day GOI T-bill"],["Lot","2,000 units (FV ₹2 lakh)"],["Quote","<b>100 − futures discount yield</b> (5% → 95.0000)"],
         ["Contract value","2,000 × (100 − 0.25 × y)"],["Tick","₹0.0025"],["Price band","±1% of base"],["Hours","9:00 am – 5:00 pm"],
         ["Cycle","3 serial monthly + 3 quarterly"],["Expiry","<b>Last Wednesday, 1:00 pm</b> (holiday → previous working day)"],
         ["Daily settlement","2,000 × (100 − 0.25 × Yw), Yw = weighted futures yield last half hour"],
         ["Final settlement","2,000 × (100 − 0.25 × y), y = weighted average discount yield of RBI's 91-day T-bill auction on expiry day"],
         ["Settlement","Cash; T+1"]]))
    sub("Overnight MIBOR futures specs", 5,
      T(["Spec","Rule"],
        [["Underlying","Daily FBIL overnight MIBOR for contract month"],
         ["Unit","Interest on ₹5 crore notional for one month, 30/365 basis, at average daily MIBOR"],
         ["Quote","Interest rate"],["Base rate","Day 1: MIBOR OIS rate of matching tenor; later: daily settlement rate"],
         ["Contract value","Rate × 100 × 411 (1 bp = 5 cr × 0.01% × 30/365 = <b>₹411</b>)"],
         ["Tick","0.25 bp (0.0025) = <b>₹102.75</b>"],["Hours","9:00 am – 5:00 pm; expiry day 9:00 – 10:00 am"],
         ["Cycle","3 serial monthly + 3 quarterly"],["Expiry","<b>Last working day</b> of month"],
         ["Daily settlement","VWAP last 30 min (min 5 trades), else last 60 min (min 5 trades), else theoretical"],
         ["Final settlement","Simple average of daily FBIL overnight MIBOR for the month (4 decimals)"],["Settlement","Cash in INR; T+1"]]))
    sub("Other / earlier IRF designs", 4,
      T(["Contract","Key features"],
        [["10Y notional 7% GOI — physical","Lot ₹2 lakh; 4 quarterly contracts; expiry <b>7th business day before last business day</b> of delivery month; deliverable GOI 7.5–15 yrs with ≥ ₹10,000 cr outstanding; conversion factor = price to yield 7%; last delivery = last business day"],
         ["10Y notional GOI — cash","Basket of GOI with 8–11 yrs residual; coupon set by exchange; 3 serial monthly + quarterly; last Thursday; FSP = weighted average yield of basket (NDS-OM last 2 hrs; &lt; 5 trades → FIMMDA/FBIL); 6-yr and 13-yr versions possible"],
         ["2Y / 5Y notional 7% GOI","Semi-annual coupon, FV ₹100; lot ₹2 lakh; 3 serial monthly; last Thursday; cash; FSP from yields polled by <b>FIMMDA</b>; basket 1.5–2.5 yrs / 4.5–5.5 yrs"]]))
    sub("Corporate bond index futures (CBIF)", 5,
      L("SEBI <b>10 Jan 2023</b>: derivatives on indices of corporate debt rated <b>AA+ and above</b>") +
      T(["Index rule","Limit"],
        [["Single issuer weight","≤ <b>15%</b>"],["Minimum issuers","<b>8</b>"],["Group weight","≤ 25% (excl. PSU, PFI, PSB)"],["Sector weight","≤ 25% (excl. PSU, PFI, PSB)"],
         ["Review","At least half-yearly"],["Track record","≥ 1 year"],["Exposure","Aggregated at issuer level"],["Duration buckets","Set by exchanges"]]) +
      T(["Contract rule","Detail"],
        [["Contract value","≥ <b>₹2 lakh</b> at launch; reviewed half-yearly"],["Hours","9:00 am – 5:00 pm"],["Tenure","Up to <b>3 years</b>"],
         ["Cycle","Weekly, 3 serial monthly, 1 quarterly or 1 half-yearly (Jun/Dec)"],["Quote / tick","INR; tick set by exchange"],
         ["Expiry","Last Thursday of cycle"],["Daily settlement","Last half-hour VWAP, else theoretical (method on website)"],
         ["Final settlement","Closing index value on expiry"],["Settlement","Cash; MTM and final next working day"]]))
