from summary_lib import *

def add(chap, sub):
    chap(19, "Interest Rate Derivatives", "2", 3)
    sub("Derivative definition & accounting criteria", 4,
      L("Derivative derived from an independent underlying; cannot exist without it (wheat farmer selling harvest forward)",
        "Accounting: <b>FAS 133</b> (US), <b>IAS 39</b> (EU), <b>AS 30</b> (India)") +
      T(["Criterion","Meaning"],
        [["1. Value linked to underlying","Price set by underlying, not by derivative demand-supply (raw material vs finished product)"],
         ["2. Settles on a 'future' date","Later than underlying settlement (underlying T+2 → derivative after T+2)"],
         ["3. No full cash outlay on trade date","Gives leverage"],
         ["4. Net settlement (FAS 133 only)","Settles or can settle on net, not gross, basis"]]) +
      K("5 asset classes: rate, credit, equity, forex, commodity · 4 generic products: forward, futures, swap, option",
        "Commodity derivatives alone for ~300 years; financial derivatives after 1970; ~two-thirds of transactions by 1990s"))
    sub("Legal definition (SCRA 1956)", 4,
      L("Securities Laws (Second Amendment) Act <b>1999</b> added derivatives to 'securities'",
        "SCRA derivative: security derived from debt, share, loan, risk instrument or contract for differences · contract deriving value from prices/index of securities · commodity derivatives · others notified by Central Govt",
        "<b>Section 18A</b>: derivative contracts legal and valid if traded on a recognised exchange, settled on its clearing house per its rules, and between parties/terms notified by Central Govt"))
    sub("Approaches to risk", 5,
      T(["Approach","Meaning"],
        [["Speculation (trading)","Taking risk — profit or loss possible"],["Hedging","Eliminates existing risk; locks future return; no explicit cost"],
         ["Insurance","Removes downside, keeps upside; explicit upfront cost; needs <b>options</b>"],
         ["Diversification","Reduces risk more than return — minimises risk per unit return"]]) +
      K("Farmer–miller forward: ₹10,000 for 100 kg wheat in 2 months; buyer long, seller short; agreed price = forward price, settlement date = expiration date",
        "Each side cuts one risk and takes another (farmer loses upside; miller loses benefit of a fall); still counterparty / no-wheat risk"))
    sub("Economic functions of derivatives", 5,
      K("Primary role: <b>risk management</b>","Hedging","Price discovery (futures/forwards show expected spot)","Market efficiency (replication keeps prices in line)",
        "Access to unavailable assets/markets (e.g. swaps give cheaper rate)","Price stability (RBI uses derivatives for INR)","More volume in underlying",
        "Speculation — calculated risk for knowledgeable traders","Shifts speculation from unorganised to organised market") +
      T(["Risk of derivatives","Meaning"],
        [["Counterparty","Default by other side"],["Price","Loss from price move"],["Leverage","Magnifies gains and losses"],["Liquidity","Can't exit"],
         ["Legal / regulatory","Enforceability"],["Operational","Fraud, poor documentation, bad execution"]]) +
      K("Read the broker's <b>Risk Disclosure Document</b>; not for those with limited resources, experience or risk tolerance"))
    sub("Forwards & FRA", 5,
      L("Forward: OTC, customised, both obliged; mostly delivery-settled; generally no margin/MTM",
        "<b>FRA</b>: exchange of interest on notional principal for a future period at agreed rate; cash-settled; borrower = long, lender = short",
        "Benchmark &gt; FRA rate → long receives difference; payment discounted to settlement date") +
      F("₹100 cr, borrow after 60 days for 91 days at 5%; 91-day T-bill at settlement 5.5%\nSaving = 100 cr × 0.5% × 91/365 = ₹12.46 lakh (before discounting)\n3×6 FRA: ₹10,00,000, FRA 5%, floating 6% → diff = 10,00,000 × 1% × 3/12 = ₹2,500\nSettlement = 2,500 ÷ (1 + 6% × 3/12) = <b>₹2,463.05</b>"))
    sub("Bond forwards (RBI 2025)", 4,
      L("RBI (Forward Contracts in Government Securities) Directions, <b>21 Feb 2025</b>; OTC",
        "Buyer agrees to buy a specific <b>G-sec only</b> on a future date at a price fixed now",
        "Eligible: residents; non-residents eligible under FEM (Debt Instruments) Regs 2019",
        "Market-makers: banks, PDs etc.; users: non-retail users under Rupee IRD Directions 2019",
        "Physical or cash settlement; cash → bilateral or RBI-approved clearing; physical → <b>CCIL</b> or approved agency"))
    sub("Futures, options, caps, floors, collars", 5,
      L("Futures = exchange-traded forwards; mostly cash-settled; margins + MTM; clearing corporation guarantees",
        "<b>Interest Rate Futures (IRF)</b>: standardised; on notional security, interest-bearing instrument, index or rate; includes money market futures",
        "<b>Interest Rate Option (IRO)</b>: OTC and exchange-traded") +
      T(["Product","Structure"],
        [["Cap","Series of interest rate <b>call</b> options (caplets); pays when rate &gt; strike"],["Floor","Series of interest rate <b>put</b> options; pays when rate &lt; strike"],
         ["Collar","Buy cap + sell floor (same rate, maturity, notional)"],["Reverse collar","Buy floor + sell cap"]]))
    sub("Swaps & swaptions", 5,
      L("Swap = series of forwards; exchange cash flows by formula on notional principal; usually one fixed, one floating",
        "IRS: fixed-to-floating or floating-to-floating") +
      F("A pays overnight MIBOR, receives 3.75% fixed; ₹100 cr; 32 days\nA pays (daily compounded MIBOR) ₹31,58,169 ; receives 100 cr × 3.75% × 32/365 = ₹32,87,671\nNet to A = +₹1,29,503 ; B = −₹1,29,503") +
      T(["Swaption","Right to enter swap as"],[["Call swaption","<b>Receiver</b> — receive fixed, pay floating"],["Put swaption","<b>Payer</b> — pay fixed, receive floating"]]) +
      K("<b>CDS</b>: protection buyer pays periodic fee; seller pays loss on reference obligation if credit event occurs"))
    sub("Four generic derivatives compared", 4,
      T(["Derivative","Feature","Market"],
        [["Forward","Buy/sell underlying for future settlement; customised","OTC"],["Futures","Same, standardised","Exchange"],
         ["Swap","Exchange returns of one asset for another / cash over a period","Mainly OTC"],["Option","Right to buy/sell for future settlement","OTC &amp; exchange"]]) +
      T(["Underlying","Forward","Futures","Swap","Option"],
        [["Interest rate / instrument","FRA, bond forward","IR &amp; bond futures","IRS","IR &amp; bond options, swaptions"],
         ["Equity","Equity forward","Equity futures","Equity swap","Equity option"],["Currency","FX forward","FX futures","FX swap","FX option"],
         ["Commodity","Commodity forward","Commodity futures","Commodity swap","Commodity option"]]) +
      K("Bond swap = sell one bond, buy another — two cash trades, not really a derivative"))
    sub("Growth drivers; IRD market size", 4,
      K("Drivers: higher volatility · global market integration · technology · better risk tools · innovation (better risk-return, lower cost)") +
      T(["BIS data","Interest rate","Currency"],
        [["ETD notional, Mar 2025 — futures / options (USD bn)","44,861 / 55,387","353 / 149"],
         ["ETD daily turnover 2024 — futures / options","10,364 / 2,262","156 / 12"],
         ["OTC notional 2024-S2 (USD bn)","5,48,341 (of 6,99,477 total)","1,30,093 FX"]]) +
      K("<b>IRDs are the largest derivatives globally</b> — every business faces interest rate risk; equity, FX, commodity risk only for some"))
    sub("Participants", 4,
      T(["Type","Role"],
        [["Hedgers","Reduce exposure — banks, MFs, insurers, corporates, home-loan borrowers, debt fund investors"],
         ["Speculators / traders","Take views; derivatives offer leverage, lower cost, speed in size"],
         ["Arbitrageurs","Exploit price gaps — cash vs derivative, OTC vs exchange, futures vs options"]]) +
      K("Participation rules from RBI, SEBI, IRDAI for banks, PDs, MFs, insurers, FPIs"))
    sub("Underlyings of IRDs", 5,
      T(["Feature","Interest rate","Notional bond","Single bond","Bond index"],
        [["Underlying","MIBOR, repo, 91-day T-bill yield","Theoretical bond, fixed coupon &amp; maturity (10-yr GoI)","Specific security (6.10% GOI 2031)","Index (8–13 yr GoI index)"],
         ["Quote","Rate","Yield or price","Price","Index value"],
         ["Settlement","Mainly cash","Cash or physical","Cash or physical","Cash"],
         ["Settlement price","From benchmark rates","Basket of deliverable bonds","Spot price of bond","Index value"]]) +
      K("Rate derivatives: borrower = long the rate (expects rise); lender = short",
        "Bond/index derivatives: buyer is <b>short the rate</b> (expects yields ↓, price ↑); seller is long the rate"))
    sub("OTC vs exchange-traded derivatives", 5,
      T(["","OTC","Exchange-traded"],
        [["Negotiation","Private, bilateral","Screen-based order matching"],["Terms","Customised","Standardised lot &amp; expiry"],
         ["Counterparty / settlement risk","Yes","No — CCP by <b>novation</b>, margins &amp; MTM"],["Transparency","Lower","Higher"],["Small sizes","Hard / costly","Possible"]]) +
      K("ETD limits: imperfect hedge (fixed size/date), cash settlement may not suit hedgers, daily MTM is operationally heavy",
        "Gap closing: exchanges offer RFQ, Exchange-for-Physical; OTC has vanilla vs exotic, e-trading, CCP clearing — <b>CCIL</b> in India"))
    sub("Workbook sample answers", 3,
      K("Role of derivatives = risk management","Largest market = interest rate derivatives","Hedgers reduce interest rate risk","FRA, IRS, IRF all are IRDs","Theoretical bond underlying = notional bond futures"))
