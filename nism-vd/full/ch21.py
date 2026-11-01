from summary_lib import *

def add(chap, sub):
    chap(21, "Exchange Traded Interest Rate Options", "6", 4)
    sub("Option basics (land example)", 4,
      L("Futures = linear, unlimited P&amp;L; options let buyer ride upside with loss capped",
        "Mr X pays Mr Y ₹50,000 non-refundable (1 Aug 2021) for the right to buy land at ₹10,00,000 in 3 months → <b>call option</b>",
        "Strike ₹10 lakh · expiry 31 Oct 2021 · time to maturity 3 months · premium ₹50,000 · X buyer, Y writer · land = underlying",
        "Land at ₹15 lakh on expiry → X exercises, pays ₹10 lakh",
        "Car insurance = buying a <b>put</b>; insurance premium = option premium") +
      K("Similarities with futures: buyer &amp; seller · set price · set settlement date; used for hedging, views, arbitrage",
        "Difference: option buyer has right only (risk = premium); seller obliged (unlimited risk, gain capped at premium)"))
    sub("Option styles", 5,
      T(["Style","Exercise"],
        [["European","Only on expiry (exchange options can still be sold before expiry)"],["American","Any time on or before expiry"],
         ["Bermudan","On specified days, usually near expiry — between European and American"]]))
    sub("Moneyness; intrinsic & time value", 5,
      T(["","Call","Put"],
        [["ITM (positive cash flow)","Strike &lt; spot","Strike &gt; spot"],["ATM (zero)","Strike = spot","Strike = spot"],["OTM (negative)","Strike &gt; spot","Strike &lt; spot"]]) +
      F("Call IV = max(0, S − X) ; put IV = max(0, X − S) ; never negative\nTime value = premium − intrinsic value") +
      K("Only ITM has intrinsic value","Longer to expiry → more time value (2-month call &gt; 1-month)","At expiry option value = intrinsic value; time value = 0",
        "Exercise decision may include transaction/regulatory charges"))
    sub("Five option price factors", 5,
      T(["Factor","Change","Call","Put"],
        [["Spot","↑","↑","↓"],["Strike","↑","↓","↑"],["Volatility","↑","↑","↑"],["Time to expiry","Longer","↑","↑"],["Interest rate","↑","↑","↓"]]) +
      K("Prices never fixed by exchange or SEBI","Time decay → 'wasting assets'; sellers have a built-in advantage","Rate = risk-free rate"))
    sub("Option Greeks (bond examples)", 5,
      T(["Greek","Measures","Example"],
        [["Delta","Δ premium per unit Δ underlying; long call/short put 0 to 1; long put/short call 0 to −1","6.10% GS 2031 at 98.80, 98.50 call ₹0.45, δ 0.55 → bond 99.00: +0.11 → <b>0.56</b>; bond 98.60: → <b>0.34</b>"],
         ["Gamma","Δ delta per unit Δ underlying; 'acceleration'","ATM put δ −0.50, γ 0.004: +10 → −0.46; −10 → −0.54"],
         ["Theta","Premium lost per day","₹2.75, θ −0.05 → ₹2.70 next day; long option θ negative, short positive — 'friendly Greek to the seller'"],
         ["Vega","Δ premium per 1% Δ volatility; + for long calls and puts; biggest with more days left","Bond 99.50, Nov 100 call ₹0.10, vega 0.02: vol 10→11% → 0.12; 10→8% → 0.06"],
         ["Rho","Δ premium per 1 pp Δ risk-free rate; calls +, puts −","Put ₹0.50, ρ −0.05, rate 5→4% → 0.55; call 0.25 → 0.20"]]))
    sub("Put-call parity", 5,
      F("C + PV(X) = P + S\nHolds only for <b>European</b> options with same underlying, strike and expiry"))
    sub("Option pricing models", 5,
      T(["Model","Points"],
        [["Binomial","William Sharpe <b>1978</b>; up/down tree at equal steps; flexible, intuitive, accurate (iterative) but slow"],
         ["Black-Scholes","Black &amp; Scholes <b>1973</b>; fast, no iteration; European, no dividends; uses <b>spot</b>"],
         ["Black (1976)","For options on futures/forwards; replaces S with F·e^(−rt) — solves negative carry; used for futures options, bond options, caps &amp; floors, swaptions, commodity options; <b>used in India for exchange-traded IROs on G-secs</b>"]]) +
      F("B-S: C = S·N(d1) − X·e^(−rt)·N(d2) ; P = X·e^(−rt)·N(−d2) − S·N(−d1)\nd1 = [ln(S/X) + (r + v²/2)t] ÷ (v√t) ; d2 = d1 − v√t\nBlack: C = e^(−rt)[F·N(d1) − X·N(d2)] ; P = e^(−rt)[X·N(−d2) − F·N(−d1)]\nd1 = [ln(F/X) + (σ²/2)t] ÷ (σ√t) ; d2 = d1 − σ√t") +
      K("Dividends cut stock price → calls worth less, puts more",
        "Short-term options: S − PV(expected dividends); long-term: adjust with constant dividend yield"))
    sub("Implied volatility", 5,
      T(["Volatility","Meaning"],
        [["Historical","From past closing prices; easy; used in calculators"],["Forecasted","Predicted with statistical models"],
         ["Implied (σ)","Market consensus expectation, backed out from premium; only model input not directly observable"]]) +
      K("IV shows size of move, not direction","IV usually rises in bearish markets, falls in bullish ones","No traded options → no IV",
        "IV ↑ after trade → good for buyer, bad for seller; IV ↓ → good for seller"))
    sub("Long & short call on G-sec (worked)", 5,
      F("6.10% GS 2031 at 98.40; buy 98.50 call @ 0.20, expiry 28 Oct 2021\nExpiry 98.25 → lapse, loss 0.20 ; BEP = X + P = <b>98.70</b> ; 98.90 → +0.40 − 0.20 = +0.20\nMax loss per lot = 2,000 × 0.20 = <b>₹400</b>\nShort call: mirror — max gain 0.20, unlimited loss; BEP also 98.70") +
      K("Long call/short call: right vs obligation; seller can be assigned","BEP is instrument-specific, not position-specific",
        "Cash-settled: buyer receives only the gain (0.40)") +
      PO(payoff("Long call","5,45 60,45 115,5","BEP 98.70"), payoff("Short call","5,25 60,25 115,65","Gain capped 0.20")))
    sub("Long & short put on G-sec (worked)", 5,
      F("Buy 98.50 put @ 0.30\nExpiry 98.75 → lapse, loss 0.30 ; BEP = X − P = <b>98.20</b> ; 98.00 → +0.50 − 0.30 = +0.20\nMax loss per lot = 2,000 × 0.30 = <b>₹600</b>\nShort put: max gain 0.30; max loss when price → 0; BEP 98.20") +
      K("Long call = long underlying; <b>long put = short underlying</b>","Options asymmetric; futures symmetric") +
      PO(payoff("Long put","5,5 60,45 115,45","BEP 98.20"), payoff("Short put","5,65 60,25 115,25","Gain capped 0.30")))
    sub("Squaring off an option (worked)", 4,
      F("1 Oct 2021: hedge ₹100 cr G-secs — buy 5,000 lots Oct 6.10% GS 2031 put, strike 101.00, at 0.20/0.21 (pays offer 0.21)\n15 Oct: sells bonds, closes put at 0.10/0.11 (receives bid 0.10)\nWorkbook: paid 5,000 × 0.21 = 1,050 ; received 5,000 × 0.10 = 500 ; net −550") +
      TRAP("The workbook figures leave out the 2,000-unit lot. Per ₹100 of face value the net loss is 0.11; on the whole position it is 5,000 × 2,000 × 0.11 = ₹11 lakh. Buy at the offer, sell at the bid."))
    sub("Exchange-traded IRO specs", 5,
      L("RBI <b>29 Dec 2016</b> introduced IROs; FIMMDA to list eligible underlyings; superseded by Rupee IRD Directions <b>26 Jun 2019</b>",
        "First exchange IROs on single GOI securities: <b>Aug 2019</b>") +
      T(["Spec","Rule"],
        [["Underlying","GOI dated security chosen with FIMMDA (e.g. 6.33% GS 2035)"],["Lot","FV ₹2 lakh = 2,000 bonds"],["Quote","Premium in ₹"],
         ["Contract value","Price × 2,000"],["Tick","₹0.0025"],
         ["Price band","Delta-based, from previous underlying close and volatility; minimum operating range; computed daily, flexed intraday"],
         ["Hours","9:00 am – 5:00 pm"],["Type","Premium-style <b>European</b> call &amp; put"],
         ["Strike interval","<b>₹0.25</b> (99.50, 99.75, 100.00…)"],["Strikes","Min <b>8 ITM, 8 OTM, 1 near-the-money</b>"],
         ["Cycle","3 serial monthly + 3 quarterly"],["Expiry","Last Thursday"],["Settlement","Cash via clearing corporation (guaranteed)"],
         ["Final settlement price","NDS-OM weighted average, last 2 hrs; &lt; 5 trades → FIMMDA/FBIL"],
         ["Daily settlement price","Last half-hour VWAP across exchanges or theoretical"],["Final settlement","T+1"]]))
    sub("Exchange-traded vs OTC IRO", 4,
      T(["","Exchange IRO","OTC IRO"],
        [["Products","Mainly European IROs","European IROs, caps, floors, collars, reverse collars, swaptions, structured products"],
         ["Terms","Standardised","Custom"],["Price discovery","Exchange","Negotiation"],["Liquidity","High","Low"],
         ["Market maker","Not applicable","Scheduled banks, PDs, AIFIs"],["Settlement","Clearing corporation, guaranteed","Bilateral"],
         ["Reporting","Online","Trade repository within 30 minutes"],
         ["Limits","Imperfect hedge; not every product listed","Liquidity, counterparty risk, not open to all"]]))
    sub("Open interest (worked) & PCR", 5,
      T(["Date","Trade","OI","Volume"],
        [["1 Jun","A buys 1, B sells 1","1","1"],["2 Jun","C buys 5, D sells 5","6","6"],["3 Jun","A sells 1, D buys 1 (both close)","5","7"],["4 Jun","E buys 5 from C (C closes)","5","12"]]) +
      T(["Underlying","OI","Reading (Ch 21)"],
        [["↑","↑","Long build-up — bullish"],["↑","↓","End of bullish trend"],["↓","↑","Short build-up — bearish"],["↓","↓","End of bearish trend"]]) +
      L("PCR = put OI ÷ call OI (or volumes)",
        "Ch 21 reading: PCR &gt; 1 → bearish sentiment; &lt; 1 → bullish; equity options average ≈ <b>0.7</b>; falling to ≈ 0.5 → bullish",
        "As contrarian: very high PCR → oversold, rebound (buy calls); very low → overbought, fall (buy puts)",
        "Limits: weigh other factors, use with other indicators, read the chart correctly") +
      TRAP("Ch 17 gives the contrarian reading (PCR &lt; 1 = bearish signal, &gt; 1 = bullish). Ch 21 gives the direct sentiment reading (high PCR = bearish). Match the answer to how the question is worded."))
    sub("Workbook sample answers", 3,
      K("Price paid by buyer = premium","Buyer limited risk, seller unlimited","Negative cash flow on exercise = OTM","Premium − intrinsic = time value",
        "98.50 put @ 0.20, expiry 98.50 → loss ₹0.20"))
