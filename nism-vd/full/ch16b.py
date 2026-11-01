from summary_lib import *

def add(chap, sub):
    sub("Futures vs options — full comparison", 5,
      T(["Futures","Options"],
        [["Buyer and seller both obliged","Buyer has right, no obligation; seller obliged if exercised"],
         ["Both pay initial margin","Buyer pays premium to seller; <b>seller deposits initial margin</b>"],
         ["Both: unlimited gains or losses","Buyer: unlimited gain, loss limited to premium; seller: unlimited loss, gain limited to premium"],
         ["Both pay/receive daily MTM","<b>Only option seller</b> subject to daily MTM margins"]]))
    sub("Five factors that determine option price", 5,
      L("Prices are never fixed by exchanges or SEBI — price discovery by market",
        "Unexpired option always has time value; intrinsic value only if ITM",
        "Time value depends on time to expiry and volatility") +
      T(["Factor","Change","Call","Put"],
        [["Spot price","↑","↑","↓"],["Spot price","↓","↓","↑"],["Strike price","↑","↓","↑"],["Strike price","↓","↑","↓"],
         ["Volatility","↑","↑","↑"],["Volatility","↓","↓","↓"],["Time to expiry","Longer","↑","↑"],["Time to expiry","Shorter","↓","↓"],
         ["Interest rates","↑","↑","↓"],["Interest rates","↓","↓","↑"]]) +
      K("Index 17,562: 17,600 call &gt; 17,700 call; 17,700 put &gt; 17,600 put","Volatility = magnitude of moves either way — same effect on calls and puts",
        "3-month option &gt; 1-month (same strike)","<b>Time decay</b> — options are 'wasting assets'; sellers have a structural advantage",
        "Interest rates matter more for stock/index options than options on futures"))
    sub("Option Greeks", 5,
      T(["Greek","Formula","Key points"],
        [["Delta (δ, Δ)","Δ premium ÷ unit Δ underlying","Most important; long call +, short call −; long put −, short put +; 0.60 → ₹1 move = 60 paise; used in margining; = <b>hedge ratio</b>: n shares ÷ delta = calls to write for a <b>delta-neutral</b> hedge"],
         ["Gamma (γ)","Δ delta ÷ unit Δ underlying","Second derivative; 'acceleration' of delta; positive; call δ 0.50, γ 0.08 → +₹1 → δ 0.58"],
         ["Theta (θ)","Δ premium ÷ Δ time to expiry","Time decay per day; call with 5 days, θ 1.2 → loses ₹1.20/day; usually negative for long call &amp; put"],
         ["Vega (ν)","Δ premium ÷ Δ volatility","Per 1% change in implied volatility; vega 0.80 → 0.80% per 1% IV change; positive for long call &amp; long put"],
         ["Rho (ρ)","Δ premium ÷ Δ cost of funding","Per 1 percentage point in risk-free rate; calls +, puts −; put ₹0.50, ρ −0.05, rates 5% → 4% → ₹0.55; call ₹0.25 → ₹0.20"]]) +
      F("ATM put δ −0.50, γ 0.004\nUnderlying +10 → Δδ = 0.004 × 10 = +0.04 → new δ −0.46 (put loses delta)\nUnderlying −10 → Δδ = −0.04 → new δ −0.54 (put gains delta)"))
    sub("Option pricing models", 5,
      T(["Model","Points"],
        [["Binomial","William Sharpe, <b>1978</b>; binomial tree of up/down moves at equal time steps with probabilities; flexible, intuitive, very accurate (iterative) but complex and slow"],
         ["Black &amp; Scholes","Fisher Black &amp; Myron Scholes, <b>1973</b>; popular, simple, fast — no iteration"]]) +
      K("B-S assumptions: European options only · lognormal prices (random walk / geometric Brownian motion, never negative) · constant known volatility · constant known risk-free rate · no dividends (adjustable) · no transaction costs or taxes · continuous trading, perfect liquidity · short selling with full use of proceeds · no arbitrage") +
      F("C = S·N(d1) − X·e^(−rt)·N(d2)\nP = X·e^(−rt)·N(−d2) − S·N(−d1)\nd1 = [ln(S/X) + (r + v²/2)t] ÷ (v√t)     d2 = d1 − v√t\nS stock, X strike, t years, r continuous risk-free rate, v annual volatility, N(x) standard normal CDF"))
    sub("Implied volatility", 5,
      L("<b>Historical volatility</b>: SD of past % price changes (e.g. weekly Nifty changes over a year)",
        "Traders want expected volatility over the option's remaining life",
        "Pharma example: historical 15%, court verdict next week → expected 70–80%",
        "<b>Implied volatility</b> = volatility backed out by running Black-Scholes in reverse from the market premium (index 17,562, 17,500 call, 9 days, ₹95, rate 6%)",
        "High IV → traders sell options (premiums rich); low IV → buy options",
        "Writers demand higher premiums as safety margin for asymmetric payoff; if risk priced in, even adverse verdict may not hurt writers"))
    sub("Choosing ITM / ATM / OTM", 4,
      K("Deep ITM: high intrinsic value → highest premium","ATM/OTM: only time value → cheaper","ATM: highest uncertainty — small move tips it ITM or OTM"))
    sub("Call buyer & seller analysis (index 17,562)", 5,
      T(["Strike","17,300","17,400","17,500","17,600"],
        [["Premium","327","250","185","130"],["BEP","17,627","17,650","17,685","17,730"],
         ["Buyer P&amp;L at 17,000","−327","−250","−185","−130"],["Buyer P&amp;L at 17,800","+173","+150","+115","+70"],
         ["Buyer ROI at 17,800","53%","60%","62%","54%"],["Seller P&amp;L at 18,000","−373","−350","−315","−270"]]) +
      K("17,300 call: IV 262, TV 65; 17,600 call: all time value","Below 17,300 all calls worthless — biggest loss on 17,300","Call seller: neutral-to-bearish; gains premium below strike"))
    sub("Put buyer & seller analysis (index 17,562)", 5,
      T(["Strike","17,300","17,400","17,500","17,600"],
        [["Premium","65","91","121","167"],["BEP","17,235","17,309","17,379","17,433"],
         ["Buyer P&amp;L at 17,000","+235","+309","+379","+433"],["Buyer ROI at 17,000","362%","340%","313%","259%"],
         ["Seller P&amp;L at 18,000","+65","+91","+121","+167"]]) +
      K("17,600 put ITM: IV 38, TV 129; others pure time value","<b>Deep OTM put buyer gets highest ROI if index falls sharply</b>",
        "Put seller: neutral-to-bullish; selling deep ITM puts = higher premium but higher risk; deep OTM = less risk, less premium"))
    sub("Workbook sample answers", 4,
      F("Short put strike 245, premium 49 → max loss = 245 − 49 = ₹196\nStock 286, 260 call at 45 → intrinsic value = 26\nOption buyer can't lose more than premium → true for ALL options\nEuropean call 'on or before' expiry → FALSE (only on expiry, at strike not market price)\nITM option = positive intrinsic value"))
