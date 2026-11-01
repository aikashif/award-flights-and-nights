"""NISM V-D Mutual Fund module (Ch1-12) summary -> HTML -> PDF.

Run: python3 nism-vd/mf_summary.py   (needs node + playwright for the PDF step)
"""
import html, json, pathlib, subprocess, re

def T(head, rows, cls=""):
    h = "".join(f"<th>{c}</th>" for c in head)
    b = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="{cls}"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>'
def KV(rows):
    return '<table class="kv"><tbody>' + "".join(f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in rows) + "</tbody></table>"
def K(*w):
    return '<div class="kw">' + "".join(f"<span>{x}</span>" for x in w) + "</div>"
def F(t):
    return f'<pre class="f">{t}</pre>'
def TRAP(t):
    return f'<div class="trap"><b>Trap</b> {t}</div>'
def L(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
V = '<span class="v">‡</span>'

CH = []
def chap(n, title, marks, stars):
    CH.append({"n": n, "title": title, "marks": marks, "stars": stars, "subs": []})
def sub(title, stars, body):
    CH[-1]["subs"].append({"t": title, "s": stars, "b": body})

# ---------------------------------------------------------------- CH 1
chap(1, "Investment Landscape", "5", 3)
sub("Saving vs investing; why invest", 2,
  KV([("Saving","Setting money aside from income (current consumption deferred)"),
      ("Investing","Deploying savings into assets to earn return / beat inflation"),
      ("Why invest","Inflation erodes purchasing power · meet goals · create wealth · retirement income"),
      ("Real return","≈ Nominal return − Inflation (exact: (1+n)/(1+i) − 1)")]))
sub("Investment objectives", 3,
  T(["Objective","Meaning","Typical product"],
    [["Safety","Protect capital","Bank FD, G-sec, liquid fund"],
     ["Liquidity","Quick conversion to cash at low cost","Liquid / overnight fund, savings a/c"],
     ["Income","Regular cash flow","Debt fund IDCW / SWP, bonds"],
     ["Growth","Capital appreciation over time","Equity fund"],
     ["Tax efficiency","Post-tax return","ELSS (80C), equity LTCG"]]) +
  K("Convenience","Tax","Time horizon decide the mix"))
sub("Financial goals & life cycle", 3,
  T(["Stage","Goals","Risk capacity"],
    [["Young earner","Emergency fund, wealth start","High"],
     ["Young family","House, children education","Medium–high"],
     ["Mid-career","Children, retirement corpus","Medium"],
     ["Pre-retirement","Protect corpus","Low–medium"],
     ["Retired","Regular income, safety","Low"]]) +
  K("SMART goals: specific, measurable, time-bound","Short (<1 yr) / medium (1–5) / long (>5)"))
sub("Asset classes", 4,
  T(["Class","Examples","Return driver","Key risk"],
    [["Equity","Shares, equity MFs","Earnings growth, valuation","Market / volatility"],
     ["Debt (fixed income)","Bonds, G-secs, CPs, CDs, FDs","Interest (coupon) + price change","Interest rate, credit, reinvestment"],
     ["Cash / money market","Savings a/c, T-bills, liquid funds","Short-term rates","Inflation"],
     ["Real estate","Property, REITs","Rent + appreciation","Illiquidity, high ticket"],
     ["Gold / commodities","Physical gold, gold ETF, SGB","Global price, USD-INR","Price, no income (except SGB)"],
     ["Alternatives","PMS, AIF, InvITs, private equity","Varies","Complexity, illiquidity"]]) +
  K("Physical vs financial assets","Real assets hedge inflation","Low correlation → diversification"))
sub("Equity vs debt: features", 3,
  T(["", "Equity", "Debt"],
    [["Holder is","Owner","Lender"],
     ["Return","Dividends + capital gain (uncertain)","Fixed coupon + principal (contractual)"],
     ["Claim on liquidation","Last (residual)","Before equity"],
     ["Maturity","Perpetual","Fixed maturity"],
     ["Risk / return","Higher / higher","Lower / lower"]]) +
  K("Primary market: issuer gets money (IPO, NFO)","Secondary market: investors trade among themselves"))
sub("Money market & debt instruments", 4,
  T(["Instrument","Issuer","Tenor / note"],
    [["T-bills","Govt of India","91 / 182 / 364 days, discount instrument"],
     ["Commercial paper (CP)","Companies","7 days – 1 yr, discount, unsecured"],
     ["Certificate of deposit (CD)","Banks (FIs 1–3 yrs)","7 days – 1 yr"],
     ["Call / notice / term money","Banks (interbank)","1 day / 2–14 days / 15 days–1 yr"],
     ["Repo / TREPS","Collateralised borrowing","Overnight–short"],
     ["G-secs / SDLs","Centre / States","Long-dated, no default risk"],
     ["Corporate bonds / NCDs","Companies","Credit rated"],
     ["PSU / bank bonds","PSUs, banks","Quasi-sovereign"]]))
sub("Investment risks", 5,
  T(["Risk","Meaning","Most affects"],
    [["Inflation risk","Return below inflation","Cash, FDs, debt"],
     ["Interest rate risk","Rates ↑ → bond prices ↓","Long-duration debt"],
     ["Reinvestment risk","Coupons reinvested at lower rate","Short-term / coupon bonds"],
     ["Credit / default risk","Issuer fails to pay","Corporate bonds, credit-risk funds"],
     ["Liquidity risk","Can't sell quickly at fair price","Small caps, unlisted, real estate"],
     ["Market risk","Whole market falls (systematic)","Equity"],
     ["Business / company risk","Company-specific (unsystematic)","Single stocks"],
     ["Concentration risk","Too much in one stock/sector","Sector/focused funds"],
     ["Exchange rate risk","INR moves vs foreign currency","International funds"],
     ["Political / regulatory / tax","Policy change","All"]]) +
  K("Systematic risk = cannot diversify away","Unsystematic = removed by diversification") +
  TRAP("Interest rate risk and reinvestment risk move in opposite directions."))
sub("Risk measures", 4,
  T(["Measure","Used for","Read as"],
    [["Standard deviation","Equity / any","Total volatility; higher = riskier"],
     ["Beta","Equity","Sensitivity to market; β &gt; 1 = more volatile"],
     ["Modified duration","Debt","% price change for 1% yield change"],
     ["Weighted avg maturity","Debt","Longer = more rate risk"],
     ["Credit rating","Debt","AAA highest; below BBB− = non-investment grade"]]))
sub("Risk management strategies", 3,
  T(["Strategy","Example"],
    [["Avoid","Don't buy what you don't understand"],
     ["Reduce / mitigate","Diversification, asset allocation"],
     ["Transfer","Insurance, hedging"],
     ["Retain / accept","Keep risk within capacity"]]))
sub("Behavioural biases", 4,
  T(["Bias","Symptom"],
    [["Herd mentality","Buy what everyone buys"],
     ["Anchoring","Stuck to a past price/number"],
     ["Confirmation bias","Seek only supporting information"],
     ["Loss aversion","Pain of loss &gt; joy of gain → hold losers"],
     ["Overconfidence","Overtrading, concentration"],
     ["Recency bias","Extrapolate the latest returns"],
     ["Mental accounting","Treat money differently by source"],
     ["Availability bias","Judge by easily recalled events"],
     ["Regret aversion","Avoid decisions to avoid regret"],
     ["Endowment effect","Overvalue what you own"]]))
sub("Risk profiling", 4,
  KV([("Risk appetite / tolerance","Willingness to take risk (psychological)"),
      ("Risk capacity","Ability to take risk: age, income, dependants, wealth, horizon"),
      ("Risk required","Risk needed to reach the goal"),
      ("Tool","Questionnaire → conservative / moderate / aggressive"),
      ("Rule","Recommend within the lower of appetite and capacity")]))
sub("Asset allocation", 5,
  T(["Type","Meaning"],
    [["Strategic","Long-term mix by goal &amp; risk profile"],
     ["Tactical","Short-term tilt on market view"],
     ["Dynamic","Changes with valuation / rules (e.g. BAF)"],
     ["Rebalancing","Bring mix back to target periodically"]]) +
  K("Asset allocation drives most of portfolio return variance","Age-based rule: equity % ≈ 100 − age (thumb rule)") )
sub("Do-it-yourself vs adviser", 1,
  K("DIY: low cost, needs knowledge & discipline","Distributor / RIA: guidance, behaviour coaching"))

# ---------------------------------------------------------------- CH 2
chap(2, "Concept & Role of a Mutual Fund", "4", 3)
sub("What a mutual fund is", 4,
  KV([("Definition","Pool of money from many investors, invested per a stated objective, managed professionally"),
      ("Legal form","Trust (SEBI-registered)"),
      ("Units","Investor gets units; ownership ∝ units held"),
      ("Face value","Usually ₹10 per unit at NFO"),
      ("NAV","Value per unit = net assets ÷ units"),
      ("AUM","Total market value of scheme assets = NAV × units"),
      ("Pass-through","Gains/losses belong to unitholders; AMC only charges fees")]))
sub("Key terms: scheme, plan, option", 4,
  T(["Term","Meaning"],
    [["Scheme","The fund (e.g. ABC Flexi Cap Fund)"],
     ["Plan","Direct (no distributor, lower TER) / Regular (via distributor)"],
     ["Option","Growth (no payout) / IDCW payout / IDCW reinvestment / IDCW transfer"],
     ["IDCW","Income Distribution cum Capital Withdrawal (renamed from 'dividend', 2021) — paid from investor's own capital/gains"]]) +
  TRAP("Direct plan NAV &gt; regular plan NAV of the same scheme (lower expenses), never the opposite."))
sub("Advantages of mutual funds", 4,
  T(["Advantage","Note"],
    [["Professional management","Research, fund manager"],
     ["Diversification","Many securities with small money"],
     ["Economies of scale","Lower transaction cost per rupee"],
     ["Liquidity","Open-ended: redeem any business day"],
     ["Tax deferral / efficiency","Tax only on redemption; no tax inside fund"],
     ["Convenience","SIP, STP, SWP, switch, online"],
     ["Low ticket size","SIP from ₹100–500"],
     ["Transparency","Daily NAV, monthly portfolio"],
     ["Regulatory comfort","SEBI regulated"]]))
sub("Limitations of mutual funds", 3,
  L("No customisation of portfolio","Choice overload (many schemes)","No control over costs / fund manager decisions","No guaranteed returns","Expenses reduce returns","Applicable NAV known only after cut-off"))
sub("Classification by structure", 5,
  T(["Type","Buy / sell","Notes"],
    [["Open-ended","Any day from AMC at NAV","No fixed maturity; unit capital varies"],
     ["Close-ended","NFO only; then on stock exchange","Fixed maturity; <b>must be listed</b>; may trade at discount/premium to NAV"],
     ["Interval","Open for purchase/redemption only in specified intervals","Listed; min 2-day interval window"]]))
sub("Classification by management style", 5,
  T(["Type","Meaning","Cost"],
    [["Active","Fund manager picks securities to beat benchmark","Higher TER"],
     ["Passive — Index fund","Replicates an index; bought from AMC at NAV","Low TER (max 1%)"],
     ["Passive — ETF","Index tracking; traded on exchange in demat, intraday price","Lowest TER; needs demat"],
     ["Fund of Funds (FoF)","Invests in other MF schemes (domestic/overseas)","Two layers of cost"]]) +
  K("Smart beta / factor indices","Tracking error = gap vs index"))
sub("Classification by asset class & objective", 4,
  K("Equity","Debt","Hybrid","Solution-oriented","Other (index, ETF, FoF)","Growth / income / liquidity objectives","Domestic vs international","Sectoral / thematic"))
sub("SEBI scheme categories (Oct 2017)", 5,
  "<p class='sub'>One scheme per category per AMC (exceptions: index funds, ETFs, FoFs, sectoral/thematic).</p>" +
  T(["Equity (11)","Rule"],
    [["Large cap","≥80% large cap (top 100)"],["Mid cap","≥65% mid (101–250)"],["Small cap","≥65% small (251+)"],
     ["Large &amp; mid","≥35% each"],["Multi cap","≥25% each in large, mid, small"],["Flexi cap","≥65% equity, any cap"],
     ["Focused","Max 30 stocks"],["Dividend yield","≥65% in dividend-yielding stocks"],["Value / Contra","Value or contra strategy (one of the two) "+V],
     ["Sectoral / thematic","≥80% in sector/theme"],["ELSS","≥80% equity, 3-yr lock-in, 80C"]]) +
  T(["Debt (16)","Rule (Macaulay duration unless stated)"],
    [["Overnight","1-day securities"],["Liquid","Up to 91 days maturity"],["Ultra short duration","3–6 months"],
     ["Low duration","6–12 months"],["Money market","Up to 1 yr maturity"],["Short duration","1–3 yrs"],
     ["Medium duration","3–4 yrs"],["Medium to long","4–7 yrs"],["Long duration","&gt;7 yrs"],["Dynamic bond","Any duration"],
     ["Corporate bond","≥80% AA+ &amp; above"],["Credit risk","≥65% AA &amp; below"],["Banking &amp; PSU","≥80% banks, PSUs, PFIs, municipal bonds"],
     ["Gilt","≥80% G-secs"],["Gilt 10-yr constant duration","≥80% G-secs, Macaulay duration 10 yrs"],["Floater","≥65% floating rate"]]) +
  T(["Hybrid (7)","Rule"],
    [["Conservative hybrid","Equity 10–25%, debt 75–90%"],["Balanced hybrid","Equity 40–60%, no arbitrage"],
     ["Aggressive hybrid","Equity 65–80%"],["(AMC offers balanced <i>or</i> aggressive)",""],
     ["Dynamic asset allocation / BAF","0–100% equity, dynamically"],["Multi-asset allocation","≥3 asset classes, ≥10% each"],
     ["Arbitrage","≥65% equity (hedged) arbitrage"],["Equity savings","≥65% equity incl. hedged, ≥10% debt"]]) +
  T(["Solution-oriented (2) &amp; other","Rule"],
    [["Retirement fund","Lock-in 5 yrs or till retirement, whichever earlier"],
     ["Children's fund","Lock-in 5 yrs or till child turns 18, whichever earlier"],
     ["Index funds / ETFs","≥95% in index securities"],["FoF (domestic/overseas)","≥95% in underlying funds"]]) +
  K("Large cap = top 100 by full market cap (AMFI list, updated half-yearly)"))
sub("Growth of MF industry in India", 3,
  T(["Phase","Period","Event"],
    [["I","1964–1987","UTI (UTI Act 1963) sole player; US-64 first scheme"],
     ["II","1987–1993","Public sector MFs (SBI MF 1987 first non-UTI)"],
     ["III","1993–2003","Private sector entry; first SEBI MF Regs 1993 (Kothari Pioneer first private MF); MF Regs 1996"],
     ["IV","2003–2014","UTI split (Feb 2003): SUUTI + UTI MF; mergers; entry load abolished 2009"],
     ["V","2014 onwards","Fast growth, B-30 push, 'Mutual Funds Sahi Hai' (2017), SIP boom"]]) +
  K("Industry AUM crossed ₹50 lakh crore (Dec 2023) " + V, "Monthly SIP flows record highs " + V))

# ---------------------------------------------------------------- CH 3
chap(3, "Legal Structure of Mutual Funds in India", "3", 3)
sub("Three-tier structure", 5,
  F("SPONSOR  (holds ≥40% of AMC net worth)\n   │ sets up trust, signs trust deed\n   ▼\nTRUSTEES  (hold assets for unitholders)\n   │ appoint AMC via Investment Management Agreement\n   ▼\nAMC  (manages the money)\n   │ appoints\n   ▼\nCustodian · RTA · Fund accountant · Auditor · Bankers · Distributors\n\nINVESTORS = beneficial owners of scheme assets") +
  K("Trust deed: sponsor + trustees","Investment Management Agreement (IMA): trustees + AMC","Registered under Indian Registration Act 1908 / Indian Trusts Act 1882"))
sub("Sponsor", 4,
  KV([("Role","Promoter; sets up trust and AMC; like a company's promoter"),
      ("Eligibility (traditional)","5 yrs in financial services · positive net worth all 5 yrs · net worth (last yr) &gt; contribution to AMC · profit in 3 of last 5 yrs incl. latest"),
      ("Stake","≥40% of AMC net worth (anyone holding ≥40% is deemed sponsor)"),
      ("Alternative route","Private equity / other sponsors allowed with conditions (2023) " + V),
      ("Liability","Not liable for scheme losses beyond initial contribution")]))
sub("Trustees", 5,
  KV([("Form","Board of trustees or trustee company"),
      ("Number","≥4 trustees; ≥2/3 independent (not associated with sponsor)"),
      ("Role","Guardians of unitholders' interest; supervise AMC"),
      ("Duties","Approve schemes · ensure AMC compliance · check AMC transactions with associates · review investor complaints · report to SEBI half-yearly"),
      ("Meetings","At least 6 a year (once every 2 months)"),
      ("Powers","Can remove AMC (with unitholder approval / SEBI); approve key personnel"),
      ("Not allowed","Trustee of one MF can't be trustee of another (unless independent in both, with approval)")]))
sub("Asset Management Company (AMC)", 5,
  KV([("Role","Manages the money; launches schemes; investment decisions"),
      ("Net worth","≥ ₹50 crore (all times)"),
      ("Board","≥50% independent directors"),
      ("Approval","SEBI-approved; appointed by trustees"),
      ("Business","Only MF management + permitted management/advisory services to pooled funds (PMS/AIF via conditions), no conflicting business"),
      ("Key people","CEO, CIO, fund managers, compliance officer, investor relations officer"),
      ("Skin in the game","AMC invests a set % of AUM in its schemes; part of key employees' pay in scheme units (lock-in) " + V),
      ("Liability","Acts as agent; trust owns assets — not AMC")]))
sub("Service providers", 4,
  T(["Entity","Role","Key rule"],
    [["Custodian","Safekeeps securities, settles trades, corporate actions","SEBI-registered; independent of sponsor (sponsor/associates hold &lt;50% of custodian's voting rights, or 50% independent directors)"],
     ["RTA","Investor records: purchase, redemption, statements","SEBI-registered (e.g. CAMS, KFintech)"],
     ["Fund accountant","Calculates NAV","Can be AMC in-house or outsourced"],
     ["Auditor","Audits scheme accounts","Different auditors for AMC and schemes"],
     ["Collecting / paying bankers","Receive and pay money",""],
     ["Distributors","Sell units","ARN holders (AMFI)"],
     ["KRA","KYC records","CVL, NDML, CAMS KRA, KFin KRA, DotEx"]]))
sub("Role of regulators", 4,
  T(["Regulator / body","Role"],
    [["SEBI","Primary regulator; SEBI (Mutual Funds) Regulations 1996; registration, investment rules, disclosure"],
     ["RBI","Bank-sponsored MFs (as bank regulator); money market &amp; debt market rules; overseas investment limits"],
     ["Ministry of Finance","Policy, taxation"],
     ["Ministry of Corporate Affairs / ROC","AMC and trustee company are companies"],
     ["Stock exchanges","Listing of close-ended / ETFs; MF platforms (NSE NMF II, BSE StAR MF)"]]))
sub("AMFI", 4,
  KV([("Set up","1995 (non-profit industry association)"),
      ("Is AMFI an SRO?","No — trade body; SEBI regulates"),
      ("Does","ARN registration of distributors · AMFI Code of Ethics (ACE) for AMCs · Code of Conduct for intermediaries · investor awareness ('Mutual Funds Sahi Hai') · publishes NAVs · large/mid/small cap list"),
      ("Objectives","Professional &amp; ethical standards, represent industry to SEBI/Govt, investor education")]))

# ---------------------------------------------------------------- CH 4
chap(4, "Legal & Regulatory Framework", "≈5–6", 4)
sub("SEBI's objectives & MF Regulations", 3,
  K("Protect investors","Develop and regulate the securities market","MF Regulations 1996: registration, constitution, schemes, investment, disclosure, accounting","New MF Regulations overhaul approved 2025 " + V))
sub("Key investment restrictions", 4,
  T(["Limit","Rule " + V],
    [["Single company equity","≤10% of scheme NAV (not for index/sector funds as per index weights)"],
     ["All schemes of AMC in one company","≤10% of that company's paid-up voting capital"],
     ["Single issuer debt","≤10% of NAV (AAA); 8% (AA); 6% (A &amp; below); +2% with trustee approval"],
     ["Sector (debt)","≤20% of NAV in one sector (exceptions apply)"],
     ["Group exposure","≤10% of NAV in one group (15% with trustees)"],
     ["Sponsor group","≤10% in listed securities of sponsor group"],
     ["Unlisted equity","≤5% (open-ended), 10% (close-ended)"],
     ["Inter-scheme investment","≤5% of NAV of the investing scheme; no fees"],
     ["Borrowing","Only for redemption/IDCW; ≤20% of net assets, ≤6 months"],
     ["Derivatives","Gross exposure ≤100% of net assets (hedging excluded)"],
     ["Loans","Schemes cannot give loans"]]))
sub("Investors' rights", 5,
  T(["Right","Detail"],
    [["Ownership","Beneficial ownership of scheme assets ∝ units"],
     ["Timely payment","Redemption in 3 working days; IDCW in 7 working days; delay → 15% p.a. interest paid by AMC"],
     ["Information","SID, KIM, SAI, NAV, portfolio, annual report on request"],
     ["Vote","On wind-up / change of trustee etc.; 75% of unitholders can wind up a scheme or remove AMC"],
     ["Exit option","30 days without load on change of fundamental attributes"],
     ["Inspect","Documents like trust deed, IMA at AMC office"],
     ["Nominate","Nominate (up to 10 " + V + ")"]]) +
  TRAP("Investor CANNOT sue the trust for poor returns — no guarantee of returns."))
sub("Investors' obligations", 2,
  L("Read offer documents (SID/KIM)","Complete KYC; give correct information","Keep contact &amp; bank details updated","Monitor investments; claim dues"))
sub("Grievance redressal", 5,
  F("Investor → AMC / RTA (Investor Relations Officer)\n        → not satisfied → SEBI SCORES (online)\n        → still not resolved → SMART ODR (online dispute resolution: conciliation, then arbitration)\n        → courts / consumer forum") +
  K("AMC must resolve within set timelines (SCORES: 21 days " + V + ")","Trustees review complaints","AMFI not a grievance forum for investors (but acts on distributor misconduct)"))
sub("AMFI Code of Ethics (ACE) — for AMCs", 2,
  K("Integrity","Due diligence","Disclosure","Professional selling","Investor protection"))
sub("AMFI Code of Conduct for intermediaries", 4,
  L("Risk-profile the client; recommend suitable products","Disclose all commissions (trail etc.) from competing schemes","Don't rebate commission or give gifts to induce","No churning (switching for commission)","Don't misrepresent / promise returns","Keep client information confidential","Ensure KYC; don't handle investor cash beyond rules","Keep ARN valid; follow SEBI &amp; AMFI circulars"))
sub("Due diligence of distributors by AMCs", 3,
  "<p class='sub'>AMCs must do due diligence on distributors meeting ANY of:</p>" +
  L("Multiple points of presence (&gt;20 locations)","AUM &gt; ₹100 crore (non-institutional) across industry","Commission &gt; ₹1 crore p.a. across industry","Commission &gt; ₹50 lakh from a single MF") + K(V))
sub("Advertisement code", 3,
  KV([("Standard warning","'Mutual Fund investments are subject to market risks, read all scheme related documents carefully.'"),
      ("Audio/visual","Warning must be clear and at readable/audible speed"),
      ("Performance ads","Show with benchmark; standard periods (1/3/5 yrs, since inception); CAGR; same scheme's direct/regular as relevant"),
      ("Not allowed","Promise of returns, comparisons that mislead, ranking without source")]))
sub("Special regulatory tools", 4,
  T(["Tool","What"],
    [["Segregated portfolio (side pocket)","After a credit event (downgrade below investment grade / default), bad paper is split into a separate portfolio; investors get units in both; no fresh subscriptions in segregated part"],
     ["Swing pricing","Open-ended debt (except overnight, gilt, gilt 10-yr): NAV adjusted in market dislocation so exiting investors bear cost"],
     ["Stress testing","Debt schemes tested monthly for liquidity and interest rate shocks"],
     ["Riskometer","6 levels, monthly review (see Ch10)"],
     ["Potential Risk Class (PRC)","Debt matrix (see Ch10)"]]))
sub("Who can be a distributor", 3,
  K("Individual: NISM certification + AMFI ARN","Corporate: ARN + employees with EUIN","Distributor can't charge advisory fee; can give incidental advice","Individual can't be both MFD and RIA (SEBI IA Regs 2020)","Can't call self 'independent' / 'adviser'"))
sub("Specialized Investment Fund (SIF) — V-D topic", 5,
  T(["Item","Rule " + V],
    [["What","New product class under MF regulations, between MF and PMS; separate brand from the MF"],
     ["Min investment","₹10 lakh per investor (PAN) across all SIF strategies of an AMC; accredited investors exempt"],
     ["Short exposure","Unhedged short via derivatives up to 25% of net assets"],
     ["Called","'Investment strategy' (not 'scheme')"],
     ["Risk label","Risk band 1–5"],
     ["Redemption","Daily / weekly / per strategy; notice period up to 15 working days"],
     ["AMC eligibility","≥3 yrs ops + avg AUM ≥ ₹10,000 cr (last 3 yrs) + clean record; OR CIO with 10 yrs &amp; ₹5,000 cr AUM + additional FM 3 yrs &amp; ₹500 cr"],
     ["Distributor","ARN + NISM V-D (or V-A + XIII)"]]) +
  T(["Strategy","Rule " + V],
    [["Equity Long-Short","≥80% equity; short ≤25%"],["Equity Ex-Top 100 Long-Short","≥65% outside top 100; short ≤25%"],
     ["Sector Rotation Long-Short","≥80% in ≤4 sectors; short at sector level"],["Debt Long-Short","Short via exchange-traded debt derivatives"],
     ["Sectoral Debt Long-Short","≥2 sectors; ≤75% in one"],["Active Asset Allocator Long-Short","Equity, debt, REIT/InvIT, commodity derivatives"],
     ["Hybrid Long-Short","≥25% equity, ≥25% debt; short ≤25%"]]))

# ---------------------------------------------------------------- CH 5
chap(5, "Scheme Related Information", "≈5–6", 4)
sub("Offer documents: SID, SAI, KIM", 5,
  T(["Document","Contains","Updated " + V],
    [["SID (Scheme Information Document)","Scheme-specific: objective, asset allocation, strategy, risks, benchmark, fund manager, loads, expenses, past performance","Annually / on material change (addendum)"],
     ["SAI (Statement of Additional Information)","Fund-house level: sponsor, AMC, trustees, legal info, tax, valuation norms, investor rights","Within 3 months of FY end; changes via addendum"],
     ["KIM (Key Information Memorandum)","Abridged SID; comes with every application form","With SID updates"]]) +
  TRAP("SID + SAI together = the full offer document. KIM must accompany application forms.") +
  K("Addendum = changes before the next update","SEBI doesn't 'approve' SID; it gives observations"))
sub("Contents of SID (checklist)", 3,
  K("Name &amp; category","Riskometer + PRC (debt)","Investment objective","Asset allocation","Strategy","Benchmark (TRI)","Fund manager","Plans &amp; options","Min amount","Loads","TER","NAV disclosure","Past performance","Risk factors","Tax","Cut-off times","Product label (for whom)"))
sub("Fundamental attributes", 5,
  KV([("Includes","Type of scheme (open/closed) · investment objective · asset allocation/investment pattern · terms of issue (liquidity, loads, fees/expenses, guarantees)"),
      ("To change","Trustees' approval + SEBI comments + written notice to unitholders + newspaper ad"),
      ("Investor protection","30-day exit window at NAV, <b>without exit load</b>")]))
sub("New Fund Offer (NFO)", 5,
  KV([("NFO period","Max 15 days (ELSS can be longer)"),
      ("NFO price","Usually ₹10 face value"),
      ("Allotment / refund","Within 5 business days of NFO closing"),
      ("Min investors (open-ended)","≥20 investors; no single investor &gt;25% of corpus (else rebalance/refund)"),
      ("NFO expenses","Borne by AMC (not the scheme)"),
      ("ASBA","Available for NFO applications"),
      ("Reopen for continuous sale","Open-ended: within 5 business days of allotment")]) +
  TRAP("'NFO at ₹10 is cheap' is a myth — NAV level doesn't mean cheap or dear."))
sub("Plans & options", 4,
  T(["Choice","Option","Effect"],
    [["Plan","Direct vs Regular","Same portfolio, different TER → different NAV"],
     ["Option","Growth","Gains stay in NAV"],
     ["","IDCW payout","Cash paid; NAV falls by IDCW"],
     ["","IDCW reinvestment","IDCW reinvested as units (no load)"],
     ["","IDCW transfer","IDCW invested into another scheme"]]) +
  K("IDCW is paid out of distributable surplus incl. investor's own capital (equalisation reserve) — hence 'capital withdrawal'"))
sub("Continuous disclosures", 5,
  T(["Item","Frequency / timeline " + V],
    [["NAV","Every business day, AMC + AMFI site by 11 pm (FoF overseas: by 10 am next day)"],
     ["Portfolio","Monthly (all schemes) within 10 days; fortnightly (debt) within 5 days"],
     ["Half-yearly financials","Unaudited, within 1 month of half-year end"],
     ["Annual report","Within 4 months of FY end (abridged sent / on website)"],
     ["Riskometer","Monthly, with portfolio"],
     ["TER","Daily on website; changes with 3 working days' notice"],
     ["Factsheet / scheme dashboard","Monthly / on website"],
     ["Commission paid","In CAS"]]))
sub("Other disclosures", 2,
  K("Scheme performance vs benchmark","Fund manager's other schemes","Portfolio turnover","Unclaimed amounts","Voting by AMC on company resolutions"))

# ---------------------------------------------------------------- CH 6
chap(6, "Fund Distribution & Channel Management", "≈5", 3)
sub("Distribution channels", 4,
  T(["Channel","Notes"],
    [["Individual MFD (IFA)","Largest by number; ARN holder"],
     ["Banks","Large branch network; ARN + EUIN for staff"],
     ["National distributors / NBFCs","Corporate ARN"],
     ["Stock brokers / exchange platforms","NSE NMF II, BSE StAR MF"],
     ["Online platforms / fintech","As distributor (regular) or execution-only platforms (direct) " + V],
     ["MF Utilities (MFU) / MF Central","Common transaction platforms for many AMCs"],
     ["RIA","Charges fee to client, uses direct plans, no commission"],
     ["AMC direct","Direct plans via AMC website/branches"]]))
sub("Becoming a distributor", 5,
  KV([("Certification","NISM Series V-A (MFD) / V-D for SIF; V-B for new cadre (simple products)"),
      ("Registration","AMFI Registration Number (ARN) via KYD (Know Your Distributor) through CAMS"),
      ("Validity","ARN valid 3 years; renew via CPE (Continuing Professional Education) before expiry"),
      ("Employees","EUIN (Employee Unique Identification Number) for each salesperson of corporate distributors"),
      ("Empanelment","With each AMC to get commission"),
      ("Age","Adult (18+)")]) +
  TRAP("EUIN identifies the salesperson who advised; for 'execution-only' a declaration is signed."))
sub("Distributor remuneration", 5,
  T(["Item","Rule " + V],
    [["Trail commission","Only model allowed; paid from scheme TER (regular plan)"],
     ["Upfront commission","Banned (Oct 2018); no upfronting of trail"],
     ["Entry load","Abolished Aug 2009"],
     ["Transaction charge","₹100 (existing) / ₹150 (first-time) on purchases ≥ ₹10,000, if distributor opts in; SIP only if commitment ≥ ₹10,000"],
     ["Disclosure","Commission shown in investor's CAS; distributor must disclose commissions of schemes recommended"],
     ["Rebating","Not allowed"],
     ["Payment","Commission paid only to ARN holder, by AMC"]]))
sub("Code of conduct & good practice", 4,
  L("Know your client (KYC + needs + risk profile)","Suitability before selling","Full disclosure of commission &amp; conflicts","No mis-selling or churning","Service: statements, nominations, updates","Keep certification &amp; ARN valid"))
sub("Change of distributor", 3,
  K("Investor can change distributor without NOC from old one","Or move to direct plan (switch = redemption for tax)","Trail of existing units goes to new distributor only from change date " + V))
sub("Distributor vs RIA", 4,
  T(["","MFD","RIA"],
    [["Earns from","Commission (AMC)","Fee (client)"],
     ["Plans used","Regular","Direct"],
     ["Advice","Incidental to sales","Full advisory"],
     ["Registration","AMFI ARN","SEBI IA registration"],
     ["Can be both?","No (individual)",""]]))
sub("New cadre & due diligence", 2,
  K("New cadre (NISM V-B): simple schemes only (e.g. index, liquid, ELSS, BAF) " + V,"AMC due diligence on large distributors (see Ch4)"))

# ---------------------------------------------------------------- CH 7
chap(7, "NAV, TER & Pricing of Units", "≈6", 5)
sub("NAV computation", 5,
  F("NAV = (Market value of investments + Receivables + Accrued income + Other assets\n       − Accrued expenses − Payables − Other liabilities) ÷ Units outstanding\n\nExample: Assets ₹110 cr, liabilities ₹10 cr, units 5 cr  →  NAV = 100/5 = ₹20\nAUM = NAV × units") +
  K("NAV computed every business day","Different NAV for direct and regular plan","NAV to 4 decimals (most schemes) " + V))
sub("Valuation of securities", 4,
  T(["Security","Valuation"],
    [["Listed equity","Closing price on principal exchange (NSE / BSE)"],
     ["Non-traded / thinly traded equity","Fair value by AMC's valuation policy"],
     ["Debt &amp; money market","Average of prices from valuation agencies (CRISIL, ICRA); fully mark-to-market (no amortisation since 2020)"],
     ["Govt securities","Agency prices"],
     ["Units of other MFs","Their NAV"],
     ["Principle","Fair valuation; valuation policy approved by AMC board &amp; trustees"]]))
sub("Income & expense accounting", 3,
  K("Dividends: accounted on ex-date","Interest: accrued daily","Expenses: accrued daily","Gains: realised/unrealised in NAV","Equalisation reserve: part of sale price kept so IDCW doesn't dilute"))
sub("Loads", 5,
  KV([("Entry load","Abolished (Aug 2009)"),
      ("Exit load","Charged on redemption within a set period; credited back to the scheme (not AMC)"),
      ("Sale price","= Applicable NAV"),
      ("Repurchase price","= NAV × (1 − exit load)"),
      ("No load on","Bonus units, IDCW reinvestment units, switch between plans of same scheme (as per SID) " + V),
      ("CDSC","Contingent deferred sales charge: load falls with holding period")]) +
  F("Example: NAV ₹50, exit load 1% → repurchase price = 50 × 0.99 = ₹49.50"))
sub("Total Expense Ratio (TER)", 5,
  T(["Daily net assets (₹ cr)","Equity-oriented","Other (debt etc.)"],
    [["First 500","2.25%","2.00%"],["Next 250","2.00%","1.75%"],["Next 1,250","1.75%","1.50%"],
     ["Next 3,000","1.60%","1.35%"],["Next 5,000","1.50%","1.25%"],
     ["Next 40,000","−0.05% per ₹5,000 cr","−0.05% per ₹5,000 cr"],["Above 50,000","1.05%","0.80%"]]) +
  T(["Scheme type","Max TER " + V],
    [["Index fund / ETF","1.00%"],["FoF investing in liquid/index/ETF","1.00%"],["FoF (equity-oriented underlying)","2.25%"],["Other FoF","2.00%"],["Close-ended / interval equity","1.25%"],["Close-ended / interval other","1.00%"]]) +
  K("Additional up to 0.30% for B-30 inflows (suspended since Mar 2023) " + V,"GST on management fee over and above TER","Brokerage cap: 0.12% cash, 0.05% derivatives " + V,"Direct plan TER lower (no distribution cost)","SEBI revised expense framework (2025–26): check workbook " + V) +
  TRAP("NFO expenses are borne by the AMC, not the scheme."))
sub("Recurring expense heads", 2,
  K("Investment management fee","Trustee fee","Custodian","RTA","Audit","Marketing &amp; selling","Distribution commission","Brokerage &amp; transaction cost (capped)","Investor education (2 bps " + V + ")"))
sub("Stamp duty & STT", 4,
  T(["Charge","Rate","On"],
    [["Stamp duty","0.005%","Purchases incl. switch-in, IDCW reinvestment (since 1 Jul 2020)"],
     ["STT","0.001%","Redemption of equity-oriented units (seller)"],
     ["No STT","—","Debt funds"]]))
sub("Applicable NAV & cut-off", 5,
  T(["Transaction","Cut-off","Applicable NAV"],
    [["Equity / debt purchase (any amount)","3:00 pm","Day funds are realised (if before cut-off)"],
     ["Liquid / overnight purchase","1:30 pm","Day <b>before</b> the day funds are realised"],
     ["Liquid / overnight redemption","3:00 pm","Day <b>before</b> the next business day"],
     ["Equity / debt redemption","3:00 pm","Same day"],
     ["Switch","As redemption (out) and purchase (in)","Switch-in needs realisation"]]) +
  K("Time-stamping of applications","Funds realisation rule for all purchases (Feb 2021)","Liquid funds: graded exit load for 1–6 days"))
sub("IDCW mechanics", 3,
  F("NAV before 15.00 · IDCW ₹1 per unit  →  ex-IDCW NAV ≈ 14.00\nInvestor's wealth unchanged (₹1 cash + ₹14 NAV) — before tax") +
  K("Declared from distributable surplus","Record date fixed","Payable within 7 working days"))

# ---------------------------------------------------------------- CH 8
chap(8, "Taxation", "3", 4)
sub("Fund categories for tax", 5,
  T(["Category","Definition " + V],
    [["Equity-oriented fund","≥65% in domestic listed equity (FoF: ≥90% in units of such funds, which hold ≥90% equity)"],
     ["Specified mutual fund (Sec 50AA)","&gt;65% in debt &amp; money market (from AY 2026-27; earlier: ≤35% equity)"],
     ["Other funds","Hybrids 35–65% equity, gold/silver ETFs &amp; FoFs, international FoFs"]]))
sub("Capital gains tax (from 23 Jul 2024)", 5,
  T(["Type","STCG","LTCG"],
    [["Equity-oriented","Held ≤12 m · 20% (111A)","Held &gt;12 m · 12.5% on gains above ₹1.25 lakh/yr (112A)"],
     ["Specified MF (debt), bought on/after 1 Apr 2023","Slab rate — always, any holding period",""],
     ["Others (listed units)","≤12 m · slab","&gt;12 m · 12.5%, no indexation"],
     ["Others (unlisted units, e.g. intl FoF)","≤24 m · slab","&gt;24 m · 12.5%, no indexation"]]) +
  K("Grandfathering: equity bought before 1 Feb 2018 → cost = higher of actual cost and (lower of FMV on 31 Jan 2018 and sale price)","No indexation benefit any more for MF units") +
  TRAP("Debt fund bought before 1 Apr 2023 and held &gt;24 m: LTCG 12.5% (no indexation) " + V))
sub("IDCW taxation", 5,
  KV([("Since 1 Apr 2020","Taxed in investor's hands at slab rate (DDT abolished)"),
      ("TDS (resident)","10% u/s 194K if IDCW &gt; ₹10,000 per FY per AMC (₹5,000 before Apr 2025) " + V),
      ("TDS (NRI)","20% + surcharge/cess (or DTAA rate)"),
      ("Growth vs IDCW","Growth defers tax till redemption → usually more tax-efficient")]))
sub("Set-off & carry forward of losses", 4,
  T(["Loss","Can set off against"],
    [["Short-term capital loss","STCG and LTCG"],["Long-term capital loss","LTCG only"],["Carry forward","8 assessment years (return filed on time)"]]))
sub("Dividend & bonus stripping", 3,
  KV([("Dividend stripping (94(7))","Buy within 3 months before record date + sell within 9 months after → loss up to IDCW ignored"),
      ("Bonus stripping (94(8))","Buy within 3 months before record date + sell original units within 9 months after → loss ignored, added to cost of bonus units")]))
sub("Tax benefits & other points", 4,
  T(["Item","Rule"],
    [["ELSS","Deduction u/s 80C up to ₹1.5 lakh (old regime only); 3-yr lock-in per instalment"],
     ["New tax regime","Default regime; no 80C"],
     ["Switch","Between schemes, or plans (regular→direct) = transfer → taxable"],
     ["SIP","Each instalment has its own holding period (FIFO on redemption)"],
     ["Segregated portfolio","Cost split between main and segregated units in NAV ratio"],
     ["NRI","TDS on capital gains by AMC"],
     ["Distributor GST","Registration if commission &gt; ₹20 lakh/yr"]]))

# ---------------------------------------------------------------- CH 9
chap(9, "Investor Services", "10", 5)
sub("Who can invest", 3,
  K("Resident individuals (single/joint)","Minors through guardian","HUF (Karta)","Companies, trusts, societies, firms (with board/trust resolution)","NRIs, PIOs, OCIs (repatriable / non-repatriable)","FPIs","Banks, FIs, insurers") +
  TRAP("OCBs (overseas corporate bodies) can't invest. Some AMCs don't accept US/Canada persons (FATCA)."))
sub("KYC", 5,
  KV([("What","One-time; recorded with a KRA, valid across all MFs and intermediaries"),
      ("Documents","PAN (mandatory), proof of address, photo, in-person verification (IPV/VIPV)"),
      ("CKYC","Central KYC registry (CERSAI) — 14-digit KIN"),
      ("e-KYC","Aadhaar-based; OTP route has investment limit " + V),
      ("KYC status","Validated (Aadhaar/official docs verified) · Registered · On hold (re-verify) " + V),
      ("FATCA / CRS","Self-declaration of tax residency"),
      ("PAN exemption","Micro investments ≤ ₹50,000 per year per investor per AMC (PEKRN), Sikkim residents, some govt officials")]))
sub("Application & payment rules", 5,
  T(["Rule","Detail " + V],
    [["Payment modes","Cheque, DD, NEFT/RTGS/IMPS, UPI, net banking, NACH/OTM mandates, ASBA (NFO)"],
     ["Cash","Up to ₹50,000 per investor per FY per MF (KYC done)"],
     ["Third-party payment","Not allowed. Exceptions: parent/grandparent/relative for minor (≤ ₹50,000 per transaction), employer for SIP via payroll, custodian for FPI, AMC to distributor (commission as units), stock broker (exchange)"],
     ["Bank accounts","Register up to 5 (individuals) / 10 (others)"],
     ["Realisation","Units allotted only on realisation of funds (all schemes)"],
     ["Joint holding","Up to 3 holders; mode: joint / anyone or survivor"]]))
sub("Minor's investments", 5,
  KV([("Holding","Minor as sole holder only — no joint holders"),
      ("Guardian","Natural (parent) or court-appointed; proof of DOB &amp; relationship"),
      ("Payment","From minor's bank account, or joint account of minor with guardian " + V),
      ("On majority (18)","Status change to major: KYC, bank details of the major; till then no transactions " + V),
      ("SIPs","Registered only till minor turns 18")]))
sub("Nomination", 5,
  KV([("Who can nominate","Individuals (single or joint); not for non-individuals, not by POA holder"),
      ("How many","Up to 10 nominees with % share " + V),
      ("Nominee can be","Minor (via guardian), individual; not a trust/company"),
      ("Opt-out","New single-holder folios: nominate or give opt-out declaration"),
      ("Effect","Nominee is a trustee for legal heirs (gets assets; heirs may claim)")]))
sub("Transmission & transfer", 4,
  T(["Case","Who gets units"],
    [["Death of sole holder with nominee","Nominee"],["Death of one joint holder","Surviving holder(s)"],["No nominee, sole holder","Legal heir(s) — succession certificate/probate above threshold " + V]]) +
  K("Documents: death certificate, claimant KYC, bank proof","Transmission is not a sale — no capital gains","Transfer of non-demat units now allowed in specified cases " + V,"Demat units: transfer via DP"))
sub("Purchase, redemption, switch timelines", 5,
  T(["Event","Timeline " + V],
    [["NFO allotment / refund","5 business days from close"],
     ["Redemption payout","3 working days (equity often T+2)"],
     ["IDCW payout","7 working days from record date"],
     ["Delay","15% p.a. interest to investor, paid by AMC"],
     ["Overseas/FoF exceptions","Extra days allowed in specified cases"]]))
sub("Account statements", 5,
  KV([("Transaction confirmation","Email/SMS within 5 business days of transaction"),
      ("CAS (monthly)","By 15th of next month for any month with a transaction (across MFs + demat, by depositories/RTAs)"),
      ("CAS (half-yearly)","For folios with no transaction in 6 months, by 21st Apr/Oct"),
      ("CAS shows","Holdings, transactions, commission paid to distributor, scheme TER"),
      ("Demat holders","Units in demat via DP; statement from depository")]))
sub("Systematic plans", 5,
  T(["Plan","What","Use"],
    [["SIP","Fixed amount at regular intervals (daily/weekly/monthly/quarterly)","Rupee-cost averaging, discipline"],
     ["STP","Transfer fixed amount from one scheme to another (e.g. liquid → equity)","Phased entry for lump sum"],
     ["SWP","Withdraw fixed amount regularly","Regular income; tax only on gains part"],
     ["Switch","Move between schemes/plans of same AMC","Taxable as redemption"],
     ["Micro SIP","≤ ₹50,000/yr without PAN (PEKRN)",""],
     ["SIP top-up / pause","Increase amount yearly / pause a few months",""]]) +
  F("Rupee-cost averaging: same ₹ buys more units when NAV is low → average cost ≤ average NAV"))
sub("Other services", 3,
  K("Pledge / lien on units (loans)","Change of address / bank mandate (with verification; cooling-off " + V + ")","Consolidation of folios","Unclaimed redemptions/IDCW: held in separate unclaimed plan; after 3 yrs investor gets value at that time, balance to investor education " + V,"MF Central / MFU / SCORES","Demat option for all schemes"))

# ---------------------------------------------------------------- CH 10
chap(10, "Risk, Return & Performance of Funds", "≈5–6", 4)
sub("Drivers of returns", 4,
  T(["Asset","Return drivers"],
    [["Equity","Earnings growth, valuation (P/E), economy, interest rates, liquidity, sentiment"],
     ["Debt","Interest (YTM), change in rates (duration), credit spread changes, rating changes"],
     ["Gold","Global price in USD, USD-INR, demand, geopolitical risk"],
     ["Real estate / REIT","Rent, occupancy, interest rates"]]) +
  K("Growth vs value styles","Large vs mid vs small cap cycles","Falling rates → long-duration debt gains"))
sub("Risks in fund categories", 5,
  T(["Fund","Main risks"],
    [["Equity","Market, volatility, sector concentration, liquidity (small caps)"],
     ["Debt","Interest rate, credit/default, liquidity, reinvestment, concentration"],
     ["Hybrid","Mix of equity &amp; debt risks"],
     ["International","Currency, country/political, overseas limits"],
     ["Gold","Price, currency"],
     ["Index/ETF","Tracking error, market risk"],
     ["All","Fund manager/AMC risk, regulatory &amp; tax change"]]))
sub("Measuring returns", 5,
  F("Absolute (simple) return = (End NAV − Start NAV) ÷ Start NAV\nAnnualised simple       = Absolute × 365 ÷ days\nCAGR                    = (End ÷ Start)^(1/years) − 1\nTotal return            = include IDCW (reinvested)\nXIRR                    = for SIPs / irregular cash flows\n\nEx: NAV 10 → 15 in 3 yrs: absolute 50%; CAGR = 1.5^(1/3) − 1 = 14.47%") +
  T(["Type","Meaning"],
    [["Point-to-point / trailing","Start and end dates fixed (e.g. 1/3/5 yrs to today)"],
     ["Rolling returns","Average of returns over every possible period → consistency"],
     ["Calendar-year","Each Jan–Dec"]]) +
  T(["SEBI rule for showing returns",""],
    [["&lt; 1 year","Simple (absolute) return"],["≥ 1 year","CAGR"],["Also show","Benchmark + additional benchmark; value of ₹10,000 invested; 1/3/5 yrs + since inception"]]))
sub("Measuring risk", 5,
  T(["Measure","Meaning"],
    [["Variance / Standard deviation","Total volatility of returns"],
     ["Beta","Market sensitivity (systematic risk)"],
     ["Downside deviation / semi-variance","Only bad volatility"],
     ["Modified duration","Debt price sensitivity to yield"],
     ["Average maturity / YTM","Debt portfolio profile"],
     ["Credit rating profile","Debt credit risk"],
     ["Portfolio turnover","Trading activity (cost)"],
     ["Tracking error","Index fund/ETF deviation from index"]]))
sub("Riskometer", 5,
  T(["Level","Typical schemes"],
    [["1 Low","Overnight"],["2 Low to Moderate","Liquid, money market"],["3 Moderate","Short duration, banking &amp; PSU"],
     ["4 Moderately High","Conservative hybrid, dynamic bond"],["5 High","Aggressive hybrid, BAF"],["6 Very High","Equity, sectoral, small cap"]]) +
  K("Evaluated monthly on portfolio","Based on market cap, volatility, liquidity (equity) and credit, interest rate, liquidity (debt)","Change communicated to investors","Disclosed in factsheet &amp; with portfolio") +
  TRAP("Six levels (Low → Very High). SIF uses risk band 1–5."))
sub("Potential Risk Class (PRC) matrix — debt", 5,
  T(["Interest rate risk ↓ / Credit risk →","A: Relatively low (CRV ≥12)","B: Moderate (CRV ≥10)","C: Relatively high (CRV &lt;10)"],
    [["Class I: Relatively low (MD ≤ 1 yr)","A-I","B-I","C-I"],
     ["Class II: Moderate (MD ≤ 3 yrs)","A-II","B-II","C-II"],
     ["Class III: Relatively high (any MD)","A-III","B-III","C-III"]]) +
  K("Shows MAXIMUM risk scheme can take","A-I safest, C-III riskiest","Change in PRC = fundamental attribute change"))

# ---------------------------------------------------------------- CH 11
chap(11, "Mutual Fund Scheme Performance", "≈5", 4)
sub("Benchmarks", 5,
  KV([("Why","To judge fund manager vs relevant market"),
      ("TRI","Total Return Index (price + dividends reinvested) mandatory since Feb 2018"),
      ("Two-tier","Tier 1: category-level benchmark (AMFI list); Tier 2: scheme-specific, optional " + V),
      ("Choice","Must match scheme's investment universe")]) +
  T(["Scheme","Typical benchmark"],
    [["Large cap","Nifty 100 TRI / BSE 100 TRI"],["Mid / small cap","Nifty Midcap 150 / Smallcap 250 TRI"],["Sectoral","Sector index TRI"],
     ["Debt","CRISIL / NSE debt indices matching duration &amp; credit"],["Hybrid","Composite (e.g. 65:35 equity:debt)"],
     ["Index fund / ETF","The tracked index"],["Gold ETF","Domestic gold price"],["International FoF","Overseas index (e.g. MSCI)"]]))
sub("Quantitative performance measures", 5,
  T(["Measure","Formula / reading"],
    [["Alpha (excess return)","Fund return − benchmark return"],
     ["Sharpe ratio","(Rp − Rf) ÷ σp · return per unit of total risk · use for diversified funds"],
     ["Treynor ratio","(Rp − Rf) ÷ βp · per unit of market risk · use for well-diversified portfolios"],
     ["Sortino ratio","(Rp − Rf) ÷ downside deviation"],
     ["Jensen's alpha","Rp − [Rf + β(Rm − Rf)] (actual − CAPM expected)"],
     ["Information ratio","Excess return ÷ tracking error"],
     ["R-squared","% of fund movement explained by benchmark (high = index-like)"],
     ["Up / down capture","% of benchmark's up / down moves captured"],
     ["Tracking error","Std dev of (fund − index) returns; lower = better for index funds/ETFs"],
     ["Tracking difference","Return gap (fund − index) over a period"]]) +
  F("Sharpe ex: Rp 15%, Rf 7%, σ 16% → (15 − 7)/16 = 0.5\nTreynor ex: same, β 1.2 → 8/1.2 = 6.67") +
  TRAP("Higher Sharpe/Treynor/Sortino = better. Lower tracking error = better. Treynor uses beta, Sharpe uses SD."))
sub("Qualitative & peer comparison", 3,
  K("Compare within same category only","Quartile ranking","Consistency (rolling returns)","Fund manager tenure &amp; process","AMC track record","Portfolio quality","Expense ratio","AUM size"))
sub("Sources of performance data", 2,
  K("Factsheets","AMFI website","SID / annual report","Scheme dashboard","Rating/research firms (CRISIL, Morningstar, Value Research)"))
sub("Index fund & ETF specifics", 4,
  KV([("Tracking error limit","≤2% (annualised) for index funds/ETFs " + V),
      ("ETF trading","On exchange via demat; price can differ from NAV; iNAV shown during the day"),
      ("Market makers / APs","Provide liquidity; large creation/redemption directly with AMC"),
      ("Direct with AMC","Investors can redeem with AMC if ETF illiquid on exchange (conditions) " + V)]))

# ---------------------------------------------------------------- CH 12
chap(12, "Mutual Fund Scheme Selection", "10", 5)
sub("Selection process", 5,
  F("Goal + horizon + risk profile  →  asset allocation  →  category  →  scheme  →  plan &amp; option") +
  T(["Horizon","Suitable category"],
    [["Days–3 months","Overnight, liquid, money market, arbitrage"],["3–12 months","Ultra short, low duration, money market"],
     ["1–3 yrs","Short duration, banking &amp; PSU, conservative hybrid, equity savings"],["3–5 yrs","Hybrid (BAF, aggressive), large cap"],
     ["&gt;5 yrs","Equity (flexi/large/mid/small), ELSS, index"]]))
sub("Choosing equity schemes", 5,
  T(["Choice","Points"],
    [["Market cap","Large: stable · Mid/small: higher return potential, higher risk, liquidity risk"],
     ["Style","Growth vs value vs blend"],
     ["Diversified vs focused vs sectoral","Concentration ↑ → risk ↑; sectoral/thematic only for informed investors"],
     ["Active vs passive","Active: chance of alpha, higher cost · Passive: low cost, market return"],
     ["Index fund vs ETF","Index fund: SIP-friendly, NAV-based · ETF: demat, intraday, lower TER, liquidity risk"],
     ["ELSS","Tax saving + equity; 3-yr lock-in (shortest among 80C options)"]]))
sub("Choosing debt schemes", 5,
  T(["Investor view / need","Pick"],
    [["Park money / emergency","Overnight, liquid"],["Rates expected to fall","Long duration, gilt, dynamic bond (gain on price)"],
     ["Rates expected to rise","Short duration, floater, overnight"],["Low credit risk","Gilt, banking &amp; PSU, corporate bond (AAA)"],
     ["Higher yield, accept credit risk","Credit risk fund"],["Hold to a date, predictable","Target maturity funds (passive debt, defined maturity)"]]) +
  K("Check: YTM, modified duration, average maturity, credit profile, PRC, expense ratio") +
  TRAP("YTM is not guaranteed return; NAV changes with rates and credit."))
sub("Choosing hybrid & other schemes", 4,
  T(["Scheme","Suits"],
    [["Conservative hybrid","Mostly debt + some equity kicker"],["Balanced advantage (BAF)","Auto equity allocation by valuation; first-time equity investors"],
     ["Aggressive hybrid","Equity-led with cushion; equity taxation"],["Multi-asset","Equity + debt + gold in one fund"],
     ["Equity savings","Low-volatility equity taxed fund"],["Arbitrage","Short-term parking with equity tax"],
     ["Retirement / children's","Goal-based, 5-yr lock-in"],["Gold / silver ETF &amp; FoF","Diversifier, inflation/crisis hedge"],
     ["International FoF","Geographic diversification; currency risk"]]))
sub("Plan & option selection", 4,
  T(["Choice","When"],
    [["Direct plan","Investor needs no help; lower cost"],["Regular plan","Wants distributor service &amp; guidance"],
     ["Growth","Wealth creation, tax deferral (most cases)"],["IDCW payout","Needs cash flow (but IDCW not assured; taxed at slab)"],
     ["SWP over IDCW","Fixed, predictable cash flow; tax only on gains"]]))
sub("Scheme-level checklist", 5,
  T(["Factor","Look for"],
    [["Performance","Consistent vs benchmark &amp; peers across periods (rolling)"],["Risk-adjusted return","Sharpe, Sortino, downside capture"],
     ["Expense ratio","Lower better, esp. debt &amp; passive"],["AUM size","Too small: concentration; too large in small caps: liquidity"],
     ["Portfolio","Quality, concentration, turnover"],["Fund manager","Tenure, process"],["Exit load &amp; lock-in","Match your horizon"],
     ["Tracking error","For index/ETF"]]))
sub("Mistakes to avoid", 3,
  L("Chasing last year's top performer","Buying NFOs because ₹10 'looks cheap'","Too many similar schemes (overlap)","Stopping SIPs in falls","Choosing IDCW for 'income' without need","Ignoring costs and tax"))
sub("Model portfolios by life stage", 3,
  T(["Investor","Equity : Debt : Gold (illustrative)"],
    [["Young, aggressive","70–80 : 15–25 : 5–10"],["Mid-life, moderate","50–60 : 30–40 : 10"],["Near retirement","30–40 : 50–60 : 10"],["Retired","20–30 : 60–70 : 10"]]))

# ---------------------------------------------------------------- RENDER
def stars(n):
    return f'<span class="st s{n}">' + "★"*n + '<i>' + "★"*(5-n) + '</i></span>'

total_subs = sum(len(c["subs"]) for c in CH)
five = [(c["n"], s["t"]) for c in CH for s in c["subs"] if s["s"] == 5]
four = [(c["n"], s["t"]) for c in CH for s in c["subs"] if s["s"] == 4]

idx_rows = "".join(
    f'<tr><td>{c["n"]}</td><td>{c["title"]}</td><td class="n">{c["marks"]}</td><td>{stars(c["stars"])}</td>'
    f'<td class="n">{len(c["subs"])}</td><td class="n">{sum(1 for s in c["subs"] if s["s"]==5)}</td></tr>' for c in CH)

def fivelist(items):
    out = {}
    for n, t in items: out.setdefault(n, []).append(t)
    return "".join(f'<p><b>Ch {n}</b> · ' + " · ".join(v) + "</p>" for n, v in out.items())

body = []
for c in CH:
    subs = "".join(
        f'<div class="sub-t"><div class="sh"><h3>{s["t"]}</h3>{stars(s["s"])}</div>{s["b"]}</div>' for s in c["subs"])
    body.append(f'''<section class="ch"><div class="chh"><span class="cn">{c["n"]:02d}</span><div><h2>{c["title"]}</h2>
      <p class="meta">≈{c["marks"]} marks · {len(c["subs"])} subtopics · chapter priority {stars(c["stars"])}</p></div></div><div class="body2">{subs}</div></section>''')

HTML = f'''<!doctype html><html><head><meta charset="utf-8"><title>NISM V-D Mutual Fund Module Summary</title>
<style>
@page {{ size: A4; margin: 11mm 10mm 12mm 10mm; }}
:root {{ --ink:#14202b; --muted:#56636f; --line:#cfd7df; --teal:#0d6a73; --teal-soft:#e2f1f2; --amber:#b86e00; --amber-soft:#fbefd9; --red:#b3261e; --red-soft:#fbe7e5; }}
* {{ box-sizing:border-box; }}
body {{ font-family: Carlito, "Liberation Sans", "DejaVu Sans", sans-serif; color:var(--ink); font-size:8.6pt; line-height:1.28; margin:0; background:#fff; }}
h1,h2,h3 {{ font-family: "Inter Display", Inter, Carlito, sans-serif; margin:0; line-height:1.12; }}
h1 {{ font-size:22pt; letter-spacing:-.01em; }}
h2 {{ font-size:13.5pt; }}
h3 {{ font-size:9.3pt; font-weight:700; }}
.cover {{ border-bottom:2.5pt solid var(--ink); padding-bottom:6pt; margin-bottom:8pt; }}
.cover .eyebrow {{ font:600 7.4pt Inter, sans-serif; letter-spacing:.08em; text-transform:uppercase; color:var(--muted); }}
.lead {{ color:var(--muted); margin:4pt 0 0; font-size:9pt; }}
.legend {{ display:flex; gap:14pt; flex-wrap:wrap; margin:6pt 0; font-size:8.2pt; }}
.st {{ font-family:"DejaVu Sans", sans-serif; color:var(--amber); letter-spacing:.5pt; font-size:8pt; white-space:nowrap; }}
.st i {{ color:#d9dde1; font-style:normal; }}
.st.s5 {{ color:var(--red); }}
table {{ border-collapse:collapse; width:100%; margin:3pt 0; page-break-inside:auto; }}
tr {{ page-break-inside:avoid; }}
th,td {{ border:.5pt solid var(--line); padding:2pt 4pt; vertical-align:top; text-align:left; }}
thead th {{ background:var(--teal-soft); font-weight:700; }}
.kv th {{ width:28%; background:#f4f6f8; font-weight:700; }}
td.n {{ text-align:right; font-variant-numeric:tabular-nums; white-space:nowrap; }}
.kw {{ display:flex; flex-wrap:wrap; gap:2.5pt; margin:3pt 0; }}
.kw span {{ border:.5pt solid var(--line); border-radius:6pt; padding:0 5pt; background:#fafbfc; font-size:8pt; }}
pre.f {{ font-family:"JetBrains Mono", "DejaVu Sans Mono", monospace; font-size:7.3pt; background:#f4f6f8; border-left:2pt solid var(--teal); padding:4pt 6pt; margin:3pt 0; white-space:pre-wrap; }}
.trap {{ background:var(--red-soft); border-left:2pt solid var(--red); padding:2.5pt 6pt; margin:3pt 0; font-size:8.2pt; }}
.trap b {{ color:var(--red); margin-right:4pt; text-transform:uppercase; font-size:7.2pt; letter-spacing:.05em; }}
.v {{ color:var(--red); font-weight:700; }}
ul {{ margin:2pt 0; padding-left:12pt; }} li {{ margin:0; }}
p {{ margin:2pt 0; }} .sub {{ color:var(--muted); }}
.ch {{ margin-top:8pt; }}
.body2 {{ columns:2; column-gap:9pt; column-fill:balance; }}
.chh {{ break-after:avoid; break-inside:avoid; display:flex; gap:8pt; align-items:center; border-bottom:1.5pt solid var(--ink); padding-bottom:4pt; margin-bottom:5pt; }}
.cn {{ font:800 22pt "Inter Display", Inter, sans-serif; color:var(--teal); line-height:1; }}
.meta {{ color:var(--muted); font-size:8pt; margin:1pt 0 0; }}
.sub-t {{ margin:0 0 5pt; break-inside:avoid; }}
.sh {{ display:flex; justify-content:space-between; align-items:baseline; gap:6pt; border-bottom:.5pt dotted var(--line); margin-bottom:2pt; padding-bottom:1pt; }}
.prio {{ background:var(--amber-soft); padding:5pt 7pt; margin:5pt 0; }}
.prio p {{ margin:1.5pt 0; }}
.cols {{ columns:2; column-gap:10pt; }}
.foot {{ color:var(--muted); font-size:7.4pt; margin-top:6pt; }}
</style></head><body>
<div class="cover">
  <p class="eyebrow">NISM-Series-V-D · Module 1 · Mutual Fund Distributors (Ch 1–12)</p>
  <h1>NISM V-D Mutual Fund Module Summary</h1>
  <p class="lead">All 12 mutual fund chapters, {total_subs} subtopics, in tables and keywords. Every subtopic has a star rating for exam importance. Read 5★ first, then 4★.</p>
  <div class="legend"><span>{stars(5)} must know, asked often</span><span>{stars(4)} high</span><span>{stars(3)} medium</span><span>{stars(2)} low</span><span>{stars(1)} skim</span><span><span class="v">‡</span> rule or number that changes often; check workbook edition</span></div>
</div>
<table><thead><tr><th>Ch</th><th>Chapter</th><th>Marks</th><th>Priority</th><th>Subtopics</th><th>5★</th></tr></thead><tbody>{idx_rows}</tbody></table>
<div class="prio"><h3>5★ list ({len(five)}) — read these first</h3>{fivelist(five)}</div>
<div class="prio" style="background:#f4f6f8"><h3>4★ list ({len(four)})</h3>{fivelist(four)}</div>
<p class="foot">Built from the NISM V-A / V-D mutual fund syllabus (V-D Ch 1–12 = V-A chapters). Marks: official where known (Ch1 5, Ch2 4, Ch3 3, Ch8 3, Ch9 10, Ch12 10), others estimated. Not copied from the workbook.</p>
{"".join(body)}
</body></html>'''

here = pathlib.Path(__file__).parent
(here / "mf-summary.html").write_text(HTML)
js = f'''const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://{(here / "mf-summary.html").resolve()}');await p.pdf({{path:'{(here / "NISM-VD-MF-Summary.pdf").resolve()}',format:'A4',printBackground:true,
displayHeaderFooter:true,headerTemplate:'<span></span>',footerTemplate:'<div style="font-size:7px;width:100%;text-align:center;color:#777;font-family:Carlito">NISM V-D · Mutual Fund Module Summary · <span class="pageNumber"></span>/<span class="totalPages"></span></div>',
margin:{{top:'11mm',bottom:'13mm',left:'10mm',right:'10mm'}}}});await b.close();}})();'''
subprocess.run(["node", "-e", js], check=True)
print("subtopics", total_subs, "5-star", len(five), "4-star", len(four))
