from summary_lib import *

def add(chap, sub):
    chap(1, "Understanding Securities Markets and Performance", "10", 4)
    sub("Financial market & securities market", 4,
      L("Financial market = money, debt, equity markets + investors (buyers) + issuers (users of funds) + intermediaries + regulators (SEBI, RBI…)",
        "Securities market = regulated framework for flow of capital (equity &amp; debt) from investors to businesses; channels <b>savings into investments</b>",
        "Securities = financial instruments issued by companies, FIs or government to raise funds; investors turn savings into financial assets"))
    sub("Definition of securities — SCRA 1956, Section 2(h)", 5,
      T(["#","Included in 'securities'"],
        [["a","Shares, scrips, stocks, bonds, debentures, debenture stock of any company / pooled investment vehicle / body corporate"],
         ["b","Derivatives"],["c","Units of a collective investment scheme"],
         ["d","Security receipts (SARFAESI Act 2002, s.2(zg))"],
         ["e","Mutual fund units — but <b>not ULIPs</b> (insurance + investment combined)"],
         ["f","Units of a pooled investment vehicle"],
         ["g","Certificates from a special purpose entity holding debt/receivables (incl. mortgage debt) — securitised instruments"],
         ["h","Government securities"],
         ["i","Others declared by Central Govt: onshore rupee bonds of ADB, IFC · <b>Electronic Gold Receipts</b> (24 Dec 2021) · <b>Zero Coupon Zero Principal</b> instruments (16 Jul 2022, not-for-profits on Social Stock Exchange)"],
         ["j","Rights or interest in securities"]]) +
      K("SCRA derivative = security derived from debt, share, loan, risk instrument or contract for differences · contract deriving value from prices/index of securities · commodity derivatives · others notified"))
    sub("Features of securities", 4,
      L("Represent terms of exchange of money between two parties; issuer and investor goals are complementary",
        "Issuer sets terms; listing makes security liquid and gives information to investors",
        "Investor gets rights: ownership, participation in management or claim on assets",
        "Broad classes: <b>equity</b> and <b>debt</b>; return = benefit; risk = chance return does not come (bond: default on interest or principal)",
        "Market lets investors take risk for return, judge it with information, and transfer it by selling"))
    sub("One-to-one contract vs security", 5,
      T(["","Bank fixed deposit","Certificate of deposit (CD)"],
        [["Type","Bilateral contract","Security"],["Repaid to","Only the depositor","Whoever holds it at maturity"],
         ["Transferable","No (receipt not transferable); early exit with penalty","Yes, at a mutually agreed market price"]]) +
      K("<b>NOT securities</b>: bank deposits · inter-corporate deposits · company FDs · deposits with HFCs/finance companies · chit funds · benefit funds · insurance policies · provident and pension fund investments"))
    sub("Structure: primary vs secondary market", 5,
      T(["Primary market","Secondary market"],
        [["'New issue market' — issuers raise capital","Stock exchange — trade in already-issued securities"],
         ["<b>Creates</b> financial assets","Makes them <b>marketable</b>; gives exit; risk moves from seller to buyer"]]) +
      K("The two segments are interdependent and inseparable",
        "Primary players: merchant bankers, MFs, FIs, FPIs, insurers, individuals, bankers to issue, brokers, DPs; issuers = companies, bodies corporate; exchanges only for <b>listing</b>",
        "Secondary players: exchanges, brokers, AMCs, FIs, FPIs, investment companies, individuals, DPs, banks",
        "RTAs, custodians, depositories serve <b>both</b> markets"))
    sub("Investors: retail vs institutional", 4,
      L("Retail = individuals on personal account (A invests ₹5,000/month in MF units)",
        "Institutional = companies, banks, govt bodies, MFs, insurers, pension funds, endowments, societies (ABC MF buys 50,000 XYZ shares)",
        "MFs are institutional investors 'by objective'; banks/FIs invest via treasury",
        "Institutions run formal processes: select securities · review &amp; monitor · manage risk, return, holding period"))
    sub("Issuers", 4,
      T(["Issuer","Why / what"],
        [["Companies","Short- and long-term capital"],["Central &amp; state govts","Debt to fund <b>deficit</b> (expenses above income)"],
         ["Local govts / municipalities","Debt for development; <b>govt agencies never issue equity</b>"],
         ["Banks &amp; FIs","Equity or debt beyond deposits/grants"],["PSUs","Shares sold to public in govt <b>disinvestment</b>"],
         ["Mutual funds","Units of schemes"],["Investment trusts","REITs, InvITs, AIFs issue units"]]) +
      K("Issued under issuer's name and common seal; issuer bears obligation","Electronic issue since mid-1990s; paper → electronic = <b>dematerialisation</b>",
        "Issuers must be authorised by the regulator"))
    sub("Intermediaries — SEBI (Intermediaries) Regulations 2008", 5,
      K("List: AMCs · portfolio managers · merchant bankers · underwriters · stock brokers · authorised persons · clearing members · derivatives trading members · bankers to an issue · registrars of an issue · share transfer agents · DPs · custodians · trustees of trust deeds · CRAs · investment advisers · KYC registration agencies") +
      T(["Intermediary","Role"],
        [["AMC","Offers units = share in a <b>pooled</b> portfolio; charges fee"],["Portfolio manager","Manages client portfolio; <b>no pooling, issues no security</b>"],
         ["Merchant banker","Issue manager / lead manager / investment banker; structures, prices, manages issue till listing; also <b>underwrites</b>"],
         ["Primary dealer","Underwriter in govt bond market"],
         ["Stock broker","Registered trading member; all exchange trades go through brokers; earns commission"],
         ["Authorised person","Broker's agent (earlier 'sub-broker'); registered with exchange"],
         ["Trading / clearing member","Trading member executes; clearing member settles funds and securities"],
         ["Banker to an issue","Collects applications &amp; money; reports to lead manager; sends data to registrar; transfers funds to issuer"],
         ["Registrar &amp; STA","Keeps investor records: first/joint holders, address, bank, signatures, nominations"],
         ["Depository participant","Opens demat accounts; <b>agent of the depository</b>; investor-level accounts (company-level held by depository)"],
         ["Custodian","For institutions: holds securities &amp; cash, settles, accounts, values; usually large banks"],
         ["Trustee","MF trustees supervise AMC; debenture trustees protect lenders"],
         ["Credit rating agency","Opinion on ability to pay interest &amp; principal; rating symbols"],
         ["Investment adviser","Advice on needs, horizon, risk; financial plans"]]) +
      K("All must register with SEBI and follow its code of conduct: investor protection, fair professional service, no collusion, timely information, adequate infrastructure"))
    sub("KYC Registration Agencies (KRA)", 5,
      L("Central KYC store uploaded by intermediaries; uniform KYC for MFs, brokers, DPs, PMS, VCFs",
        "KYC done once is valid across all SEBI-registered intermediaries",
        "KRAs share data with each other via <b>inter-operability process (IOP)</b>; may share with RBI, IRDAI, PFRDA if notified",
        "Digital KYC must be accessible to persons with disabilities incl. visual impairment (SEBI 23 May 2025)",
        "Investor charter for KRAs (6 May 2025) shared via website, email, office display") +
      T(["KRA validates","Through"],[["Aadhaar","UIDAI"],["Mobile &amp; email","OTP or successful delivery of SMS/email"],["PAN","Income Tax database"]]))
    sub("Regulators", 5,
      T(["Regulator","Scope"],
        [["SEBI","Statutory body, <b>SEBI Act 1992</b>; under Ministry of Finance; chief securities regulator; aims: develop markets, protect investors"],
         ["RBI","Money market, forex market, govt securities (issue manager for govt), banks; monetary, forex, credit policy"],
         ["MCA","Corporate sector; Companies Act; issuance by companies"],
         ["MoF","Dept of Financial Services → banks, insurance, pension; <b>Dept of Economic Affairs → capital markets</b>"],
         ["IRDAI","Insurance; IRDA Act <b>1999</b>; registers insurers/re-insurers"],
         ["PFRDA","Pensions incl. NPS; PFRDA Act <b>2013</b>"],
         ["IBBI","<b>2016</b> under Insolvency &amp; Bankruptcy Code; regulates IPAs, IPs, information utilities; members from MoF, MCA, RBI"],
         ["IFSCA","GIFT City, Gandhinagar; set up <b>2020</b> under IFSCA Act <b>2019</b>; unified regulator for IFSC"]]))
    sub("SEBI's functions", 5,
      L("Recognises and regulates stock exchanges; administers <b>SCRA 1956</b>; Central Govt may nominate up to <b>3</b> persons on each exchange; exchanges submit bye-laws for approval, periodic and daily monitoring reports",
        "Codified regulations for all activities and intermediaries",
        "Primary market: <b>SEBI (ICDR) Regulations 2018</b> — public &amp; rights issues, QIP, preferential, bonus, IDRs; debt: <b>SEBI (NCS) Regulations 2021</b> (9 Aug 2021, merged Debt Securities Regs 2008 and NCRPS Regs 2013)",
        "Listing agreement: continuous information flow, governance, investor protection",
        "Inspections; investigations into manipulation, artificial volume, insider trading, takeover code, issue malpractice; surveillance at exchanges",
        "Powers: call for information, summon, examine witnesses, search &amp; seizure; penalties = suspension, monetary penalty, prosecution",
        "Insider trading code: compliance officer, insider disclosures, confidentiality; penalties incl. prosecution, market ban, voiding trades"))
    sub("Role of securities markets", 5,
      T(["Role","Example"],
        [["Orderly channel for funds","Disintermediation — company issues CP/bonds instead of bank loan"],
         ["Productive investment","Many households jointly fund a large steel plant"],
         ["Liquidity","Buy 100 XYZ at ₹25, sell at ₹45 → ₹2,000 gain; confidence to lock into long-term assets"],
         ["Price discovery","Fair price set by buyers and sellers, not by regulator"],
         ["Information signalling","Poor monsoon → fertiliser company prices fall"]]))
    sub("Technology in markets", 3,
      L("19th century: brokers met under the banyan tree in front of Mumbai Town Hall, Fort area",
        "1990s: 'pit trading' / 'open outcry' → screen-based electronic trading",
        "Phone orders → online and mobile trading; brings <b>cyber-attack</b> risk"))
    sub("Cyber Security & Cyber Resilience Framework (CSCRF)", 5,
      L("SEBI CSCRF for all Regulated Entities (REs), phased, supersedes earlier circulars (20 Aug 2024; updates Dec 2024, Mar 2025, Apr 2025)",
        "MIIs under CSCRF: stock exchanges · depositories · clearing corporations · <b>KRAs</b> · <b>QRTAs</b>",
        "Cyber security = prevent attacks; cyber resilience = prepare, respond, keep working, recover") +
      T(["Goal","Function","Key points"],
        [["Anticipate","Governance","Board-approved policy; roles &amp; accountability; RE solely accountable for third-party services"],
         ["Anticipate","Identify","Classify critical systems (Board approves list); assess risks"],
         ["Anticipate","Protect","Need-based access (not by rank); strong passwords, 2-factor, access logs; vendor supervision; full-disk + file encryption; vulnerability assessment; audit by <b>CERT-In empanelled</b> auditor"],
         ["Anticipate","Detect","Continuous monitoring for anomalies and data leaks"],
         ["Withstand &amp; Contain","Respond","Report via <b>SEBI incident portal</b>; incident plan, SOPs, Cyber Crisis Management Plan (CCMP); root cause analysis; forensics"],
         ["Recover","Recover","Timely restoration; alternate services; inform stakeholders"],
         ["Evolve","—","Adaptive controls to reduce attack surface"]]) +
      K("5 goals: <b>Anticipate, Withstand, Contain, Recover, Evolve</b>","RE category fixed at start of FY on previous FY data, unchanged during the year","Vendors managing RE systems must follow SEBI rules","Periodic cyber audit mandatory"))
    sub("Innovation Sandbox vs Regulatory Sandbox", 5,
      T(["","Innovation Sandbox","Regulatory Sandbox"],
        [["Who","FinTechs, start-ups, unregulated entities, individuals","<b>SEBI-registered</b> entities (alone or with a FinTech)"],
         ["Testing","<b>Offline</b>, isolated from live market","<b>Live</b>, limited customers, limited time"],
         ["Oversight","Steering committee of exchanges, depositories, QRTAs (revised framework 2 Feb 2021)","SEBI designated officer (framework 5 Jun 2020)"]]) +
      K("'Regulatory sandbox' coined by UK FCA in <b>2015</b>; &gt; 20 countries use it; need arose after 2008 crisis",
        "Criteria: genuine innovation adding value, genuine need for live test, no risk to financial system; clients told of risks",
        "Relaxations possible, but <b>never</b> from investor protection, KYC and AML rules"))
    sub("Workbook sample answers", 3,
      K("MF collecting money and issuing units = <b>issuer</b>","Facilitators between investors and issuers = intermediaries","Loss-making results → price falls = information signalling",
        "Issued securities traded on stock exchanges where listed","RBI regulates money and forex markets = True"))
