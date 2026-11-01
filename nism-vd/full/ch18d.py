from summary_lib import *

def add(chap, sub):
    sub("Primary vs secondary debt market; participants", 4,
      L("Primary: govt issues by <b>auction</b>; corporates mostly by <b>private placement</b>",
        "Secondary: exit route + price discovery (credit appetite, spreads, default probability)",
        "Issuance needs underwriting, rating, listing, issue managers, legal and bankruptcy framework; SMEs prefer bank loans (regulatory cost)") +
      T(["Role","Who"],
        [["Issuers","Govts, banks, PSUs, private companies"],["Intermediaries","Investment / merchant banks, brokers"],
         ["Investors","Corporate treasuries, MFs, insurers, banks, pension funds, HNIs; domestic &amp; foreign"],
         ["Regulators","<b>RBI</b> and <b>SEBI</b>"]]) +
      K("Segments: G-secs (GoI dated, T-bills; states' SDLs) · PSU &amp; bank bonds · private corporate debt",
        "GoI also issues FRBs, inflation-indexed bonds, special securities, CMBs; states issue UDAY bonds",
        "Banks issue CDs + long bonds; corporates issue bonds, debentures, CPs, FRNs, ZCBs"))
    sub("G-sec primary market: auctions", 5,
      L("RBI issues on behalf of govt — aim: fund fiscal deficit at low cost",
        "Centre: T-bills + dated securities; states: dated securities only",
        "Yield-based or price-based auctions, generally <b>weekly</b>; min bid <b>₹10,000</b> and multiples") +
      T(["Auction / bid","Rule"],
        [["Uniform price","All winners pay the cut-off rate"],["Multiple price","Each winner pays own bid"],
         ["Competitive","Institutions (banks, PDs, insurers, FIs, MFs) bid price/yield; multiple bids allowed; allotted if within cut-off"],
         ["Non-competitive (NCB)","Retail without current/SGL account; via aggregators (banks, PDs, exchanges) or <b>RBI Retail Direct</b>; no price quoted; allotted at <b>weighted average</b> of accepted competitive bids"]]))
    sub("G-sec secondary market", 5,
      T(["Venue","Points"],
        [["NDS-OM","Anonymous screen-based order matching, <b>Aug 2005</b>; run by Clearcorp Dealing Systems (CCIL subsidiary) for RBI; direct for banks/PDs, indirect via custodians / primary members; retail via primary members who are DPs"],
         ["OTC / telephone","Via bank / PD / FI or SEBI broker; report on NDS-OM within <b>15 minutes</b>"],
         ["NDS-OM-Web","<b>29 Jun 2012</b>; gilt account holders see live quotes, primary members act as risk controllers"],
         ["Stock exchanges","Retail platform; demat settlement"],
         ["RBI Retail Direct","Retail Direct Gilt (RDG) account with RBI; rbiretaildirect.org.in"]]) +
      L("RBI 7 Feb 2025: SEBI-registered non-bank brokers may access NDS-OM ('Stock Broker Connect' for demat clients)",
        "SEBI 11 Feb 2025: via a <b>Separate Business Unit (SBU)</b> — ring-fenced, NDS-OM only, separate accounts, separate net worth; exchange grievance mechanism, IPF and SCORES <b>not</b> available to SBU clients"))
    sub("G-sec settlement & market operations", 5,
      T(["Item","Rule"],
        [["Settlement","Net basis — <b>DvP-III</b>; CCIL is CCP by <b>novation</b>; outright trades <b>T+1</b> (FPIs OTC: T+1 or T+2, reported on trade date)"],
         ["Switch / conversion auction","Sell source security, buy destination from GoI; bids on <b>e-Kuber</b>; source price = previous day FBIL close"],
         ["OMO","RBI sells G-secs to absorb excess liquidity, buys to inject — durable liquidity tool"],
         ["Buyback","Govt redeems early: cut cost (high coupons), fewer securities, liquidity, cash management; auction (large) or NDS-OM (small)"],
         ["Securities lending (GSL)","RBI Directions Dec 2023; lend G-secs for a fee against other G-secs; borrowers = short-sale eligible; lenders = repo eligible"]]))
    sub("Holding G-secs", 4,
      L("RBI <b>Public Debt Office (PDO)</b> = registry and central depository",
        "RBI-regulated entities must hold G-secs in demat (SGL) form from <b>20 May 2002</b>",
        "Physical stock certificate: transfer by transfer form registered with PDO, not by endorsement") +
      T(["Demat route","Who"],
        [["SGL account with RBI","Banks, PDs, select UCBs &amp; NBFCs"],["Gilt account","With bank/PD holding a <b>CSGL (SGL II)</b> account at RBI"],
         ["Depository demat (NSDL/CDSL)","Enables trading on exchanges"]]))
    sub("Corporate bond primary market", 5,
      L("Mostly private placement to institutions; small share by public issue",
        "Public issue: prospectus; must list; offer document <b>not</b> approved by SEBI — in-principle approval from exchange; Companies Act 2013 + SEBI NCS Regulations 2021",
        "Private placement: Private Placement Memorandum (PPM)",
        "Face value of privately placed listed debt / NCRPS: <b>₹1 lakh</b> (reduced from ₹10 lakh, Oct 2022); ₹10,000 allowed with conditions") +
      T(["EBP rule","Detail"],
        [["Introduced","SEBI 21 Apr 2016; revised 10 Oct 2022 &amp; 16 May 2025"],
         ["Mandatory","Single issue ≥ <b>₹20 crore</b> (incl. green shoe); shelf ≥ ₹20 crore in a FY; subsequent issue taking FY total ≥ ₹20 crore"],
         ["Optional","Securitised debt, security receipts, CPs, CDs, REIT/SM REIT/InvIT units, issues &lt; ₹20 crore"],
         ["Documents","PM + term sheet ≥ 2 working days before (first-time issuer: 3); bidding announcement ≥ 1 working day before"],
         ["Disclose","Open/closed bidding · uniform/multiple yield allotment · settlement via clearing corp or escrow · T+1 or T+2"],
         ["Anchor portion","Up to 30% / 40% / 50% of base issue, by rating"],
         ["Cut-off","Estimated cut-off yield to EBP ≥ 1 hour before bidding"],
         ["Participants","Issuers, arrangers (merchant bankers, brokers, PDs), QIBs, non-QIBs, custodians (for FPIs)"]]))
    sub("Corporate bond secondary market", 5,
      L("Mainly OTC, institutional, negotiated; reported to exchange platform; settled DvP-I via clearing corporation",
        "Every trade reported within <b>15 minutes</b>; settlement T+0 to T+2",
        "<b>RFQ platform</b> launched early 2020 — pre-trade transparency, audit trail; exchanges also run order matching for bonds",
        "RFQ cash-flow dates not adjusted for day count — use scheduled due date") +
      T(["SEBI step","Detail"],
        [["19 Oct 2022","Debt-segment brokers may bid on RFQ for clients"],["28 Oct 2022","Face value ₹10 lakh → ₹1 lakh"],
         ["14 Nov 2022","Online Bond Platform orders must go through exchange RFQ, settled by clearing corporations"],
         ["9 Jan 2023","RBI-authorised payment mechanisms allowed besides RTGS"],
         ["2 Aug 2023","From 1 Apr 2024 brokers do ≥ <b>25%</b> of proprietary CB trades (value, monthly) via RFQ (OTO or OTM)"],
         ["7 Aug 2023","FPIs ≥ <b>10%</b> of CB secondary trades via RFQ, quarterly"]]) +
      K("Similar RFQ mandates for MFs, AIFs, PMS","<b>OBPP</b> = online platform (not exchange, not EBP) offering listed debt — gives retail access"))
    sub("Money market instruments", 5,
      T(["Instrument","Key facts"],
        [["Call money","Unsecured, overnight; only SCBs + PDs; NDS-CALL (CCIL)"],["Notice money","Unsecured, 2–14 days; NDS-CALL"],
         ["Term money","Unsecured, 15 days – 1 yr; NDS-CALL"],
         ["Market repo","Ready forward: sell security + repurchase at higher price (interest); reverse repo = collateralised lending; G-sec repo on <b>CROMS</b>, settled by CCIL"],
         ["Triparty repo (TREPS)","Triparty Agent handles collateral, settlement, custody; CBLO (20 Jan 2003) → TREP <b>5 Nov 2018</b>; exempt from CRR/SLR; seller may substitute security"],
         ["T-bills","Zero-coupon, discount; 91/182/364 days; weekly auction <b>Wednesday</b>"],
         ["CMBs","&lt; 91 days; temporary govt cash mismatches"],
         ["Commercial paper","Corporates/NBFCs/AIFIs; ₹5 lakh multiples; 7 days – 1 yr; demat; min rating <b>A3</b>; IPA appointed; others need net worth ≥ ₹100 crore; bank facilities must be standard assets"],
         ["Certificate of deposit","Banks; usance promissory note; ₹5 lakh multiples; 7 days – 1 yr; AIFIs 1–3 yrs"],
         ["Repo in corporate bonds","RBI 2010; listed bonds (not own/related), CPs, CDs, debt ETF units"],
         ["Tri-party repo on corporate debt","On exchanges; <b>AMC Repo Clearing Ltd (ARCL)</b> = LPCC and tri-party agent"]]))
    sub("Call money market, MIBOR & repo utility", 4,
      L("Call money = second most liquid asset after cash; day-end liquidity, no collateral, same-day settlement",
        "Pure interbank (incl. PDs) since <b>Aug 2005</b>",
        "<b>Overnight MIBOR</b>: administered by <b>FBIL</b>, CCIL calculation agent; volume-weighted average of NDS-CALL trades in the <b>first hour</b>; RBI 'significant benchmark'",
        "Repo market funds positions and lets traders short G-secs (borrow security to deliver); short sale allowed up to <b>90 days</b>"))
    sub("Role of regulators", 4,
      T(["Regulator","Scope"],
        [["RBI","Govt borrowing (Centre, states, UTs); money market and G-sec market; bank instruments; laws: RBI Act 1934, Govt Securities Act 2006, PSS Act 2007, FEMA 1999, Banking Regulation Act"],
         ["SEBI","Corporate bonds incl. bank/PSU issues &gt; 1 yr; risk disclosures; FPIs, MFs; debenture trustees, CRAs, merchant bankers"]]))
    sub("Credit rating agencies", 5,
      L("Sovereign home-currency debt = credit risk free; others priced on issuer creditworthiness",
        "CRAs regulated by SEBI — <b>SEBI (CRA) Regulations 1999</b>; at least one rating mandatory for debt issue",
        "Rating = relative probability of default; used to set credit spread; agencies ask investors to use other information too; bonds often rated by more than one CRA") +
      T(["Rating","Meaning"],
        [["AAA","Highest safety"],["AA","High safety"],["A","Adequate safety"],["BBB","Moderate safety"],["BB","Moderate risk"],["B","High risk"],["C","Very high risk"],["D","Default"]]) +
      K("AAA to BBB− = investment grade · BB+ to CCC− = junk · D = default · short-term scale A1+ to D","'+' / '−' show position within category"))
    sub("Workbook sample answers", 3,
      K("BBB has higher credit risk than A or AAA","Credit spread = price of credit risk","LR 10%, SR 8% → normal/positive curve","Accrued interest applies to coupon bonds","Higher coupon → modified duration decreases"))
