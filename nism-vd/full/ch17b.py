from summary_lib import *

def add(chap, sub):
    sub("Short strangle", 4,
      F("Sell OTM 6,200 call @ 145 + OTM 6,000 put @ 140 → max profit 285 between 6,000 and 6,200\nBEPs 5,715 and 6,485; loss unlimited beyond either") +
      K("Outlook: price stays stable (like short straddle)"))
    sub("Covered call", 5,
      F("Buy stock 1,590 + sell 1,600 call @ 10\nExpiry 1,640: stock +50, call −30 → +20 (max profit = 1,600 − 1,590 + 10 = 20)\nExpiry 1,520: stock −70, call +10 → −60 ; BEP 1,580") +
      L("Generates income on existing holdings, lowers acquisition cost",
        "Payoff = <b>synthetic short put</b> (capped upside, large downside)",
        "Arbitrage: if 1,600 put trades at ₹17 (≠ ₹20 implied) → covered call + buy put = ₹3 risk-free (before frictions)",
        "Strike choice: near spot → more premium but gains capped early; far → less premium, longer ride",
        "Sell calls at your target exit price; when reached, sell stock and cover the call") +
      PO(payoff("Covered call","5,65 60,25 115,25","= short put shape")))
    sub("Collar", 5,
      F("Long stock 1,590 + short 1,600 call @ 10 + long 1,580 put @ 7\nExpiry 1,490: −100 + 10 + 83 = −7 (covered call alone: −90)\nExpiry 1,690: +100 − 80 − 7 = +13 (covered call alone: +20)\nMax loss 7, max profit 13") +
      K("Extension of covered call: own stock + buy OTM put below price + sell OTM call above price","Call premium offsets put cost","Put lowers downside but also cuts max profit; BEP rises by put premium") +
      PO(payoff("Collar","5,48 40,48 80,22 115,22","Floor −7, cap +13")))
    sub("Butterfly spread", 5,
      F("Long call butterfly: buy 6,000 call @ 230, sell 2 × 6,100 calls @ 150, buy 6,200 call @ 100\nNet cost = −230 + 150 + 150 − 100 = −30 (max loss, ≤ 6,000 or ≥ 6,200)\nMax profit at 6,100 = 100 − 30 = 70\nLower BEP = 6,000 + 30 = 6,030 ; upper BEP = 6,200 − 30 = 6,170") +
      L("Extension of <b>short straddle</b> — buy OTM call and OTM put to cap losses",
        "Long call butterfly: neutral, expects very low volatility; bull spread + bear spread; buy 1 ITM, sell 2 ATM, buy 1 OTM, strikes equidistant",
        "Risk = net premium paid; profit = adjacent strike gap − net debit",
        "With puts: buy highest, sell 2 middle, buy lowest; with calls + puts: buy low call, sell middle call, buy high put, sell middle put — limited profit &amp; loss") +
      T(["Strategy","Construction","View"],
        [["Long put butterfly","1 long ITM put, 2 short ATM puts, 1 long OTM put","Neutral/stable"],
         ["Short call butterfly","1 short ITM call, 2 long ATM calls, 1 short OTM call","Significant volatility"],
         ["Short put butterfly","1 short ITM put, 2 long ATM puts, 1 short OTM put","Significant volatility"],
         ["Iron butterfly","Short ATM call + short ATM put + long OTM call + long OTM put","Neutral/stable"]]) +
      PO(payoff("Long call butterfly","5,45 35,45 60,15 85,45 115,45","Max profit 70 at 6,100")))
    sub("Hedging with options; protective put", 5,
      L("Buying a call = insurance against a surprise rally in a stock you plan to buy (stock 463, buy 460 call @ 19; if 520, call gain offsets; if 430, buy in market)",
        "Buying a put protects a holding against unexpected falls",
        "Fund manager fearing a fall: selling portfolio or shorting futures gives up upside → buy puts instead (insurance)") +
      F("Protective put: buy stock 1,600 + buy 1,600 put @ 20\nExpiry 1,530: −70 + 50 = −20 (loss capped at premium)\nExpiry 1,660: +60 − 20 = +40 ; BEP 1,620") +
      K("Payoff = <b>synthetic long call</b> (limited loss, unlimited gain)") +
      PO(payoff("Protective put","5,45 60,45 115,5","= long call shape")))
    sub("Put-call parity arbitrage", 5,
      F("c + X·e^(−rt) = p + S0      (European options, same strike and expiry)\nStock 1,251; 1,240 call (1 month) 47.50; r 8% → fair put = 28.26\nPut trades 23.15 (underpriced) → buy put + buy stock, short call → outflow 1,226.65 borrowed at 8%\nRepay 1,226.65 × e^(0.08/12) = 1,234.86\nExpiry 1,275: 1,275 − 35 (call) − 1,234.86 = +5.14 ; Expiry 1,200: 1,200 + 40 (put) − 1,234.86 = +5.14\nGain = fair − traded put price") +
      K("Hard to execute: three simultaneous legs; one leg failing → naked exposure",
        "Synthetic long futures = buy ATM call + sell ATM put (same expiry) → compare with actual futures",
        "Synthetic short put = covered call → compare with actual put","Costs (transaction, impact, margin, borrowing) ignored in examples"))
    sub("Delta hedging", 5,
      F("Stock 100; short 10 ATM calls, lot 50, delta 0.50\n₹1 rise → loss 0.50 × 50 × 10 = ₹250\nFutures delta ≈ 1 → long 5 futures lots (1 × 5 × 50 = +250) vs calls −0.5 × 10 × 50 = −250 → delta-neutral\nStock → 110, call delta → 0.60 → need 6 lots") +
      K("Delta-neutral only for small moves","Delta changes with price → keep adjusting = 'delta hedging'"))
    sub("Open interest & delta-adjusted OI", 5,
      L("OI = positions opened and not closed (May index futures OI 2,56,000)",
        "<b>New OI (SEBI 29 May 2025)</b>: portfolio-level net <b>delta-adjusted</b> open positions across futures and options — Future Equivalent OI (FutEq OI)") +
      T(["Position","Delta"],
        [["Long futures","+1"],["Short futures","−1"],["Long call","0 to +1"],["Short call","0 to −1"],["Long put","0 to −1"],["Short put","0 to +1"]]) +
      F("Client 2 long 500 calls, δ 0.5 → FutEq OI 250 (notional 500)\nMarket-wide example: notional OI 2,800 → FutEq OI 900") +
      T(["Futures price","OI","Signal"],
        [["↑","↑","Bullish — go long"],["↑","↓","Short covering"],["↓","↑","Short build-up, bearish — go short"],["↓","↓","Long positions squared up"]]))
    sub("Put-call ratio (PCR)", 5,
      F("PCR = put volume (or OI) ÷ call volume (or OI)\nPut OI 8,000, call OI 12,000 → PCR = 0.67") +
      L("Generally a <b>contrarian</b> indicator",
        "PCR &lt; 1: more calls written → sellers don't expect rise → bearish signal; PCR &gt; 1 (e.g. 1.25): bullish signal",
        "Very high PCR → oversold → possible rebound (consider buying calls); very low PCR → overbought → possible fall (consider buying puts)",
        "Limitations: weigh other factors; use with other indicators; read the chart correctly"))
    sub("Rollover", 4,
      F("Roll cost = (Next series price − Current series price) ÷ Current series price × 100") +
      L("Carry position to next expiry: close current, open next; expressed as % of positions; compared with trailing 3-month average",
        "Lower-than-average rollover → uncertainty; higher → strong sentiment",
        "May→June index rollover 70% vs 65% average → conviction — but check OI base",
        "High rollover + rising cost of carry (premium over spot) → bullish; high rollover + falling carry → bearish",
        "Price ↑ + higher rollover → strength continues; price ↓ + higher rollover → weakness continues; price ↑ + lower rollover → strength fading; price ↓ + lower rollover → weakness easing / bottoming"))
    sub("Volatility index (India VIX)", 5,
      L("Market's expectation of near-term volatility ('rate and magnitude of price changes')",
        "'VIX' is a trademark of <b>CBOE</b>, first volatility index in <b>1993</b>",
        "India VIX by NSE from best bid-ask of near and next-month <b>NIFTY 50 options</b>; shows volatility over next <b>30 calendar days</b>",
        "Higher VIX = more expected volatility; options more valuable for buyers when volatility rises",
        "Trade volatility via straddles/strangles (expensive); no India VIX futures currently",
        "India VIX and NIFTY 50: <b>negative correlation</b>",
        "VIX peaks → managers raise high-beta exposure; low VIX → low-beta stocks (as stated in workbook)",
        "VIX, rollover, PCR, OI = sentiment indicators, no guarantee"))
    sub("Workbook sample answers", 3,
      K("Buy lower-strike call + sell higher-strike call = bullish spread","Hedged position = protective put","Put-call parity: call &amp; put on same stock, same strike, same maturity","Bullish: rising futures price + rising OI"))
