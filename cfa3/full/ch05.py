from summary_lib import *
from helpers import P

def add(chap, sub):
    chap(5, "P5 Yield Curve Strategies", "13% of PM", 5)
    sub("Yield curve changes & the 5-step return decomposition", 5,
      P("<b>In plain words:</b> the yield curve plots government bond yields against maturity. It moves in three ways — up/down (<b>level</b>), steeper/flatter (<b>slope</b>), more/less bent (<b>curvature</b>). Level shifts explain most bond price changes.") +
      F("Slope = long yield − short yield (rising = steepening)\nButterfly spread = −short + 2 × medium − long  (rising = more curvature = NEGATIVE butterfly)\n1. Coupon income = annual coupon / price\n2. Rolldown = (price with unchanged curve − today's price) / today's price\n3. Yield change = −MD × ΔY + ½ C × ΔY²\n4. Spread change = −MD × ΔS + ½ C × ΔS²\n5. Currency gain/loss (compound: (1 + R_local)(1 + R_FX) − 1)") +
      K("Curves built from liquid on-the-run issues (off-the-run would give a higher curve — liquidity premium); interpolation and bond choice matter",
        "Higher convexity → better in volatile rates → trades at a premium (lower yield)","Barbell (dispersed cash flows) has more convexity than a bullet of the same duration") +
      F("Bullet 10-yr (MD 9.52, C 104.8) vs barbell 46.68% 2-yr (1.86, 5.2) + 53.32% 20-yr (16.23, 292.8), same duration 9.52\n+50 bp: bullet −4.63% ; barbell 0.4668×(−0.92%) + 0.5332×(−7.75%) = <b>−4.56%</b> → barbell wins on convexity") +
      TRAP("A <b>negative</b> butterfly twist = curvature <b>up</b> = butterfly spread <b>up</b> (the curve 'frowns' more)."))
    sub("Static curve strategies (view = market's forward view)", 5,
      T(["Strategy","How","Main risk"],
        [["Buy and hold","Extend duration for higher coupons; low turnover","Rates rise (parallel shift up)"],
         ["Rolling down the curve","Buy at the end of a <b>steep</b> segment; yield falls as it ages → price gain; sell and roll out","Curve shifts/flattens"],
         ["Repo carry trade","Borrow short (repo) to buy long bonds","Rates rise; funding"],
         ["Long futures","Implicit leverage via margin","Rates rise"],
         ["Receive-fixed swap","Earn carry = swap fixed rate − MRR + mark-to-market","Rates rise"]]) +
      F("Bond vs swap, £50m, 6 months, rates −25 bp\nTrade A: 10-yr 3% gilt at 104.3998 (yield 2.5%)\nCoupon = 1.5% × 50m = £750,000 ; new price (19 periods, 1.125%) 106.3828 → +£991,500\nof which rolldown (price at old yield 104.2048) = −£97,500 ; rate change = +£1,089,000\nTrade B: receive 3%, pay MRR 0.5% → carry = (3% − 0.5%)/2 × 50m = £625,000\nFixed leg at 2.75%: 1.020776 × 50m = 51,038,817 → MTM = <b>+£1,038,817</b> (floating leg resets to par)") +
      K("Futures contracts = target BPV ÷ (BPV_CTD / CF_CTD)","LIBOR replaced by market reference rates (MRR)") +
      TRAP("Stable-curve manager adds duration: <b>receive-fixed</b> swap, <b>repo</b> (borrow), not reverse repo."))
    sub("Divergent view on level", 5,
      P("<b>In plain words:</b> expect rates to fall (<b>bullish</b>) → lengthen duration. Expect rates to rise (<b>bearish</b>) → shorten duration.") +
      T(["Tool","Increase duration","Decrease duration"],
        [["Cash bonds","Buy long bonds","Buy short bonds / sell long"],["Futures","Buy","Sell"],["Swaps","Receive fixed","Pay fixed"]]) +
      F("Benchmark equal-weight 2/10/20-yr: D 9.203, C 134.3 ; bearish portfolio 50/25/25: D 7.368, C 102\n+40 bp: benchmark −3.57%, portfolio −2.87% → excess <b>+0.70%</b>\nSame via swap: BPV target 73,680 − 92,030 = −18,350 ; pay-fixed swap MD −8.354\nNP = −18,350 / (−8.354 × 0.0001) = <b>$21.98m</b>"))
    sub("Divergent view on slope", 5,
      P("<b>In plain words:</b> buy bonds whose yields you think will fall relative to others; short bonds whose yields will rise. Set overall duration by your level view: positive if bullish, negative if bearish, zero if neutral.") +
      T(["View","What happens","Position"],
        [["Bull steepener","Short rates fall more (central bank cuts in recession)","Long short end; duration positive"],
         ["Bear steepener","Long rates rise more (CB too loose → inflation fears)","Short long end; duration negative"],
         ["Bear flattener","Short rates rise more (CB hikes)","Short short end; duration negative"],
         ["Bull flattener","Long rates fall more (flight to quality)","Long long end; duration positive"]]) +
      F("Steepener, duration-neutral: long £100m 2-yr → BPV 100m × 1.86 × 0.0001 = £18,600\nShort 10-yr MV = 18,600 / (9.52 × 0.0001) = <b>£19,537,815</b>\n2-yr −20 bp: +0.373% = +£373,040 ; 10-yr +20 bp: −1.883% → short gains £367,903 → total ≈ <b>+£740,900</b>\nBull steepener next → tilt to positive duration (add 2-yr or short less 10-yr)") +
      TRAP("Negative duration + long short-term + short long-term = <b>bear steepener</b>."))
    sub("Divergent view on curvature: butterfly trades", 5,
      T(["View","Means","Trade"],
        [["Curvature ↑ (negative butterfly)","Middle yields rise vs wings","<b>Short body (bullet), long wings (barbell)</b>"],
         ["Curvature ↓ (positive butterfly)","Middle yields fall vs wings","<b>Long body, short wings</b>"]]) +
      F("Positive butterfly, duration-neutral, equal wings: long £100m 10-yr → BPV £95,200\nMV_w × (1.86 + 16.23) × 0.0001 = 95,200 → MV_w = <b>£52,625,760</b> each wing short\nWings +10 bp, body −25 bp: body +2.413% (£2.41m) ; short 2-yr gains ≈ £0.10m ; short 20-yr gains ≈ £0.85m → ≈ <b>+£3.36m</b>") +
      K("Butterflies are duration-neutral but <b>not</b> convexity-neutral: long body/short wings = short convexity"))
    sub("Volatility views: embedded & stand-alone options", 4,
      T(["Instrument","Effect on duration","Benefits when"],
        [["Callable bond (bond + short call)","Lower; negative convexity at low yields","Rates stable/rising, low volatility"],
         ["Putable bond (bond + long put)","Lower; price floor at high yields","Rates rise / volatility high"],
         ["Long call on bond or bond futures","↑","Rates fall"],["Long put on bond or futures","↓","Rates rise"],
         ["Long receiver swaption","↑","Rates fall"],["Long payer swaption","↓","Rates rise"]]) +
      F("Effective duration = (PV₋ − PV₊) / (2 × ΔCurve × PV₀)\nEffective convexity = (PV₋ + PV₊ − 2PV₀) / (ΔCurve² × PV₀)") +
      K("Use effective (not modified) measures for bonds with options","Embedded options always <b>lower</b> duration","Expect rates up → least likely to buy option-free bond (falls most)"))
    sub("Key rate durations", 5,
      P("<b>In plain words:</b> a key rate duration shows the price change if only one point on the curve moves. They add up to effective duration and reveal slope and curvature bets.") +
      K("Zero-coupon bond: KRD = its modified duration × weight","Active KRD &gt; 0 at a maturity → expects that rate to fall; &lt; 0 → expects it to rise",
        "Example: active duration −3.875 (bearish), +0.98 short end, 0 long end, large negative middle → <b>bear steepener + negative butterfly</b>",
        "KRDs +3, −0.5, −3 at 10/20/30-yr via derivatives → receive-fixed 10-yr, short 20-yr futures, pay-fixed 30-yr"))
    sub("Across currencies: unhedged, hedged, carry", 5,
      F("R_DC = (1 + R_FC)(1 + R_FX) − 1   (R_FX from the DIRECT quote, DC/FC)\nAustralian buys US 2-yr zero at 96.374 → 99.939 after 1 yr: R_FC = 3.70%\nUSD/AUD 0.90 → 0.80 ⇒ AUD/USD 1.1111 → 1.25: R_FX = 12.5% → R_DC = 1.037 × 1.125 − 1 = <b>16.66%</b>\nCIRP: F = S × [(1 + r_DC)/(1 + r_FC)]^T\nUS yield (100/96.374)^½ − 1 = 1.864%; AUD 5% → F = 1.1111 × (1.05/1.01864)² = <b>1.1806</b>\nHedged: 100 × 1.1806 = 118.06 vs cost 107.08 → (118.06/107.08)^½ − 1 = <b>5.0%</b> = domestic rate") +
      K("CIRP: high-rate currency at a forward <b>discount</b> → hedged foreign bond earns the <b>domestic</b> rate",
        "UIRP says high-rate currencies depreciate — usually fails → <b>forward rate bias</b> → carry trades profit on average",
        "Hedge a coupon bond with a <b>fixed-fixed cross-currency swap</b> (pay foreign, receive domestic) = 2 fixed-for-floating swaps + cross-currency basis swap (exchanges principal); dropping one leg leaves a rate view with currency still hedged",
        "Negative basis: non-USD leg below CIRP fair rate (borrowers of USD pay up)") +
      F("Carry: borrow USD 1%, roll 90-day INR at 5% → (1.0125)⁴ − 1 = 5.1% → +4.1% if stable\nINR rates 5,6,4,3% → 4.6%; INR/USD 70 → 85: USD/INR 0.014286 → 0.011765 = −17.6%\nTotal = 4.6 − 1.0 − 17.6 = <b>−14.0%</b> (flight to quality crash risk)") +
      K("Cross-market swaps: receive fixed where rates will fall, pay fixed where they will rise; receive floating where rates will rise",
        "Foreign bull steepener + stable domestic → pay foreign floating, receive domestic fixed") +
      TRAP("Excess carry returns mean <b>uncovered</b> parity fails — covered parity is not involved."))
    sub("Evaluating a yield curve strategy (worked)", 5,
      F("CAD zero-coupon, US investor, CAD −0.5%, yields +25 bp\nBullet: rolldown (98.75 − 96.75)/96.75 = 2.067% ; yield −4.89×0.0025 + ½×28.5×0.0025² = −1.214%\nBarbell: rolldown (98.95 − 97)/97 = 2.010% ; yield −4.92×0.0025 + ½×43×0.0025² = −1.217%\nUSD: bullet (1 + 0.02067 − 0.01214)(0.995) − 1 = <b>0.35%</b> ; barbell <b>0.29%</b>\nBullet wins on rolldown (sits on a steeper part of the curve)") +
      F("Quiz: barbell 60% 2-yr + 40% 10-yr, bear flattener 2-yr +50, 10-yr +30\n0.6 × (−0.92%) + 0.4 × (−2.81%) = <b>−1.68%</b>") +
      K("Schweser recommends compounding currency (multiplicative); adding is unlikely to be marked wrong"))
