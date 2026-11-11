from summary_lib import *
from helpers import P

def add(chap, sub):
    chap(8, "P8 Case Study: Institutional (University Endowment)", "15% of PM", 5)
    sub("How to read this case", 5,
      P("<b>In plain words:</b> this reading has almost no new theory. It takes one university endowment (QU) and asks you to apply ideas from the whole curriculum: liquidity, asset allocation, ethics, derivatives, rebalancing and ESG. Expect it as an <b>essay set</b>: 'justify', 'recommend', 'identify the violation'.") +
      K("Answer with the case numbers: quote the % or bp from the exhibit, then give the reason",
        "One recommendation + one reason per point earns the marks; long lists do not"))
    sub("Managing liquidity risk: four tools", 5,
      T(["Tool","What it does"],
        [["1. Liquidity profile &amp; time-to-cash table","Sorts assets by how fast they turn into cash (e.g. highly liquid, liquid, semi-liquid, illiquid). <b>Liquidity budget</b>: minimums for liquid tiers, a <b>maximum</b> for the illiquid tier. Exit &gt; 1 year = illiquid. Same asset can differ by vehicle (ETF vs commingled fund)"],
         ["2. Rebalancing &amp; commitment policy","<b>Systematic rebalancing</b>: calendar or percent-range (wider ranges for volatile assets). <b>Automatic adjustment</b>: PE 2% under target (β ≈ 1) → hold +2% public equity → same systematic risk, less illiquidity. <b>Commitment pacing</b> model (drawdown and distribution rates); diversify across funds and vintages; scenario analysis"],
         ["3. Stress testing","Test assets <b>and</b> liabilities together: high volatility, low returns, high correlation, low liquidity, higher payouts. Base on history, statistical models or hypothetical scenarios"],
         ["4. Derivatives","Little cash needed. Futures overlay rebalances without touching external managers. Buy options = cheap leverage; sell options = premium income (liquidity)"]]) +
      TRAP("Calendar and percent-range rules are <b>systematic</b> rebalancing policies — a quiz statement that calls them something else is wrong."))
    sub("The illiquidity premium", 4,
      P("<b>In plain words:</b> investors want extra return for money they cannot get back quickly. The longer the lock-up, the bigger the premium.") +
      F("Option view: price of illiquid asset = price of same marketable asset − value of a put (the right to sell you gave up)\nIlliquidity premium = expected return of illiquid asset − expected return of marketable asset") +
      K("Hard to measure: many other factors drive returns",
        "Estimates use broad indexes, but a real investor holds few funds → more <b>unsystematic</b> risk → needs a liquidity budget") +
      TRAP("'The illiquidity premium is easy to measure' is <b>false</b>."))
    sub("QU endowment: facts you need", 5,
      T(["Item","Detail"],
        [["Size","$8bn: 75% unrestricted, 25% donor-restricted"],
         ["Role","Pays about 60% of the $583m operating budget"],
         ["Spending rule","Changed from 5% of beginning value to a <b>geometric smoothing</b> rule (uses prior spending $358.1m and prior year-end value $7,002.3m)"],
         ["Return need","7–8% nominal = 5% spending + 2–3% inflation"],
         ["Risk target","Standard deviation 12–14%"],
         ["Manager","QUINCO: 11-person board, 13 staff, <b>external managers only</b>, 5 asset classes; Board approves managers; CIO Winter leads the investment committee"]]) +
      T(["Asset class","1996","2017"],
        [["Cash","1%","1%"],["Domestic stocks + bonds","~70%","~30%"],["International developed equity","25%","10%"],["Emerging markets","0","10–15%"],
         ["Private equity","&lt; 5%","15–20%"],["Real assets","&lt; 5%","10–15%"],["Diversifying strategies","0","10–15%"]]) +
      K("Review: PE returns are smoothed → <b>unsmooth</b> them and volatility rises",
        "QU lagged peers because it took less risk and held fewer illiquid assets"))
    sub("Proposed allocation: justify it & name the trade-offs", 5,
      P("<b>In plain words:</b> CIO Thompson wants more private equity and real assets. You must argue for it, name what it costs, and say what to check.") +
      T(["Metric","Existing","Proposed"],
        [["Sharpe ratio","0.33","0.34"],["Standard deviation","12.5%","13.2% (+0.7%)"],["P(keep ≥ 75% purchasing power, 20 yrs)","65%","70%"]]) +
      K("<b>Why more illiquids:</b> long horizon lets QU earn the illiquidity premium → efficient frontier shifts up · 20 years of good private-asset results with expert managers · QU is under-weight illiquids vs peers",
        "Thompson's reasons: lower expected returns everywhere · QU takes less risk than peers · fixed income has a low Sharpe ratio · Monte Carlo shows better purchasing power",
        "<b>Trade-offs:</b> higher volatility (but needed to earn the same return) · higher fees (exhibit returns are already <b>net of fees</b>)",
        "<b>Reduce the new risk:</b> many smaller commitments (less unsystematic risk) or cash-flow modelling under stress",
        "<b>Before approving, confirm:</b> 13.2% SD and 30% chance of 25% erosion fit risk appetite · new mix still meets all liquidity needs") +
      TRAP("More illiquids raise <b>unsystematic</b> risk — diversify across many funds and vintages."))
    sub("Why liquidity gets worse in a crisis", 5,
      T(["Cause","Effect"],
        [["Capital calls &gt; distributions","PE funds call cash (a legal duty) while exits stop"],
         ["Gates / lock-ups","Hedge funds may block withdrawals"],
         ["Lagged PE valuations (denominator effect)","Public assets fall now, PE marks fall later → PE share rises, liquid share falls"],
         ["Spending rule is countercyclical","Smoothed spending is &gt; 5% of value after a fall → more cash needed exactly when markets are weak"]]) +
      T(["Profile (highly liquid / liquid / semi / illiquid)","Normal","Stress"],
        [["Existing","19 / 26 / 22 / 33","15 / 26 / 20 / 39"],["Proposed","14 / 24 / 23 / 39","11 / 25 / 21 / 43"]]) +
      K("Proposed: highly liquid −5% and illiquid +6% (normal); −4% and +4% (stress)",
        "Follow-up: cash-flow forecasts, commitment pacing, liquidity budget, regular stress tests (historical + hypothetical), monitoring at high-risk times"))
    sub("Ethics in manager selection (who broke what)", 5,
      P("<b>In plain words:</b> a donor-trustee's firm (GVC) is a finalist for a QU mandate. Many people act badly. For each person, name the Standard and the fact.") +
      T(["Person","Standards","Why"],
        [["Aaron Winter, CIO","VI(A), I(B), III(E), I(C)/III(D), V(A)","Did not disclose GVC owner's link to QU or that GVC's MD is a former colleague; under pressure; suspected confidential data and inflated returns but did not report or investigate"],
         ["Virginia Hall, trustee &amp; GVC owner","VI(A), IV(A), III(E)","Conflict (trustee + finalist owner); put own business before QU; may have obtained confidential data"],
         ["QU president &amp; treasurer","IV(A), III(E), VI(A)/I(B)","Pressured Winter to hire GVC; may have leaked data; should disclose bias and abstain from the vote"],
         ["Jason Allen, GVC MD","I(C), III(D)","Presented possibly wrong / inflated performance"],
         ["Bud Davis, senior PM","VI(A), I(B)","Spouse is Hall's daughter; recommended GVC without disclosing"]]) +
      K("Standards list: I(B) Independence &amp; Objectivity · I(C) Misrepresentation · III(D) Performance Presentation · III(E) Confidentiality · IV(A) Loyalty · V(A) Diligence · VI(A) Disclosure of Conflicts",
        "GVC context: raising $300m Fund II after a $100m Fund I; it cut its fee; rival finalist Beacher") +
      TRAP("Non-CFA people (president, treasurer) are judged by the same tests in this case answer — apply the Standards to each actor named."))
    sub("Equity exposure: ETF vs futures vs total return swap", 5,
      P("<b>In plain words:</b> QU wants +1% US large-cap ($80m) for tactical asset allocation. Compare cost, work, tracking error and risk.") +
      T(["","ETF","Futures","Total return swap"],
        [["Cost","<b>35 bp</b> (70% impact + fee)","42 bp (half is roll cost)","51 bp"],
         ["Logistics","None (ETF manager runs it)","Quarterly roll, daily margin","None"],
         ["Tracking error","Cash drag, diversification rules","Liquidity, rate differences","<b>None</b> (receives index return)"],
         ["Rate / counterparty risk","None","Interest rate risk","Rate + counterparty"],
         ["Overall (no leverage)","<b>Best</b>","",""]]) +
      F("With leverage 4 (25% cash, 75% financed): financing 2% for futures/swaps, 2.5% for ETF\nETF: 80m × 75% × 2.5% = $1.5m = 1.875% → total 0.35 + 1.875 = <b>2.225%</b>\nFutures: 80m × 75% × 2% = $1.2m = 1.5% → total 0.42 + 1.5 = <b>1.92%</b> (cheapest by 9 bp)\nSwap: 1.5% + 0.51 = <b>2.01%</b>") +
      K("Policy changes: tracking error limit 100 → 250 bp (150 bp for TAA); max leverage 5%; TAA uses fair-value / mean-reversion models (1–3 yrs, backtested)",
        "ETF on 50% margin: $80m exposure = $40m cash + $40m borrowed"))
    sub("Rebalancing: cash market or derivatives?", 5,
      K("Policy: rebalance quarterly; check drift monthly; liquid classes back to target or corridor edge; illiquid classes via new commitments",
        "Now: int'l developed equity 11.5% (top of range 11%) · fixed income 6.5% (target 9%, range 6–12%) · PE 19.2% (low end 18%) · real assets 13.8% (low end 13%)") +
      T(["Trade","Cash market","Futures","Choose"],
        [["0.5%, ~3 months","30 bp (spread 5 + impact 5 + cash drag 20)","24 bp (3 + 4 + tracking 17)","<b>Futures</b>"],
         ["2.5% (to 9% target), ~1 year","60 bp (5 + 5 + cash drag 50)","82 bp (4 + 4 + tracking 68 + roll 6)","<b>Cash</b> (saves 22 bp)"]]) +
      K("Cash market: cash drag (delays, disrupting active managers) = two-thirds of cost",
        "Futures: short equity + long bond futures → two contracts → tracking error 17 bp vs 8 bp for one; tracking error &gt; 70% of cost",
        "<b>Rule:</b> small, short-term, reversible, needs speed → derivatives overlay (no effect on active managers). Large, long-term, permanent → cash market") +
      TRAP("Derivatives' three roles here: <b>rebalancing, TAA changes, short-term liquidity</b>."))
    sub("ESG policy & the child-labour case", 5,
      P("<b>In plain words:</b> a portfolio company (Portro) used a supplier with child labour (ILO report). Students demand divestment. What should QU do?") +
      K("QUINCO ESG policy: ESG and financial factors both affect risk and return · transparency · long-term sustainability",
        "<b>Manager due diligence</b> (added by Natalya Long, CFA): formal ESG policy? · how ESG enters the process · timely disclosure of material ESG issues · fit with QUINCO policy",
        "<b>Responsible ownership</b>: proxy voting and engagement (human capital, climate, disclosure) · reporting · communication · UN PRI signatory",
        "<b>Monitoring metrics</b>: ESG scores vs peers and policy benchmark · sensitivity to climate risks · portfolio carbon footprint · track trends over time",
        "<b>Response</b>: engage the manager and Portro · join other investors · vote proxies · remove the supplier's goods from the campus store · divest only as a <b>last resort</b>") +
      TRAP("Divestment is <b>not</b> the first answer — engagement is preferred."))
