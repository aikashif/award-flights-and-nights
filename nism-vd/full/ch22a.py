from summary_lib import *

def add(chap, sub):
    chap(22, "Strategies using Exchange Traded Interest Rate Derivatives", "6", 4)
    sub("Hedgers, speculators, arbitrageurs", 4,
      T(["Type","Role","Example"],
        [["Hedger","Real rate exposure; removes it","₹10 cr in 6.10% GOI pays ₹61 lakh/yr; rates → 6.50% → new bonds pay ₹65 lakh; selling old bond means lower price"],
         ["Speculator","No exposure; takes view; supplies other side, depth and liquidity","Trader buys wheat futures from farmer expecting higher price"],
         ["Arbitrageur","No exposure, no risk taken; locks profit across markets; brings prices to equilibrium","Spot 100, March futures 110, lot 50 → buy cash, sell futures → ₹10 × 50 = <b>₹500</b> whether expiry is 108 or 95"]]) +
      K("Arbitrage risks: execution gap, illiquid leg (naked exposure), unwinding when not cash-settled","Costs (transaction, impact, carry) ignored in examples",
        "Traders and arbitrageurs bring liquidity → better price discovery, lower costs, less manipulation"))
    sub("Choosing instrument, side, contract month", 5,
      T(["Parameter","Rule"],
        [["Instrument","Match tenor: 3-month rate → T-bill futures; 10-yr rate → 10Y GOI bond futures/options"],
         ["Market side","Match expected rate direction"],["Contract month","Match timing of expected rate change"]]) +
      T(["Expect rates","Position","Trades"],
        [["↑ (rise)","Long the rate","Sell GOI bond futures · buy GOI bond put · sell T-bill futures · <b>buy</b> overnight MIBOR futures"],
         ["↓ (fall)","Short the rate","Buy GOI bond futures · buy GOI bond call · buy T-bill futures · <b>sell</b> overnight MIBOR futures"]]) +
      K("Future borrower fears a rise → sells bond futures OR buys MIBOR futures"))
    sub("Short hedge (worked)", 5,
      F("20 Sep 2021: X holds ₹5 cr 6.10% GS 2031 at 100.00 (yield 6.10%); fears rise after Oct policy\nSell 250 lots (5 cr ÷ 2 lakh) Oct futures at 99.95\nExpiry 28 Oct: bond 98.36 (yield 6.32%)") +
      T(["Scenario","Amount on expiry","Plus","Minus"],
        [["I. Sell now, T-bills 3.20% for 38 days","₹5,07,53,106","No rate risk","Loses accrued interest"],
         ["II. Hold unhedged","₹5,00,86,528","Accrued interest; gains if price rises","Full rate risk"],
         ["III. Hold + short futures","<b>₹5,08,81,528</b> (futures gain (99.95 − 98.36) × 250 × 2,000 = ₹7,95,000)","Accrued interest; no rate risk","Impact cost; expiry vs trade price mismatch; gives up gains if price rises"]]) +
      K("Bondholder = long bond, short the rate → hedge by <b>selling</b> bond futures","Fund manager liquidating bonds in 45 days: sell bond futures to lock price"))
    sub("Portfolio (duration-based) hedge", 5,
      F("Max short IRF = (portfolio MD × portfolio market value) ÷ (futures MD × futures price ÷ par)\n₹26 cr, portfolio duration 6.1, futures duration 4.7, futures 98.50\nLots = 26,00,00,000 × 6.1 ÷ (98.50 × 4.7 × 2,000) ≈ <b>1,713</b>") +
      K("Makes position duration zero","Limits: duration accurate only for small moves → large moves cause <b>under-hedging</b> (convexity); <b>basis risk</b> if prices don't move together"))
    sub("Hedging future borrowing & long hedge", 5,
      F("Future borrowing: corporate to issue 10-yr NCDs in 1 month at G-sec + 50 bp\n14 Aug: sell 7.59% GOI futures 95.60 (yield 7.93%) ; 24 Sep FSP 94.80 (8.08%) → gain ₹0.80 per bond offsets higher cost (basis risk remains)\nLong hedge: insurer expects ₹200 cr premiums in March; fears fall in rates\n12 Feb: 6.45% GS 2029 spot 99.79 (6.48%), March futures 99.60 (6.51%) → buy 10,000 lots\nExpiry 101.58 (6.23%): gain (101.58 − 99.60) × 10,000 × 2,000 = <b>₹3.96 cr</b>\nIf expiry 99.00 (6.59%): loss <b>₹1.20 cr</b> — hedging also cuts potential profit") +
      K("Long hedge = buy futures to lock purchase price/yield (insurers with inflows, bonds maturing soon)",
        "Options alternative: long hedge → buy bond <b>call</b>; short hedge / future borrowing → buy bond <b>put</b>; max loss = premium"))
