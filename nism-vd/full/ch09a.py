from summary_lib import *

def add(chap, sub):
    chap(9, "Investor Services", "10", 5)
    sub("NFO process", 4,
      L("AMC picks scheme using CIO (investment objective) + CMO (market interest) inputs",
        "One scheme per category — NFO only in a category where AMC has none, or multi-scheme categories (sector/theme, index, FoF)",
        "SID prepared → approved by <b>Trustees and AMC Board</b> → filed with SEBI → SEBI observations incorporated → issued",
        "Timetable per market; ads &amp; PR per SEBI code; events for intermediaries and press; documents &amp; forms circulated") +
      T(["Date","Meaning"],
        [["NFO open date","Investors can start investing"],["NFO close date","Last day to invest"],
         ["Scheme re-opening date","Open-ended: ongoing sale &amp; repurchase at NAV-based prices (close-ended has none — trade on exchange)"]]) +
      KV([("NFO period","Minimum <b>3 working days</b>; maximum <b>15 days</b> (except ELSS)"),
          ("Allotment / refund","Within <b>5 business days</b> of NFO close"),
          ("Re-open (open-ended)","Within <b>5 business days</b> of allotment"),
          ("Deployment","Reg 35(5): realistic deployment timelines in SID")]))
    sub("NFO & ongoing prices", 4,
      K("NFO price = price per unit during NFO (usually face value ₹10)","Ongoing sale price = NAV (no entry load)","Redemption/switch-out price = NAV − exit load (if any)"))
    sub("Direct and regular plans", 5,
      L("Every MF must offer both; different TERs → separate NAVs",
        "Direct: lower expense (no distribution expense/commission); only for investors buying directly from the fund",
        "Routed through distributor → regular plan",
        "No other plans based on expense ratio allowed"))
    sub("Growth, IDCW payout, IDCW reinvestment", 5,
      L("Same portfolio → same portfolio return; differ in cash flows, taxability, units, value → different post-tax returns",
        "Dividend option renamed IDCW from <b>1 April 2021</b>",
        "Some liquid/very short debt funds declare IDCW daily (if profits)",
        "<b>Cum-dividend NAV</b>: after announcement, before payout · <b>Ex-dividend NAV</b>: reduced NAV after payout",
        "Payout: cash to bank, units unchanged, taxed in investor's hands",
        "Reinvestment: units added at <b>ex-dividend NAV</b> (₹2 × 100 units = ₹200 ÷ ₹20 = 10 units); taxed in year of receipt",
        "Growth: no IDCW; NAV captures full gain; units unchanged") +
      T(["Parameter","IDCW payout","IDCW reinvestment","Growth"],
        [["IDCW in bank","Yes","No","No"],["Tax on IDCW","Yes","Yes","N.A."],["More units","No","Yes","No"],
         ["NAV","Falls by IDCW","Falls by IDCW","Captures all valuation changes"]]))
    sub("Illustration 9.1 — three investors", 5,
      F("A (growth), B (payout), C (reinvest): 100 units at NAV ₹10; NAV → ₹12; IDCW 10% (of face value ₹10 = ₹1/unit)\nB gets ₹100 cash; C reinvests ₹100 at ex-NAV ₹11 → 9.09 units\nA: 100 × 12 = ₹1,200 (₹200 capital gain)\nB: 100 × 11 = ₹1,100 + ₹100 IDCW = ₹200 total return\nC: 109.09 × 11 = ₹1,200 (₹100 gain + ₹100 reinvested IDCW)\nPost-tax returns differ (IDCW vs gains taxed differently)") +
      TRAP("IDCW % is declared on FACE VALUE, not NAV."))
    sub("Allotment of units", 5,
      T(["Case","Rule"],
        [["NFO","Units at face value ₹10; full allotment to valid applications if minimum subscription met; trustee may reject any application without reason; allotment within 5 business days; demat credit within <b>2 working days</b>; SOA (non-demat) within 5 business days of NFO close; FPIs subject to RBI approval; ASBA: account debited on allotment intimation by CAMS"],
         ["Ongoing","Amount ÷ sale price (NAV): ₹12,000 ÷ ₹12 = 1,000 units"],
         ["Rights issue","Amount ÷ rights price (less meaningful for MFs)"],
         ["Bonus 1:3","1 free unit per 3 held; net assets same → NAV falls proportionately; value unchanged"],
         ["Refund delay","Beyond 5 business days → <b>15% p.a.</b> interest, charged to AMC"]]) +
      K("Demat units fully and freely transferable (subject to lock-in and lien)","Transfer on operation of law/pledge enforcement with satisfactory evidence"))
    sub("Account statements", 5,
      T(["Statement","Rule"],
        [["Monthly SOA","Every month if any transaction: value, NAV, units, closing balance &amp; value"],
         ["Annual SOA","For unitholders with no transaction in last 6 months; may be soft copy by email"],
         ["Consolidated Account Statement (CAS)","Each calendar month (post/email) for investors with a transaction: all transactions &amp; holdings across all schemes of all MFs"],
         ["Half-yearly CAS","No transaction in 6 months ending September or March"],
         ["Common investor","Identified by <b>PAN</b>"]]) +
      K("'Transaction' = purchase, redemption, switch, IDCW payout, IDCW reinvestment, SIP, SWP, STP, bonus"))
    sub("Eligible individual investors", 5,
      T(["Investor","Rule"],
        [["Resident adults (18+)","Singly or jointly — max 3 names"],
         ["Minors (&lt;18)","Through guardian; payment from bank account of minor, parent or legal guardian, or joint account of minor with parent/guardian; existing folios: change of payout bank mandate before redemption"],
         ["HUF","Karta invests; adds 'HUF' after name"],
         ["NRIs / PIOs","Repatriable or non-repatriable; PIO/OCI card"],
         ["Foreign investors (QFIs)","Sub-category of FPI; from FATF member (or member of group in FATF) + IOSCO MMOU signatory country; via demat (direct) or Unit Confirmation Receipt (UCR)"]]))
    sub("Eligible non-individual investors", 3,
      K("Indian companies/corporate bodies","Registered &amp; co-operative societies","Trustees of religious/charitable and private trusts","Partners of firms","AOP/BOI","Banks (incl. co-op, RRBs), FIs, investment institutions",
        "Other SEBI-registered MFs","SEBI-registered FPIs (direct: demat via DP; indirect: UCR)","Govt-approved international multilateral agencies","Army/Navy/Air Force, para-military","Scientific &amp; industrial research orgs","Universities &amp; educational institutions") +
      K("Some gilt plans only for PFs, superannuation, gratuity, pension funds, religious/charitable and private trusts","Check 'Who can invest?' in SID"))
    sub("Application form — key fields", 5,
      T(["Field","Rule"],
        [["Direct/Regular","Write 'Direct' in ARN box; regular → ARN/RIA number"],
         ["Holders","Up to 3; folio in name of first holder; all benefits (IDCW, redemption, tax) to <b>first holder</b>; overseas address for FPI/NRI/PIO"],
         ["Minor","Guardian (natural parent or court-appointed) does KYC/PAN; proof of relationship/guardianship; minor's DOB + age proof; no joint holders; at majority folio <b>frozen</b> until status changed (KYC, PAN, bank-attested signature, bank details)"],
         ["PoA","PoA holder and issuer KYC/PAN; certified PoA copy; grantor can still operate; PoA holder can do everything <b>except make/change nominations</b>"],
         ["Mode of holding","Single / joint / either or survivor; default if not chosen; joint holders can't be added or removed except deletion on death"],
         ["Address","After first holder's PAN validated for KYC, KYC address overrides form"],
         ["KYC","KYC acknowledgement + occupation, gross annual income/net worth, PEP status"],
         ["FATCA/CRS","If birth/citizenship/tax residency outside India: city &amp; country of birth, citizenship, tax countries &amp; Tax IDs"],
         ["Bank details","Mandatory for sole/first holder: bank, branch, city, account no., type (savings, current, NRO, NRE, FCNR), MICR, IFSC; demat holders → bank linked to demat"],
         ["Payout account different from paying account","Proof: cancelled cheque with name, passbook/statement ≤ 3 months old, or bank letter"],
         ["Investment details","Scheme mandatory; plan/option defaults apply if blank"],
         ["Payment","Payable to MF's specified account; application/folio no. on reverse; paying bank need not equal payout bank"],
         ["Demat option","DP name, ID, beneficiary account; DP KYC accepted; client master/DP statement copy"],
         ["Nomination","Max <b>3</b> nominees; at application or later; change any number of times; single holder should nominate or declare opt-out (SEBI circular effective 1 Mar 2025)"],
         ["Minimum investment","Higher for initial, lower for additional; signed by all holders whatever the mode"]]))
    sub("Financial transactions: purchase, additional purchase, repurchase", 5,
      L("Initial purchase: full application form + KIM (common application form) → folio created",
        "Existing investor: may use same form with folio no.; personal info not repeated",
        "Additional purchase: transaction slip (often pre-printed with folio) + payment; folio data overrides conflicting form data; name mismatch → may be rejected",
        "Repurchase: transaction slip with folio, holders, scheme/plan/option; signed per mode of holding; specify amount or units",
        "Repurchase price = applicable NAV − exit load; units redeemed on <b>FIFO</b> basis",
        "If balance falls below minimum, all units may be redeemed and folio closed",
        "Demat units: redemption form to DP → AMC/RTA → paid to demat-linked bank",
        "Pool accounts of brokers/clearing members discontinued; units credited/debited directly (DIS to DP still allowed for demat redemption)",
        "Switch = redemption + purchase in one transaction",
        "Subscription and redemption frequency same for all MF schemes — except SIFs (e.g. daily subscription, weekly redemption)"))
    sub("Digital payment modes", 4,
      T(["Mode","Key points"],
        [["Online / internet banking","PIN-based access; NEFT (batched), IMPS (instant, mobile/net/ATM), RTGS (instantaneous), SWIFT (from abroad, slower); bank acknowledgement with first holder as account holder"],
         ["2FA","SEBI mandates Two-Factor Authentication for subscription and redemption"],
         ["NACH","By NPCI; replaced ECS; repetitive bulk payments; same-day presentation &amp; settlement; NACH Credit &amp; Debit; ECS mandates migrated automatically"],
         ["UPI","VPA via mobile app (BHIM, bank apps); multiple accounts, one default; Aadhaar-based transfer version"],
         ["ASBA","For NFOs: amount blocked, debited only on allotment; earns interest meanwhile; no refunds"],
         ["AEPS","Aadhaar-linked; fingerprint as password"],
         ["NUUP (*99#)","USSD mobile banking without smartphone/internet; 11 regional languages"],
         ["Cards","Debit &amp; prepaid; <b>credit cards NOT allowed</b> for MF purchases"],
         ["E-wallets","Max <b>₹50,000</b> per investor per FY (umbrella limit with cash, per MF); only money loaded via cash/debit card/net banking; not credit card, cashback, promos; no third-party; RBI KYC compliant"]]))
    sub("One-Time Mandate (OTM)", 4,
      L("Authorises bank to process debits raised by a specified MF via NACH — one-time registration",
        "Needs bank name, account no., type, IFSC, MICR + cancelled cheque; folio/application no., email, phone",
        "Frequency: monthly, quarterly, half-yearly or 'as and when presented'; fixed amount or daily maximum (e.g. ₹5,000 as and when presented — unlimited transactions within daily max)",
        "Validity period specified; signed by bank account holders; registration takes <b>3–4 weeks</b>",
        "Folio-level; MF specifies eligible schemes/transactions (fresh lump sum, additional, SIP); usable via physical, online, SMS; cancel via OTM form"))
    sub("Cheque / DD rules", 4,
      L("Cheque/DD in favour of the scheme; investor name/PAN and scheme details on instrument; separate instrument per scheme/plan",
        "DD accepted mainly where no official collection centre; AMC bears outstation DD charges within limits",
        "NRI: non-repatriable → NRO/NRE/FCNR cheque; repatriable → NRE/FCNR; drafts bought abroad need debit certificate / FIRC",
        "Local or 'payable at par' cheques; signed by investor; drawn on account where first holder is an account holder",
        "No post-dated (except SIP), no stale (&gt; 3 months)",
        "Payment only through modes with independent traceability of end investor (SEBI)"))
    sub("Third-party payments (Box 9.1)", 5,
      KV([("Definition","Payment from a bank account other than the first holder's (joint account OK if first holder is a joint holder)"),
          ("Exception 1","Parents/related persons for a minor (love &amp; affection/gift) — max <b>₹50,000</b> per purchase or per SIP instalment; payer KYC + Third Party Declaration"),
          ("Exception 2","Employer via payroll deduction; custodian on behalf of FPIs"),
          ("Documents","Declaration identifying beneficiary; third party KYC + PAN regardless of amount; source proof: pre-printed cheque name / statement / bank letter / DD funding proof / NEFT acknowledgement"),
          ("Not accepted","DDs issued against cash for ₹50,000 or more")]))
    sub("Cash payments", 5,
      L("Up to <b>₹50,000 per investor, per MF, per FY</b> (PMLA &amp; AML compliance)",
        "Only resident individuals, sole proprietorships, minors via guardians — KYC compliant (with or without PAN)",
        "Physical application; deposit slip at ISC; cash at designated bank branches; bank acknowledgement + form to ISC for time stamping",
        "Redemptions/IDCW only via banking channel") +
      K("Not accepted: stock-invests, postal orders, money orders, cash (beyond exception), outstation cheques, post-dated cheques (except systematic)",
        "AMCs may pay via RTGS, NEFT, IMPS, direct credit, cheque, DD, warrants"))
    sub("Repurchase payments & multiple bank accounts", 5,
      L("Cheque (slow: preparation, post, deposit, clearing) or electronic (direct credit, RTGS, NEFT, NACH)",
        "Paid to sole/first holder; cheques to unitholder's address; demat → DP-registered bank",
        "NRIs paid in rupees; conversion cost on investor; repatriable → NRE/FCNR; TDS applies",
        "Register up to <b>5</b> bank accounts (individual) or <b>10</b> (non-individual); first holder in each; one default; change default any time",
        "NRI: paid via NRO → register NRO; paid via NRE → NRO or NRE",
        "Credit to a non-registered account requested with redemption → paid to default account; change not processed"))
    sub("Instant Access Facility (IAF)", 5,
      KV([("What","Same-day credit of redemption"),("Where","Only <b>liquid</b> schemes"),
          ("Limit","Lower of <b>₹50,000</b> or <b>90%</b> of latest value — per day, per scheme, per investor")]))
    sub("Cut-off timings & applicable NAV", 5,
      T(["Scheme","Transaction","Cut-off","Applicable NAV"],
        [["Equity &amp; debt (not liquid/overnight)","Purchase / switch-in (any amount)","3:00 pm","NAV of business day on which funds are available for utilisation before cut-off"],
         ["Liquid &amp; overnight","Purchase / switch-in","1:30 pm","Application + funds before cut-off → NAV of day <b>immediately preceding</b> day of receipt; after cut-off with funds same day → NAV of day preceding <b>next business day</b>; funds not available → NAV of day preceding day funds available"],
         ["Equity &amp; debt (not liquid)","Redemption / switch-out","3:00 pm","Same-day NAV before cut-off; next business day NAV after"],
         ["Liquid","Redemption / switch-out","3:00 pm","Before cut-off → NAV of day preceding next business day; after → next business day NAV. IAF before cut-off: lower of previous calendar day NAV and NAV of day of receipt; IAF after: lower of day of receipt and next calendar day"],
         ["Overnight","Redemption / switch-out","3:00 pm","Before → NAV of day preceding next business day; after → next business day NAV; <b>online cut-off 7:00 pm</b>"]]) +
      K("Liquid funds: NAV for every calendar day","Not applicable to NFOs and international schemes","Funds-realisation rule for all purchases since 1 Feb 2021 (SEBI circular 17 Sep 2020; earlier &lt; ₹2 lakh got same-day NAV)"))
    sub("Cut-off worked examples", 5,
      F("Week: Mon, Wed, Thu, Fri = business days; Sun, Tue, Sat = holidays\n1. Equity purchase ₹3 lakh applied Mon, funds Wed by 2 pm → Wed NAV; funds Wed by 5 pm → Thu NAV\n2. Liquid purchase Mon, funds by 1 pm Mon → Sun NAV; funds by 3 pm Mon → Tue NAV; funds 10 am Wed → Tue NAV\n3. Equity redemption Mon before cut-off → Mon NAV; after → Wed NAV\n4. Liquid redemption Mon before cut-off → Tue NAV; after → Wed NAV"))
