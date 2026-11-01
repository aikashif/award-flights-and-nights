from summary_lib import *

def add(chap, sub):
    chap(5, "Scheme Related Information", "7", 4)
    sub("Mandatory scheme documents; caveat emptor", 5,
      KV([("Scheme related documents","SID, SAI and KIM"),
          ("Caveat emptor","'Let the buyer beware' — investor presumed to have read them; signing the form = legal acceptance; can't later claim unawareness"),
          ("Two key documents","<b>SID</b> (scheme details) + <b>SAI</b> (statutory info on MF/AMC; one SAI for all schemes)"),
          ("Legal technicality","SAI is part of the SID (in practice separate documents)"),
          ("Format","Prescribed by SEBI, same sequence; MF may add any 'material' disclosure; simple language"),
          ("SEBI role","Does NOT approve; gives observations → documents are <b>'vetted'</b>, not approved"),
          ("Where","Draft SID/SAI on SEBI website (public); final documents on AMFI website; every MF's site")]) +
      K("Contract: offer via documents → investor accepts by signing &amp; paying → MF completes by issuing units"))
    sub("SID — nature & cover page", 4,
      KV([("Purpose","Info a prospective investor ought to know before investing"),
          ("Validity","Effective until a 'material change' (other than fundamental attribute) → filed with SEBI and communicated / newspaper ads"),
          ("Cover page","Scheme name, type (open/close/interval; equity/debt/liquid/hybrid), face value, NFO dates (open, close, re-open), SID date, MF name, AMC &amp; trustee contacts"),
          ("Standard clause","Prepared per SEBI MF Regulations 2026, filed with SEBI with AMC's <b>Due Diligence Certificate</b>; units 'not approved or recommended by SEBI nor has SEBI certified the accuracy or adequacy' of the SID")]))
    sub("SID structure", 3,
      K("Table of contents","Highlights","Introduction","Risk factors (standard + scheme-specific)","Minimum number of investors","Special considerations","Definitions","Due Diligence Certificate (AMC)",
        "Information about the scheme: name &amp; type, objectives &amp; policies, asset allocation, where it invests, strategy, fundamental attributes, benchmark, managers, restrictions, performance",
        "Units and offer","Fees &amp; expenses","Rights of unitholders","General unitholder info","Penalties, litigation"))
    sub("Using the SID — where to find what", 4,
      T(["Question","Where"],
        [["Eligible / ineligible investors","NFO &amp; Ongoing Offer Details"],
         ["Risk-o-meter + suitability statement","Front page of SID"],
         ["Risks","Risk section: standard risks (no guarantee; sponsor not liable beyond contribution; past performance not indicative) + specific (credit, interest rate, liquidity, pre-payment, reinvestment; equity volatility; unlisted liquidity; foreign, securitised, derivatives) + mitigation"],
         ["Type, objective (primary/secondary), asset allocation, instruments, restrictions, strategy, investment management structure","'Information about the Scheme' (objective also in Highlights)"],
         ["When to buy","Cover page: open-ended (NFO + continuous at NAV), close-ended (only NFO), interval (NFO + transaction periods)"],
         ["How to apply","SAI + SID together"],["Purchase/redemption price","NFO &amp; Ongoing Offer (applicable NAV, cut-off, amount)"],
         ["Loads","Load structure segment"],["Min purchase, min balance, min redemption","Highlights + Ongoing Offer"],
         ["Plans (regular/direct) &amp; options","Highlights + Ongoing Offer"],["Modes of transaction","SAI 'How to Apply' (also SID)"],
         ["Liquidity &amp; redemption","Highlights"],["Fees, expenses (with examples)","SID"],
         ["SIP, STP, triggers, switch, IDCW transfer","SID special products"],["Periodic info, performance vs benchmark","SID"],
         ["NAV computation, tax (brief)","SID"]]) +
      TRAP("SEBI has WITHDRAWN the transaction charges framework (Aug 2025 circular)."))
    sub("Fundamental attributes (Box 5.1)", 5,
      T(["Attribute","Includes"],
        [["(i) Type of scheme","Open/close/interval; sectoral, equity, balanced, income, index, other"],
         ["(ii) Investment objective","Main objective (growth/income/both); tentative portfolio break-up with min–max allocation (may alter short-term on defensive considerations)"],
         ["(iii) Terms of issue","Liquidity (listing, repurchase, redemption); aggregate fees &amp; expenses; any safety net or guarantee"]]) +
      KV([("Regulation 22(9)(c)","Trustees ensure no change in fundamental attributes / trust / fees &amp; expenses / other modification unless: (a) written communication (email/SMS ok) to each unitholder (b) details on AMC website (c) exit option at prevailing NAV without exit load")]))
    sub("Statement of Additional Information (SAI)", 4,
      T(["Content","Description"],
        [["Constituents","Sponsors, AMC, trustee company, service providers (custodian, RTA, statutory auditor, fund accountant if outsourced, collecting bankers): experience, condensed financials (schemes of last 3 FYs), key personnel, rights &amp; obligations"],
         ["How to apply","Guidance"],["Rights of unitholders","Beneficial ownership, service timelines, information, exit on changes"],
         ["Investment valuation norms","SEBI-standardised valuation"],["Tax, legal &amp; general","Nominations, transfer/transmission, minors, pledge/lien, taxation"],
         ["Investor grievance","How to register"]]) +
      K("Downloadable on MF website; right to a printed copy; all SAIs on AMFI website"))
    sub("Key Information Memorandum (KIM)", 5,
      KV([("Why","Circulating SID/SAI with forms is costly → KIM mandatorily circulated with application form"),
          ("What","Summary of SID and SAI"),("Rule","Every application form accompanied by KIM")]) +
      K("AMC, MF, trustee, fund manager &amp; scheme names","Issue open/close/re-opening dates","Objective","Asset allocation","Risk profile (risk to principal, horizon, securities)","Plans &amp; options","Benchmark","Dividend policy","Performance vs benchmark: 1, 3, 5 yrs, since inception","Expenses","Grievance info"))
    sub("Addendum", 4,
      K("Interim changes between updates","Part of scheme documents; must accompany KIM"))
    sub("Updating SID, SAI, KIM", 5,
      T(["Document","Rule"],
        [["SID (open-ended &amp; interval)","First: within 6 months from end of the half-year (H1/H2) of launch, data as of previous month-end. Then: within <b>1 month</b> from end of each half-year, data as of end-September / end-March"],
         ["SAI","Regular update by end of <b>3 months</b> of every FY; material changes ongoing, uploaded on MF &amp; AMFI websites"],
         ["KIM","At least once every <b>half-year</b>, within 1 month of half-year end (Sept/March data); filed with SEBI electronically"]]) +
      T(["Change","Procedure"],
        [["Fundamental attribute (Reg 22(9)(c))","Addendum on website immediately · SID revised after exit window (≥ 30 days from notice) · public notice in one English national daily + one regional-language paper (HO region)"],
         ["Other changes","Addendum on website immediately · circulated to distributors/brokers/ISCs to attach to KIM &amp; SID in stock · latest addendum part of KIM/SID (e.g. load change) · account statements continue to show load structure"]]))
    sub("Current value & daily NAV disclosure", 5,
      F("Current value of investment = Unit balance × Current NAV") +
      KV([("Daily NAV","End of each business day on AMC website + AMFI website (amfiindia.com/net-asset-value)"),
          ("Open-ended","NAV every business day, released to press"),
          ("Liquid &amp; overnight","NAV declared on <b>Sundays/holidays</b> too (accrual)"),
          ("Close-ended","NAV at least <b>once a week</b>"),
          ("Overseas schemes","Revised time limit (SEBI, Mar 2023)")]))
    sub("TER / Base Expense Ratio disclosure", 5,
      F("TER = Base Expense Ratio (BER) + Brokerage cost + Transaction cost + Statutory levies (incl. GST)") +
      T(["Requirement","Rule"],
        [["Daily disclosure","Scheme-wise, date-wise TER (all schemes except IDFs) in section 'Total Expense Ratio of Mutual Fund Schemes' on AMC + AMFI websites; downloadable, machine-readable; TER broken into components"],
         ["BER change notice","Email/SMS at least <b>3 working days</b> before; website section updated 3 working days ahead"],
         ["No prior notice","If BER change due only to AUM fluctuation, or a decrease due to regulation"],
         ["Governance","BER changes intimated to AMC Board (with rationale) and to trustees quarterly"],
         ["SID/KIM","All expenses identified; web link to TER of last 6 months, daily TER, factsheet; numerical illustration of TER impact for direct &amp; regular; separate regular/direct disclosures"],
         ["Half-yearly CAS","Average TER % with breakup: investment &amp; advisory fees · distributor commission · other expenses"],
         ["Annual accounts","Any single expense item &gt; <b>10%</b> of total expenditure disclosed separately"],
         ["Abridged annual report","TER as % of average AUM, plan-wise"]]))
    sub("Scheme dashboard", 3,
      K("Scheme name","Classification/category","Open/close-ended","Objective","Fund manager","Benchmark (+ additional)","Exit load &amp; lock-in","Plans &amp; options","Min investment","Month-end AUM","TER","Inception date","Month-end portfolio","Performance"))
    sub("Risk-o-meter", 5,
      T(["Level","Colour"],
        [["Low","Irish Green #08A04B"],["Low to Moderate","Chartreuse #7FFF00"],["Moderate","Neon Yellow #FFFF33"],
         ["Moderately High","Caramel #C68E17"],["High","Dark Orange #FF8C00"],["Very High","Red #F70D1A"]]) +
      L("Pictorial risk to principal + written statement below","Risk value per SEBI parameters; evaluated <b>monthly</b>",
        "Change → notice-cum-addendum + email/SMS to unitholders","Show risk-o-meter of scheme AND benchmark when disclosing performance",
        "First step only — not the only factor; consult MFD/RIA (product labelling circular 18 Mar 2013)") +
      T(["Commodity annualised volatility (quarterly, 15 yrs of benchmark prices)","Risk value"],
        [["&lt; 10%","3 (Moderate)"],["10–15%","4 (Moderately High)"],["15–20%","5 (High)"],["&gt; 20%","6 (Very High)"]]))
    sub("Risk-Band for SIFs", 5,
      KV([("Why","SIFs riskier than all MF schemes → separate meter to avoid confusion"),
          ("Levels","5: level 1 (lowest) → level 5 (highest)"),
          ("Assigned","At NFO; change → notice-cum-addendum + email/SMS"),
          ("Evaluation","Monthly; disclosed on website within 10 days of month close"),
          ("Annual","Risk level as on 31 March + number of changes in the year, on AMC &amp; AMFI websites")]))
    sub("Portfolio disclosure", 5,
      T(["Item","Rule"],
        [["All schemes","As on last day of month / half-year, with ISIN, on AMC + AMFI websites within <b>10 days</b>; downloadable spreadsheet"],
         ["Debt schemes","<b>Fortnightly</b>, within <b>5 days</b> of every fortnight; plus yield of each instrument"],
         ["Email","Monthly &amp; half-yearly portfolio statements emailed within 10 days to registered emails"],
         ["SIFs","Last day of every <b>alternate month</b>: May, Jul, Sep, Nov, Jan, Mar; within 10 days; all securities with ISIN"],
         ["SIF scenario analysis","In Investment Strategy Information Document (<b>ISID</b>) — expected loss from market moves"]]))
    sub("Financial results & annual reports", 4,
      T(["Item","Rule"],
        [["Half-yearly results","Unaudited, on website within <b>1 month</b> of half-year end (31 Mar, 30 Sep); SEBI format; email/SMS to unitholders on availability"],
         ["Annual report","Full or abridged on AMC + AMFI websites; emailed within <b>4 months</b> of FY end (31 Mar); physical copy on request if no email; ad in all-India editions of ≥ 2 dailies (one English, one Hindi); functional link to full scheme-wise annual reports"],
         ["Change in control of AMC","Draft letter/email + draft newspaper ad filed with SEBI while seeking approval"]]))
    sub("Fund factsheet (non-mandatory)", 4,
      KV([("Status","Not a regulatory requirement; voluntary monthly market practice; part of AMFI best practices; SEBI disclosure rules apply (marketing document)"),
          ("Contents","Inception date, AUM, NAV, benchmark, style box, performance vs benchmark, SIP returns, sector &amp; security allocation (some only top 10), derivatives exposure"),
          ("Equity measures","PE, standard deviation, beta, Sharpe ratio, <b>information ratio</b> (mandatory — SEBI circular 17 Jan 2025)"),
          ("Debt measures","Rating profile, average maturity, duration"),
          ("Investment details","Min amount, plans/options, loads, expenses, systematic facilities")]) +
      TRAP("MFs may use derivatives for hedging but cannot take open (naked) derivative positions — as stated in the factsheet section."))
