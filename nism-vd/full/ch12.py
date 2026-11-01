from summary_lib import *

def add(chap, sub):
    chap(12, "Mutual Fund Scheme Selection", "10", 5)
    sub("Selection based on investor need, risk profile, allocation", 5,
      L("Need: long-term appreciation, periodic income, or parking with high liquidity",
        "Portfolio = means to an end (goal) — never lose sight of the goal",
        "Step 1: set financial goals; Step 2: understand situation and risk appetite",
        "Risk appetite = need + ability + willingness to take risk (SEBI due-diligence circular and AMFI code stress risk profiling)",
        "Asset allocation decided after risk profile, goals, situation: growth → equity (needs long horizon); income → debt",
        "Long horizon but unwilling to take risk → may prefer debt",
        "<b>Age alone is not a good basis</b> — goals and situations differ even within an age group; family goals",
        "Use <b>time horizon to the goal</b>: longer horizon → more risk capacity; liquidity may be needed even in long-term portfolios"))
    sub("Core and satellite portfolio", 5,
      KV([("Core","Long-term needs: diversified equity, large cap, mid cap funds etc."),
          ("Satellite","Tactical, short-term views: sector funds (cyclical), long-term gilt when rates expected to fall, gold when inflation high or uncertainty"),
          ("Split","Conservative: very small satellite; moderate: ~80% core / 20% satellite (illustrative); aggressive: higher satellite")]))
    sub("Risk-return hierarchies (Illustrations 12.1.1–12.1.6)", 5,
      T(["Hierarchy (risk and potential return rise left → right unless stated)",""],
        [["All MFs","Liquid → Debt → Hybrid → Equity"],
         ["Debt (interest rate risk, similar credit)","Overnight → Liquid → Ultra short → Low duration → Short → Medium → Medium to long → Long duration"],
         ["Debt (credit risk, similar rate risk)","Gilt → Banking &amp; PSU → Corporate bond → Credit risk"],
         ["Equity (risk <b>decreases</b> left → right)","Small cap → Mid cap → Multi cap → Large &amp; mid cap → Large cap"],
         ["Concentration","Diversified → Focused → Thematic → Sector"],
         ["Hybrid","Arbitrage → Conservative hybrid → Equity savings → Dynamic asset allocation → Multi asset → Balanced hybrid → Aggressive hybrid"]]) +
      K("Large-cap sector fund (concentration risk) not comparable with diversified small-cap fund (size risk)","Different sector funds have different risk",
        "Product labelling (SEBI 2013) against mis-selling: disclaimer to consult financial adviser if unsure; risk-o-meter (Ch 5)"))
    sub("Selection by strategy: objective → strategy → portfolio", 4,
      L("Same objective can have multiple strategies; same strategy, different portfolios — evaluate each",
        "Low-risk equity: index fund or value fund; more risk for return: growth fund",
        "Debt for better returns: regular-income fund, or long-term gilt if rates expected to decline"))
    sub("Active vs passive funds", 5,
      L("Passive: asset-class exposure without manager-selection risk; index funds (not exchange-traded) mimic index constituents and weights; no selection risk; lower cost (no research expenses); ETFs (exchange-traded) also passive",
        "Active: higher cost and risk to beat benchmark; outperformance not guaranteed",
        "Want just equity growth, not to beat market → index fund",
        "<b>Index fund NAV does fall when the index falls</b>; long horizon → does well with market"))
    sub("Open-ended vs close-ended", 5,
      T(["","Open-ended","Close-ended"],
        [["Exit","Repurchase at NAV − exit load","Sell on exchange — needs counterparty"],
         ["Liquid assets","Kept for redemptions → can dilute equity returns","Not needed — can hold illiquid / long-gestation stocks"],
         ["Flows risk","Large sales/repurchases pressure manager","No redemption pressure"],
         ["Price vs NAV","At NAV","May trade at discount (no limit); converges to NAV near maturity"],
         ["Suits","Those wanting liquidity","Those who can lock money till maturity"]]))
    sub("Diversified vs focused vs sector vs thematic", 5,
      L("Diversified: multi-sector → less risky; active manager tilts to better sectors",
        "Focused: concentrated in few stocks → riskier than diversified, less risky than sector",
        "Sector (pharma, banking): concentration risk; needs skill to time entry before up-cycle and exit before downturn → <b>satellite</b> portfolio",
        "'Diversification is a protection against ignorance'",
        "Thematic (MNC, PSU, infrastructure): between diversified and sector"))
    sub("Large vs mid vs small cap; multi/flexi", 4,
      L("Large caps: established, stable revenues/profits, withstand downturns",
        "Mid/small caps: early growth; boom in good times, many fall by the wayside in turmoil; attractive when front-line stocks get expensive; winners re-rated as they grow",
        "Need careful selection — risky to put a large share of portfolio there",
        "Multi cap: spread across caps, lower risk than mid/small; large &amp; mid: riskier than large, less than mid; flexi cap: manager's freedom",
        "Choose multi cap (similar allocation), flexi cap (manager decides) or separate large/mid/small funds (investor decides)"))
    sub("Growth vs value funds", 4,
      K("Growth: companies growing above economy; do well in bull phase, fall more in downturns","Value: cheap vs future unlockable value; outperform in falling markets / over long periods","Both can sit in core portfolio; value pays over longer holding"))
    sub("International equity funds", 4,
      L("Two exposures: foreign equity market + exchange rate (stronger USD helps; stronger rupee hurts)",
        "Reasons: attractive overall return; diversification per asset allocation; specific opportunity → satellite or small core allocation"))
    sub("Debt fund selection: FMP, TMF, short duration, liquid, ultra-short, floater", 5,
      T(["Fund","Suitability"],
        [["FMP","Close-ended debt; horizon = scheme maturity; more predictable return, generally above FD; check credit risk; exit only via exchange"],
         ["TMF","Gradually replacing FMPs; G-secs/SDLs/AAA PSUs; index TMFs bought/redeemed with AMC like open-ended — <b>liquidity advantage over FMPs</b>"],
         ["Short duration","Maturities 1–3 yrs; market yields; good when rates expected to rise (reinvest at higher rates); low volatility, core for low-risk investors, short-term parking"],
         ["Liquid","Lowest risk, low returns; comparable to savings account; park up to 91 days; don't use for long periods"],
         ["Ultra-short","3–6 months; similar role, low volatility, high liquidity"],
         ["Floater","Floating rate instruments → steady NAV"]]) +
      K("Accrual strategy → steady, low volatility","Lower-quality paper for yield → be comfortable with it","Total-return/duration strategy → volatile; risk of wrong rate call"))
    sub("Hybrid and gold fund selection", 4,
      L("Two routes: own mix of equity + debt schemes (more choice, more decisions) or a hybrid scheme (simpler, accept its mix)",
        "Equity gives appreciation, debt gives stability — for equity exposure with lower risk",
        "Evaluate equity part (caps, sectors) and debt part (credit, duration) separately; 'conservative' refers only to equity allocation",
        "Be cautious of dynamic asset allocation variants",
        "Balanced schemes taxed as equity or non-equity depending on portfolio",
        "Gold Sector Funds (gold mining/processing shares) vs Gold ETFs (track gold price): miners can rise/fall more than gold and depend on company factors; <b>ETF = more efficient gold exposure</b>"))
    sub("Selecting among AMCs / within a category", 5,
      T(["Factor","What to check"],
        [["AMC","Comfort with approach, style, values"],
         ["Portfolio vs objective","Style drift: 'value fund' full of fully-valued front-liners; short-term debt fund with big long-term exposure; hybrid with aggressive small caps/credit; liquid/ultra-short taking high credit risk; non-gilt debt: credit quality and <b>sector concentration</b>"],
         ["Fund manager","Some managers better at spotting trend changes"],
         ["Performance","Consistent outperformance; protect downside; equity ≥ <b>5 years</b>; long-term debt ≥ <b>3 years</b>; short-term debt shorter; liquid: 7 days, 15 days, 1 month; vs benchmark, peers, rolling periods, bull &amp; bear cycles; CAGR for 1, 3, 5 yrs and since inception (allotment date)"],
         ["Portfolio","Equity: diversification, segment, cash, holding length, churn, strategy. Debt: average maturity, duration, credit profile, interest vs gains, liquid holdings"],
         ["Fund age","Track record; avoid new fund with lacklustre manager; matters more where dispersion is high (multi cap vs large cap)"],
         ["Fund size","Large-cap fund: size helps (diversification, scale); sector/mid-cap: size can hurt; small funds more flexible"],
         ["Portfolio turnover","Frequent churn = costs + unsteady management; view with style"],
         ["Expenses","Drag on returns; especially important for debt and index funds"]]))
    sub("Portfolio turnover ratio", 5,
      F("Turnover = lower of (purchases, sales) in period ÷ average net assets\nEx: ₹10,000 cr ÷ ₹5,000 cr = 2 (200%) → average holding = 12 ÷ 2 = 6 months") +
      K("6 months too short for value style, fine for momentum","Short holding may signal tactical rather than long-term investing"))
    sub("Research agency rankings & ratings (Box 12.1)", 4,
      L("Ranking = order within category; rating = grouping by performance traits; methodologies on agency websites",
        "Star ratings: 5-star better than 4-star — but almost always based on past performance, no predictive ability",
        "Best fund this quarter rarely best next quarter; switching costs hurt",
        "Aim: stay in top 'few' consistently — 3 to 5 in small categories or top 10–15% in large ones",
        "Taxes and exit loads also matter"))
    sub("Selecting options", 5,
      L("IDCW payout: money flow; growth: grows gross (no annual tax)",
        "Repurchase = sale → capital gain/loss; may be booked to set off other gains/losses",
        "Monthly IDCW not assured — depends on distributable surplus → regular income better via <b>SWP</b> (STT for equity, capital gains tax applies)",
        "IDCW taxed at slab → IDCW option not preferable except for tax-exempt investors",
        "Taxation and liquidity needs decide the option"))
    sub("Do's and don'ts", 5,
      T(["Rule","Point"],
        [["Ensure suitability","SEBI Fraudulent &amp; Unfair Trade Practices regulation applies to MF sales"],
         ["Stick to asset allocation","Keep it at the core of scheme selection"],
         ["Don't chase past performance","'Past performance may or may not be sustained in future'"],
         ["Understand objective &amp; strategy","Know what to expect"],
         ["Watch taxes &amp; loads","Check capital gains and exit loads on redemptions; compare IDCW vs growth tax periodically"],
         ["Consistent written methodology","Helps stay on course"]]))
