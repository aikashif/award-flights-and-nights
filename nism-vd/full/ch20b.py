from summary_lib import *

def add(chap, sub):
    sub("Lot size, tick value & contract value", 5,
      T(["Contract","Contract value","Tick value / lot"],
        [["GOI bond futures","2,000 × price; 5 lots at 101 → ₹10,10,000","2,000 × 0.0025 = <b>₹5</b>"],
         ["91-day T-bill futures","2,000 × (100 − 0.25y) × lots; 10 lots at 95 (y = 5%) → ₹19,75,000","2,000 × 0.0025 × 0.25 = <b>₹1.25</b>"],
         ["Overnight MIBOR futures","Rate × 100 × 411 × lots; 10 lots at 4.50% → ₹18,49,500","411 ÷ 4 = <b>₹102.75</b>"]]) +
      K("Bond futures FV always a multiple of ₹2 lakh (no ₹3 or ₹5 lakh)","Wholesale cash market lot ₹5 crore = 250 futures contracts",
        "Market value = face value × price ÷ 100","Contract value drives margins, transaction and regulatory charges") +
      F("Sample: 10 lots of bond futures at ₹99 → 10 × 2,000 × 99 = <b>₹19,80,000</b>"))
    sub("Why exchange-traded IRDs in India", 4,
      L("Banks, insurers, PDs, provident funds hold &gt; <b>80%</b> of G-sec rate risk — need a credible 'true hedge'",
        "Households: savings + housing loans → rate risk; <b>Fisher effect</b> (expected inflation ↑ → nominal rate ↑) makes IRDs the main inflation hedge",
        "Policy aim: <b>market completion</b> — wider hedging tools",
        "Exchange benefits: near-zero counterparty/settlement risk, transparency, wider reach — complementary to OTC",
        "OIS is successful but not a true hedge for the stock of G-secs",
        "G-sec curve = risk-free proxy for time value of money; all assets priced at a spread over it"))
    sub("FRA vs interest rate futures", 5,
      T(["Parameter","FRA","IRF"],
        [["Mechanism","Bilateral OTC (may use e-platform)","Exchange platform"],["Terms","Custom","Standardised"],
         ["Underlying","Usually interest rate","Rate, instrument, index"],["Price discovery","Negotiation — not efficient","Free interaction on exchange"],
         ["Liquidity","Low","High"],["Market maker","Scheduled banks, PDs, AIFIs","Currently not applicable"],
         ["Settlement","Bilateral, usually cash","Clearing corporation, guaranteed; cash or physical"],
         ["Information","Report to trade repository within <b>30 minutes</b>","Online nationwide"]]) +
      T(["","Advantages","Limitations"],
        [["FRA","Perfect hedge (custom); fewer margin/MTM issues","Liquidity risk, counterparty risk, not open to all"],
         ["IRF","Transparency; no counterparty risk; open to all; credit agnostic; lower liquidity risk; lower impact cost","Imperfect hedge (fixed size/date); MTM and margin operations"]]) +
      K("FRA: borrower long the rate; benchmark &gt; FRA rate → long receives; below → long pays",
        "Bond/index futures buyer is long bond = <b>short the rate</b>"))
    sub("Forward rates", 5,
      F("₹1,000 for 2 yrs: 2-yr spot 6% → 1,123.60 ; 1-yr spot 5% then F\n1,000 × 1.06² = 1,000 × 1.05 × (1 + F) → <b>F = 7.0095%</b>\nF = [(1 + S1)^n1 ÷ (1 + S2)^n2]^(1/(n1 − n2)) − 1\n6-m spot 5.60%, 1-yr spot 5.85% (semi-annual) → 6-m rate 6 m from now = <b>6.10%</b>") +
      K("No arbitrage: one long investment = rolled short investments"))
    sub("Cost of carry, income & basis", 5,
      L("Financing cost = interest to carry the asset to expiry",
        "Income on cash position = accrued interest to expiry + coupons received + interest on reinvested coupons",
        "<b>Basis = spot − futures</b>",
        "Futures &gt; spot → <b>negative basis</b> (contango); futures &lt; spot → <b>positive basis</b> (backwardation)",
        "Bond futures: basis usually <b>positive</b> — income on bond &gt; financing cost, so futures trade at a discount"))
    sub("Bond futures pricing (worked)", 5,
      F("Futures price = cash price + financing cost − income on cash position\n5.75% GS; last coupon 29 Apr; trade 3 Aug, settle 4 Aug (T+1); clean 101.5000\nAI (30/360, 29 Apr–4 Aug) = 1.5174 → dirty (A) = 103.0174\nFinancing 4% on dirty, 4–27 Aug, Actual/365 → (B) = 0.2597\nFuture dirty = 103.2771 ; AI 29 Apr–27 Aug (C) = 1.8847\nTheoretical futures clean = A + B − C = <b>101.3924</b>") +
      K("Each participant has its own funding cost → many 'fair values' — that keeps the market trading",
        "Assumptions: underlying plentiful · easy to hold · can be shorted · no transaction costs · no taxes · no margins",
        "Not valid for non-storable or non-shortable assets"))
    sub("Expectancy model & convergence", 5,
      L("Futures price = <b>expected future spot price</b>; matters most when asset can't be stored or shorted",
        "Futures may trade at premium or discount; show expected direction",
        "Futures &gt; spot bond price → market expects rates ↓ (prices ↑); futures &lt; spot → expects rates ↑",
        "Oct-2021 6.10% GS 2031 futures at ₹98.50 in Sep → market expects spot ₹98.50 at close on last Thursday (28 Oct 2021)",
        "Futures and spot <b>converge at expiry</b> — all futures settle at underlying cash price"))
    sub("91-day T-bill futures pricing", 4,
      L("Use forward rate: trade 1 Oct 2021, expiry 27 Oct 2021 → need 26-day and 117-day yields from FBIL T-bill curve (interpolate/extrapolate if missing)",
        "Forward formula gives the 91-day rate on 27 Oct","All models theoretical, based on assumptions"))
    sub("Workbook sample answers", 3,
      K("91-day T-bill futures = cash settled","Cash-settled 10-yr bond futures last trading day = last Thursday","Total contracts outstanding = open interest","Short at 100, expiry 101 → loss ₹1","10 lots at 99 → ₹19,80,000"))
