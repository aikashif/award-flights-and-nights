"""NISM V-D derivatives modules (Ch13-22) summary -> PDF. Run: python3 nism-vd/deriv_summary.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from summary_lib import *

CH = []
def chap(n, title, marks, stars):
    CH.append({"n": n, "title": title, "marks": marks, "stars": stars, "subs": []})
def sub(title, stars, body):
    CH[-1]["subs"].append({"t": title, "s": stars, "b": body})

# ================================================================ CH 13
chap(13, "Basics of Derivatives", "10", 5)
sub("Definition & underlying", 4,
  KV([("Derivative","Contract whose value is derived from an underlying"),
      ("Underlying","Shares, index, commodity, currency, interest rate, bond, credit, weather…"),
      ("Legal (India)","SCRA 1956 Sec 2(ac): derivative = security (amended 1999)"),
      ("Key features","Leverage · zero-sum (before costs) · future settlement · notional value")]) +
  K("Notional value = price × lot × lots","Zero-sum: one side's gain = other side's loss"))
sub("Types of derivatives", 5,
  T(["Type","What","Traded"],
    [["Forward","Agreement to buy/sell later at price fixed today","OTC"],
     ["Futures","Standardised forward, daily MTM","Exchange"],
     ["Option","Right (not obligation) to buy (call) / sell (put)","Both"],
     ["Swap","Exchange of cash-flow streams (e.g. fixed ↔ floating)","OTC"],
     ["Others","Warrants, LEAPS (long-dated options), basket options, swaptions","Varies"]]))
sub("Exchange-traded vs OTC", 5,
  T(["Feature","Exchange-traded","OTC"],
    [["Terms","Standardised","Customised"],["Counterparty risk","None to traders (clearing corp, novation)","Yes"],
     ["Margins / MTM","Mandatory, daily","Usually none / bilateral"],["Liquidity","High","Low"],
     ["Transparency","Public prices","Private"],["Regulation","SEBI (exchange)","RBI for OTC rate/FX"],["Examples","Index futures, stock options, IRF","Forwards, IRS, FRA"]]))
sub("Participants", 5,
  T(["Participant","Goal","Example"],
    [["Hedger","Reduce existing risk","Fund sells index futures to protect portfolio"],
     ["Speculator","Profit from view; takes risk; gives liquidity","Buys futures expecting a rise"],
     ["Arbitrageur","Riskless profit from mispricing; aligns prices","Buy spot, sell overpriced futures"],
     ["Margin trader","Uses leverage of margin","Buys futures instead of cash shares"]]))
sub("Economic functions", 3,
  K("Price discovery","Risk transfer (hedgers → speculators)","More liquidity in cash market","Lower transaction cost","Market completeness","Encourages entrepreneurial activity") +
  TRAP("Derivatives do NOT guarantee returns or create wealth."))
sub("History — world", 2,
  K("Rice futures, Dojima Japan (1700s)","Chicago Board of Trade (CBOT) 1848 — first organised futures exchange","Currency futures CME 1972","CBOE options 1973","Black-Scholes model 1973"))
sub("History — India", 4,
  T(["Year","Event"],
    [["1996–98","L.C. Gupta Committee — framework for derivatives trading"],
     ["1998","J.R. Varma Committee — risk containment (margins)"],
     ["1999","SCRA amended — derivatives = securities"],
     ["Jun 2000","Index futures (first)"],["Jun 2001","Index options"],["Jul 2001","Stock options"],["Nov 2001","Stock futures"],
     ["2008","Currency futures"],["2009/2014","IRF relaunch / cash-settled bond futures " + V],["2018–19","Physical settlement of stock F&amp;O"]]) +
  K("Badla (carry-forward) system banned 2001"))
sub("Clearing & settlement", 4,
  KV([("Clearing corporation","Central counterparty: buyer to every seller, seller to every buyer (novation)"),
      ("Members","Trading member (TM) · Clearing member (CM) · Self-clearing member · Professional clearing member (clears for others, doesn't trade)"),
      ("Settlement Guarantee Fund (SGF)","Covers member default so settlement completes"),
      ("MTM settlement","Daily, in cash (T+1)"),
      ("Final settlement","Index: cash · Stocks: physical delivery")]))
sub("Margins & risk management", 5,
  T(["Margin","Rule"],
    [["Initial margin","SPAN (scenario worst-case loss, portfolio-based, VaR) — paid upfront"],
     ["Exposure / ELM margin","Extra flat % over SPAN"],["MTM","Daily P&amp;L in cash"],
     ["Premium","Option buyer pays full premium upfront"],["Delivery margin","Near expiry for physically settled positions"],
     ["Who pays","Futures: both sides · Options: seller only"]]) +
  K("Position limits: client, trading member, market-wide","MWPL: stock enters ban at 95% OI; exits below 80%","Peak margin reporting " + V))
sub("Risks in derivatives", 3,
  K("Leverage risk","Market risk","Counterparty risk (OTC)","Liquidity risk","Basis risk","Operational / legal risk","Model risk"))
sub("Regulation & stock eligibility", 2,
  K("SCRA 1956, SEBI Act 1992, SEBI regulations, exchange bye-laws","Stocks chosen by market cap, liquidity, MWPL, median order size " + V,"Min contract value for index derivatives ₹15–20 lakh (Nov 2024) " + V,"One weekly index expiry per exchange " + V))
sub("Taxation of derivatives", 3,
  T(["Item","Rule " + V],
    [["F&amp;O income","Non-speculative business income (Sec 43(5))"],["Losses","Set off vs business income; carry forward 8 years"],
     ["STT futures","On sell side, % of value (raised Oct 2024; check latest)"],["STT options","On premium (sell); on intrinsic value if exercised"],
     ["Audit","Turnover-based tax audit rules"]]))

# ================================================================ CH 14
chap(14, "Understanding Index", "≈4–6", 3)
sub("What an index is & uses", 3,
  K("Barometer of market","Benchmark for funds","Underlying for index funds, ETFs, futures, options","Measures relative change from base"))
sub("Index construction", 4,
  F("Index value = Current market cap ÷ Base market cap × Base value\n(Free-float market cap = Price × Shares × Investible weight factor)\nDivisor adjusted for corporate actions so the index doesn't jump") +
  KV([("Base date / value","Starting point (e.g. Nifty 1,000 on 3 Nov 1995)"),
      ("Selection","Liquidity (impact cost), free float, market cap, listing history"),
      ("Rebalancing","Semi-annual review; replacement on delisting/merger")]))
sub("Weighting methods", 5,
  T(["Method","Weight by","Example / note"],
    [["Free-float market cap","Price × public float shares","Nifty 50, Sensex (standard in India)"],
     ["Full market cap","Price × all shares","Older method"],["Price-weighted","Share price only","Dow Jones; high-price stock dominates"],
     ["Equal-weighted","Same weight","Nifty 50 Equal Weight; needs frequent rebalancing"],["Factor / fundamental","Earnings, value, momentum etc.","Smart-beta indices"]]) +
  TRAP("In a market-cap index, a split or bonus does NOT change the index (market cap unchanged). Rights/new issues do → divisor changes."))
sub("Free float", 4,
  KV([("Free float","Shares available for public trading"),
      ("Excludes","Promoter holdings, govt strategic holding, locked-in shares, cross-holdings, FDI strategic stakes"),
      ("Investible weight factor (IWF)","Free-float shares ÷ total shares")]))
sub("Major Indian indices", 3,
  T(["Index","Stocks","Base","Base value"],
    [["Nifty 50 (NSE)","50","3 Nov 1995","1,000"],["BSE Sensex","30","1978–79","100"],
     ["Nifty Bank","Banking stocks","1 Jan 2000","1,000"],["Nifty Next 50","50","",""],["Nifty Midcap 150 / Smallcap 250","150 / 250","",""]]) )
sub("Desirable attributes & impact cost", 4,
  F("Ideal price  = (best bid + best ask) ÷ 2\nImpact cost  = (actual execution price − ideal price) ÷ ideal price × 100\nLower impact cost = more liquid") +
  K("Diversified (low unsystematic risk)","Liquid (low impact cost)","Professionally maintained","Transparent rules"))
sub("Index-based products & uses", 3,
  K("Index funds","ETFs (traded on exchange)","Index futures &amp; options","Benchmarking","Beta hedging","Tracking error = SD of return difference"))

# ================================================================ CH 15
chap(15, "Forwards & Futures", "15", 5)
sub("Forward contracts", 4,
  KV([("Features","OTC, bilateral, customised size/date, settled at maturity"),
      ("Limitations","Counterparty risk · illiquid · no price transparency · hard to exit"),
      ("Use","Exact-date hedges (e.g. exporter with bank)")]))
sub("Futures: features", 5,
  K("Standardised (lot, expiry, quality)","Exchange-traded","Clearing corp guarantee","Daily MTM","Both sides post margin","Can close before expiry by opposite trade","Linear payoff"))
sub("Futures terminology", 5,
  T(["Term","Meaning"],
    [["Spot price","Current cash-market price"],["Futures price","Agreed price for future date"],
     ["Contract cycle","3 months: near, mid, far"],["Expiry day","Last trading day of contract " + V],
     ["Lot / contract size","Fixed quantity per contract"],["Basis","Spot − Futures"],
     ["Cost of carry","Interest − income (dividend)"],["Initial margin","Upfront deposit (SPAN + exposure)"],
     ["MTM","Daily settlement of P&amp;L"],["Open interest","Outstanding contracts"],["Settlement price","Price used for MTM"]]))
sub("Futures payoff", 5,
  PO(payoff("Long futures","5,65 115,5","Gain if price ↑, unlimited both ways"),
     payoff("Short futures","5,5 115,65","Gain if price ↓"),
     payoff("Long spot + short futures","5,35 115,35","Hedged: flat")) +
  K("Linear and symmetric","P&amp;L = (exit − entry) × lot × lots"))
sub("Pricing: cost of carry", 5,
  F("Simple:       F = S × (1 + r × t)\nContinuous:   F = S × e^(r t)\nWith dividend: F = (S − PV(D)) × e^(r t)   or  F = S × e^((r − d) t)\nCommodities:  F = S × e^((r + storage − convenience yield) t)\n\nEx: S 1,000, r 8%, 3 months → simple 1,020 · continuous 1,020.20") +
  K("Fair value ignores views about future price","Higher r → higher F","Higher dividend → lower F"))
sub("Basis, contango, backwardation, convergence", 5,
  T(["Term","Condition"],
    [["Contango (normal)","F &gt; S, basis negative"],["Backwardation","F &lt; S, basis positive (dividend &gt; interest)"],
     ["Convergence","F → S as expiry nears; basis = 0 at expiry"],["Basis strengthens","S − F rises → good for long spot + short futures"]]))
sub("Uses: hedge, speculate, arbitrage", 5,
  T(["Situation","Trade"],
    [["Hold shares, fear fall","Sell futures (short hedge)"],["Will buy later, fear rise","Buy futures (long / anticipatory hedge)"],
     ["Bullish with limited cash","Buy futures (leverage)"],["Futures overpriced","Cash-and-carry: buy spot + sell futures"],
     ["Futures underpriced","Reverse cash-and-carry: sell spot + buy futures"]]) +
  K("Arbitrage funds earn ≈ money-market rate"))
sub("Beta hedging", 5,
  F("Lots to hedge fully  = Portfolio value × β ÷ (Futures price × lot)\nChange beta β₀ → β₁  = (β₁ − β₀) × Portfolio ÷ (Futures price × lot)   (−) sell · (+) buy\n\nEx: ₹1.5 cr, β 1.25, Nifty 25,000, lot 75 → 1.875 cr ÷ 18.75 L = 10 lots (sell)") +
  K("Fully hedged portfolio earns ≈ risk-free rate","Hedge removes market risk, not stock-specific risk"))
sub("Open interest & volume", 4,
  T(["Price","OI","Reading"],
    [["↑","↑","Long build-up (bullish)"],["↓","↑","Short build-up (bearish)"],["↑","↓","Short covering"],["↓","↓","Long unwinding"]]) +
  K("Volume = contracts traded today; OI = contracts still open"))
sub("Spreads & rollover", 3,
  K("Calendar spread: buy one expiry, sell another (same underlying) — lower margin","Inter-commodity spread: two related underlyings","Rollover: close near month, open next month; cost = spread"))
sub("Contract specifications (India)", 4,
  T(["Item","Index futures","Stock futures"],
    [["Settlement","Cash","Physical delivery"],["Cycle","3 monthly","3 monthly"],["Final settlement price","Closing index value on expiry","Closing price on expiry"],
     ["Lot","Min contract value ₹15–20 lakh " + V,"Set per stock " + V],["MTM","Daily","Daily"]]))
sub("Basis risk & cross hedge", 3,
  K("Basis risk: hedge closed before expiry or asset ≠ futures underlying","Cross hedge: e.g. mid-cap portfolio with Nifty futures","Perfect hedge only with same asset held to expiry"))

# ================================================================ CH 16
chap(16, "Introduction to Options", "13", 5)
sub("Option basics", 5,
  T(["Term","Meaning"],
    [["Call","Right to BUY at strike"],["Put","Right to SELL at strike"],["Buyer (holder)","Pays premium; has right"],
     ["Seller (writer)","Gets premium; has obligation; pays margin"],["Strike (K)","Exercise price"],["Premium","Price of option"],
     ["European","Exercise only on expiry (India: index &amp; stock options)"],["American","Exercise any time till expiry"]]))
sub("Moneyness", 5,
  T(["","Call","Put"],[["ITM","S &gt; K","S &lt; K"],["ATM","S = K","S = K"],["OTM","S &lt; K","S &gt; K"]]) +
  TRAP("Put with K 1,100 when S 1,050 is ITM by 50."))
sub("Intrinsic & time value", 5,
  F("Call IV = max(0, S − K)        Put IV = max(0, K − S)\nPremium = Intrinsic value + Time value\nOTM/ATM: premium = 100% time value · at expiry time value = 0\nEx: S 520, call K 500 @ 32 → IV 20, TV 12") +
  K("Time value highest ATM","Time value decays faster near expiry"))
sub("Payoff profiles", 5,
  PO(payoff("Long call","5,45 60,45 115,5","Max loss premium · BE K+P"),
     payoff("Short call","5,25 60,25 115,65","Max gain premium · loss unlimited"),
     payoff("Long put","5,5 60,45 115,45","Max gain K−P · BE K−P"),
     payoff("Short put","5,65 60,25 115,25","Max gain premium · max loss K−P"),
     payoff("Long futures (compare)","5,65 115,5","Linear"),
     payoff("Protective put","5,45 60,45 115,5","Stock + long put = call shape")) +
  T(["Position","Max profit","Max loss","Breakeven"],
    [["Long call","Unlimited","Premium","K + P"],["Short call","Premium","Unlimited","K + P"],
     ["Long put","K − P","Premium","K − P"],["Short put","Premium","K − P","K − P"]]))
sub("Factors affecting premium", 5,
  T(["Factor ↑","Call","Put"],
    [["Spot price","↑","↓"],["Strike price","↓","↑"],["Volatility","↑","↑"],["Time to expiry","↑","↑ (usually)"],
     ["Interest rate","↑","↓"],["Dividend","↓","↑"]]))
sub("Option Greeks", 5,
  T(["Greek","Measures","Long call","Long put","Key point"],
    [["Delta","Δ premium per ₹1 spot","0 to +1","−1 to 0","ATM ≈ ±0.5; = hedge ratio"],
     ["Gamma","Δ delta per ₹1 spot","+","+","Highest ATM near expiry; same for call &amp; put"],
     ["Theta","Δ premium per day","−","−","Time decay; sellers gain"],
     ["Vega","Δ premium per 1% vol","+","+","Highest ATM, long-dated"],
     ["Rho","Δ premium per 1% rate","+","−","Least important"]]) +
  F("Δ premium ≈ delta × Δspot   ·   new delta ≈ delta + gamma × Δspot\nEx: delta 0.6, spot +10 → premium +6"))
sub("Pricing models", 3,
  T(["Model","Points"],
    [["Binomial","Price moves up/down each step; works for American"],
     ["Black-Scholes (1973)","European; inputs S, K, t, r, σ (+ dividend); assumes lognormal prices, constant σ and r, no costs"]]) +
  K("Only σ is not directly observable","Implied volatility = σ backed out from market premium"))
sub("Put-call parity", 4,
  F("C + K·e^(−rt) = P + S        (European, same K and expiry)\nEx: C 50, S 1,000, PV(K) 980 → P = 50 + 980 − 1,000 = 30\nSynthetic long futures = long call + short put") )
sub("Volatility", 4,
  KV([("Historical volatility","From past prices (SD of returns, annualised)"),
      ("Implied volatility (IV)","From current option prices; market's expectation"),
      ("India VIX","NSE volatility index from Nifty option IVs; 'fear gauge'"),
      ("Put-call ratio (PCR)","Put OI ÷ call OI — sentiment indicator")]))
sub("Options vs futures", 4,
  T(["","Futures","Options (buyer)"],
    [["Obligation","Both sides","Buyer: right only"],["Upfront","Margin","Premium"],["Payoff","Linear","Non-linear"],["Max loss","Unlimited","Premium"]]))
sub("Contract specs & margins (India)", 4,
  T(["Item","Index options","Stock options"],
    [["Style","European","European"],["Settlement","Cash","Physical delivery"],["Premium settlement","T+1","T+1"],
     ["Margin","Seller: SPAN + exposure · buyer: premium","Same"],["Exercise","Auto-exercise of ITM at expiry","Same"]]) +
  K("STT on exercised options: on intrinsic value " + V))

# ================================================================ CH 17
chap(17, "Strategies using Futures & Options", "≈8–10", 5)
sub("Hedging strategies", 5,
  T(["Strategy","Build","Effect"],
    [["Protective put","Long stock + long put","Floor on loss; keeps upside; costs premium"],
     ["Covered call","Long stock + short call","Extra income; caps upside"],
     ["Collar","Long stock + long put + short call","Low-cost floor and cap"],
     ["Short futures hedge","Long stock + short futures","Locks value (both ways)"]]) +
  PO(payoff("Protective put","5,45 60,45 115,5","= long call shape"),
     payoff("Covered call","5,65 60,25 115,25","= short put shape"),
     payoff("Collar","5,48 40,48 80,22 115,22","Floor + cap")))
sub("Spread strategies", 5,
  T(["Spread","Build","View","Net","Max profit","Max loss"],
    [["Bull call","Buy low-K call, sell high-K call","Mod. bullish","Debit","K₂−K₁−net","Net debit"],
     ["Bull put","Sell high-K put, buy low-K put","Mod. bullish","Credit","Net credit","K₂−K₁−credit"],
     ["Bear put","Buy high-K put, sell low-K put","Mod. bearish","Debit","K₂−K₁−net","Net debit"],
     ["Bear call","Sell low-K call, buy high-K call","Mod. bearish","Credit","Net credit","K₂−K₁−credit"]]) +
  PO(payoff("Bull call spread","5,45 45,45 75,25 115,25","BE = K₁ + net debit"),
     payoff("Bear put spread","5,25 45,25 75,45 115,45","BE = K₂ − net debit"),
     payoff("Bull put spread","5,48 45,48 75,26 115,26","Credit")))
sub("Volatility strategies", 5,
  T(["Strategy","Build","View","Breakevens"],
    [["Long straddle","Buy call + put, same K","Big move either way","K ± total premium"],
     ["Short straddle","Sell call + put, same K","No move; unlimited risk","K ± total premium"],
     ["Long strangle","Buy OTM call + OTM put","Big move; cheaper","K_put − prem, K_call + prem"],
     ["Short strangle","Sell OTM call + OTM put","Range-bound","Same"],
     ["Long butterfly","Buy 1 K₁, sell 2 K₂, buy 1 K₃ (calls)","Price stays near K₂; limited risk","K₁+debit, K₃−debit"]]) +
  PO(payoff("Long straddle","5,5 60,55 115,5","Same strike"),
     payoff("Long strangle","5,5 45,50 75,50 115,5","Two strikes"),
     payoff("Long butterfly","5,45 35,45 60,15 85,45 115,45","Low volatility")) +
  TRAP("Straddle = same strike · strangle = different strikes."))
sub("Synthetic positions", 4,
  T(["Synthetic","Equals"],
    [["Long call + short put (same K)","Long futures"],["Short call + long put","Short futures"],
     ["Long stock + long put","Long call"],["Long stock + short call","Short put"],["Long futures + long put","Long call"]]))
sub("Strategy selection matrix", 5,
  T(["View ↓ / Volatility →","Expect ↑ volatility","Expect ↓ volatility"],
    [["Bullish","Long call, bull call spread","Short put, bull put spread"],
     ["Bearish","Long put, bear put spread","Short call, bear call spread"],
     ["Neutral","Long straddle / strangle","Short straddle / strangle, butterfly"]]))
sub("Arbitrage strategies", 3,
  K("Cash-and-carry (spot vs futures)","Conversion: long stock + long put + short call (parity)","Reversal: short stock + short put + long call","Box spread: bull call + bear put = riskless (K₂−K₁)"))
sub("Directional trades", 4,
  K("Bullish: long futures / long call / short put","Bearish: short futures / long put / short call","Futures: linear, margin both sides","Long options: limited loss, time decay"))

# ================================================================ CH 18
chap(18, "Interest Rates, Instruments & Fixed Income Markets", "≈6", 4)
sub("Interest rate basics", 4,
  F("Simple:     FV = P × (1 + r t)\nCompound:   FV = P × (1 + r/m)^(m t)\nContinuous: FV = P × e^(r t)\nEffective annual rate = (1 + r/m)^m − 1\nPV = FV ÷ (1 + r)^t\nReal rate ≈ nominal − inflation") +
  K("Time value of money","Discounting","Rule of 72"))
sub("Monetary policy tools (RBI)", 4,
  T(["Tool","Meaning"],
    [["Repo rate","RBI lends to banks against G-secs (policy rate)"],["SDF","Standing Deposit Facility — floor of corridor"],
     ["MSF","Marginal Standing Facility — ceiling, penal borrowing"],["Reverse repo","Banks park with RBI (now below SDF)"],
     ["CRR","Cash reserve with RBI (% of deposits)"],["SLR","Liquid assets (G-secs) held by banks"],["OMO","RBI buys/sells G-secs to manage liquidity"]]) +
  K("Corridor: SDF ≤ repo ≤ MSF " + V))
sub("Money market instruments", 4,
  T(["Instrument","Feature"],
    [["Call / notice / term money","1 day / 2–14 days / 15 days–1 yr interbank"],["T-bills","91/182/364 days, discount, GoI"],
     ["Cash management bills","&lt;91 days, GoI"],["CP","Companies, 7 days–1 yr"],["CD","Banks, 7 days–1 yr"],
     ["Repo / TREPS","Collateralised borrowing"],["MIBOR","Mumbai interbank overnight rate (benchmark for OIS)"]]))
sub("Government securities market", 3,
  K("Dated G-secs, T-bills, SDLs, STRIPS","RBI manages issuance (auctions: uniform price / multiple price)","Primary dealers underwrite","NDS-OM trading platform; SGL accounts","RBI Retail Direct for individuals","Zero credit risk; benchmark for other rates"))
sub("Bond features", 4,
  T(["Feature","Meaning"],
    [["Face value","Par, repaid at maturity (₹100 quote basis)"],["Coupon","Annual interest % of face"],["Maturity","Redemption date"],
     ["Zero-coupon","No coupon, issued at discount"],["Floating rate","Coupon resets to benchmark"],["Call / put option","Issuer can redeem early / investor can sell back"],
     ["Credit rating","AAA highest; below BBB− = junk"]]))
sub("Bond pricing", 5,
  F("Price = Σ C/(1+y)^t + FV/(1+y)^n\nDirty (full) price = Clean price + Accrued interest\nPrice ↑ when yield ↓ (inverse)\nCoupon &gt; yield → premium bond · coupon &lt; yield → discount bond · equal → par"))
sub("Yield measures", 5,
  T(["Measure","Formula / meaning"],
    [["Coupon rate","Coupon ÷ face value"],["Current yield","Annual coupon ÷ market price"],
     ["YTM","IRR of all cash flows held to maturity (assumes reinvestment at YTM)"],["YTC","Yield to call date"]]))
sub("Duration, PVBP, convexity", 5,
  F("Macaulay duration = weighted average time of cash flows (years)\nModified duration  = MacD ÷ (1 + y/n)\n%ΔP ≈ −MD × Δy           Ex: MD 6, y +0.25% → −1.5%\nPVBP (DV01) = MD × Price × 0.0001\nConvexity: price rises more than it falls for same Δy (helps holder)") +
  T(["Duration higher when","Duration lower when"],
    [["Longer maturity","Shorter maturity"],["Lower coupon","Higher coupon"],["Lower yield","Higher yield"],["Zero-coupon: MacD = maturity",""]]))
sub("Yield curve & term structure", 4,
  T(["Shape","Meaning"],[["Normal (upward)","Long &gt; short rates"],["Inverted","Short &gt; long; recession signal"],["Flat","Similar rates"],["Humped","Mid-tenor highest"]]) +
  K("Expectations theory","Liquidity preference theory","Market segmentation theory","Steepening / flattening"))
sub("Corporate bond market", 2,
  K("NCDs, PSU bonds","Rated by CRISIL, ICRA, CARE, India Ratings","Credit spread = corporate yield − G-sec yield"))

# ================================================================ CH 19
chap(19, "Interest Rate Derivatives (OTC)", "2", 2)
sub("Forward Rate Agreement (FRA)", 3,
  KV([("What","Lock a borrowing/lending rate for a future period"),("Settlement","Only interest difference, discounted, paid at start of period"),("Notation","3×6 FRA = 3-month period starting in 3 months")]) +
  F("Payment = (Ref rate − FRA rate) × Notional × days/365 ÷ (1 + Ref × days/365)"))
sub("Interest Rate Swap (IRS)", 3,
  K("Plain vanilla: fixed ↔ floating on notional (notional not exchanged)","OIS: floating leg = overnight MIBOR (most common in India)","MIFOR: MIBOR-forward premium based " + V,"Borrower fearing rate rise → pay fixed, receive floating"))
sub("Caps, floors, collars, swaptions", 2,
  T(["Product","Use"],[["Cap","Max rate for floating borrower (series of call options on rate)"],["Floor","Min rate for floating lender"],["Collar","Buy cap + sell floor"],["Swaption","Option to enter a swap"]]))
sub("Uses & regulation", 2,
  K("Hedge, speculate, change liability/asset profile","OTC IRD regulated by RBI","Exchange IRD by RBI + SEBI"))

# ================================================================ CH 20
chap(20, "Exchange Traded Interest Rate Futures", "10", 5)
sub("Products & history (India)", 3,
  K("2003: first IRF on NSE (low volumes)","2009: 10-yr GoI bond futures (physical, CTD basket)","2014 onwards: cash-settled single-bond futures " + V,"91-day T-bill futures","Traded on NSE, BSE"))
sub("Contract features", 4,
  T(["Item","Bond futures " + V,"T-bill futures " + V],
    [["Underlying","GoI security (e.g. 6/10/13-yr)","91-day T-bill"],["Contract size","₹2 lakh face value","₹2 lakh face value"],
     ["Quote","Clean price per ₹100","100 − annualised discount yield"],["Settlement","Cash (daily &amp; final)","Cash"],
     ["Expiry","Monthly contracts (3 serial)","Monthly"],["MTM","Daily","Daily"]]))
sub("Pricing of bond futures", 4,
  F("Futures price ≈ (Spot clean + accrued) × (1 + r t) − coupons received (with interest) − accrued at expiry\nThen ÷ conversion factor for the CTD (physical contracts)") +
  K("Cost of carry: financing cost vs coupon income","Positive carry if coupon yield &gt; repo"))
sub("CTD, conversion factor, invoice price", 5,
  T(["Term","Meaning"],
    [["Deliverable basket","Several bonds acceptable for delivery (physical contracts)"],
     ["Conversion factor (CF)","Price of a bond at the notional yield (e.g. 7%) per ₹1; coupon &gt; notional → CF &gt; 1"],
     ["Invoice price","Futures settlement price × CF + accrued interest"],
     ["CTD","Bond costing short least to deliver: min (price − F × CF); highest implied repo"],
     ["Delivery options","Quality option (which bond) + timing option — with the short"],
     ["Gross basis","Cash price − F × CF"],["Implied repo","Return from buy bond + sell futures + deliver"]]) +
  F("Ex: F 98.50, CF 1.032, AI 1.20 → invoice = 98.50 × 1.032 + 1.20 = 102.85"))
sub("Hedging with IRF", 5,
  T(["Risk","Who","Trade"],
    [["Rates ↑ (bond prices ↓)","Bond holder, bank, debt MF","Sell IRF"],["Rates ↓","Future investor, insurer","Buy IRF"]]) +
  F("N = (MD_p × V_p) ÷ (MD_f × V_f)        = PVBP_portfolio ÷ PVBP_futures\nDuration change: N = (MD_target − MD_current) × V_p ÷ (MD_f × V_f)\nEx: PVBP 4,00,000 ÷ 160 = 2,500 contracts (sell)"))
sub("Speculation & arbitrage", 4,
  K("Expect rates ↓ → buy IRF","Expect rates ↑ → sell IRF / T-bill futures","Cash-and-carry: buy bond + sell futures when implied repo &gt; repo","Reverse: short bond + buy futures when implied repo &lt; repo"))
sub("Margins & settlement", 3,
  K("Initial margin (SPAN-based) + extreme loss margin","Daily MTM in cash","Final settlement on weighted average price " + V,"Clearing corporation guarantee"))
sub("Participants", 2,
  K("Banks","Primary dealers","Mutual funds","Insurance &amp; pension funds","FPIs (limits)","Corporates","Retail"))

# ================================================================ CH 21
chap(21, "Exchange Traded Interest Rate Options", "≈5", 3)
sub("Features", 4,
  KV([("Underlying","GoI bond (price-based) " + V),("Style","European"),("Settlement","Cash"),
      ("Buyer","Pays premium"),("Seller","Pays margin")]) +
  TRAP("On a bond-PRICE option: call gains when rates fall; put gains when rates rise. On a RATE option (cap) it's the opposite."))
sub("Payoffs & uses", 4,
  T(["Position","Gains when","Use"],
    [["Long call (bond price)","Rates fall","Lock purchase price for future bond buyer"],
     ["Long put (bond price)","Rates rise","Protect bond portfolio (floor)"],
     ["Short call / put","Rates stable","Earn premium"]]))
sub("Pricing", 2,
  K("Black (1976) model for options on futures/bonds","Inputs: price, strike, time, rate, volatility of bond price","Volatility of bond price ↑ with duration"))
sub("Caps & floors as options", 3,
  K("Cap = series of caplets (calls on rate)","Floor = series of floorlets (puts on rate)","Collar = long cap + short floor"))

# ================================================================ CH 22
chap(22, "Strategies using Interest Rate Derivatives", "≈5", 4)
sub("Hedging & duration management", 5,
  T(["Goal","Trade"],
    [["Cut duration / protect portfolio","Sell IRF"],["Add duration","Buy IRF"],["Floor on bond value","Buy puts on bond price"],
     ["Lock future investment yield","Buy IRF / buy calls on bond"],["Floating borrower fears rise","Pay fixed in IRS / buy cap / sell IRF"],
     ["Investor fears fall","Receive fixed in IRS / buy floor / buy IRF"]]))
sub("Yield curve strategies", 5,
  T(["View","Trade"],
    [["Steepening (long yields ↑ more)","Buy short-tenor futures, sell long-tenor futures"],
     ["Flattening (short yields ↑ more)","Sell short-tenor futures, buy long-tenor futures"],
     ["Parallel shift","Outright long/short futures"]]) +
  K("Weight legs by PVBP so a parallel move nets to zero"))
sub("Basis & arbitrage trades", 3,
  K("Cash-and-carry (long basis): buy bond, sell futures","Reverse cash-and-carry (short basis)","Calendar spreads between IRF expiries","Implied repo vs actual repo decides"))
sub("Asset-liability management", 3,
  K("Banks: fixed assets vs floating deposits → swap or sell IRF","Insurers: long liabilities → buy duration","Corporates: convert floating loan to fixed via IRS"))

render(CH,
  eyebrow="NISM-Series-V-D · Modules 2 &amp; 3 · Equity Derivatives (Ch 13–17) · Interest Rate Derivatives (Ch 18–22)",
  title="NISM V-D Derivatives Summary",
  lead="All 10 derivatives chapters, {n} subtopics, in tables, formulas and payoff charts. Every subtopic is rated for exam importance. Derivatives = 55% of the exam. Read 5★ first.",
  foot="Built from the NISM Series VIII (equity derivatives) and interest rate derivatives syllabi that V-D draws on. Marks: Ch13 10, Ch15 15, Ch16 13, Ch19 2, Ch20 10 from published tables; others estimated. Not copied from the workbook.",
  html_name="deriv-summary.html", pdf_name="NISM-VD-Derivatives-Summary.pdf", footer_label="NISM V-D · Derivatives Summary")
