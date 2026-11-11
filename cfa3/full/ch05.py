from summary_lib import *
from helpers import P

def add(chap, sub):
    chap(5, "P5 Yield Curve Strategies", "13% of PM", 5)
    sub("What this reading is about", 3,
      P("<b>In plain words:</b> how to add value by positioning along the <b>government (credit-risk-free) yield curve</b>: what to do if you expect the curve to stay the same, or to change in level, slope or shape; how options and volatility fit; how key rate durations reveal a manager's view; how to invest across currencies; and how to estimate a strategy's return. (Credit comes in P6.)") +
      T(["LOS","Topic"],[["P5.a","Factors affecting returns from benchmark yield changes"],["P5.b","Strategy when your view = market view (static curve)"],
        ["P5.c","Strategy when your view differs: level, slope, curvature"],["P5.d","Strategy for expected volatility changes"],["P5.e","Key rate durations of portfolio vs benchmark"],
        ["P5.f","Yield curve strategies across currencies"],["P5.g","Expected return and risks of a yield curve strategy"]]))
    sub("The yield curve and how it changes", 5,
      P("<b>In plain words:</b> a yield curve plots yields (usually YTM) of one type of bond, normally government bonds, against maturity. Active management adds value only if your view is correct <b>and</b> not already in prices.") +
      K("Building a curve needs choices: interpolation to fill gaps, accounting/regulatory rules, which bonds to use",
        "Built from liquid, recently issued <b>on-the-run</b> bonds; using off-the-run bonds too would give a <b>higher</b> curve (liquidity premium)") +
      T(["Change","Meaning","Measure"],
        [["Level","Parallel shift: all yields up or down equally — <b>explains most</b> bond price change","—"],
         ["Slope (twist)","Curve steeper or flatter","Long yield − short yield (rising = steepening)"],
         ["Curvature (butterfly)","Curve more or less bent","Butterfly spread = −short + 2 × medium − long (rising = more curvature)"]]))
    sub("Five-step return decomposition; convexity; bullet vs barbell", 5,
      F("1. Coupon income = annual coupon ÷ current price\n2. Rolldown = (price if curve unchanged − beginning price) ÷ beginning price\n3. Yield change = (−MD × ΔY) + (½ C × ΔY²)\n4. Spread change = (−MD × ΔS) + (½ C × ΔS²)\n5. Currency gain/loss (weighted by exposure)") +
      K("Higher convexity → outperforms when rates are volatile → trades at a <b>premium</b> (lower YTM)",
        "More cash-flow dispersion around duration → more convexity → <b>barbell</b> has more convexity than a <b>bullet</b> of the same duration") +
      F("UK bonds: 2-yr MD 1.86, C 5.2 ; 10-yr MD 9.52, C 104.8 ; 20-yr MD 16.23, C 292.8\nBullet = 100% 10-yr ; barbell = 46.68% 2-yr + 53.32% 20-yr (duration 0.4668×1.86 + 0.5332×16.23 = 9.52)\n+50 bp: 2-yr −0.92% ; 10-yr −4.63% ; 20-yr −7.75%\nBullet −4.63% vs barbell 0.4668×(−0.92) + 0.5332×(−7.75) = <b>−4.56%</b> → barbell wins") +
      TRAP("Barbell beats bullet for both <b>up and down</b> parallel moves (quiz C)."))
    sub("Static yield curve: strategies when your view = the market's", 5,
      P("<b>In plain words:</b> if you expect an upward-sloping curve to stay unchanged, earn more by taking more duration or leverage.") +
      T(["Strategy","How it earns","Main risk"],
        [["Buy and hold","Duration longer than benchmark → higher coupons; low turnover and costs","Parallel shift <b>up</b> (quiz A)"],
         ["Rolling down the curve","Coupon + <b>rolldown</b>: buy bonds at the end of a <b>steep</b> segment; yield falls as they age → price gain; sell and roll out","Curve shifts or flattens"],
         ["Repo carry trade","Borrow short via repo, buy longer bonds (leverage)","Rates rise; funding cost"],
         ["Long bond futures","Implicit leverage — only margin needed","Rates rise"],
         ["Receive-fixed swap","Swap carry (fixed − MRR) + mark-to-market; fixed leg holds the duration","Rates rise"]]) +
      F("Futures BPV = BPV_CTD ÷ CF_CTD ; contracts to buy = target BPV ÷ futures BPV") +
      K("LIBOR replaced by <b>MRR</b> (market reference rates, often secured overnight)") +
      TRAP("Stable curve → <b>receive-fixed</b> swap or <b>repo</b> (borrowing). Pay-fixed or reverse repo (lending) are wrong (quiz A)."))
    sub("Worked: bond vs receive-fixed swap over six months", 5,
      F("£50m par, 6-month horizon, rates fall 25 bp\nTrade A: 10-yr 3% semiannual gilt, yield 2.5%, price 104.3998\nCoupon = 0.03/2 × 50m = <b>£750,000</b>\nNew price: N 19, I/Y 1.125, PMT 1.5, FV 100 → 106.3828 → gain (106.3828 − 104.3998)% × 50m = <b>£991,500</b>\nAt unchanged 2.5% yield: 104.2048 → rolldown = −£97,500 ; yield change = +£1,089,000\nTrade B: receive 3%, pay MRR 0.5%\nCarry = (0.03 − 0.005)/2 × 50m = <b>£625,000</b>\nFixed leg at 2.75%: N 19, I/Y 1.375, PMT 0.015, FV 1 → 1.020776 × 50m = £51,038,817\nFloating leg resets to par → MTM = <b>+£1,038,817</b>") +
      K("Rolldown here is negative: the curve between 9.5 and 10 years is assumed flat, and the bond's premium pulls to par"))
    sub("Divergent view on level", 5,
      P("<b>In plain words:</b> expect yields to fall (<b>bullish</b>) → lengthen duration. Expect yields to rise (<b>bearish</b>) → shorten duration.") +
      T(["Tool","Increase duration (bullish)","Decrease duration (bearish)"],
        [["Cash bonds","Buy long / sell short bonds","Buy short / sell long bonds"],["Futures","Buy","Sell"],["Swaps","Receive fixed (pay floating)","Pay fixed (receive floating)"]]) +
      F("Benchmark equal-weight 2/10/20: D = (1.86 + 9.52 + 16.23)/3 = 9.203 ; C = 134.3\nBearish 50/25/25: D = 7.368 ; C = 102.0\n+40 bp: benchmark −3.57% ; portfolio −2.87% → excess <b>+0.70%</b>\nSame with a swap on $100m: BPV target 73,680 − benchmark 92,030 = −18,350\nPay-fixed swap MD −8.354 → NP = −18,350 / (−8.354 × 0.0001) = <b>$21.98m</b>") +
      TRAP("Expect rates down → <b>pay-floating</b> (= receive-fixed) swap (quiz A)."))
    sub("Divergent view on slope", 5,
      P("<b>In plain words:</b> buy bonds whose yields will fall relative to the rest; short bonds whose yields will rise. Steepening → long short end, short long end. Flattening → long long end, short short end. Then set net duration by your level view: + if bullish, − if bearish, 0 if none.") +
      T(["View","What happens","Typical cause","Net duration"],
        [["Bull steepener","Short rates fall more than long","Central bank cuts in a contraction","Positive"],
         ["Bear steepener","Long rates rise more than short","CB too loose too long → inflation fears","Negative"],
         ["Bear flattener","Short rates rise more than long","CB starts hiking","Negative"],
         ["Bull flattener","Long rates fall more than short","Flight to quality","Positive"]]) +
      F("Steepener, no level view (duration-neutral): long £100m 2-yr → BPV = 100m × 1.86 × 0.0001 = £18,600\nShort 10-yr: MV × 9.52 × 0.0001 = 18,600 → MV = <b>£19,537,815</b>\n2-yr −20 bp: +0.373% → +£373,040 ; 10-yr +20 bp: −1.883% → short gains ≈ £367,900\nTotal ≈ <b>+£740,900</b>\nIf next view is bull steepener → make duration positive: buy more 2-yr or short less 10-yr") +
      K("Don't memorise the table: buy where yields fall relative, sell where they rise relative, then set duration sign") +
      TRAP("Negative duration + long short end + short long end = <b>bear steepener</b> (quiz B)."))
    sub("Divergent view on curvature: butterfly trades", 5,
      P("<b>In plain words:</b> a butterfly combines a bullet (the <b>body</b>, medium maturity) with a barbell (the <b>wings</b>, short + long). Duration-neutral, but <b>not</b> convexity-neutral.") +
      T(["View","Middle yields","Butterfly spread","Trade"],
        [["More curvature = <b>negative</b> butterfly twist","Rise vs wings","Rises","<b>Short body, long wings</b>"],
         ["Less curvature = <b>positive</b> butterfly twist","Fall vs wings","Falls","<b>Long body, short wings</b>"]]) +
      F("Positive butterfly, duration-neutral, equal-value wings; long £100m 10-yr → BPV £95,200\nMV_w × 1.86 × 0.0001 + MV_w × 16.23 × 0.0001 = 95,200 → MV_w = <b>£52,625,760</b> short each wing\n2- and 20-yr +10 bp, 10-yr −25 bp:\nBody +2.413% → +£2.41m ; short 2-yr gains ≈ £0.10m ; short 20-yr gains ≈ £0.85m → ≈ <b>+£3.36m</b>") +
      K("Long body + short wings = <b>short convexity</b> → hurts if yields move equally; here the body moved more, so its convexity term was bigger",
        "Memory aid: negative butterfly = the curve 'frowns' more") +
      TRAP("Long wings, short body = expects a <b>negative butterfly twist</b> (quiz C) — the butterfly spread <b>rises</b>."))
    sub("Volatility views: embedded options", 4,
      T(["Bond","Structure","Behaviour"],
        [["Callable","Option-free bond + <b>short</b> call (issuer's)","Call gains as yields fall → price rises slowly → <b>negative convexity</b> at low yields"],
         ["Putable","Option-free bond + <b>long</b> put (investor's)","Put gains as yields rise → price <b>floor</b> at high yields"]]) +
      F("Effective duration = (PV₋ − PV₊) / (2 × Δcurve × PV₀)\nEffective convexity = (PV₋ + PV₊ − 2PV₀) / (Δcurve² × PV₀)") +
      K("Use <b>effective</b> measures — Macaulay/modified ignore uncertain cash flows",
        "An embedded option always <b>lowers</b> duration vs the option-free bond",
        "Expect rates ↑ → <b>least</b> likely to buy the <b>option-free</b> bond (falls most) — quiz C"))
    sub("Volatility views: stand-alone options", 4,
      T(["Position","Gains when","Portfolio duration"],
        [["Long call on bond or bond futures","Yields fall","Increases"],["Long put on bond or bond futures","Yields rise","Decreases"],
         ["Long receiver swaption (right to receive fixed)","Rates fall","Increases"],["Long payer swaption (right to pay fixed)","Rates rise","Decreases"]]) +
      TRAP("Expect yields down → <b>long call on bond futures</b> (quiz C). Short receiver or long payer would lose."))
    sub("Key rate durations: reading a manager's view", 5,
      P("<b>In plain words:</b> a key rate (partial) duration shows the value change if <b>one</b> maturity's yield moves and others stay put. They sum to effective duration. Active KRD = portfolio KRD − benchmark KRD.") +
      F("KeyRateDur_k = −(1/PV) × ΔPV / Δr_k\nZero-coupon bond: KRD = MD × weight (MD = maturity ÷ (1 + y)) — not for coupon bonds") +
      K("Active KRD <b>&gt; 0</b> at a maturity → expects that yield to <b>fall</b>; &lt; 0 → expects it to rise",
        "Worked example (3 zeros, equal-weight benchmark): active duration −3.875 → <b>bearish</b>; short end +0.98, long end 0 → short rates rise less → <b>steepener</b>; big negative middle, positive wings → <b>negative butterfly</b> → overall: bear steepener + negative butterfly",
        "Quiz: active KRDs +3 (10-yr), −0.5 (20-yr), −3 (30-yr) via derivatives → <b>receive-fixed 10-yr, short 20-yr futures, pay-fixed 30-yr</b> (A)"))
    sub("Across currencies: unhedged foreign bonds", 5,
      F("R_DC = (1 + R_FC)(1 + R_FX) − 1\nR_FX from the <b>direct</b> quote (DC/FC: domestic per 1 foreign)\nSeveral markets: compute R_DC for each, then weight") +
      F("UK investor, Japanese bond: JPY/GBP 150 → 125 ⇒ GBP/JPY 0.006667 → 0.0080 → R_FX = <b>+20%</b>\nAustralian buys US 2-yr zero at 96.374 → 99.939 after 1 yr: R_FC = <b>3.70%</b>\nUSD/AUD 0.90 → 0.80 ⇒ AUD/USD 1.1111 → 1.2500 → R_FX = <b>12.5%</b>\nR_DC = 1.037 × 1.125 − 1 = <b>16.66%</b>") +
      TRAP("Invert the quote if the domestic currency is the base. Direct quote up = foreign currency up = gain."))
    sub("Hedging: covered vs uncovered interest parity", 5,
      P("<b>In plain words:</b> hedging = sell the foreign currency forward. Under <b>covered interest rate parity (CIRP)</b> the high-rate currency trades at a forward <b>discount</b>, so a hedged foreign bond earns only your <b>domestic</b> risk-free rate.") +
      F("F (DC/FC) = S × [(1 + r_DC) / (1 + r_FC)]^T\nUS 2-yr yield = (100/96.374)^½ − 1 = 1.864% ; AUD 2-yr 5%\nF = 1.1111 × (1.05 / 1.01864)² = <b>1.1806</b> AUD/USD\nSell USD 100 forward → AUD 118.06 ; cost 96.374 / 0.90 = AUD 107.0822\nReturn = (118.06 / 107.0822)^½ − 1 = <b>5.0%</b> = AUD rate\nUSD at 3.1% forward premium: (1.1806/1.1111)^½ − 1 offsets lower USD yield") +
      K("<b>Uncovered parity (UIRP)</b>: high-rate currencies should actually depreciate to the forward rate → all unhedged investors earn the same",
        "UIRP usually <b>fails</b>: spot ends between 1.1111 and 1.1806 → forward is a biased predictor = <b>forward rate bias</b> → carry trades profit on average",
        "Quiz: EUR 1% (100/99.01 − 1), USD 3% → USD (high rate) at a 2% forward <b>discount</b>; 'sell USD at a 2% premium' is least likely (B)"))
    sub("Hedging foreign coupon bonds: fixed-fixed cross-currency swap", 4,
      F("AUD investor, USD 100m 10-yr Treasury at par, USD/AUD 0.80\nEnter fixed-fixed cross-currency swap: <b>pay USD fixed, receive AUD fixed</b>; principals USD 100m / AUD 125m\nNet: like owning an Australian bond") +
      T(["Building block","Legs"],
        [["Swap A (USD)","Pay USD fixed, receive USD floating"],["Swap B (AUD)","Receive AUD fixed, pay AUD floating"],
         ["Swap C (cross-currency basis)","Receive AUD floating, pay USD floating; exchange principals at start and end"]]) +
      K("Floating legs of A and B cancel with C; C funds the USD purchase and converts par back to AUD",
        "Paying USD floating = borrowing USD → receive USD principal at start, repay at end",
        "<b>Negative basis</b>: non-USD floating leg below CIRP fair rate → USD borrowers accept less on their own currency",
        "Skip Swap A → net receive USD fixed, pay USD floating → profits if USD rates fall, currency still hedged"))
    sub("Unhedged cross-currency: the carry trade", 5,
      P("<b>In plain words:</b> borrow in a low-rate currency, deposit in a high-rate currency. It earns the rate gap unless the high-rate currency falls.") +
      F("Borrow USD 1-yr at 1% ; roll 90-day INR at 5% ; INR/USD 70\nStable: (1 + 0.05/4)⁴ − 1 = 5.1% → profit <b>4.1%</b>\nINR rates 5, 6, 4, 3%: (1.0125)(1.015)(1.01)(1.0075) − 1 = 4.6%\nINR/USD 70 → 85: USD/INR 0.014286 → 0.011765 = <b>−17.6%</b>\nTotal = 4.6 − 1.0 − 17.6 = <b>−14.0%</b> (crisis / flight to quality)") +
      K("Swap views across markets: receive floating where rates will rise, pay floating where they will fall; receive fixed where rates will fall, pay fixed where they will rise; watch FX",
        "Quiz: foreign bull steepener + stable, higher-yield domestic curve → <b>pay foreign floating, receive domestic fixed</b> (C)") +
      TRAP("Carry trade profits mean <b>uncovered</b> parity fails — covered parity is not involved (quiz B)."))
    sub("Evaluating a yield curve strategy (scenario analysis)", 5,
      F("US manager, Canadian zeros, 1 year, CAD −0.5%, yields +25 bp\nCoupon: 0 (zeros) ; spread: 0\nBullet rolldown (98.75 − 96.75)/96.75 = 2.067% ; yield −4.89×0.0025 + ½×28.5×0.0025² = −1.214%\nBarbell rolldown (98.95 − 97)/97 = 2.010% ; yield −4.92×0.0025 + ½×43×0.0025² = −1.217%\nUSD: bullet (1 + 0.02067 − 0.01214)(0.995) − 1 = <b>0.35%</b> ; barbell <b>0.29%</b>\nBullet wins by 6 bp — sits on a steeper part of the curve (more rolldown)") +
      F("Quiz: barbell 60% 2-yr + 40% 10-yr; bear flattener 2-yr +50, 10-yr +30\n2-yr −0.92% ; 10-yr −9.52×0.003 + ½×104.8×0.003² = −2.81%\n0.6 × (−0.92) + 0.4 × (−2.81) = <b>−1.68%</b>") +
      TRAP("Schweser recommends <b>compounding</b> currency (multiplicative). Adding it, as in an earlier reading, is unlikely to be marked wrong."))
