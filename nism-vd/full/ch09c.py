from summary_lib import *

def add(chap, sub):
    sub("Triggers — more detail", 3,
      L("Set on index value or investment value (e.g. switch into equity if market falls 20% or NAV falls x%)",
        "On trigger: redeem only appreciation, entire value, or a % of value; or switch to another scheme",
        "Stop-loss usually → redeem entire value; appreciation trigger → redeem appreciation",
        "MF decides trigger types and schemes; separate request per investment in a folio; notice period may apply",
        "<b>One-time</b> facility — extinguishes once activated and action completed"))
    sub("Nomination — rules", 5,
      T(["Rule","Detail"],
        [["Scope","Folio nomination covers all investments in the folio"],
         ["Number","Up to <b>3</b> nominees with % totalling 100; if % not given → equal shares"],
         ["Single holder","Nomination required unless holder declares intent not to nominate"],
         ["Joint holding","All holders sign, whatever the mode"],
         ["Who can nominate","Only individuals; NOT minors' folios; NOT PoA holders"],
         ["Who can be nominee","Individuals incl. minors (with guardian) and NRIs; Central/State govts; local authorities"],
         ["Can't be nominee","Trust (except religious/charitable), society, body corporate, partnership, Karta of HUF, PoA holder"],
         ["Change/cancel","Any time, by all original holders; new nomination supersedes old; death of sole nominee cancels; multiple → remaining nominees"],
         ["Demat units","Demat account nomination applies (depository bye-laws)"],
         ["Opt-out","Investors subscribing on/after <b>1 Aug 2022</b>: nominate or sign opt-out declaration"]]) +
      TRAP("The workbook says 'up to 3 nominees' in Ch 4 and Ch 9, but the new SEBI nomination section (incapacitated investors) says 'Investors can nominate up to 10 persons'. For the exam, 3 is the figure used in the sample question; know both."))
    sub("Nominee for incapacitated investors; joint holder death", 4,
      L("Investor may empower any one nominee (not a minor) to operate the folio if physically incapacitated but able to contract",
        "Specify % or absolute value the nominee can encash; change mandate any number of times",
        "On death of a joint holder: assets transmitted to surviving holder(s) by name deletion — survivors receive as <b>owners, not trustees</b>",
        "No limit on how often nomination is made/changed/cancelled"))
    sub("Pledge / lien of units", 4,
      L("Pledge form by unitholder (pledger) in favour of lender (pledgee)",
        "Units must have completed lock-in; all holders sign whatever the mode; name, scheme, plan, option, number of units",
        "Non-individuals: board resolution/authorisation",
        "Pledged units can't be sold/switched until pledgee's written NOC",
        "Lender can enforce and redeem with documents; scheme minimum redemption doesn't apply",
        "IDCW on pledged units to unitholder or lender per agreement"))
    sub("Demat account for MF units", 4,
      L("MFs must offer demat option; ISIN for each option of a scheme, shown on account statements",
        "Tie-up with NSDL / CDSL; demat account with DP; KYC incl. IPV for demat → no separate KYC by AMC/distributor",
        "Application: DP name, DP ID, beneficiary account no. (+ DP statement); names, holding mode, PAN matched; units credited after funds realised",
        "Mismatch → treated invalid for demat; physical units issued if otherwise valid",
        "Address, bank, nomination per depository records; changes via depository; redemption via depository or exchange",
        "Existing SOA units can be dematerialised; proceeds to demat-linked bank",
        "Demat → physical = <b>re-materialisation</b>") +
      K("Benefits: less paperwork · direct credit of bonus &amp; rights units · single change of address with DP · all investments in one account"))
    sub("Change in folio details", 5,
      T(["Change","Where / how"],
        [["Name, status/nationality, PAN, address, contact, spouse's/father's name","KRA change form (once) → KRA informs all MFs; give name, DOB, PAN or PERN, Aadhaar as per KYC; self-attested PAN + supporting documents (originals for verification)"],
         ["Bank account, mode of holding, nomination","With each MF separately"],
         ["Demat address","Per DP procedure"],
         ["Change of guardian (minor)","New guardian KYC + PAN, bank details, <b>NOC from existing guardian</b>"],
         ["Minor → major","Investor's PAN/KYC replaces guardian's; signature &amp; new bank updated; guardian stops operating"]]))
    sub("Change of bank account", 4,
      L("Register with each MF; up to <b>5</b> (individuals) / <b>10</b> (non-individuals); one default",
        "Before deleting the default account, designate another default (Part B of Multiple Bank Registration Form)",
        "Details: bank, account no. &amp; type, branch, IFSC, MICR + cancelled cheque with first holder's name (else statement/passbook/bank certificate); originals if photocopies",
        "Signed per mode of holding; without multiple-bank registration use Change of Bank Details form"))
    sub("Transfer and gifting of MF units", 5,
      L("Units now transferable in SOA or demat mode — can be gifted",
        "Eligible relatives: <b>spouse, children, parents, siblings, parents-in-law</b>",
        "Excluded: <b>ETFs</b> and <b>retirement/children's solution-oriented</b> funds",
        "Both giver and receiver KYC-compliant",
        "Units under lock-in (e.g. ELSS &lt; 3 yrs) or lien can't be transferred"))
    sub("Transmission of units", 5,
      T(["Situation","Units go to"],
        [["First holder dies (joint)","Second holder becomes first holder"],["Single holder with nominee","Nominee"],
         ["Joint holding with nominee","Joint holder's right takes precedence"],["No nomination","Legal successors"]]) +
      L("Nomination = authorisation to MF to transfer; nominee holds in trust for legal heirs — no title or beneficial interest; inheritance laws apply",
        "MF needs nominee's KYC, death certificate, indemnity",
        "Standard Transmission Request Form + common documents (AMFI), on AMC, RTA and AMFI websites; NOC form; documents vary by situation"))
    sub("Minor turned major", 5,
      L("Folio <b>frozen</b> for guardian on date of majority; no financial/non-financial transactions till status changed",
        "IDCW payout/reinvestment continues (net of TDS)",
        "SIP/SWP/STP registered beyond majority stop from that date (suspended if documents not received)",
        "Bank accounts &amp; demat of minors-turned-major: no debits until signature attested by banker; demat must be reopened as new account (minor accounts are single-name)",
        "PAN reissued with same number and new signature",
        "AMCs usually send reminder letters before majority") +
      KV([("Before MAM form","(i) Get PAN (ii) Complete KYC (iii) Change bank account status or open new account with pre-printed cheque book")]) +
      K("MAM documents: MAM form · PAN copy · KYC acknowledgement/form · cancelled cheque or statement/passbook · banker's signature attestation · nomination form · fresh SIP/STP/SWP mandate",
        "Signature in MAM form attested by registered parent/guardian, or Notary, or Judicial Magistrate First Class (JMFC)",
        "SEBI circular 24 Dec 2019 (partly modified May 2023)"))
    sub("NRI to resident Indian", 4,
      KV([("Bank","Can't operate NRO/NRE/FCNR(B); inform bank; open Resident Rupee account; may open Resident Foreign Currency (<b>RFC</b>) account for NRE/FCNR balances"),
          ("Demat","Inform authorised dealer (Portfolio Investment Scheme) and DP; open new 'Resident' demat; transfer holdings; NRI demat closed"),
          ("Mutual funds","Inform AMCs of status, address, bank; KYC change form to KRA (acknowledgement issued)")]))
    sub("Change in Karta of HUF", 3,
      K("Letter from new Karta with reason (or AMC form): deceased Karta's name, folio, scheme, units","KYC of new Karta and HUF (HUF KYC not needed if already compliant)","Attested death certificate","Bank certificate of new Karta's signature","Indemnity bond by all co-parceners + new Karta"))
    sub("Turnaround times (SEBI)", 5,
      T(["Service","Turnaround"],
        [["NAV calculation &amp; disclosure","Daily"],["NFO open (other than ELSS)","Max 15 days"],
         ["Allot units / refund","Within 5 business days of NFO close (delay → 15% p.a. interest, not charged to scheme)"],
         ["Re-open open-ended scheme (other than ELSS)","Within 5 business days of allotment"],
         ["IDCW &amp; redemption transfer","As specified by SEBI (delay interest borne by AMC)"],
         ["Annual report / abridged summary","4 months from FY close"],
         ["Portfolio statement to unitholders","Within 10 days from close of each half-year (31 Mar, 30 Sep)"],
         ["Half-yearly unaudited results on website","Within 1 month of half-year close (schemes other than debt/money market)"],
         ["Debt &amp; money market trades (incl. inter-scheme)","Daily, with 15-day lag (from 1 Oct 2020)"],
         ["CAS monthly / half-yearly","As specified by SEBI"],
         ["Unit certificate","Within 5 working days of request"],
         ["Close-ended: demat units on request","Within 2 working days"]]) +
      K("SOA or demat units: within 5 working days of closure of initial subscription or receipt of application","Demat units on request within 2 working days",
        "SOA also to dormant investors (no transaction for 6 months) — with portfolio statement/annual return; monthly soft copy if requested",
        "Other services: online consolidated family view, valuation, income, returns, capital gains workings"))
    sub("Unclaimed assets & MITRA", 4,
      K("SEBI measures: norms for inactive/dormant folios · mandatory contact &amp; bank details · nominate or opt out · simpler transmission · central reporting of investor's death") +
      KV([("MITRA","Mutual Fund Investment Tracing and Retrieval Assistant — RTA platform to trace inactive/unclaimed folios; industry-level search"),
          ("Hosted by","Two Qualified RTAs (QRTAs): <b>CAMS and KFintech</b>, as agents of AMCs; links on AMC, QRTA, AMFI, SEBI websites"),
          ("Benefits","Find overlooked investments or ones you're legal claimant to · encourage KYC · reduce unclaimed folios · transparent ecosystem · fraud mitigants"),
          ("DigiLocker","Govt digital wallet (Aadhaar, PAN, DL, death certificate…); bank, insurance, NPS statements already there; adding MF &amp; demat statements; nomination facility — nominee's mobile &amp; email needed")]))
    sub("Voluntary lock-in / debit freeze", 4,
      K("Investor can voluntarily lock folio against unauthorised redemption","Demat and non-demat (SOA) folios","No units debited until unlocked","Phase 1: via <b>MF Central</b> (RTAs) — SEBI circular Mar 2026"))
