from summary_lib import *

def add(chap, sub):
    chap(3, "Legal Structure of Mutual Funds in India", "3", 3)
    sub("Definition of 'mutual fund' (SEBI MF Regulations 2026)", 4,
      KV([("Definition","Fund established as a <b>trust</b>, registered under regulation 3, raising money by sale of units to the public under one or more schemes, investing in securities, money market instruments, gold/gold-related, silver/silver-related and other SEBI-specified assets"),
          ("Must have","A separate Asset Management Company (AMC)")]) +
      K("Established as a trust","Sells units to public / section of public","Under one or more schemes","Invests in securities incl. money market, gold, silver, real estate assets"))
    sub("Legal structure — checks and balances", 5,
      T(["Element","Rule"],
        [["Governing law","Indian Trusts Act, 1882 (MFs are trusts)"],
         ["Creator","One or more <b>sponsors</b>"],
         ["Beneficiaries","Unitholders (investors)"],
         ["Trust deed","Executed between sponsor and trustees; SEBI prescribes clauses; names first trustees + procedure to change them; registered under <b>Indian Registration Act, 1908</b>"],
         ["Trustees","Protect beneficiaries; individuals (= Board of Trustees) or Trustee Company (acts via Board of Directors)"],
         ["AMC","Day-to-day management; appointed by sponsor or trustees (with SEBI approval)"],
         ["IMA","Investment Management Agreement: trustees ↔ AMC"],
         ["Custodian","Holds assets (securities, gold, real estate, silver); appointed by <b>trustees</b>"],
         ["RTA","Investor records — by AMC itself or an appointed RTA"]]))
    sub("Sponsor eligibility", 4,
      L("Applies to SEBI for MF registration; then invests in AMC capital",
        "Sound track record, reputation of fairness and integrity",
        "Business in financial services for <b>≥ 5 years</b>",
        "Net worth (share capital + reserves − accumulated losses) <b>positive in all 5 preceding years</b>",
        "Positive <b>liquid net worth</b> &gt; proposed capital contribution to AMC (on change of control via share acquisition: ≥ higher of par or market value of shares acquired)",
        "<b>Net profit</b> (after depreciation, interest, tax) in <b>each</b> of preceding 5 years",
        "<b>Average net annual profit ≥ ₹10 crore</b> over preceding 5 years",
        "Fit and proper person") +
      K("Liquid net worth = net worth in unencumbered liquid assets: cash, money market, G-secs, T-bills, repo on G-secs etc.",
        "AMFI website lists AMCs by sponsor category: Banks, Institutions, Private sector (Indian, foreign, predominantly Indian JV)"))
    sub("Trustees (Regulation 11)", 5,
      KV([("Eligibility","Fit &amp; proper (Schedule II, SEBI Intermediaries Regs 2008) · NOT a director (incl. independent), officer or employee of an AMC · NOT trustee of any other MF · furnish info SEBI seeks"),
          ("SEBI approval","Prior approval needed to appoint a trustee"),
          ("Independence","≥ <b>two-thirds</b> independent (not associates of sponsor, AMC or trustee company)"),
          ("Rights &amp; responsibilities","1. Appoint/terminate AMC 2. Conflict of interest &amp; broker empanelment 3. Regulatory compliance 4. Oversight for investor interests 5. Additional oversight 6. Due diligence as specified by SEBI")]))
    sub("Asset Management Company", 5,
      T(["Rule","Detail"],
        [["Appointment","Sponsor/trustees appoint AMC with SEBI approval"],
         ["Directors","Adequate professional experience in finance; directors &amp; key personnel fit and proper"],
         ["Board independence","≥ <b>50%</b> directors not associates of sponsor, its subsidiaries or trustees"],
         ["Cross-holding","AMC directors (incl. Chairman) can't sit on any MF trustee board; trustees' prior approval to appoint AMC director; a person can't be director of more than one AMC"],
         ["Net worth","≥ <b>₹50 crore</b> (deployed in specified assets, effective 1 Jan 2024); maintained continuously — sponsor's responsibility"],
         ["Change of control","Prior approval of trustees + SEBI; letter/email to each unitholder; ad in one English national daily + one regional-language paper (HO region); exit at NAV <b>without exit load</b> within ≥ <b>30 calendar days</b>"],
         ["Duties","Offices, staff, software, advertising, regulator interaction; due diligence so investments comply with regulations and trust deed"],
         ["Termination","By <b>majority of trustees</b> or <b>75% of unitholders</b>; change needs prior approval of SEBI and unitholders"],
         ["SIF","AMCs launching SIF must meet additional eligibility"]]))
    sub("Custodian", 5,
      KV([("Role","Custody of assets; accepts/gives delivery; settles all transactions; tracks corporate actions (dividends, bonuses, rights)"),
          ("Registration","SEBI (Custodian) Regulations, 1996"),
          ("Appointed by","Trustees (custodial agreement trustees ↔ custodian)"),
          ("Independence","If sponsor/associates control ≥ 50% voting rights, or ≥ 50% of custodian's directors represent sponsor → can't be appointed (unless specific conditions met)"),
          ("Why","Ensures securities are really held for investors — control aspect")]))
    sub("AMC organisation structure", 4,
      T(["Function","Role"],
        [["Compliance","Compliance Officer signs due-diligence certificate in new scheme documents; reports <b>directly to head of AMC</b>; works with trustees; reports non-compliance directly &amp; immediately to trustees"],
         ["Fund management (most critical)","Analysts (identify opportunities: equity, credit, interest rates) · Fund managers (decide; responsible for performance) · Dealers (place orders with brokers)"],
         ["Operations &amp; customer service","Front office + back office; call centres, chat bots; RTA unit (records, allot/redeem, account statements); Custody team (settlement); Fund accounting (books per scheme, daily NAV)"],
         ["Risk management","Independent specialised function (SEBI RMF); dedicated risk officers for investment, compliance, operational and cyber security risk"],
         ["Sales &amp; marketing","Branding, ads, events, distribution; interacts with MFDs; training"],
         ["Support","Accounts (AMC's own finances — different from fund accounting) · Administration (often reports to finance) · HRD · IT (website, investor/distributor tech)"]]))
    sub("Service providers", 5,
      T(["Provider","Key points"],
        [["Fund accountant","Calculates NAV; in-house or outsourced; <b>no SEBI registration</b> needed"],
         ["RTA","Investor records; offices = Investor Service Centres (ISCs); process purchases/redemptions, update unit capital &amp; folios; appointed by <b>AMC</b>; not compulsory (AMC may do in-house); must register with SEBI"],
         ["Auditors","Scheme accounts separate from AMC; scheme auditor ≠ AMC auditor; scheme auditor appointed by <b>trustees</b>, AMC auditor by <b>AMC</b>"],
         ["Distributors","Individuals or institutions; empanel with many AMCs; NISM V-A + AMFI registration; new cadre: NISM V-B (limited schemes; SEBI circular 13 Sep 2012)"],
         ["Collecting bankers / payment aggregators","Appointed by AMC; scheme bank accounts; payment gateways, digital wallets, payment banks"],
         ["KRAs","KYC mandatory under PMLA; SEBI KRA regulations 2011 → common KYC; registered with SEBI; issue letter/number usable with any intermediary; confidentiality; computerised connectivity among KRAs"],
         ["Valuation agencies","For non-traded/thinly traded debt; ≥ 2 agencies; AMFI appointed <b>CRISIL Ltd. and ICRA Ltd.</b>"],
         ["Credit rating agencies","Ratings = initial input; corporate bond &amp; credit risk funds defined by ratings; capital protection schemes rated; FMPs may disclose proposed rating profile and must invest within it or better"],
         ["Depositories &amp; DPs","Hold demat units; NSDL and CDSL; DP ≈ bank branch, depository ≈ head office; ETFs compulsorily demat"]]))
    sub("Stock exchanges & transaction platforms", 4,
      T(["Platform","Point"],
        [["Exchange listing","Close-ended funds &amp; ETFs compulsorily listed on ≥ 1 exchange"],
         ["BSE StAR MF","BSE's MF segment"],["NSE NMF-II","NSE Mutual Fund II platform"],
         ["MF Utilities India","AMFI industry initiative; one platform for transactions across many MFs"],
         ["MF Central","Investor services hub by <b>KFintech &amp; CAMS</b>; all folios in one view, service requests"]]))
    sub("Execution Only Platforms (EOP)", 4,
      KV([("Definition","Digital/online platform for subscription, redemption, switch in <b>direct plans</b>"),
          ("Excluded","Platforms of SEBI RIAs and stock brokers for their own clients"),
          ("Registration","From SEBI or AMFI — none may operate without it"),
          ("Category 1","Registered with <b>AMFI</b>; body corporate; agent of <b>AMCs</b>; integrates with AMCs/RTAs; may aggregate direct-plan transactions"),
          ("Category 2","Registered as <b>stock broker</b> (SEBI Stock Brokers Regs 2026) in EOP segment of exchanges; body corporate; agent of <b>investor</b>; only via exchange platforms")]))
    sub("AMFI — role and functions", 5,
      L("Association of all registered AMCs",
        "Define and maintain high professional and ethical standards",
        "Recommend best practices and code of conduct",
        "Interact with and represent to SEBI; represent to Government, RBI and others",
        "Nationwide investor awareness programme",
        "Disseminate information; studies &amp; research",
        "Regulate conduct of distributors incl. disciplinary action (cancellation of ARN)",
        "Protect interest of investors",
        "Register distributors — allots <b>ARN</b> (mandatory); issues best-practice circulars") +
      TRAP("AMFI is NEITHER a regulator NOR a Self-Regulatory Organisation (SRO)."))
