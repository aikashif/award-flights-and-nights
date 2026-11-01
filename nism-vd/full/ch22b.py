from summary_lib import *

def add(chap, sub):
    sub("Vertical spreads on G-sec options", 5,
      T(["Spread","Legs","Net","Max profit","Max loss","BEP"],
        [["Bull call","Long 98.75 call @ 0.45, short 99.50 call @ 0.20","Debit 0.25","0.50 (≥ 99.50)","0.25 (≤ 98.75)","99.00"],
         ["Bull put","Short 99.50 put @ 0.40, long 99.00 put @ 0.10","Credit 0.30","0.30","0.20","99.20"],
         ["Bear call","Short 98.50 call @ 0.60, long 99.25 call @ 0.20","Credit 0.40","0.40","0.35","98.90"],
         ["Bear put","Long 99.50 put @ 0.40, short 99.00 put @ 0.25","Debit 0.15","0.35","0.15","99.35"]]) +
      K("Spreads: same underlying &amp; type, different strikes/expiries; limited profit and loss","Bull = view rates ↓ (bond prices ↑); bear = rates ↑",
        "Bull put = <b>buy lower-strike put, sell higher-strike put</b>; net premium receipt",
        "Horizontal (calendar): same strike, different expiry — play on time-value gap; no payoff chart","Diagonal: different strikes and expiries; complex"))
    sub("Straddles & strangles on G-sec options", 5,
      T(["Strategy","Legs","Max loss / profit","BEPs"],
        [["Long straddle","Buy 99 call @ 0.30 + 99 put @ 0.20","Max loss 0.50 at 99; unlimited profit","98.50 / 99.50"],
         ["Short straddle","Sell both","Max profit 0.50; unlimited loss","98.50 / 99.50"],
         ["Long strangle","Buy OTM 99.25 call @ 0.20 + 98.75 put @ 0.15","Max loss 0.35 between strikes","98.40 / 99.60"],
         ["Short strangle","Sell both","Max profit 0.35; unlimited loss","98.40 / 99.60"]]) +
      K("Long = expects big move either way (rate uncertainty); short = expects stable yields — use with care") +
      PO(payoff("Long straddle","5,5 60,55 115,5","BEPs 98.50 / 99.50"), payoff("Long strangle","5,5 45,50 75,50 115,5","BEPs 98.40 / 99.60")))
    sub("Covered call & protective put on bonds", 5,
      F("Covered call: buy bond 99.50 + sell 100 call @ 0.10 → = <b>synthetic short put</b>, strike 100, premium 0.60\nIf 100 put trades at 0.50 → covered call + buy put = 0.10 risk-free (before costs)\nProtective put: buy bond 99.50 + buy 99.50 put @ 0.20 → loss capped at 0.20, upside open") +
      K("Covered call 'sells volatility' for income; strike near price → more premium, gains capped early","Sell calls at your target exit price",
        "Protective put keeps upside, unlike short futures","Coupons/accrued interest ignored in these examples"))
    sub("Long call butterfly on bonds", 4,
      F("Buy 98.50 call @ 0.60, sell 2 × 99.00 calls @ 0.30, buy 99.50 call @ 0.20\nNet cost = 0.60 − 0.60 + 0.20 = 0.20 debit\nLower BEP 98.70 ; upper BEP 99.30 ; max profit 0.50 − 0.20 = 0.30 at 99.00") +
      K("Neutral, low-volatility view; bull + bear spread; 4 options, 3 strikes, equal gaps","Variants: short call, long/short put, iron butterfly"))
    sub("Speculation with IRF", 5,
      T(["Long view (rates ↓)","Buy bond (₹5 lakh)","Long IRF, 5% margin, ₹1 cr","IRF ₹5 lakh + CD for rest"],
        [["Buy price (2 Mar 2020)","100.70","100.62","100.62"],["Exit (26 Mar)","101.59","101.59","101.59"],
         ["Price gain","₹4,450","₹97,000","₹4,850"],["Accrued interest","₹2,150","Nil","Nil"],["CD return","—","—","₹2,300"],
         ["Total","₹6,600","<b>₹97,000</b>","₹7,150"]]) +
      L("Leverage magnifies losses too; futures earn no accrued interest; buy calls to cap loss",
        "Short view (rates ↑, prices ↓): not everyone may short G-secs → sell bond futures or buy bond puts",
        "Change portfolio duration fast and cheaply: buying bond futures raises duration, selling lowers it") +
      TRAP("The workbook says managers 'lengthen duration when rates are expected to rise'. That is backwards. Expect rates to rise → <b>shorten</b> duration (sell futures). Expect rates to fall → lengthen (buy futures)."))
    sub("Arbitrage with single-bond IRF (worked)", 5,
      T(["","Cash-and-carry","Reverse"],
        [["When","Futures &gt; theoretical","Futures &lt; theoretical"],
         ["Trades","Buy bond 102.60 (repo funded 5%), sell futures 102.62; 500 lots, FV ₹10 cr","Sell bond 102.60, lend in repo 5%, buy futures 102.40"],
         ["Expiry 102.30","AI 4,42,750 + IRF 3,20,000 − bond loss 3,00,000 − funding 2,95,151","Bond gain 3,00,000 + lending 2,95,151 − AI 4,42,750 − IRF loss 1,00,000"],
         ["Expiry 102.80","AI + bond gain 2,00,000 − IRF loss 1,80,000 − funding","IRF gain 4,00,000 + lending − AI − bond loss 2,00,000"],
         ["Net (both cases)","<b>₹1,67,599</b>","<b>₹52,401</b>"]]) +
      K("Synthetic T-bill: long 15-yr bond + short 3-month futures = riskless 3-month security; if its yield &gt; cash T-bill yield → yield enhancement",
        "Risks: execution gap, illiquid leg, settlement type, short-sale rules, costs (brokerage, stamp duty, margin, impact)"))
    sub("Spread trading with IRF", 5,
      F("Calendar: sell Sep 6.10% GS 2031 futures 99.00, buy Oct 99.05 (spread 0.05)\nAfter 10 days: Sep 98.80, Oct 98.95 → spread 0.15 → gain 0.10 × 2,000 = <b>₹200 per contract</b>") +
      K("Calendar spread: only basis risk → lower margins; use exchange spread order to avoid execution risk",
        "Inter-bond spread: long one GOI bond future, short another, same expiry (6.10% 2031 vs 5.85% 2030; or 10-yr vs 5-yr 7.27% 2026) — a play on steepening/flattening"))
    sub("Limits of IRDs for hedgers", 5,
      K("Standardised, cash-settled → imperfect hedge, basis risk","Expiry fixed (last Thursday) vs exposure date","Not available on every instrument/tenor (corporate bonds, floating home loans poorly correlated)",
        "Cash settlement: timing/price gap between closing futures and real trade","Offsets: transparency, small lots, easy execution"))
    sub("Workbook sample answers", 3,
      K("Multi-bond portfolio → duration-based hedge ratio","Bull put spread → buy lower-strike put, sell higher-strike put","Expect rates ↑ → sell GOI bond futures",
        "Buy one month, sell another = calendar spread","Hedger limits → standardised contracts AND not available on all underlyings"))
