from summary_lib import *

def add(chap, sub):
    sub("Valuing bonds between coupon dates (worked)", 4,
      L("Dirty price = PV of the bond = clean price + accrued interest",
        "Step 1: value the bond at the previous coupon date (coupon, yield, residual maturity)",
        "Step 2: carry that value forward to the settlement date with a future value factor",
        "Step 3: deduct accrued interest → clean (trade) price") +
      F("Settle 12-Aug-2020; maturity 11-May-2030; coupon 5.79% semi-annual; yield 5.90%; 30/360E\nLast coupon 11-May-2020 → 91 days = 0.252778 yr\nAI = 5.79 × 91/360 = ₹1.4636\nDirty ₹100.6464 (sum of 20 discounted cash flows) → clean = 100.6464 − 1.4636 = ₹99.1828"))
    sub("Spot rates vs YTM; YTM drawbacks", 5,
      L("Spot (zero) rate = true return: counts premium/discount, redemption gain/loss and reinvestment; read directly from zero-coupon prices",
        "Bond price = each cash flow discounted at its own zero rate",
        "Price set by demand-supply for <b>money</b> (via zero rates), not for the bond itself",
        "A coupon bond has many returns, one per cash flow (10Y semi-annual → 20); YTM averages them into one number",
        "YTM is just another way to quote price — <b>not a true return</b> and not a test of mispricing") +
      F("3Y 8% bond, zero rates 7.75% / 8.00% / 8.25%\n8/1.0775 + 8/1.08² + 108/1.0825³ = 7.4246 + 6.8587 + 85.1413 = 99.4246 → YTM ≈ 8.29%\nBond B (9% coupon, same issuer &amp; maturity) → 101.9983, YTM 8.2215%") +
      K("Both bonds fairly priced on the same zero curve — mispricing only if market price differs from 99.4246 / 101.9983",
        "Prefer B if you expect rates to rise (more to reinvest); prefer A if capital gains taxed lower than income") +
      T(["YTM drawback","Why"],
        [["Assumes flat zero curve","Same rate for every cash flow"],["Coupon effect","Same maturity, different coupons → different YTMs"],
         ["Inconsistent reinvestment rate","Assumes each bond's own YTM; actual rates unknown"]]))
    sub("Price-yield relationship rules", 5,
      L("Inverse; uses <b>clean</b> price; curve is non-linear (convex)",
        "Longer maturity → more price volatility (same coupon and price)",
        "Higher coupon → less volatility; lower coupon → more",
        "Higher YTM → less volatility than lower YTM (same coupon and maturity)") +
      T(["Bond selling at","Coupon vs yield","CR, CY, YTM"],
        [["Par","CR = R → V = F","CR = CY = YTM"],["Discount","CR &lt; R → V &lt; F","CR &lt; CY &lt; YTM"],["Premium","CR &gt; R → V &gt; F","CR &gt; CY &gt; YTM"]]) +
      T(["Required rate (10Y 9% bond)","5%","7%","9%","11%","13%"],[["Value ₹","130.89","114.05","100.00","88.22","78.30"]]) +
      K("Each 1% rise cuts price by a smaller amount (8.81 → 4.75)"))
    sub("Price time path; pull to par", 4,
      T(["Years left","Discount (11%)","Par (9%)","Premium (7%)"],
        [["10","88.22","100","114.05"],["5","92.61","100","108.20"],["1","98.20","100","101.87"],["0","100","100","100"]]) +
      K("<b>Pull to par</b>: price moves to face value as maturity nears — premium bonds fall, discount bonds rise"))
    sub("Interest rate risk; price volatility properties", 5,
      L("Sovereign → no credit risk; held to maturity → no price/liquidity risk (pull to par); zero-coupon → no reinvestment risk",
        "Price risk and reinvestment risk act in opposite ways; price effect is instant, reinvestment effect slow",
        "Longer bonds more sensitive: 25 bp move → 2030 bond ≈ ₹1.6–2.1, 2060 bond ≈ ₹2.4–4.9",
        "5.79% GS 2030: +25 bp → −1.89%; −25 bp → +1.93%; SD of price changes for 50 bp shocks ≈ 4× that for 25 bp") +
      T(["Property (option-free bond)","Point"],
        [["1","% price change differs across bonds with different coupon, maturity, yield (8.50% GS 2030 falls 1.76% vs 1.89% for 5.79% GS 2030)"],
         ["2","Very small yield change (1–2 bp): % change ≈ same up or down"],
         ["3","Large change (100–200 bp): up and down moves differ"],
         ["4","Price gain when yields fall &gt; price loss when yields rise (5.79% GS 2030: +7.88% vs −7.18% for 100 bp) — due to <b>convexity</b>"]]))
    sub("Macaulay duration", 5,
      L("Time-weighted average of PV of cash flows; weighted average maturity / payback period; in <b>years</b>",
        "Zero-coupon: duration = maturity; coupon bond: duration &lt; maturity",
        "Falls as time passes; does not rise endlessly with maturity — it levels off",
        "5.77% GS 2030 at 5.85% → 7.50 yrs; at 6.50% → 7.43 yrs") +
      F("Mac D = Σ [PV(CFt) × t] ÷ market price\nSpreadsheet: 5.79% GS 2030 on 07-Jul-20 → 761.4442 ÷ 100.5953 = 7.5694 yrs") +
      T(["Bond (5.77%)","Yield","Duration"],[["2030","5.85%","7.50"],["2060","6.50%","14.67"],["2090","6.80%","14.93"]]) +
      T(["Factor ↑","Duration"],[["Maturity","↑"],["Coupon","↓"],["Yield (YTM)","↓"]]))
    sub("Portfolio duration", 4,
      F("D portfolio = Σ wi × Di\n30% in 3-yr + 70% in 5-yr → 0.3×3 + 0.7×5 = 4.40 yrs"))
    sub("Modified duration", 5,
      F("MD = Mac D ÷ (1 + YTM/n)     n = coupons per year\nMac D 5.34, yield 4.5%: annual → 5.11 ; semi-annual → 5.34/1.0225 = 5.22\n% ΔPrice ≈ −MD × ΔYield") +
      K("MD 5.11 → 100 bp yield move ≈ 5.11% price move, opposite direction","Applies to the <b>dirty</b> price",
        "Linear approximation — good for small moves, poor for large ones; convexity fixes this"))
    sub("PV01 (price value of a basis point)", 5,
      F("PV01 = Dirty price × MD ÷ 10,000\nPrice 100 → 99.95 for 1 bp → PV01 = ₹0.05 (5 paise)"))
    sub("Convexity", 5,
      L("Duration = first derivative (tangent line); convexity = second derivative — curvature of price-yield curve",
        "MD <b>overestimates</b> the fall when yields rise and <b>underestimates</b> the gain when yields fall; error grows with shock size (+2% shock: actual −11.85 vs MD −13.22)") +
      F("Approx convexity = (P₊ + P₋ − 2P₀) ÷ [2 × P₀ × (Δy)²]\nConvexity adjustment = Convexity × 100 × (Δy)²\n3-yr 10% semi-annual bond at 9% → convexity 8.2135 ; divide semi-annual convexity by 4 to annualise\n% ΔP = −MD × Δy + Convexity × 100 × (Δy)²\nMD 10.66, convexity 81.96, yield 5% → 3%: +21.32% + 3.28% = <b>+24.60%</b>\nYield 5% → 7%: −21.32% + 3.28% = <b>−18.04%</b>") +
      T(["Factor ↑","Convexity"],[["Coupon","↓"],["Yield","↓"],["Maturity","↑"]]) +
      K("Portfolio convexity = weighted sum","Positive convexity → gain on fall &gt; loss on rise"))
    sub("Role of the debt market", 4,
      L("Super asset classes: underlying, derivative, structured finance (+ collective schemes, physical, alternative assets)",
        "Underlying classes: money, bond, equity, forex — independent, 'traditional'",
        "Money + bond = fixed income market; debt + equity = capital market (money market = short-term &lt; 1 yr)",
        "Underlying markets → <b>financing</b>; derivatives → <b>risk management</b>; structured finance → both",
        "Debt = charge on income; equity return = appropriation of profit; debt avoids dilution but too much → bankruptcy risk") +
      K("Importance: govt raises debt cheaply · liquid market lowers cost for all, better pricing · less reliance on banks (risk spread) · better bank ALM · channels MFs and retail · lets pension funds/insurers match liabilities"))
