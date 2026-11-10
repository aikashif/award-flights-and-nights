from summary_lib import *

def add(chap, sub):
    chap(2, "Securities: Types, Features, Asset Allocation & Investing", "20", 5)
    sub("Equity vs debt — two asset classes", 5,
      T(["","Equity","Debt"],
        [["Capital","Kept as long as needed (perpetual)","Returned after set time"],["Return","No fixed return, no principal guarantee","Fixed interest + principal at maturity"],
         ["Role","Owner","Lender"],["Management","Participates","Does not"],["Profile","Risky, long-term, growth, volatile","Lower risk, steady, short-term, income"]]) +
      F("Borrow at 12%, assets earn 14% → lender gets 12%; extra 2% goes to equity\nIf assets earn less than 12% → equity may get nothing") +
      K("Splitting surplus between equity and debt by return, horizon, risk appetite, needs = <b>asset allocation</b>"))
    sub("Other asset classes & products", 5,
      T(["Product","Key points","Suits"],
        [["Hybrid securities","Features of debt and equity","—"],
         ["Commodities","Real assets (gold, silver, copper, agri); via commodity MFs, ETFs, derivatives","Retail via ETFs/MFs"],
         ["Derivatives","Contracts on price, quantity, date; most traded products in last 20 years","Sophisticated investors"],
         ["Mutual funds","Pool money, invest per mandate","<b>Retail</b> (best suited)"],
         ["Structured products","Bond/currency + embedded options/swaps; customised, illiquid","<b>HNIs</b> with high risk appetite"],
         ["Distressed securities","Equity, bonds, trade debt of near-bankrupt / heavily downgraded firms; steep discount; banks/MFs/insurers exit","Hedge funds, sophisticated investors"],
         ["Electronic Gold Receipts (EGR)","Gold in electronic form; Gold Exchange framework (10 Jan 2022): create → trade → convert to physical; SEBI (Vault Managers) Regulations 2022","—"],
         ["Zero Coupon Zero Principal (ZCZP)","Issued by NPOs for social projects; <b>no financial return</b>, only social return; listed on Social Stock Exchange segment","—"]]))
    sub("Issuer's choice: equity or debt financing", 5,
      L("Needs: (a) working capital — short-term debt; (b) long-term capital — equity or debt",
        "Governments issue <b>only debt</b>") +
      T(["Factor","Choose debt if…","Choose equity if…"],
        [["Ability to pay interest","Stable profits (e.g. banks fund loans with deposits)","Irregular profits"],
         ["Dilution","Owners won't dilute stake","Dilution acceptable"],
         ["Collateral","Has assets to pledge","Service business, few assets"],
         ["Time period","Short-term need (working capital)","Long-term need lenders won't fund"]]))
    sub("Features of equity capital", 5,
      T(["Feature","Point"],
        [["Nature","Owners' risk capital; profits not fixed"],
         ["Denomination","Face value ₹1, ₹2, ₹5 or ₹10; shareholders jointly own → '<b>joint stock company</b>'"],
         ["Inside vs outside","Insiders = promoters (+ early VCs); outsiders = public investors later"],
         ["Part ownership","10,000 shares × ₹10 = ₹1,00,000 capital (× ₹2 = ₹20,000); 5,100 of 10,000 = 51% majority stake; ESOPs give employees a stake"],
         ["Return","Perpetual; dividend not fixed; <b>residual claim</b> — last for profits and assets (after govt, lenders, employees, preference holders)"],
         ["Net worth","Retained profits → reserves → belong to shareholders, raise net worth; equity = '<b>risk capital</b>'"],
         ["Control","Board manages; independent directors protect small holders; one share one vote; general meeting, postal ballot, e-voting"]]))
    sub("Types of equity: DVR & preference shares", 5,
      L("<b>DVR shares</b>: separate profit right from vote — usually higher dividend, fewer votes; promoters raise capital without losing control",
        "<b>Preference shares</b>: fixed dividend; paid after all other payments but before equity dividend; priority over equity in dividend and in capital on winding up; no voting, no claim on assets",
        "<b>Cumulative</b> preference: unpaid dividend carried forward if terms allow",
        "Usually unlisted, little capital appreciation — value not tied to company performance") +
      T(["Preference share","Debenture"],
        [["Holder is a shareholder","Holder is a creditor"],["Unsecured (not a borrowing)","Usually secured"],["Dividend paid from profit after tax","Interest is a pre-tax expense"]]))
    sub("Equity risk & return", 4,
      L("Return = dividend + price appreciation; depends on future residual cash flows and price paid",
        "Risk: benefits not assured; prices 'noisy' as many players react to news",
        "Prices mirror performance — barometer of company, sector, economy"))
    sub("Features of debt capital", 5,
      T(["Feature","Point"],
        [["Instruments","Debentures, bonds, CPs, CDs, pass-through certificates; rate as % p.a. on face value"],
         ["Floating rate","Linked to benchmark (e.g. <b>MIBOR</b>), reset at agreed frequency"],
         ["Credit rating","Issuer appoints CRA; tells outsiders about ability to service"],
         ["Priority","Interest paid before tax and before equity; missed payment = default; lenders paid first on failure"],
         ["Security","Mortgage on assets → secured borrowing"],
         ["Control (covenants)","Restrict unrelated diversification, more borrowing, second charge; ask owners for more equity"],
         ["Conversion","Convertible debentures → equity at set date and price; interest stops on conversion"]]) +
      F("Borrow ₹100 cr: one bank loan OR 1 crore securities of ₹100; investor with ₹1,000 gets 10"))
    sub("Debt security terms; bond vs debenture", 5,
      T(["Term","Meaning"],
        [["Principal / face value","Amount borrowed; each investor owed a share"],
         ["Coupon","Interest rate as % of face value; frequency agreed (quarterly, semi-annual, annual)"],
         ["Maturity","Date principal repaid; bond then extinguished"]]) +
      K("India: govt / PSU debt = <b>bond</b>; private corporate = <b>debenture</b> (old view: debentures secured, bonds unsecured) — terms now used interchangeably",
        "Secured debt gives claim on assets; unsecured does not","Listed bonds trade on NSE/BSE; unlisted held to maturity"))
    sub("Bond structures", 5,
      T(["Structure","Feature"],
        [["Plain vanilla","Fixed coupon, issued and redeemed at par (₹100)"],
         ["Zero coupon","No coupons; issued at discount, redeemed at FV (or issued at FV, redeemed at premium); long ZCB = <b>deep discount bond</b>"],
         ["Floating rate","Reset vs benchmark (e.g. 1-yr G-sec + 50 bp, semi-annual); 'variable / adjustable rate' when reset ≥ 1 yr — common in housing loans"],
         ["Deferred interest","No coupons in first 1–3 years"],["Step-up","Coupon rises over time"],
         ["Callable","<b>Issuer</b> may redeem early — used when rates fall; investor loses high coupon"],
         ["Puttable","<b>Investor</b> may seek early redemption — useful when rates rise"],
         ["Amortising","Principal repaid over life (auto, consumer, home loans); maturity = last payment"]]) +
      F("Box 2.1 ZCB: ₹4,280 cr, secured by receivables; FV ₹100; Series 1 at ₹85.80, Series 2 at ₹82.55\nBox 2.2 callable: XYZ Bank, CARE AAA, FV ₹10,000, 9.75% annual, 10 yrs, call after 5 yrs + 1 day"))
    sub("Classification of debt; money market securities", 5,
      L("By borrower: government vs non-government; by tenor: up to 1 yr = <b>money market</b>; longer = capital market (not mutually exclusive)",
        "Central govt securities = no default risk (can tax, borrow, print money); quasi-govt = state, local, municipal",
        "Company fixed deposits: rated but <b>unsecured</b>, not securities, no liquidity",
        "All money market securities issued at <b>discount</b>, redeemed at par (zero coupon)",
        "Call, term money and inter-corporate deposits create no security — excluded") +
      T(["Instrument","Point"],
        [["Repo / reverse repo","Borrow against G-secs, SDLs, select corporate bonds; repo for borrower = reverse repo for lender"],
         ["Tri-party repo","On CCIL or exchange platform; CCP guarantees, collects margins (regular repo settled bilaterally)"],
         ["CD","Banks; tradable but rarely traded"],
         ["T-bills","Central govt; <b>91, 182, 364 days</b>; RBI auction; listed soon after"],
         ["CP","Companies; must be rated but unsecured; up to <b>364 days</b>; <b>90-day</b> most popular"]]) +
      K("Money market participants: banks, PDs, FIs, MFs, PF/pension funds, companies, govt"))
    sub("Government securities", 5,
      L("Fund fiscal deficit; RBI electronic auction; <b>half-yearly issuance calendar</b>; tenor 1 to <b>40 years</b>",
        "Dated securities: fixed coupon, <b>semi-annual</b> interest, redeemed at par; also T-bills, FRBs, ZCBs, inflation-indexed bonds",
        "G-sec rate = benchmark; others pay a spread (10-yr G-sec 8.4% → corporate pays more)",
        "Listed on issue; &gt; <b>90%</b> of long-term debt trading is G-secs; concentrated in benchmarks (1, 5, 10, 15, 30 yr)"))
    sub("Corporate bonds; special bonds", 5,
      L("Segments: PSU (incl. public FIs) and private corporate; PSU &amp; institutional dominate; financial sector ≈ <b>70%</b> of issuance, manufacturing ≈ 30%",
        "Tax-free bonds: PSUs (infra) authorised by govt; interest tax-free",
        "Capital gains bonds: NHAI, NABARD, NHB etc. — save LTCG tax under <b>Section 54EC</b>",
        "<b>Credit spread</b> = corporate yield − G-sec yield; higher rating → lower spread") +
      T(["Bond","Feature"],
        [["Masala bond","Issued <b>abroad</b> by Indian companies in <b>rupees</b>; currency risk on foreign investor; first by <b>IFC</b>, listed on <b>London Stock Exchange</b>"],
         ["Green debt securities","For renewable energy, clean transport, climate adaptation, green buildings, biodiversity; part of ESG; Sovereign Green Bonds announced in Budget FY 2022-23"],
         ["Bharat Bond ETF","Tracks Nifty Bharat Bond Index (AAA PSU bonds); fixed tenure (5 &amp; 11 yr series); very low cost; taxed like debt funds"],
         ["Tri-party repo on corporate bonds","Exchange platform, anonymous, order matching; basket repo <b>1–7 days</b>; eligible securities chosen by clearing corporation"]]) +
      F("Box 2.3 LMN NCD: ₹500 cr + green shoe ₹3,000 cr; CRISIL AA/Stable; min ₹10,000 (10 NCDs)\nSeries I–V: 3y 9.85% annual · 5y 10% · 7y 10.15% · 5y 9.57% monthly · 3y cumulative → ₹1,368.02 per ₹1,000"))
    sub("Benefits & risks of debt", 5,
      K("Benefits: <b>fixed income</b> (legal right; suits retirees) · <b>fixed tenor</b> (capital tied up for limited time)") +
      T(["Risk","Meaning"],
        [["Inflation / purchasing power","8% bond loses in real terms if inflation &gt; 8%; coupons can't rise"],
         ["Default / credit","All except G-secs; rating is a guide; secured lower risk → company FDs pay more"],
         ["Reinvestment","Coupons taken out may be reinvested at lower rates; cumulative option reinvests at bond's rate"],
         ["Call","Issuer calls when rates fall → reinvest lower"],
         ["Liquidity","Thin market, institution-dominated → hold to maturity; can't profit from price rise or switch when rates rise; credit quality may fall"]]))
    sub("Choosing debt or equity as investor", 4,
      T(["Factor","Debt","Equity"],
        [["Need","Regular income (retirees)","Growth"],["Horizon","Short (debt issued 7 days – 30 years; most common 90 days – 7 years)","Long"],
         ["Risk appetite","Lower; principal returned on maturity (default risk)","Higher; no assured dividend or principal"],
         ["Review","Buy and hold","Active review and trading"]]))
    sub("Convertible debentures", 5,
      L("Pay coupon; at redemption investor may take shares instead of cash",
        "Terms fixed at issue: conversion date · ratio · price (usually below market) · portion converted") +
      T(["Type","Conversion"],[["FCD","Whole face value converted"],["PCD","Part converted; rest stays debt, earns interest, redeemed"],["OCD","Converted at holder's option"]]) +
      K("Issuer: lower coupon, no repayment — but existing holders diluted","Investor: coupon early, upside after conversion"))
    sub("Depository receipts", 5,
      T(["DR","Listed"],
        [["ADR","US exchange (e.g. NYSE)"],["GDR","Exchange outside the US"],["IDR","<b>India</b>, with foreign shares as underlying"]]) +
      K("Represent local company shares, traded abroad, in foreign currency (usually USD)","Shares lodged with a custodian bank which authorises DRs; may be convertible to shares"))
