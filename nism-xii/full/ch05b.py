from summary_lib import *

def add(chap, sub):
    sub("Debt funds — how returns arise", 5,
      L("Debt from govt, PSUs, banks, companies; short-term (T-bills, CP, CD) or long-term (G-secs, PSU and corporate bonds)",
        "Credit risk (corporate bonds) vs none (G-secs); <b>MTM risk</b> = price change when rates move — larger for longer tenor",
        "Rates ↑ → prices ↓ (more for long tenor); rates ↓ → prices ↑",
        "Short-term funds: mostly coupon, little MTM; gain when rates rise (higher coupons)",
        "Long-term funds: higher coupon + bigger MTM swings; gain most when rates fall",
        "Credit-risk bonds pay higher coupons; risk shown by portfolio ratings"))
    sub("Debt scheme categories", 5,
      T(["Category","Rule"],
        [["Overnight","Securities maturing in <b>1 day</b>"],["Liquid","Debt &amp; money market up to <b>91 days</b>"],
         ["Ultra short term","Macaulay duration <b>3–6 months</b>"],["Ultra short to short term","Macaulay duration <b>6–12 months</b>"],
         ["Money market","Money market instruments up to <b>1 year</b>"],["Short term","Duration <b>1–3 years</b>"],
         ["Medium term","Duration <b>3–4 years</b> (1–4 in adverse situation)"],["Medium to long term","Duration <b>4–7 years</b> (1–7 adverse)"],
         ["Long term","Duration <b>&gt; 7 years</b>"],["Dynamic","Across durations"],
         ["Corporate bond","≥ <b>80%</b> in <b>AA+ and above</b>"],["Credit risk","≥ <b>65%</b> in <b>AA and below</b> (excl. AA+); no 'high yield' style names"],
         ["Banking &amp; PSU","≥ <b>80%</b> in banks, PSUs, PFIs, <b>municipal bonds</b>"],["Gilt","≥ <b>80%</b> G-secs across maturity"],
         ["10-yr constant maturity gilt","≥ 80% G-secs; portfolio Macaulay duration = <b>10 years</b>"],
         ["Floater","≥ <b>65%</b> floating rate (incl. swapped fixed-rate)"],
         ["Sectoral debt","≥ <b>80%</b> in one sector, AA+ and above; e.g. financial services, energy, infrastructure, housing &amp; real estate"]]))
    sub("Hybrid scheme categories", 5,
      T(["Category","Equity","Debt / other"],
        [["Conservative hybrid","10–25%","Debt 75–90%"],["Balanced hybrid","40–60%","Debt 40–60%; <b>no arbitrage</b>"],
         ["Aggressive hybrid","65–80%","Debt 20–35%"],["Dynamic asset allocation / Balanced advantage","Managed dynamically",""],
         ["Multi asset allocation","≥ 3 asset classes, ≥ <b>10%</b> each","Foreign securities not a separate class"],
         ["Arbitrage","Equity ≥ <b>65%</b>","Debt only G-secs &lt; 1 yr + G-sec repo"],
         ["Equity savings","Equity ≥ <b>65%</b>","Debt ≥ <b>10%</b>; hedged/unhedged minimums in SID"]]) +
      K("Offer <b>either</b> aggressive hybrid <b>or</b> balanced hybrid","More equity → more risk",
        "Residual portion may go to InvITs (not arbitrage funds), ETCDs, gold ETFs, silver ETFs",
        "Arbitrage: buy cash, sell futures; spread = interest element, locked till expiry; NAV volatility like a liquid fund"))
    sub("Life cycle funds", 5,
      L("Open-ended with target maturity and <b>glide path</b> — grows more conservative near maturity",
        "Multi-asset: equity, debt, InvITs, ETCDs, gold &amp; silver ETFs",
        "Tenure <b>5 to 30 years</b> in multiples of 5; max <b>6</b> open for subscription at a time"))
    sub("Other schemes: index, ETF, gold/silver ETF, FoF", 5,
      T(["Scheme","Rule"],
        [["Index fund / ETF","≥ <b>95%</b> in index securities"],
         ["ETF","Units issued at launch, then traded on exchange via brokers; need broking + demat; real-time prices linked to NAV"],
         ["Gold ETF","Gold in electronic form; usually <b>1 unit = 1 gram</b>; holds physical gold/receipts"],
         ["Silver ETF","Mainly silver and silver instruments (norms 24 Nov 2021)"],
         ["Commodity ETFs","<b>Dedicated fund manager</b> with commodity skills; NAV daily on AMC website"],
         ["Fund of Funds","≥ <b>95%</b> in underlying fund(s); mostly own fund house's schemes"]]))
    sub("FMPs, infrastructure debt funds, real estate funds", 4,
      T(["Scheme","Features"],
        [["Fixed Maturity Plan","Closed-end; securities mature with scheme → returns locked in; main risk = <b>credit</b>; listed"],
         ["Infrastructure Debt Fund","Closed-end, tenor ≥ <b>5 years</b>; ≥ <b>90%</b> infra debt/securitised debt; NAV at least <b>quarterly</b>; min investment <b>₹1 crore</b>; unit FV ≥ <b>₹10 lakh</b>; listed; sponsor needs infra experience"],
         ["Real estate MF","Property or real estate company securities; closed-end, listed"]]))
    sub("Active vs passive investing", 5,
      T(["","Active","Passive"],
        [["Aim","Beat benchmark","Match benchmark (replicate index weights)"],["Cost","High (research, churn)","Low (no stock-picking team)"],
         ["Measure","Outperformance (often fails in US)","<b>Tracking error</b> → as near zero as possible"]]) +
      T(["","Index fund","ETF"],[["Traded","With AMC at NAV (cut-off rules)","On exchange all day at market price; limit orders possible"]]) +
      K("SEBI passive norms (23 May 2022): direct ETF deals with AMC only above <b>₹25 crore</b> · <b>iNAV</b> shown continuously on exchange · ELSS may be active (equity) or <b>passive</b> (Others; index of top <b>250</b> stocks) · FoFs value ETFs at exchange <b>closing price</b>"))
    sub("Investment channels; PAN & KYC", 5,
      L("Offline: AMC, distributor or RTA office → KYC + form + cheque → folio + account statement",
        "Online: AMC/RTA website; choose scheme, option, lump sum or SIP, payment",
        "Exchanges: <b>NSE MFSS</b>, <b>BSE StAR MF</b> (one-time registration); <b>MF Utilities (MFU)</b> industry platform, online and offline",
        "<b>PAN mandatory</b> except individual investments ≤ <b>₹50,000 a year per mutual fund</b> (lump sum + SIP)",
        "Eligible: residents, NRIs, PIOs, foreign nationals, institutions, trusts",
        "KYC once, valid across MFs and capital market; includes IPV; Aadhaar <b>eKYC</b> removes paperwork and IPV; <b>CAMS / KFinTech</b> are KYC User Agencies (OTP)"))
    sub("FATCA & CRS", 4,
      L("MFs identify foreign reportable accounts; report to US IRS / other govts via Indian tax authorities",
        "Disclose citizenship, birthplace, tax residency outside India + taxpayer ID",
        "If covered → value of <b>all folios</b> reported, incl. beneficiaries and controlling persons",
        "Status change → inform fund within <b>30 days</b>"))
    sub("Purchases: NFO & continuous offer", 5,
      T(["Rule","Detail"],
        [["NFO period","<b>15 days</b> (except ELSS)"],["Allotment","Within <b>5 business days</b> of NFO close (except ELSS)"],
         ["NFO documents","Form comes with <b>KIM</b>"],["Payment","Cheque, NEFT, RTGS, ASBA etc.; from bank account of the <b>first holder</b>"],
         ["Cash","Up to <b>₹50,000</b> per fund house; DD only in specified cases"],
         ["Continuous offer","New investors: application form; existing: <b>transaction slip</b> with folio; submit at Official Point of Acceptance (AMC office or ISC); units at applicable NAV; Statement of Account"],
         ["Joint holders","Up to <b>3</b>; all do PAN &amp; KYC; mode 'joint' (all sign) or 'either or survivor'"]]) +
      K("Scheme documents free at ISCs/AMC offices: <b>SAI</b> (fund/AMC statutory info) · <b>SID</b> (scheme) · <b>KIM</b> (key facts)",
        "<b>Riskometer</b> on NFO form, SID, KIM front pages and in adverts",
        "<b>Factsheet</b> monthly: objective, category, options, AUM, benchmark, minimum, exit load, riskometer, manager profile, top 10 holdings, sectors, past returns, ratios",
        "Exchange channel: brokers with <b>ARN</b> + exchange permission; units in demat"))
    sub("Redemptions (worked)", 5,
      F("500 units, NAV ₹24, exit load 1%\nPrice = 24 × 0.99 = ₹23.76 → amount = 500 × 23.76 = <b>₹11,880</b>") +
      L("Open-ended: any time at NAV; closed-end: only at maturity",
        "State amount or units; signatures per holding mode",
        "Bank details mandatory at purchase; payout to bank or cheque with pre-printed account (anti-fraud)",
        "Register up to <b>5</b> bank accounts; one is default"))
    sub("Non-financial transactions, statements, demat, commission", 5,
      L("Changes (address, bank, joint holder) via transaction slip + documents; central agencies update across funds",
        "<b>SoA</b> after every transaction; <b>CAS</b> monthly if any transaction; every <b>6 months</b> if none",
        "Later SoAs show balance units, NAV, value, <b>average TER</b> and <b>gross commission</b> paid to distributors",
        "Units may be held in demat; investor bears demat and broker costs",
        "Commission: <b>full trail model</b>; no upfront commission; upfronting of trail only for <b>SIP</b> inflows (with conditions)"))
    sub("Systematic plans & switches", 5,
      K("Specify: type · period · frequency · day · amount") +
      T(["Facility","How it works","Example"],
        [["SIP","Fixed sum invested periodically; more units when NAV low → <b>rupee cost averaging</b>","₹5,000 on 5th monthly → ₹60,000 a year; quarterly SoA"],
         ["SWP","Fixed sum redeemed periodically; book profits / regular income","₹5,000 on 5th; NAV ₹20 → 250 units; if balance insufficient → all redeemed, folio closed"],
         ["STP","SWP from source + SIP into destination, same fund house","₹10,000 monthly liquid → equity for 6 months"],
         ["Switch","One-off redeem + buy, any amount/date; also between options (growth → IDCW)","Exit load applies on source"]]))
    sub("Information, benefits & costs", 5,
      K("Information: scheme documents · brochures · monthly factsheets vs benchmark · SEBI and AMFI websites, rating sites") +
      T(["Benefits","Costs / limits"],
        [["Diversification from ₹500","Fees and expenses"],["Professional management","Limited control over decisions"],
         ["Liquidity","Indirect ownership — held in trust's name; investor is beneficial owner"],
         ["Flexibility (lump sum/SIP, IDCW/growth)",""],["Tax efficiency (fund exempt)",""],["Access to wholesale/unlisted debt",""]]))
    sub("Regulation of mutual funds", 5,
      L("<b>SEBI (Mutual Funds) Regulations 1996</b> (amended 1 Nov 2025); only SEBI-registered entities",
        "Trust structure; trustees ensure investor interest; money off AMC's balance sheet",
        "Rules on sponsor track record and capital, AMC/trustee roles",
        "Schemes need <b>trustee and SEBI</b> approval; disclosure formats set",
        "Investment limits, diversification, valuation and accounting set by SEBI",
        "Expense types and limits capped",
        "Returns published with benchmark returns; reports to SEBI, trustees, AMC board",
        "<b>Risk Management Framework</b>: identify, measure, manage, report risks"))
    sub("Investor service standards", 5,
      T(["Service","Standard (this workbook)"],
        [["NAV, sale &amp; redemption prices","Daily"],["Allotment","NFO: within 5 business days; ongoing: transaction date"],
         ["Dividend (IDCW)","Within <b>15 days</b> of declaration"],["Redemption","Within <b>10 working days</b>"],
         ["Delay","AMC pays <b>15% p.a.</b> interest — borne by AMC, not scheme"]]) +
      K("Investor Charter for MFs on AMC websites (10 Dec 2021)","<b>AMFI</b> = industry body; best practices, codes of conduct",
        "Mandatory voting on governance, capital structure, pay, CSR, director changes, related-party deals (5 Mar 2021)") +
      TRAP("These are the XII workbook's timelines. The V-D (Sept 2026) workbook gives shorter, newer SEBI timelines. For the XII exam, use 15 days and 10 working days."))
    sub("Specialized Investment Fund (SIF)", 4,
      K("New product line under MF Regulations (amended 16 Dec 2024)","Minimum investment <b>₹10 lakh</b> across all strategies"))
    sub("Workbook sample answers", 3,
      K("NAV mainly reflects current market value of portfolio","ETF: transact with brokers, units in demat","KYC by <b>all holders including minors</b>",
        "Fixed periodic purchase = SIP","Daily NAV disclosure = True"))
