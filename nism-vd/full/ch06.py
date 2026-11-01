from summary_lib import *

def add(chap, sub):
    chap(6, "Fund Distribution & Channel Management Practices", "4", 3)
    sub("Role of the MF distributor vs fund manager", 4,
      F("Investor  →  Mutual fund distributor  →  Fund manager  →  Portfolio   (Chart 6.1)") +
      T(["Professional","Analyses"],
        [["Fund manager","Market factors: company, industry, economy, liquidity, mood → portfolio per scheme objective"],
         ["MF distributor","Investor's needs, limitations, resources, goals → asset allocation → suitable schemes"]]))
    sub("Kinds of distributors", 4,
      T(["Type","Points"],
        [["Individual","Long history (LIC, UTI agents; small savings); single-handed; = 'individual' channel"],
         ["Non-individual","Partnerships, regional/national distributors, NBFCs, banks, stock brokers; distribution cos &amp; banks = 'institutional'; models: own branches &amp; employees (fixed cost, salary) or sub-agents (variable cost, commission)"],
         ["Banks","MNC banks entered first, then private &amp; PSU, now some co-operative banks; segments: retail, wealth/priority/private banking; PSU banks for non-urban reach"],
         ["Sub-agents (agency channel)","Not employees; extended distribution arm of NBFCs/brokers"],
         ["E-commerce / online","No physical office; EOP guidelines apply"]]) +
      K("Channels: individual MFDs, bank branches, national distributors, post offices, AMCs direct"))
    sub("Modes of distribution", 3,
      K("Physical (paper forms → Official Points of Acceptance, OPOAs)","Digital","Hybrid","Online channel partners: own websites, beyond geography"))
    sub("Stock exchange platforms", 5,
      T(["Point","Detail"],
        [["Platforms","NSE <b>NMF II</b> (two versions: trading members, distributors) · BSE <b>StAR MF</b>"],
         ["Who can use","Trading members registered with AMFI as MFD and signed with the MF; clearing members; <b>DPs — redemptions only</b>; AMFI-registered distributors via limited-purpose membership"],
         ["Eligible schemes","Notified by MFs; these open-ended schemes are <b>not listed</b>"],
         ["Settlement","Exchange = order routing only; does <b>not</b> replace RTA; <b>no settlement guarantee</b> — AMC responsible; exchange grievance mechanism available"],
         ["Direct access","SEBI circular 26 Feb 2020: investors can directly use exchange infrastructure to buy/redeem from AMCs"],
         ["Facilities","Units in demat; pay-in/pay-out via exchange &amp; clearing corporation; SIP, STP, SWP, switch possible"],
         ["Listing","Close-ended &amp; interval schemes must be listed; ETFs traded on exchange"]]))
    sub("MF Utilities (MFU) & MFCentral", 5,
      T(["MFU","Detail"],
        [["What","Transaction aggregation platform: investors, RTAs, distributors, banks, AMCs"],
         ["CAN","Common Account Number — consolidates holdings; KYC compliance needed (MFU facilitates KYC); multiple CANs possible by holding pattern/mode"],
         ["Common Transaction Form","One form, many schemes across MFs; submit via MFD or neutral Points of Service (PoS); single payment for multiple subscriptions"],
         ["Override","Bank &amp; nomination details given to MFU override folio details"],
         ["Online access","Transact, view holdings, lodge &amp; track complaints"]]) +
      T(["MFCentral","Detail"],
        [["What","Unified single-window portal by <b>CAMS and KFintech</b> under SEBI mandate (RTA interoperable platform, operational since 31 Dec 2021)"],
         ["Functions","Consolidated portfolio view (demat + non-demat) · service requests (bank mandate, email/mobile, KYC, nominee) · transactions (lump sum/SIP, redemption, switch) · folio management (consolidation, minor→major, FATCA/CRS) · CAS, unclaimed dividends · family portfolio tracking"]]))
    sub("Apps, AMC platforms, new-age platforms", 2,
      K("Distributor apps (smartphones, feature phones, tablets)","AMC web/mobile apps, SMS, WhatsApp = dealing directly with MF","New-age platforms (Groww, Kuvera, Paytm Money, Coin): low cost, direct plans, little paperwork"))
    sub("Prerequisites to become a distributor", 5,
      T(["Step","Rule"],
        [["Who","AMC may appoint individual, bank, NBFC, distribution company"],
         ["Certification","NISM Series V-A mandatory for all in sale/distribution; SIF needs additional eligibility"],
         ["Exemption (grandfathered)","Age ≥ 50 or ≥ 10 yrs experience in MF distribution as of <b>31 May 2010</b> → pass exam OR CPE classroom credits"],
         ["KYD (Know Your Distributor)","Self-attested PAN + address proof at <b>CAMS-PoS</b> with originals; biometric: <b>right-hand index finger</b> (new &amp; renewal; authorised persons for non-individuals); acknowledgement sent to all empanelled AMCs. New cadre: no KYD/biometrics, only ID &amp; address proof"],
         ["ARN","Allotted by AMFI after certification + KYD; minimum age <b>18</b>"],
         ["Empanelment","With any number of AMCs, or work as agent of an empanelled distributor — compulsory to earn commission"],
         ["Employees of institutions","Clear NISM V-A + get <b>EUIN</b>; quote EUIN on forms; no separate ARN (operate under institution's ARN)"],
         ["Online only","From <b>1 Oct 2024</b>, ARN &amp; EUIN applications only online on AMFI website"]]))
    sub("AMC empanelment form & declaration", 3,
      K("Personal info (name, age, trade name, contact, ARN, PAN, tax category)","Key sales/ops people","Business details (branches, employees, area, experience, investors, agents, AMCs, AUM)","Bank details (direct credit)","Info preferences","Nominee") +
      L("Info correct; keep transactions confidential; follow instructions/codes",
        "No ads/publicity except AMC-provided or pre-approved","Risk factors with performance info","Give documents AMC asks for",
        "All selling staff have EUIN","No rebating, gifts or pass-back","AMC may terminate empanelment any time") +
      K("No standard format — each AMC has its own","Some AMCs empanel only high-business distributors; commission may be linked to volume"))
    sub("Distributor revenue: trail commission only", 5,
      L("Upfront commission and transaction charges <b>withdrawn</b> by SEBI",
        "Commission on Regular Plan investments, paid by AMCs per their commission structure (typically monthly)",
        "SEBI MF Master Circular <b>20 March 2026</b>: full trail model; no upfront, no upfronting of trail, directly or indirectly, cash or kind, sponsorships or other route",
        "Trail paid only in monetary terms; no other incentives",
        "Reg 66(6): AMC pays distribution commission as SEBI specifies (to curb mis-selling)",
        "Exception: <b>upfronting of trail allowed only for SIP inflows</b>"))
    sub("Trail commission calculation", 5,
      F("Trail for the day = AUM × trail rate p.a. ÷ 365\nEx: ₹10 lakh at NAV 10 → 1,00,000 units; 1% p.a.\nDay 1: 10,00,000 × 1% ÷ 365 = ₹27.40 ; August 2019 total = ₹853.13\nBought 1,000 units at ₹10; NAV rises to ₹15 → trail on ₹15,000, not ₹10,000") +
      K("% of net assets; daily balances; paid monthly/quarterly","Rises with market value","Paid as long as money stays invested (unlike insurance)","No commission on distributor's own investments (self-business)",
        "Must disclose commissions from competing schemes considered","Change of distributor → no trail to either for 12 months"))
    sub("Additional commission: B-30 & women investors", 5,
      KV([("Eligible inflows","(a) New individual investors (new PAN) from <b>B-30 cities</b> (industry level) (b) New <b>women</b> individual investors (new PAN) from Top-30 and B-30 cities"),
          ("Lump sum","1% of first application, max <b>₹2,000</b>, if investor stays ≥ 1 year"),
          ("SIP","1% of total investment in first year, max <b>₹2,000</b>"),
          ("Source","2 bps of daily net assets set aside annually for investor education, awareness &amp; financial inclusion; claw-back provisions"),
          ("Over and above","Existing trail commission"),
          ("No dual incentive","Woman from B-30 paid once; Top-30 woman only if B-30 commission not claimed"),
          ("Reference","Reg 52(4A); SEBI circular 27 Nov 2025")]))
    sub("Transaction charges — withdrawn", 4,
      L("Earlier: AMCs could pay transaction charges on subscriptions &gt; ₹10,000",
        "SEBI circular <b>Aug 2025</b>: framework withdrawn → no investor-borne transaction charges; no upfront commission by investors",
        "Distributors paid directly by AMCs (agents of AMCs); nothing deducted from investor contributions"))
    sub("GST on distributor commission", 3,
      KV([("From","July 2017"),("Threshold","Annual turnover &gt; <b>₹20 lakh</b>"),
          ("Registered MFD","Raises invoice, pays GST"),
          ("Reverse charge","Sec 9(4) CGST Act &amp; Sec 5(4) IGST Act — registered recipient pays tax on procurement from unregistered supplier")]))
    sub("Commission disclosure by AMCs", 4,
      T(["Disclose total commission &amp; expenses for distributors meeting ANY (non-institutional incl. HNI)",""],
        [["Multiple points of presence","&gt; 20 locations"],["AUM raised across industry","&gt; ₹100 crore"],["Commission across industry","&gt; ₹1 crore p.a."],["Commission from single MF/AMC","&gt; ₹50 lakh"]]) +
      K("Data to AMFI; AMFI publishes consolidated data","Yearly: distributor-wise gross inflows (flag associate/group of sponsor), net inflows, average AUM, AUM/gross inflow ratio",
        "Portfolio turnover &gt; 2× industry average → additional due diligence"))
    sub("Due diligence of distributors by AMCs", 4,
      KV([("Applies to","Same 4 criteria (any one)"),("Reference","SEBI circular CIR/IMD/DF/13/2011, 22 Aug 2011"),
          ("Fit &amp; proper factors","(a) Business model, experience, proficiency (b) Record of levies, fines, penalties, suits, compensation + corrective actions (c) Associates &amp; subsidiaries (d) Controls delinking customer risk evaluation and scheme appropriateness from sales/RM")]))
    sub("Distributor vs investment adviser; advisory vs execution only", 5,
      KV([("Investment adviser","Paid to give investment advice, or holds out as adviser; <b>excludes</b> AMFI-registered MFD giving advice incidental to primary activity"),
          ("Rules","Distributor cannot call itself investment adviser; adviser can't earn both advisory fee and commission"),
          ("Advisory","Subject to <b>appropriateness</b>: sell only products best suited within defined upper ceiling of risk appetite — no exception"),
          ("Execution only","If inappropriate: written communication of unsuitability acknowledged by investor + confirmation of 'execution only' before execution; investor pays nothing extra"),
          ("No third category","Only advisory or execution only"),
          ("Group/associate products","Disclose conflict of interest")]) +
      K("Distributor compliance reviews: product review criteria &amp; periodicity; customer risk appetite factors &amp; review",
        "Other due diligence: internal audit of transactions/exceptions; recruitment, training, certification; onboarding, servicing, grievances; audits; investor sample surveys",
        "Distributors can't project as investment advisers or financial planners"))
    sub("Mis-selling (Box 6.8.3)", 5,
      KV([("Exemption","SEBI Investment Adviser Regulations 2013 exempt MFDs giving incidental advice"),
          ("Suitability","Required in both advisory and execution-only"),
          ("Regulation","SEBI (Prohibition of Fraudulent and Unfair Trade Practices) 2003 — includes MF mis-selling")]) +
      L("False or misleading statement","Concealing/omitting material facts","Concealing risk factors","Not taking reasonable care for suitability"))
    sub("Nomination for distributors & commission to nominee", 4,
      L("AMFI advised AMCs to offer nomination to MFDs at empanelment",
        "Commission paid to nominee, or legal heirs if no nominee (heirship documents)",
        "Paid until investor changes the deceased's ARN code / AUM becomes nil; no new business or new/changed systematic transactions under deceased's ARN",
        "Nominee: death certificate only, no succession certificate; need not be an ARN holder",
        "Only for assets procured while ARN valid; ARN valid &amp; not suspended on date of death; later expiry ignored",
        "Nominee receives as <b>trustee</b> for legal heirs",
        "Assets transferred to nominee's account only on investor's request and if nominee holds valid ARN",
        "Nominee/heir informs AMFI with Gazette-officer-attested death certificate; AMFI informs AMCs (not for overseas distributors)") +
      KV([("AUM transfer to nominee","Deceased's ARN valid/not suspended at death; nominee has valid ARN, KYD compliant, annual self-certification done; inform all clients — investors get <b>15 days</b> to object to AMC")]))
    sub("Change of distributor", 5,
      L("Investor may change distributor without reason, by written request, without NOC",
        "No commission to old or new distributor; AMCs may pay new distributor after <b>12-month</b> cooling-off",
        "Exception: change due to distributor's <b>voluntary cessation</b> → new distributor gets trail per SEBI/AMFI rules") +
      T(["Distributor-initiated change allowed only for",""],
        [["i","Change in name/legal status (individual → partnership → LLP; private ↔ public ltd)"],
         ["ii","Merger/acquisition/consolidation/transfer within same group (non-individuals)"],
         ["iii","AUM consolidation within family/close relatives (individuals)"],
         ["iv","Transfer of business by individual distributors"]]) +
      K("Entire AUM must transfer, to a valid KYD-compliant ARN holder","Old ARN surrendered; no further business"))
