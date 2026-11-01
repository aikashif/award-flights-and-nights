from summary_lib import *

def add(chap, sub):
    chap(18, "Interest Rate, Interest Rate Instruments & Fixed Income Market", "6", 4)
    sub("Interest rate concept: loan vs debt instrument", 4,
      F("A borrows X from B for 3 months, repays X + Δ ; Δ = X × R% × 3/12") +
      L("Signed agreement = <b>loan</b> (generally non-tradable); written 'note' = <b>debt instrument</b> (tradable) — A issuer, B investor, R yield",
        "Interest rate = charge for use of an asset; cost for borrower, return for lender; quoted annually = nominal annual rate",
        "'Interest rate is subjective': varies with tenor, amount, credit risk (home loan 15 yrs 6%, personal loan 7%, home 20 yrs 6.5%, &gt; ₹50 lakh 6.25%, 5-yr G-sec 5%, 5-yr AAA 5.50%)",
        "Low-risk borrower → lower rate; high-risk → higher"))
    sub("Macro & micro factors affecting interest rates", 5,
      T(["Macro factor","Effect"],
        [["Demand for money","Strong economy → more demand → rates ↑; recession → rates ↓"],
         ["Supply of money","Central bank tightens in inflation → policy rate ↑"],
         ["Fiscal deficit &amp; govt borrowing","High borrowing → higher rates, corporates crowded out"],
         ["Inflation","Savers need compensation → nominal rates ↑; falls as inflation falls"],
         ["Global rates &amp; FX","Higher rates abroad → capital moves → domestic rates must rise"],
         ["Central bank actions","Repo ↑ → money market rates ↑ → bond yields ↑"]]) +
      T(["Micro factor","Effect"],
        [["Maturity / tenor","Rates usually rise with tenor"],["Credit risk","Higher risk → higher rate"],["Seniority","Order of payment on default; junior → higher rate"],
         ["Security","Unsecured pays more than secured"],["Liquidity","Easy-to-trade bonds command a premium (lower yield)"],["Investor sentiment","Negative mood → rush to G-secs"]]))
    sub("Effective rate; nominal vs real rate", 5,
      F("Effective rate = (1 + annual rate ÷ n)^n − 1\n6% compounded semi-annually: ₹1,000 → ₹30 + ₹30.90 = ₹60.90 → (1.03)² − 1 = 6.09%\n(1 + r)(1 + i) = (1 + R)  ; approx r = R − i\nNominal 9%, inflation 6% → real ≈ 3% ; nominal 7%, inflation 9% → real ≈ −2%") +
      K("Interest rate risk = uncertainty in rate movement — both directions hurt someone"))
    sub("Fixed income securities & key components", 5,
      L("Pay fixed interest (coupons) periodically, principal at maturity; bonds/debentures most common",
        "'Fixed' because life is fixed (exception: Dutch perpetual bond of <b>1648</b>; Indian perpetuals have issuer call option) and cash flows mostly fixed (floaters: timing known, size not)") +
      T(["Component","Meaning"],
        [["Issue price","Usually = face value for coupon bonds; below FV for zero-coupon"],
         ["Face value (par, principal)","Coupon calculated on it; repaid at maturity (sometimes with premium)"],
         ["Coupon / coupon rate","Cash flow at fixed dates; % of FV; usually stated annually"],
         ["Coupon frequency","Monthly, quarterly, semi-annual, annual"],["Interest payment dates","Dates coupons are paid"],
         ["Maturity date","Principal repaid; security ceases"],["Call / put date","Issuer / investor may redeem early"],
         ["Redemption value","Above FV = premium; below = discount; equal = par"]]) +
      F("Example: FV ₹1,000 issued 1 Apr 2021 at ₹1,000, 10 yrs, 7% half-yearly (1 Apr &amp; 1 Oct), maturity 1 Apr 2031, no call/put, redeemed ₹1,000"))
    sub("Bond vs loan; classification criteria", 3,
      K("Bond is tradable, can change hands; loan usually not","Bond value changes continuously with rates and credit; loan value doesn't",
        "Classification by: issuer · maturity · coupon · currency · embedded options · security · priority of claims · purpose · underlying · taxation"))
    sub("By issuer", 5,
      T(["Issuer type","Points"],
        [["Government / sovereign / gilt-edged","Domestic currency; issued by auction, traded in secondary market; risk-free (can print money) — but defaults possible (European debt crisis 2008–2012); lowest rates; largest Indian segment incl. <b>State Development Loans (SDLs)</b> and special securities (oil, fertiliser, bank recapitalisation subsidies)"],
         ["Municipal ('muni')","Local authorities fund infrastructure, libraries, parks; few in India; SEBI regulation for issuance &amp; listing"],
         ["Corporate bonds / NCDs","Depend on company's revenues; cheaper than equity, no dilution; may be collateralised; higher risk → higher rates; CPs for short-term/working capital; public issue or private placement; CRAs rate (AAA safest; 'junk'/'high-yield'); credit spread = corporate − govt yield"],
         ["Securitised debt","Illiquid loans → SPV → tradable asset-backed securities"]]))
    sub("By maturity", 4,
      T(["Type","Tenor"],
        [["Overnight","Banks borrow from money market &amp; RBI; collateralised cheaper than clean; RBI supplies/absorbs liquidity via banks &amp; Primary Dealers"],
         ["Ultra-short (money market)","Up to 1 yr: CP, CD, T-bills, Cash Management Bills (CMB)"],["Short term","1–5 yrs"],
         ["Medium term (intermediate)","5–12 yrs — bulk of issuance"],["Long term","&gt; 12 yrs (GoI bonds mostly)"],
         ["Staggered / serial","Portions mature every few years — orderly retirement"],["Perpetual (consol)","No maturity; banks issue for Tier-I capital (Basel III)"]]) +
      K("No fixed rule for short/medium/long; MFs classify debt funds by <b>duration</b>, not maturity","Long-term bonds usually costlier (lock-in, illiquidity)"))
    sub("By coupon", 5,
      T(["Type","Feature"],
        [["Plain vanilla / straight / bullet","Fixed coupon, defined maturity, issued &amp; redeemed at FV"],
         ["Zero-coupon (ZCB)","No interest; issued at discount, redeemed at FV; single cash flow; e.g. T-bills, CMBs, <b>STRIPS</b>; highly rate-sensitive; used by pension funds/insurers"],
         ["Floating rate (FRB)","Coupon linked to benchmark (e.g. 182-day T-bill), reset each coupon date; trades near FV; largely immune to interest rate risk"],
         ["Cap / floor / collar","Cap protects issuer; floor protects investor; both = collar"],
         ["Inverse floater","Coupon moves opposite to benchmark (fixed coupon minus spread over MIBOR); NBFC issuers, MF investors"],
         ["Inflation-indexed","Par (or par and coupons) indexed to WPI/CPI"],
         ["Step-up / step-down","Low then high coupons (start-ups, risky) / high then low (declining revenues, e.g. leasing)"],
         ["Deferred coupon","Mix of coupon bond and ZCB — nothing early, high coupons later (long gestation)"],
         ["Deep discount","ZCB at big discount (≥ 20%, longer maturity); infrastructure cos; high risk"]]))
    sub("By embedded options", 4,
      T(["Bond","Feature"],
        [["Straight","Regular coupons, principal at maturity"],
         ["Callable","Issuer may repay early on call date — used when market rates fall; usually pays a premium when called"],
         ["Puttable","Investor may seek early redemption — used when rates rise; usually at a discount"],
         ["Call &amp; put","Both rights"]]) +
      K("Embedded options raise risk and are valued using option premia"))
    sub("By security & seniority", 4,
      T(["Type","Feature"],
        [["Secured","Backed by specific assets; paid first from collateral; higher recovery"],["Unsecured","No collateral; issuer's name"],
         ["Credit-enhanced","Extra collateral, insurance, or third-party guarantee → better rating, lower cost"],
         ["Senior","Paid before junior debt and shareholders; lower rate"],["Subordinated (junior)","Paid just before equity; higher coupon; banks issue for Tier II capital"]]))
    sub("Other instruments", 4,
      T(["Instrument","Feature"],
        [["Annuities","Regular payments over time; fixed income but not tradable; most consumer &amp; housing loans structured as annuities"],
         ["AT1 bonds","Basel III Additional Tier 1: unsecured, perpetual, non-convertible bonds meeting RBI conditions (Tier 1 = CET1 + AT1)"],
         ["Tier 2 bonds","Subordinated, unsecured; min <b>5 years</b>; no put; call only after ≥ 5 yrs with RBI approval"],
         ["Convertible bonds","Convert to equity at pre-fixed price; issuer can't refuse"],
         ["REITs / InvITs","SEBI-registered trusts in commercial real estate / infrastructure"],
         ["Green bonds","For climate &amp; environmental projects; usually same rating as issuer's other debt"],
         ["Tax-free bonds","Govt enterprises; interest exempt under Section 10"],["Tax-saving bonds","Tax benefit on investment, lock-in; interest taxable"],
         ["Asset-linked bonds","Linked to asset performance; credit enhancement"],
         ["ESG debt securities","SEBI framework 5 Jun 2025: green, social, sustainability, sustainability-linked bonds per international frameworks"],
         ["Masala bonds","Rupee-denominated bonds issued outside India by Indian entities"]]))
    sub("Equity vs debt; pros & cons of debt", 4,
      T(["","Equity","Debt"],
        [["Represents","Ownership","Loan"],["Maturity","None","Yes"],["Returns","Variable (dividend, gains)","Predefined interest"],
         ["Voting","Yes","No"],["Liquidation","Last","Before equity"],["Risk","Higher","Lower"]]) +
      K("Debt pros: no loss of control · lender priority · known obligations · interest tax-deductible (lowers WACC) · private placement simpler · no shareholder meetings/votes · committed lenders · cheaper long-run",
        "Debt cons: covenants/exclusivity · must be repaid · refinancing/cash flow risk · leverage raises default risk · fixed regardless of conditions · poor planning hurts operations · high D/E = riskier · liens / sinking funds"))
    sub("Risk-free rate & risks in bonds", 5,
      L("Fixed income ≠ fixed return — timing (and often size) of cash flows known, return not guaranteed",
        "7-yr 9% corporate bond: <b>credit risk</b> (may not pay) · <b>price / interest rate / market risk</b> (sell before maturity at unknown price) · <b>reinvestment risk</b> (coupons reinvested at unknown rates)",
        "Interest rate risk hits both sides: future borrower fears rise, future lender fears fall; banks/NBFCs on both sides",
        "Also liquidity, call, inflation risk",
        "Sovereign in home currency → no credit risk → <b>risk-free rate</b>; others pay a <b>credit spread</b> (risk-free 8.25% + AAA 0.10% = 8.35%; AA 0.25% → 8.50%)",
        "Risk-free rate = benchmark/opportunity cost for all valuations",
        "Market risk disappears if held to maturity; reinvestment risk disappears for zero-coupon",
        "<b>Sovereign, home-currency, zero-coupon, no call, held to maturity → no risk; fixed income = fixed return</b>") +
      T(["Rates","Price risk","Reinvestment risk"],[["Rise","Prices fall (loss)","Reinvest at higher rate (gain)"],["Fall","Prices rise (gain)","Reinvest at lower rate (loss)"]]))
    sub("Term structure of interest rates", 5,
      L("Rate depends on <b>term</b> and on <b>borrower credit</b>",
        "Standard tenors — money market: ON, 1W, 2W, 1M to 1Y monthly; bond market: 2Y, 5Y, 7Y, 10Y, 15Y, 20Y, 25Y, 30Y, 40Y",
        "Sovereign rate quoted directly; others as credit spread by rating") +
      T(["Term","Risk-free","AAA spread","A spread","BBB spread"],
        [["1M","5.00%","0.15%","0.25%","0.35%"],["3M","5.25%","0.25%","0.50%","0.75%"],["1Y","5.75%","0.40%","0.75%","1.10%"],["5Y","6.50%","0.85%","1.50%","2.25%"]]) +
      K("Rate vs term plotted = term structure = <b>yield curve</b> (risk-free curve, AAA curve, BBB curve…)","Risk-free term structure = most important valuation tool (ultimate opportunity cost)"))
