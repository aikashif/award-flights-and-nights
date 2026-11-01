from summary_lib import *

def add(chap, sub):
    sub("What sets short-term & long-term rates", 5,
      T(["Segment","Main driver","Central bank tools"],
        [["Short-term rates","Liquidity in the system","Repo / reverse repo (policy rates)"],
         ["Long-term rates","Inflation outlook, capex demand","Bank rate, CRR, SLR, OMO"]]) +
      K("SLR forces banks to hold G-secs → distorts G-sec yields (captive demand)","Global rates matter through capital flows (uncovered interest parity)"))
    sub("Yield curve shapes", 5,
      T(["Shape","Meaning"],
        [["Normal (upward)","Long rates &gt; short rates — usual case"],["Inverted (downward)","Short rates &gt; long rates — often signals slowdown"],
         ["Flat","Short ≈ long rates"],["Humped","Medium rates highest"]]))
    sub("Yield curve shifts", 5,
      T(["Shift","Description"],
        [["Steepening","Gap long − short widens; curve turns <b>anti-clockwise</b>"],["Flattening","Gap narrows; curve turns <b>clockwise</b>"],
         ["Parallel","All rates move by the same amount"],["Twist","Short and long move in opposite directions"],["Convexity change","Curvature changes (middle moves vs ends)"]]) +
      T(["Base SR 7%, LR 8% → new","Result"],
        [["6.90 / 8.10","Steepening twist"],["7.10 / 7.90","Flattening twist"],["7.10 / 8.10","Parallel shift up"]]))
    sub("Simple vs compound interest; FV & PV", 5,
      F("₹100 at 8% for 5 yrs: simple → 140 ; compound → 146.93\nFV single period: ₹2,000 at 9% → 2,180\nMulti-period (5 yrs): 2,000 × 1.09^5 = 3,077.25 (interest 1,077.25 vs simple 900)\n₹1,00,000 at 7.3% for 4 yrs → 1,32,555.85 (annual) ; 1,33,215.41 (semi-annual)\nFV = PV × (1 + r/m)^(m×n)     PV = FV ÷ (1 + r/m)^(m×n)") +
      T(["12% nominal compounded","Effective rate"],[["Annually","12.00%"],["Semi-annually","12.36%"],["Quarterly","12.55%"],["Monthly","12.68%"]]) +
      K("More frequent compounding → higher effective rate"))
    sub("Day count conventions", 5,
      K("Count first day, exclude last day") +
      T(["Convention","Used for (India)"],
        [["Actual/Actual","Corporate bonds"],["30/360 (European)","<b>G-secs</b>"],["Actual/365","Money market instruments"],["Actual/360","Swaps"]]) +
      F("30/360: days = 360(Y2−Y1) + 30(M2−M1) + (D2−D1), day 31 → 30\n31-Dec-2020 to 25-Jan-2021 = 25/360"))
    sub("Accrued interest; clean & dirty price", 5,
      L("<b>Clean price</b> = quoted / negotiated price",
        "<b>Dirty (invoice / full) price</b> = clean + accrued interest = settlement price",
        "AI grows from 0 after each coupon, drops at coupon → <b>saw-tooth</b> pattern",
        "AI change is deterministic; clean price change is stochastic",
        "Equities have no 'accrued dividend'") +
      F("6.90% semi-annual bond, coupons 13 Jan &amp; 13 Jul, trade 5 Mar\nActual/Actual: AI = 3.45 × 51/181 = 0.972099\n30/360: AI = 3.45 × 52/180 = 0.996667\nClean 101.50 → dirty 101.50 + 0.9967 = 102.4967"))
    sub("Spot (zero) rate & holding period return", 4,
      F("₹100 → ₹150 in 3 yrs: annual 14.4714% ; semi-annual 13.9826% ; quarterly 13.7464% ; monthly 13.5919%") +
      K("Spot/zero rate = yield on a single cash flow (zero-coupon)","HPR known only after the event (ex post)"))
    sub("Sources of bond return", 5,
      T(["Source","Point"],
        [["Coupon","7% GS 2027 → ₹3.50 each half-year; 7.17% GS 2028 → ₹3.585 on 8 Jan &amp; 8 Jul"],
         ["Capital appreciation","Price rises when yields fall"],["Term premium","Extra yield for longer tenor"],
         ["Reinvestment income","YTM assumes coupons reinvested at YTM"]]))
    sub("Price-yield relation; current yield", 5,
      L("Price and yield move <b>inversely</b>",
        "Coupon &gt; yield → premium; coupon &lt; yield → discount; coupon = yield → par") +
      F("All yield 7.5%: 10% coupon → 117.37 ; 8% → 103.47 ; 6% → 89.58\nCurrent yield = annual coupon ÷ clean price = 7.17 ÷ 96.2290 = 7.45%") +
      K("Current yield ignores capital gain/loss and time value"))
    sub("YTM, BEY, discount yield, effective yield", 5,
      T(["Measure","Formula / point"],
        [["YTM","IRR of bond cash flows at current price; Excel YIELD(); assumes held to maturity and reinvestment at YTM"],
         ["Bond equivalent yield (BEY)","(FV − P) ÷ P × 365 ÷ days ; T-bill 99.6898, 34 days → 3.34%"],
         ["Discount yield","(FV − P) × 360 ÷ (FV × days) ; used for 91-day T-bill futures"],
         ["Effective yield","(1 + r/m)^m − 1 ; 4.20% paid monthly → 4.28%"]]) +
      TRAP("Doubling a semi-annual yield <b>understates</b> the effective annual yield"))
    sub("Bond pricing (worked)", 5,
      F("10% coupon, 5 yrs, yield 8%, annual\nDiscount factors: 0.9259 / 0.8573 / 0.7938 / 0.7350 / 0.6806 ; PVIF(annuity) 3.9927\nPrice = 10 × 3.9927 + 100 × 0.6806 ≈ 107.99\nSemi-annual: 5 × PVIF 8.1109 + 100 × DF → 108.11\nP = Σ C/(1+y)^t + FV/(1+y)^n ; continuous: P = Σ C·e^(−yt)\nUnder 1 yr: V = FV ÷ (1 + R × n) ; zero-coupon: V = FV ÷ (1 + R/m)^(m×t)"))
