from summary_lib import *

def add(chap, sub):
    chap(16, "Introduction to Options", "13", 5)
    sub("What an option is", 5,
      L("Futures = linear payoff, unlimited loss/profit; options let you ride upside while restricting downside",
        "Option = <b>right, not obligation</b>, to buy/sell the underlying on or before a stated date at a predetermined price",
        "Right bought for the <b>option premium</b>, paid upfront by buyer (holder, long) to seller (writer, short)",
        "Buyer exercises only when favourable; writer legally bound if exercised",
        "<b>Call</b> = right to buy; <b>Put</b> = right to sell"))
    sub("Option quote example & terminology", 4,
      T(["Field (May 10, 20XX)","Nifty call","Nifty put"],
        [["Expiry / type","25 May, European call","25 May, European put"],["Strike","18,400","18,400"],
         ["Open / High / Low","125 / 130 / 93.65","193.55 / 236 / 171.50"],["Close (premium)","124.50","177.60"],
         ["Volume / OI","61,330 / 14,97,650","31,388 / 4,97,950"],["Underlying","18,315.10","18,315.10"]]) +
      T(["Term","Meaning"],
        [["Index option / stock option","Underlying = index (Nifty, Sensex) / stock (ONGC, NTPC)"],
         ["Buyer","Right, pays premium; right to buy (call) or sell (put)"],
         ["Writer","Receives premium; obligation — sell if call exercised, buy if put exercised"],
         ["American","Exercise any time on/before expiry"],["European","Exercise only on expiry; <b>all Indian index &amp; stock options</b>"],
         ["Premium","Per unit; × lot size for contract premium"],["Spot (S)","Underlying's cash price (18,315.10)"],
         ["Strike / exercise price (X)","Price at which call buyer may buy / put buyer may sell"],
         ["Open interest","Outstanding option contracts; SEBI uses <b>delta-adjusted open position</b> for options"],
         ["Exercise","Indian options exercised only at maturity vs settlement/closing price"],
         ["Assignment","Allocation of exercised options to one or more sellers"]]))
    sub("Opening & closing option positions", 4,
      L("Opening purchase = create/increase long on option; opening sale = create/increase short on option",
        "Long on call = long the underlying; <b>long on put = short the underlying</b>",
        "Closing (squaring off) = offsetting trade in the <b>same</b> option (same strike and expiry) — buying a put does not close a long call"))
    sub("Option contract specifications", 5,
      T(["Spec","Rule"],
        [["Lot size","Exchange sets; same as futures (e.g. Nifty 50 → call premium 124.50 × 50 = ₹6,225; put 177.60 × 50 = ₹8,880)"],
         ["Stock options cycle","Same tenor as stock futures; NSE 3-month cycle (near, mid, far)"],
         ["Index options","Wider range; Nifty 50 &amp; Sensex up to <b>5 years</b>; weekly &amp; monthly; one weekly benchmark index option per exchange (Tuesday or Thursday); 3 quarterly (Mar/Jun/Sep/Dec) after 3 serial months; long-term: 8 half-yearly (Jun–Dec cycle) after quarterlies"],
         ["Weekly options now","NSE: Nifty 50; BSE: Sensex"],
         ["Expiry rules","SEBI 26 May 2025 (same as futures: Tue/Thu; others last week of month)"],
         ["Tick size","Set by exchange — see exchange specs"],
         ["Final settlement","No daily settlement for options; exercise/assignment only on expiry; index = closing price of underlying; stocks = VWAP of closing prices across exchanges (CAS SOP)"],
         ["Trading hours","9:15 am – 3:40 pm, Mon–Fri (as stated for options)"]]) +
      T(["BSE Sensex options","Spec"],
        [["Contract size","20"],["Tick","₹0.05"],["Cycle","7 serial weekly, 3 monthly, 3 quarterly, 8 semi-annual"],
         ["Trading hours","9:15 am – 3:30 pm"],["Style","European"],["Expiry","Monthly/quarterly/semi-annual: last Thursday; weekly: Thursday"],
         ["Strikes","Min <b>101</b> (50 ITM, 1 ATM, 50 OTM); interval 100 index points"],["Settlement","Cash, closing index value"]]) +
      TRAP("Workbook gives two trading-hour figures for derivatives (futures 9:15–3:30; options 9:15–3:40; Sensex futures 3:40, Sensex options 3:30). Normal market hours are 9:15 am – 3:30 pm."))
    sub("Moneyness", 5,
      T(["","Call","Put"],
        [["In-the-money (ITM)","Strike &lt; Spot","Strike &gt; Spot"],["At-the-money (ATM)","Strike = Spot (closest strike)","Strike = Spot"],["Out-of-the-money (OTM)","Strike &gt; Spot","Strike &lt; Spot"]]) +
      K("ITM: positive cash flow if exercised now; ATM: zero; OTM: negative","Index 18,415 with strikes 18,350/18,400/18,450 → 18,400 is ATM","Quote example: 18,400 put is ITM; 18,400 call is OTM"))
    sub("Intrinsic value & time value", 5,
      F("Call IV = max(0, S − X)     Put IV = max(0, X − S)     IV never negative\nTime value = Premium − Intrinsic value\nPut 18,400 with spot 18,315.10: IV = 84.90 ; TV = 177.60 − 84.90 = 92.70\nCall 18,400: IV = 0 ; TV = entire 124.50") +
      K("Only ITM options have intrinsic value","ATM &amp; OTM = pure time value"))
    sub("Long & short options — general", 4,
      T(["","Long (buyer)","Short (writer)"],
        [["Right / obligation","Right to exercise","Obligation; may be assigned (any time if American)"],
         ["Max loss","Premium paid","Theoretically unlimited"],["Max profit","Depends on underlying","Premium received"],["Margin","None","Must pay margin"]]))
    sub("Long call (worked)", 5,
      F("Index 17,562; buy call 17,500 at ₹95\nExpiry 17,400 → don't exercise → loss ₹95\nExpiry 17,595 → payoff 95 − premium 95 = 0 → BEP = X + P = 17,595\nExpiry 18,000 → payoff 500 → profit 405\nLot 50: contract value ₹8,75,000 ; max loss 95 × 50 = ₹4,750") +
      PO(payoff("Long call","5,45 60,45 115,5","Loss capped ₹95, unlimited profit")) +
      K("Index options cash-settled: ITM holder receives (closing index − strike)","Call buyer pays no margin"))
    sub("Short call (worked)", 5,
      L("Mirror image of long call; max gain = premium ₹95; loss unlimited as index rises",
        "Index 17,000 → +95; 17,700 → −105",
        "BEP = X + P = 17,595 for short call too — <b>BEP depends on the instrument, not the position</b>",
        "Writer pays margin (obligation, potentially unlimited loss — risk to system)") +
      PO(payoff("Short call","5,25 60,25 115,65","Gain capped at premium")))
    sub("Long put (worked)", 5,
      F("Buy put 17,500 at ₹150\nExpiry ≥ 17,500 → lapse → loss ₹150\nBEP = X − P = 17,350\nMax profit when index = 0 → 17,500 − 150 = ₹17,350\nExpiry 17,100 → payoff 400 → profit 250\nLot 50: max loss ₹7,500 ; contract value ₹8,75,000") +
      PO(payoff("Long put","5,5 60,45 115,45","Loss capped at premium")) +
      K("Put buyer pays no margin — no obligation"))
    sub("Short put (worked)", 5,
      L("Opposite of long put; max gain = premium ₹150; losses below BEP 17,350; max loss when index hits zero",
        "Expiry 17,100 → −250; 17,400 → +50; ≥ 17,500 → +150",
        "Writer pays margin (obligation to buy, losses can be huge)") +
      PO(payoff("Short put","5,65 60,25 115,25","Gain capped at premium")) +
      T(["","Risk","Return"],[["Long option","Premium paid","Unlimited"],["Short option","Unlimited","Premium received"]]))
    sub("Options vs futures; leverage", 5,
      L("Options: <b>asymmetric</b> payoff; futures: <b>symmetric</b>",
        "Leverage: small premium vs contract value (₹4,750 or ₹7,500 vs ₹8,75,000) → large % gains from small moves",
        "Leverage magnifies % loss too; worthless expiry loses whole premium",
        "Both used for trading, hedging, arbitrage") +
      T(["Futures","Options"],
        [["Buyer and seller both obliged","Buyer has right, no obligation; seller has obligation"]]))
