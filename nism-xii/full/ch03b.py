from summary_lib import *

def add(chap, sub):
    sub("Book building — cut-off price (worked)", 5,
      T(["Bid price","Shares","Cumulative demand"],[["₹144","1,000","1,000"],["₹140","1,500","2,500"],["₹135","2,500","<b>5,000</b>"],["₹130","1,000","6,000"],["₹120","500","6,500"]]) +
      K("5,000 shares, band ₹120–144 → filled at <b>₹135 = cut-off</b>; bids at ₹135 and above succeed",
        "Issuer may set cut-off lower than the clearing price for investors' benefit",
        "Retail discount to cut-off allowed, max <b>10%</b>"))
    sub("Allocation in the net offer", 5,
      T(["Category","Issuer meets profit/asset tests","Issuer fails tests (75% QIB route)","Non-book-built"],
        [["Retail (RII)","≥ <b>35%</b>","≤ <b>10%</b>","≥ <b>50%</b>"],["Non-institutional","≥ <b>15%</b>","≤ 15%","Rest (with institutions)"],
         ["QIB","≤ <b>50%</b> (5% of it for MFs)","≥ <b>75%</b> (5% of it for MFs)","—"]]) +
      K("NII portion: <b>1/3</b> for ₹2–10 lakh applications; <b>2/3</b> for &gt; ₹10 lakh"))
    sub("Public issue process — steps", 5,
      L("Board + shareholder resolutions",
        "Appoint lead manager (investment / merchant banker, issue manager); LM appoints RTA, bankers, brokers, underwriters; pricing set with issuer",
        "In-principle approval of stock exchange · optional IPO grading · agreements with <b>both</b> depositories",
        "Draft prospectus to <b>SEBI</b> → SEBI changes → file with <b>Registrar of Companies</b>; LM signs <b>due diligence</b>",
        "Marketing: adverts in national papers, analyst/broker meets; every form carries an <b>abridged prospectus</b>",
        "Bids via brokers, SCSBs, RTAs, DPs — <b>ASBA only</b> (retail may use UPI)",
        "Banks &amp; RTA reconcile daily → final collection certificate → cut-off set (book built)",
        "Basis of allotment finalised <b>with the stock exchange</b> → shares credited to demat, rejected amounts unblocked → listing and trading"))
    sub("Constituents of a public issue", 4,
      T(["Constituent","Duties"],
        [["RTA","Pre-issue: design forms, bidding procedures · issue: daily collection data, cut-off collation, reconciliation · post-issue: scrutiny, rejections, basis of allotment (with LM, issuer, exchange), allotment, statutory reports"],
         ["Bankers to issue","Collection branches in mandatory centres; collection updates decide closure"],
         ["Brokers / syndicate","Exchange members; collect bids with blocking authorisation; commission by collection"],
         ["Underwriters","Brokers &amp; merchant bankers; fixed price optional, book built mandatory; 90% minimum subscription <b>includes</b> underwriters' take-up"]]) +
      K("All constituents registered with SEBI; roles laid out by SEBI"))
    sub("Prospectus & red herring prospectus", 5,
      T(["Document","Use"],
        [["Prospectus","Fixed-price issue; format by SEBI + Companies Act"],
         ["Red herring prospectus (RHP)","Book-built issue; price band (or issue size) but no final price; preliminary RHP filed before opening; final price added after closure, signed prospectus filed"]]) +
      K("Contents: issuer, promoters, board, key staff, business · objects of issue · dates, LM, RTA, bankers, listing · terms, application, allotment, refund · financials, capital structure, accounting policies · statutory disclosures · <b>risk factors</b>",
        "Prospectus information updated annually") +
      T(["SEBI may reject draft if…",""],
        [["Promoter contribution non-compliant",""],["Use of proceeds unclear or creates no tangible assets",""],["Misleading business model",""],["Inconsistent financials",""],["Litigation risking business",""]]))
    sub("Applying to a public issue", 5,
      T(["Rule","Detail"],
        [["Exchange IPO bidding","Screen-based via broker terminals; <b>10 am – 5 pm</b>; LM may extend on closing day"],
         ["e-IPO (since 2013)","Bid through <b>any</b> exchange broker, appointed or not"],
         ["Price band announced","≥ <b>2 working days</b> before opening"],
         ["Minimum application","₹<b>10,000 – 15,000</b> (minimum bid lot)"],
         ["Bid at cut-off","Accept discovered price → application always accepted"],
         ["Revision","Any time before close (form or online)"],
         ["Payment","<b>ASBA only</b>; submitted to the Self-Certified Syndicate Bank (SCSB) holding the account"],
         ["UPI","Phased from <b>1 Jan 2019</b>; mandatory for individuals up to <b>₹5 lakh</b> from <b>1 May 2022</b>; SMS alerts for block/unblock"],
         ["Extra channels","Online ASBA (SCSB portal) · physical ASBA (SCSB branch) · broker's linked trading-demat-bank account"]]) +
      K("Oversubscribed → <b>proportionate</b> allotment, excess unblocked; undersubscribed → all valid bids at/above cut-off allotted",
        "Offer documents on SEBI and lead manager websites"))
    sub("Basis of allotment (worked)", 5,
      T(["Bid (shares)","Applications","Shares applied","Allotted each (÷1.52)","Total allotted"],
        [["20","100","2,000","13","1,300"],["30","150","4,500","20","3,000"],["40","200","8,000","26","5,200"],["50","160","8,000","33","5,280"]]) +
      K("Retail oversubscribed <b>1.52×</b>; each category separately (retail, NII, QIB)","Bidder for 20 gets 13, 7 unblocked","Minimum allotment = minimum application size",
        "Basis approved by company board, published in national newspapers"))
    sub("Green shoe option", 5,
      L("Extra allotment up to <b>15%</b> of issue size",
        "Proceeds in separate account; used to buy shares if price falls <b>below issue price</b> after listing",
        "Stabilising agent (usually lead manager) acts for <b>30 days</b> from listing"))
    sub("Listing", 4,
      L("Listing agreement + listing fee + rules on price-sensitive information, investor service, governance",
        "Brings liquidity and fair price discovery; price can be above or below issue price") +
      T(["Company","Issue","Current","Change"],[["ABC Infra","15","44.90","+199.33%"],["XYZ Retail","10","16.60","+66%"],["MNP Microfinance","985","565.80","−42.56%"],["DEF Restaurants","150","157","+4.67%"]]))
    sub("Rights issue", 5,
      L("Companies Act: new shares must <b>first</b> be offered to existing holders — avoids dilution (10 lakh → 20 lakh shares halves stake)",
        "Ratio set by board (1:1 doubles capital; 1:2, 2:3, 2:5…)",
        "Listed company fixes a <b>record date</b>; draft letter of offer to SEBI; abridged letter of offer to all holders; may apply on plain paper",
        "Open <b>7 to 30 days</b>; entitlements credited to demat",
        "Payment by <b>ASBA only</b>; offer document and entitlement form may be emailed",
        "<b>Renunciation</b>: decline or sell entitlement; entitlements trade separately and stop trading before issue closes"))
    sub("Public issue of debt — rules (NCS Regs 2021)", 5,
      T(["Rule","Detail"],
        [["Eligible issuer","<b>Public limited company</b>; even unlisted companies may issue and list debentures; issuers incl. PSUs, statutory corporations, REITs, InvITs"],
         ["Offer document","Draft filed with <b>stock exchanges</b> (via LM), open for public comments → final to RoC; LM gives due diligence certificate to SEBI first"],
         ["Shelf prospectus","File once with RoC, issue in tranches (tranche prospectus); for PFIs, scheduled banks, CBDT tax-free bond issuers, infra debt funds, listed entities, eligible NBFCs/HFCs"],
         ["Listing","<b>Mandatory</b>; in-principle approval before filing draft"],
         ["Credit rating","≥ <b>1</b> SEBI-registered CRA; disclose all ratings obtained"],
         ["Minimum subscription","<b>75%</b> of base issue, else unblock (interest if delayed); tax-free bonds exempt"],
         ["Demat","Agreement with a depository"],
         ["Debenture trustee","SEBI-registered banks/FIs; check security adequacy"],
         ["Debenture Redemption Reserve","Transfer part of profits each year until redemption"],
         ["Security","Disclose charge; assets free of encumbrance or prior creditor consent for second/pari passu charge"],
         ["Unsecured debentures","Treated as <b>deposits</b> → Companies (Acceptance of Deposits) Rules"],
         ["Coupon","Set with LM, or by book building"]]))
    sub("Public issue process — debt", 4,
      K("Issuer must not be a <b>wilful defaulter</b> or barred from market",
        "Steps: board + shareholder resolution → draft to exchanges &amp; SEBI → final to RoC → listing application → demat → adverts → <b>debenture trust deed</b> → rating → compliance → allotment / unblock → listing"))
    sub("G-sec primary issue", 5,
      L("RBI auctions on behalf of govt; calendar every <b>six months</b>",
        "Competitive bids: only those with <b>current account + SGL account</b> at RBI (SCBs, PDs)",
        "Non-competitive: co-op banks, NBFCs, MFs, pension funds, companies — allotted at <b>weighted average</b> price/yield",
        "Retail via <b>stock exchanges</b> (RBI 23 Nov 2017): brokers take bids till cut-off; exchange submits one consolidated non-competitive bid, then allocates per investor"))
    sub("Private placement & preferential allotment", 5,
      L("Offer to ≤ <b>50 persons</b> (Companies Act 2013); SEBI public-issue rules don't apply",
        "Offer by name to identified persons; details filed with RoC; payment through banks only, <b>no cash</b>; <b>no advertising</b> or distribution channels",
        "May list if SEBI/exchange rules met; any company, listed or not",
        "Pros: informed investors, less compliance, faster, cheaper") +
      K("<b>Preferential allotment</b> = private placement of shares or convertibles (FCDs, PCDs, warrants) by a <b>listed</b> company: shareholder resolution · SEBI pricing formula · promoter allotment locked in"))
    sub("Qualified Institutions Placement (QIP)", 5,
      T(["Rule","Detail"],
        [["What","Listed issuer places eligible securities with QIBs privately; includes promoter OFS via QIP"],
         ["Eligibility","<b>Special resolution</b>; listed ≥ <b>1 year</b> before notice"],
         ["Promoter OFS","To reach <b>25%</b> minimum public shareholding (SCR Rules 1957)"],
         ["Bidding","ASBA only; no downward revision or withdrawal after close"],
         ["MF quota","≥ <b>10%</b> to mutual funds (unsubscribed part to other QIBs)"],
         ["Price","SEBI formula"],["Resale","Within 1 year only on a recognised exchange"]]) +
      K("Eligible securities: equity, non-convertible debt with warrants, convertibles other than warrants"))
    sub("Electronic Book Provider (EBP) for private debt", 5,
      T(["Rule (as stated in this workbook)","Detail"],
        [["Mandatory for","Single issue ≥ <b>₹50 crore</b> (incl. green shoe) · shelf ≥ ₹50 crore in FY · subsequent issue taking FY total ≥ ₹50 crore · issuers &lt; <b>3 years</b> old · bank/NBFC non-equity regulatory capital"],
         ["Registration","Issuer, arrangers, QIBs, custodians register with exchange"],
         ["Documents","PPM, term sheet ≥ <b>2</b> working days before (first-time issuer: <b>5</b>); disclose bidding mode, allotment manner, settlement, cycle"],
         ["Announcement","≥ 1 working day before bidding"],
         ["Bid cap via arranger","Lower of <b>₹100 crore</b> or <b>5%</b> of base issue; FPIs via custodians"],
         ["Allotment","Price-time priority (coupon fixed) or yield-time priority (coupon discovered)"],
         ["Fairness","No selective preferential access"]]) +
      TRAP("The Series XII workbook still gives the older EBP thresholds (₹50 crore; 5 working days for a first-time issuer). SEBI's May 2025 revision, used in the V-D workbook, cut these to ₹20 crore and 3 days. For the XII exam, answer with the XII workbook figures."))
    sub("Workbook sample answers", 3,
      K("Retail investor = invests ≤ ₹2 lakh","OFS proceeds go to existing shareholders","Mandatory listing = all shares issued through a public offer",
        "Heavy oversubscription → fewer shares per investor","Public issue of debt → must be credit rated"))
