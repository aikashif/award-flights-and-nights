from summary_lib import *

def add(chap, sub):
    sub("Time stamping", 4,
      L("Official Points of Acceptance (OPoAs) disclosed in SID &amp; website; time stamping done at OPoA",
        "Distributor may collect but must forward quickly — <b>time at OPoA counts</b>, not time given to distributor",
        "Machines with tamper-proof seal; opened only by vendor/nominated persons, documented and reported to trustees",
        "Sequential numbering through machine's full range — daily stamping does NOT restart at 1",
        "Purchase application, reverse of payment instrument and acknowledgement: location code, machine ID, serial no., date and time",
        "Repurchase application + acknowledgement stamped similarly",
        "Non-financial (e.g. change of address): date stamp matters, not time",
        "Online: time of the web server receiving the instruction"))
    sub("KYC — who and when", 5,
      L("All investors: individuals, non-individuals, joint holders, NRIs, PoA holders &amp; issuers, guardians of minors — <b>irrespective of amount</b>",
        "Applies to new/additional purchases, switches, new SIP/micro-SIP, STP, DTP registrations",
        "Purpose: identity and address under anti-money laundering laws; application carries KRA acknowledgement",
        "Documents given to distributor or other SEBI intermediary (broker, DP); updated in KRA's central system"))
    sub("KYC documents & PAN exemptions", 5,
      KV([("PAN","Mandatory proof of identity (with photo) except exempt; intermediaries may verify PAN online on IT website if another ID proof given"),
          ("PAN-exempt","Central/State govt transactions &amp; court-appointed officials · <b>Sikkim</b> residents · tax-exempt UN entities/multilateral agencies · MF investments up to <b>₹50,000 per investor per year per MF</b> → give alternate photo ID"),
          ("Address proof","Passport, voter ID, ration card, DL, bank statement, utility bill etc.; both addresses if different; spouse's address proof acceptable"),
          ("Attestation","Self-attested copies + originals for verification; else attested by authorised persons"),
          ("Formats","Prescribed by SEBI")]))
    sub("PAN-exempt investments & PEKRN (Box 9.2)", 5,
      L("Micro-SIP: annual SIP (rolling 12 months or Apr–Mar) ≤ <b>₹50,000</b>",
        "Composite ₹50,000 limit for micro-SIP + lump sum per MF per FY",
        "For individuals, minors, sole-proprietary firms",
        "KYC still via KRA → quote <b>PAN Exempt KYC Reference Number (PEKRN)</b> + letter copy") +
      K("Alt photo IDs: voter ID, DL, govt/defence ID, passport, photo ration card, photo <b>debit</b> card (not credit card), ROC-registered company employee ID, IDs by bank managers/gazetted officers/MLAs/MPs, bank employee IDs, senior citizen/freedom fighter ID, university / ICAI / ICMAI / ICSI cards, <b>PRAN</b> card (NPS, by CRA NSDL), other govt IDs (ESIC, EPFO)",
        "Current &amp; valid; self-attested or attested by ARN holder (with ARN)"))
    sub("KYC Registration Agencies & CKYC", 5,
      KV([("Central KYC","One KYC with one intermediary → valid across capital market"),
          ("IPV","In-Person Verification by intermediary + upload to KRA → KYC valid market-wide"),
          ("Uniform form","SEBI circulars 22 Aug 2011, 5 Oct 2011, 26 Dec 2013 → standard Account Opening Form (AOF): Part I basic KYC, Part II exchange-specific"),
          ("CERSAI","Notified <b>26 Nov 2015</b> as Central KYC Records Registry (CKYCR) under PML Rules 2005"),
          ("CKYC upload","CERSAI template = Part I of AOF for individuals; upload for accounts opened on/after <b>1 Aug 2016</b>"),
          ("CKYCR functions","Store/safeguard/retrieve KYC records online · share updates with reporting entities · services on prepaid fee · de-duplicate and issue unique <b>KYC Identifier</b>")]) +
      K("With KYC Identifier, entity downloads records — re-submission only if information changed, current address to verify, or entity needs it for verification / enhanced due diligence / risk profile"))
    sub("e-KYC via UIDAI & KYC through intermediaries", 4,
      L("UIDAI e-KYC accepted: details + photo = proof of identity and address; client authorises access",
        "Notified entities may do Aadhaar authentication under <b>Sec 11A of PMLA</b> as KYC User Agencies (KUAs); intermediaries/MFDs sign with one KUA and register as <b>sub-KUAs</b>",
        "Demat holding or exchange route: DP's KYC accepted",
        "Mandatory additional fields: occupation, gross annual income/net worth, PEP status (individuals &amp; non-individuals)",
        "MFs, depositories, RTAs, KYD-compliant MFDs, brokers can facilitate KYC"))
    sub("KYC process & online KYC", 4,
      L("Form + documents verified with originals, or true copy attested by Notary, Gazetted Officer or Scheduled Commercial Bank manager",
        "Originals returned; data uploaded to a KRA",
        "<b>IPV mandatory</b>; name, designation, organisation of verifier recorded; IPV by a scheduled commercial bank accepted",
        "After upload, no further KYC for any securities market segment; change of address etc. done once with any intermediary",
        "Online KYC: eSign, DigiLocker, e-signatures (IT Act 2000); mobile/email via OTP; Aadhaar via UIDAI; PAN via IT database; bank via <b>penny drop</b>/API; OVDs via DigiLocker/eSign; wet signature scan or cropped signature via eSign",
        "Supreme Court 30 Apr 2025: digital KYC must be accessible to persons with disabilities (SEBI FAQ revised)") +
      T(["Special case","KYC rule"],
        [["Minor","Guardian's KYC + minor's age proof"],["PoA","Both investor and PoA holder; PoA holder can't apply for KYC on issuer's behalf"],
         ["NRI","PAN = sole identification number; passport/PIO/OCI copy + overseas address proof mandatory"]]))
    sub("Institutional investors & UBO", 5,
      L("Eligibility to invest: incorporation documents (MoA/AoA, trust deed) must permit; some states need Charity Commissioner's permission for religious/charitable trusts",
        "Authorisation to invest: Board Resolution",
        "Authorised signatories (in Board Resolution); MF acts only on forms signed by authorised signatories") +
      T(["Ultimate Beneficial Owner (UBO)","Threshold"],
        [["Company","&gt; <b>25%</b> of shares or profits"],["Partnership / body of persons","&gt; <b>15%</b>"],
         ["Trust","Settlor, trustees, beneficiaries with ≥ 15% of benefits"],["Exempt","Listed companies and their (majority-owned) subsidiaries; individual investors"]]) +
      K("Client Due Diligence under PMLA","UBO proof (name, address, PAN/passport) + UBO declaration to AMC/RTA; intimate changes"))
    sub("FATCA & CRS", 4,
      L("Due diligence to identify foreign reportable accounts; report to US IRS / foreign govt / Indian tax authorities",
        "Info if citizenship, nationality, birthplace or tax residency outside India; tax countries + taxpayer IDs",
        "Covered investor → entire value of all folios reported, with direct/indirect beneficiaries and controlling persons",
        "Change in status reported to MF within <b>30 days</b>"))
    sub("Systematic transactions — why", 3,
      K("Tailor investments/payouts to goals","Align with investible surplus, regular income needs, rebalancing","Execute without repeated instructions → protects from investor inertia"))
    sub("SIP & rupee cost averaging", 5,
      T(["Month","NAV","Units for ₹1,000","Cumulative"],
        [["1","10","100.000","100.000"],["2","12","83.333","183.333"],["3","9","111.111","294.444"],
         ["4","11","90.909","385.353"],["5","10","100.000","485.353"],["6","12","83.333","568.686"]]) +
      F("Average cost = 6,000 ÷ 568.686 = ₹10.55  <  average NAV ₹10.67  → Rupee Cost Averaging") +
      K("Buy volatile markets over time without predicting","Smaller amounts easier than lump sums","Via post-dated cheques, NACH, Standing Instructions","Can open a folio or add; lower minimum than lump sum; can start during NFO"))
    sub("Systematic Withdrawal Plan (SWP)", 5,
      L("Redeem a constant value periodically — avoid exiting all at a trough",
        "₹1,000/month: NAV 10 → 100 units; NAV 12 → 83.333; NAV 9 → 111.111",
        "Exit load raises units needed: 1% load at NAV 10 → effective ₹9.90 → <b>101.0101 units</b> for ₹1,000",
        "Register amount, periodicity (usually monthly), period; some allow only appreciation or IDCW to be withdrawn (variable SWP — capital not withdrawn)",
        "Reasons: avoid trough risk; regular expenses (retirement); regularly encash profits",
        "Exit loads and taxes apply"))
    sub("Systematic Transfer Plan (STP)", 5,
      L("SWP from source scheme + SIP into target scheme of the same MF",
        "One transfer = switch; multiple pre-defined tranches = STP",
        "Transfer = redemption → exit loads &amp; taxes apply",
        "Scheme minimum investment/redemption limits do NOT apply to STP",
        "MF defines eligible source and target schemes",
        "Avoids idle funds &amp; double paperwork; used for phased equity entry, rebalancing, profit booking; fixed amount or appreciation",
        "SIP, SWP, STP may be offered for SIF strategies (with minimum investment threshold)") +
      F("₹10 lakh in short-term debt fund → STP ₹1 lakh × 10 to equity; exit load 0.25% for 3 months\nFirst 3 instalments: load ₹250 → ₹99,750 transferred; thereafter full ₹1,00,000"))
    sub("Switch & Transfer of IDCW Plan (DTP)", 4,
      KV([("Switch","Redemption + purchase in one transaction (e.g. book equity profits → short-term debt)"),
          ("DTP","Invest IDCW of one scheme into another scheme of the same MF")]) +
      L("Must hold IDCW option of source scheme; DTP overrides payout/reinvestment instructions; covers all units in that option",
        "Target units in same folio; target scheme minimum doesn't apply; MF may set minimum IDCW to transfer",
        "Invested on the <b>next business day after the record date</b>",
        "Register a set number of days before record date; ends automatically when source holding is nil or by written request",
        "Uses: low-risk investor transfers debt IDCW into equity; equity IDCW into debt to rebalance"))
    sub("Operational aspects — SIP registration", 4,
      L("MF specifies schemes, minimum per tranche, dates, minimum tenure; investor picks amount, frequency (monthly, quarterly, semi-annual, annual), period, dates; defaults if not chosen",
        "Minor: SIP registered only till majority",
        "New investor: application form + SIP enrolment form (must tally); existing: only enrolment form with folio no.; signed per mode of holding (all holders if joint)",
        "Enrolment typically <b>15–30 days</b> before first instalment (e.g. submitted 5 Sep, SIP date 15th, 30 days needed → first on 15 Oct); shorter if OTM registered",
        "Payment: post-dated cheques or NACH, direct debit, Standing Instructions (bank/branch tie-up)",
        "First instalment: cheque on the registered bank, or any bank + photocopy of registered bank's cheque, or no cheque if form attested by debiting bank"))
    sub("SIP top-up & SIP pause", 4,
      F("Top-up fixed: ₹2,500/month, +₹500 a year → Y1 ₹2,500, Y2 ₹3,000, Y3 ₹3,500\nTop-up %: +10% a year → Y1 ₹2,500, Y2 ₹2,750, Y3 ₹3,025") +
      L("Upper limit or end date for top-up; after that SIP stays constant till tenure ends",
        "At enrolment or later for an existing SIP (give existing SIP details)",
        "May not apply to micro-SIPs, or SIP + top-up ≤ ₹50,000 in rolling 12 months/FY",
        "<b>SIP pause</b>: 1–6 months (per AMC) without cancelling mandate; auto-resumes; units keep growing; avoids NACH bounce charges/new mandate"))
    sub("Renewal & cancellation; SWP/STP registration", 3,
      L("SIP renewal form: scheme, plan, option, amount, date, period",
        "SIP cancellation: notice to AMC (period set by AMC) + cancel bank mandate; may auto-cancel on insufficient funds; online/offline via AMC site/app, MFDs, platforms",
        "SWP: register scheme, plan, option, amount, frequency, period; minimum notice; credited to default or registered account; minimum per tranche usually lower than normal redemption; ends when all units redeemed or by written notice",
        "STP/switch: source &amp; target per MF list; MF sets minimum; notice period to register/cancel; switch via transaction slip in rupees or units; target units in same folio",
        "Each tranche at applicable NAV of that date (each leg of a transfer at its own NAV); loads &amp; taxes apply; cancel any time by written notice"))
    sub("Triggers", 3,
      L("Profit-booking trigger: redeem when market reaches a level (lose further upside)",
        "Date trigger: redeem specified units on a date",
        "Stop-loss trigger: redeem at a NAV level or % fall",
        "Entry trigger: transfer money into equity scheme when market falls to a level"))
