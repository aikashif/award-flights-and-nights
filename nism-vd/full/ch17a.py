from summary_lib import *

def add(chap, sub):
    chap(17, "Strategies using Equity Futures & Equity Options", "9", 5)
    sub("Long hedge with stock futures", 5,
      KV([("Purpose","Lock price of a planned future purchase"),
          ("Example","Buy 1,500 ABC shares on 20 Jun (FD matures); spot ₹455 on 10 May; June futures (expiry 29 Jun) ₹457.30, lot 1,500 → long 1 lot")]) +
      T(["Scenario on 20 Jun","Cash cost","Futures P&amp;L","Net cost / share"],
        [["Price ↑ to 520 (futures 521.20)","₹7,80,000","+₹95,850","₹6,84,150 → <b>₹456.10</b>"],
         ["Price ↓ to 390 (futures 391.10)","₹5,85,000","−₹99,300","₹6,84,300 → <b>₹456.20</b>"]]) +
      K("Either way effective price ≈ initial futures price ₹457.30"))
    sub("Short hedge with stock futures", 5,
      KV([("Purpose","Lock price of a planned future sale"),
          ("Example","Sell 1,200 PQR shares on 10 Jul for loan; spot ₹1,690 (10 May), July futures ₹1,706, lot 600 → short 2 lots")]) +
      T(["Scenario on 10 Jul","Cash received","Futures P&amp;L","Net per share"],
        [["Price ↓ to 1,440 (futures 1,441)","₹17,28,000","+₹3,18,000","₹20,46,000 → <b>₹1,705</b>"],
         ["Price ↑ to 1,800 (futures 1,802)","₹21,60,000","−₹1,15,200","₹20,44,800 → <b>₹1,704</b>"]]))
    sub("Hedging a portfolio with index futures", 5,
      L("Diversified 15-stock portfolio → specific risk ≈ 0 but market risk remains",
        "Options: sell entire portfolio and hold cash, or short index futures") +
      F("Hedge ratio = (β × portfolio value) ÷ (futures price × lot)\n= (1.3 × 90,00,000) ÷ (17,700 × 50) = 13.22 → short 13 contracts"))
    sub("Futures for trading: bullish & bearish", 5,
      T(["","Bullish: long XYZ futures","Bearish: short RSB Bank futures"],
        [["View","Stock 1,298 → 1,350","Stock 1,595 → 1,520"],
         ["Position","Futures 1,300, lot 850 → contract ₹11,05,000; margin 20% = ₹2,21,000","Futures 1,602, lot 550 → contract ₹8,81,100; margin 20% = ₹1,76,220"],
         ["Outcome","Futures 1,346 → profit (1,346 − 1,300) × 850 = ₹39,100 → ROI <b>17.69%</b> vs buying shares: ₹39,950 on ₹11,03,300 = 3.62%","Futures 1,527 → (1,602 − 1,527) × 550 = ₹41,250 → ROI <b>23.41%</b>"]]) +
      K("Leverage explains popularity","Shorting futures expresses a bearish view without owning shares (cash sale needs shares in demat)"))
    sub("Cash-and-carry arbitrage (worked)", 5,
      F("Stock A spot ₹1,500; 3-month futures ₹1,550; multiplier 100; carry 9% p.a. (0.75%/month)\nFair = 1,500 × e^(0.09 × 3/12) = 1,534.13 → futures overvalued by 15.87\nBuy 100 shares, sell 1 futures → arbitrage profit = 100 × 15.87 = ₹1,587\nExpiry 1,580: +8,000 − 3,000 = 5,000 − financing 3,413 = ₹1,587\nExpiry 1,480: −2,000 + 7,000 = 5,000 − 3,413 = ₹1,587\nExpiry 1,500: 0 + 5,000 − 3,413 = ₹1,587   (same in every case)"))
    sub("Reverse cash-and-carry arbitrage (worked)", 5,
      F("Stock B spot ₹100; 1-month futures ₹90 (negative carry); multiplier 200\nBuy 1 futures at 90, sell 200 shares at 100 → locked ₹2,000\nExpiry 110: −2,000 + 4,000 = 2,000 ; Expiry 85: +3,000 − 1,000 = 2,000 ; Expiry 100: 0 + 2,000\nInterest on ₹20,000 sale proceeds at 9% for 1 month = 20,000 × e^(0.09/12) − 20,000 = ₹150.56 → total ₹2,150.56\nEarly exit on 15th: spot 130, futures 135 → −6,000 + 9,000 = ₹3,000 + interest 15 days ₹74.11 = ₹3,074.11") +
      K("Assumes arbitrageur owns the stock; else borrow stock and include borrowing cost","Positions can be squared off before expiry when favourable"))
    sub("Calendar spread arbitrage (futures)", 5,
      F("Spot 120; near futures 121.30; mid futures 121.50; rate 8%\nFair near = 120 × e^(0.08 × 1/12) = 120.80 ; fair mid = 120 × e^(0.08 × 2/12) = 121.61 → fair gap ≈ 0.81\nActual gap 0.20 → near is overpriced vs mid → SHORT near at 121.30, LONG mid at 121.50\nCase 1: near expires 122, mid 122.82 → −0.70 + 1.32 = +0.62\nCase 2: near expires 120, mid 120.80 → +1.30 − 0.70 = +0.60") +
      K("Buy underpriced, sell overpriced","Low risk, low return; no directional bet","Rare in practice — mispricing vanishes quickly; both legs must be executed and squared simultaneously"))
    sub("Option spreads: vertical, horizontal, diagonal", 5,
      T(["Spread","Construction"],
        [["Vertical","Same expiry, different strikes (calls or puts); bullish or bearish"],
         ["Horizontal (time / calendar)","Same type, same strike, different expiries; bet on time-value gap; no payoff chart possible"],
         ["Diagonal","Different expiries and strikes; complex; better suited to OTC"]]) +
      K("Spreads = same underlying, same type, different strikes/maturities","Limited profit, limited loss"))
    sub("Bull call spread (worked)", 5,
      F("Long 17,500 call @ 185 + short 17,800 call @ 61 → net debit 124\nMax loss 124 (≤ 17,500) ; max profit = 300 − 124 = 176 (≥ 17,800)\nBEP = lower strike + net premium = 17,500 + 124 = 17,624") +
      K("Bullish but wants lower cost; gains above short strike given up; higher short strike → bigger profit cap but smaller premium") +
      PO(payoff("Bull call spread","5,45 45,45 75,25 115,25","Debit 124; BEP 17,624")))
    sub("Bull put spread (worked)", 5,
      F("Short 17,500 put @ 125 + long 17,000 put @ 34 → net credit 91\nMax profit 91 (≥ 17,500) ; max loss = 500 − 91 = 409 (≤ 17,000)\nBEP = higher strike − net credit = 17,500 − 91 = 17,409") +
      K("Bullish; long lower put = insurance against unlimited loss on short put","Net premium receipt strategy"))
    sub("Bear call spread (worked)", 5,
      F("Short 17,500 call @ 185 + long 17,800 call @ 61 → net credit 124\nMax profit 124 (≤ 17,500) ; max loss 176 (≥ 17,800) ; BEP 17,624") +
      K("Bearish; long higher call caps the unlimited loss of the short call; starts with net inflow"))
    sub("Bear put spread (worked)", 5,
      F("Long 17,500 put @ 125 + short 17,000 put @ 34 → net debit 91\nMax profit = 500 − 91 = 409 (≤ 17,000) ; max loss 91 (≥ 17,500) ; BEP 17,409") +
      PO(payoff("Bear put spread","5,25 45,25 75,45 115,45","Debit 91; BEP 17,409")))
    sub("Long & short straddle (worked)", 5,
      F("Stock 6,000; ATM call 257, put 136 → total 393\nLong straddle: max loss 393 at expiry = 6,000\nBEPs = strike ± total premium = 5,607 and 6,393\nExpiry 5,300: put +564, call −257 → +307 ; expiry 6,700: call +443, put −136 → +307\nShort straddle: max profit 393 at 6,000; losses beyond 5,607 / 6,393 — unlimited") +
      K("Long straddle: market-neutral; expects big move either way (major announcements) — a volatility view","Short straddle: expects stability; limited profit, unlimited loss — use with care") +
      PO(payoff("Long straddle","5,5 60,55 115,5","BEPs 5,607 / 6,393"),
         payoff("Short straddle","5,65 60,15 115,65","Max profit 393")))
    sub("Long strangle (worked)", 5,
      F("Stock 6,100; buy OTM 6,200 call @ 145 + OTM 6,000 put @ 140 → total 285 (max loss, between strikes)\nExpiry 5,700: put +160, call −145 → +15 ; expiry 6,800: call +455, put −140 → +315\nBEPs = 6,000 − 285 = 5,715 and 6,200 + 285 = 6,485") +
      K("Same outlook as straddle but different strikes, both OTM → cheaper, needs bigger move") +
      PO(payoff("Long strangle","5,5 45,50 75,50 115,5","Max loss 285")))
