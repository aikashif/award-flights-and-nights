from summary_lib import *

def add(chap, sub):
    chap(7, "NAV, Total Expense Ratio & Pricing of Units", "5", 5)
    sub("Why fair valuation", 3,
      K("Ownership changes as investors enter/exit → each must get a fair price","Valuation per <b>Seventh Schedule</b> of SEBI MF Regulations 2026",
        "Aims: fair treatment of existing, entering and exiting investors; address mispricing; reduce short-term debt schemes' vulnerability to redemption pressure"))
    sub("10 principles of fair valuation", 5,
      T(["#","Principle"],
        [["1","Fair valuation = realisable value; good faith, true and fair, via policies &amp; procedures"],
         ["2","AMC Board-approved policies name methodology per security type; invest in a <b>new type</b> of security only after its valuation method is approved by AMC Board"],
         ["3","Consistent valuation; process for exceptional events when quotes are unreliable"],
         ["4","Periodic review; update Trustee &amp; AMC Boards; reviewed by <b>independent auditor at least once a FY</b>"],
         ["5","Policies address conflict of interest"],
         ["6","Disclose valuation policy in <b>SAI</b>, AMC/MF website and as SEBI specifies"],
         ["7","AMC responsible for true &amp; fair valuation and correct NAV; may deviate from policy to reach fair value — with reporting to both Boards and disclosure to investors"],
         ["8","Policies to detect and prevent incorrect valuation"],
         ["9","Document rationale (incl. inter-scheme transfers) for audit trail"],
         ["10","Debt &amp; money market: consider trades of same/similar security on all public platforms"]]) +
      TRAP("If Fair Valuation Principles conflict with SEBI Valuation Guidelines, the PRINCIPLES prevail.") +
      K("Valuation per SEBI &amp; AMFI guidelines for traded, non-traded and thinly traded securities, gold &amp; silver; adjust for illiquidity"))
    sub("Net assets — worked example", 5,
      T(["Liabilities side","₹ cr"],
        [["Unit capital (20 cr units × ₹10)","200"],["Profits: 8 income − 4 paid − 1 payable","3"],["Capital appreciation (10% of 140)","14"],
         ["<b>Unitholders' funds (net assets)</b>","<b>217</b>"],["Expenses payable","1"],["Scheme liabilities","218"]]) +
      T(["Assets side","₹ cr"],[["Investments at market (140 + 10%)","154"],["Bank &amp; money market (60 + 8 − 4)","64"],["Scheme assets","218"]]) +
      F("NAV = Net assets ÷ units = 217 ÷ 20 = ₹10.85\nAlt: (Total assets − liabilities other than to unitholders) ÷ units = (218 − 1) ÷ 20 = ₹10.85") +
      K("Net assets = original money + booked profits + appreciation","Rise with market price even if unsold","<b>Accrual principle</b>: expenses and income of the period counted whether paid/received or not",
        "Current liabilities: payables for securities bought; borrowings ≤ 6 months for liquidity; intra-day borrowing returned same day"))
    sub("NAV drivers & profitability metric", 5,
      F("Profit = Interest + Dividend + Realised gains + Valuation gains − Realised losses − Valuation losses − Scheme expenses\nHigher income/gains → higher NAV · Lower expenses → higher NAV"))
    sub("NAV worked examples (workbook)", 5,
      F("Ex 1: (150 stocks + 67 bonds + 2.36 MM + 1.09 dividend accrued + 2.68 interest accrued − 0.36 fees payable) ÷ 1.90 cr units\n     = 222.77 ÷ 1.90 = ₹117.25\nEx 2: (230 stocks + 5 MM + 2.39 dividend accrued + 2.34 receivable on sale − 7.5 payable on purchase − 0.41 fees) ÷ 2.65\n     = 231.82 ÷ 2.65 = ₹87.48\nNAV = (Investments + income accrued + current assets − current liabilities − accrued expenses) ÷ units"))
    sub("Mark to market — why", 5,
      KV([("Meaning","Value each security at current market value"),
          ("Example","Shares bought at ₹15 now worth ₹50 — valuing at ₹15 meaningless")]) +
      T(["Case (NAV ₹15, 10,000 units, net assets ₹1,50,000)","Result"],
        [["Issue 100 units at face value ₹10","Net assets 1,51,000 ÷ 10,100 = NAV <b>₹14.95</b> (falls for all)"],
         ["Redeem 100 units at ₹10","1,49,000 ÷ 9,900 = NAV <b>₹15.05</b> (rises for rest)"]]) +
      K("MTM → fair buy/sell prices; helps judge fund manager performance"))
    sub("Expenses: rules", 4,
      L("All expenses clearly identified and paid from the scheme, within base expense limits + brokerage + transaction cost + statutory levies",
        "Excess over base limits borne by AMC, trustees or sponsors",
        "Investment &amp; advisory fees charged by AMC — disclosed in SID",
        "AMC pays distribution commission as SEBI specifies"))
    sub("Recurring expense heads (a)–(o)", 4,
      K("(a) Marketing &amp; selling incl. distribution commission","(b) Brokerage","(c) Registrar services","(d) Trustee fees","(e) Audit fees","(f) Custodian fees",
        "(g) Investor communication","(h) Fund transfer between locations","(i) Account statements, IDCW/redemption cheques &amp; warrants","(j) Insurance premium",
        "(k) Winding-up costs","(l) Statutory advertisements","(m) Storage &amp; handling of commodities / gold / silver","(n) Listing fees","(o) Others approved by SEBI"))
    sub("TER limits (2026)", 5,
      KV([("Equity-oriented (for TER)","Scheme (other than index fund/ETF) investing ≥ 65% of net assets in equity per SID"),
          ("TER covers","Investment &amp; advisory fee; excludes issue/redemption expenses")]) +
      T(["Open-ended: daily net assets","Equity-oriented","Other than equity"],
        [["First ₹500 cr","<b>2.10%</b>","<b>1.85%</b>"],["Next ₹250 cr","1.90%","1.65%"],["Next ₹1,250 cr","1.60%","1.40%"],
         ["Next ₹3,000 cr","1.50%","1.25%"],["Next ₹5,000 cr","1.40%","1.15%"],
         ["Next ₹40,000 cr","−0.05% per ₹5,000 cr (or part)","−0.05% per ₹5,000 cr"],["Balance","0.95%","0.70%"]]) +
      T(["Scheme type","TER cap"],
        [["Index fund / ETF (incl. advisory fee)","<b>0.90%</b>"],
         ["FoF investing in liquid, index, ETF","0.90% (incl. weighted avg TER of underlying)"],
         ["FoF ≥ 65% in equity-oriented schemes","2.10%"],["Other FoF","1.85%"],
         ["Close-ended / interval — equity-oriented","1.00%"],["Close-ended / interval — others","0.80%"]]) +
      K("FoF's own TER over underlying ≤ 2 × weighted average TER of underlying (within ceilings)"))
    sub("Charges over and above base TER", 5,
      T(["Item","Limit"],
        [["Brokerage &amp; transaction cost — cash market","Up to <b>0.06%</b> of trade value"],
         ["— derivatives","Up to <b>0.02%</b> of trade value"],
         ["Total charged to investors","Base expense + brokerage + transaction cost + statutory levies"],
         ["Nothing else","Except base expense ratio, brokerage, transaction cost, statutory levy and exit load"],
         ["Additional commission","For MFDs onboarding new investors (B-30, women) as SEBI specifies"]]) +
      K("Daily scheme-wise TER on AMC + AMFI websites under 'Total Expense Ratio of Mutual Fund Schemes'"))
    sub("Perpetual (AT-1 / Tier 2) bonds", 4,
      K("Bank-issued perpetual bonds that absorb losses before equity / convert on trigger","SEBI exposure limits apply","AT-1 bonds valued on <b>Yield to Call</b> basis (SEBI Aug 2024)"))
    sub("IDCW & distributable reserves", 5,
      L("Accrued income/expense = only a matter of time; valuation gains may never be realised",
        "IDCW only from <b>distributable reserves</b>: all accrual profits count; <b>valuation gains ignored</b>; <b>valuation losses adjusted</b>; part of new-unit sale price attributable to valuation gains excluded",
        "Trustees decide quantum and record date; up to monthly frequency may be delegated to AMC officials, ratified at next Board meeting",
        "Record date = cut-off for eligibility; NAV adjusted at end of record date",
        "AMC issues public notice within <b>1 day</b> of trustees' decision; record date = <b>5 calendar days</b> from notice; notice states NAV will fall by payout + statutory levy",
        "Delay → interest from record date",
        "No notice needed for liquid/debt schemes with daily-to-monthly IDCW (disclosed in SID); listed schemes follow listing agreement",
        "No assurance of rate, quantum or regularity",
        "Realised gains in sale price → <b>equalisation reserve</b>, usable for IDCW; disclose how much is NAV appreciation vs capital distribution"))
    sub("Entry & exit load", 5,
      F("Old entry load: NAV 11 + 1% → sale price ₹11.11 (banned now → sale price = NAV, subject to stamp duty)\nExit load: NAV 11 − 1% → repurchase price ₹10.89\n₹25,000 at NAV 43.21 → 578.570 units") +
      L("Graded load (e.g. 3% year 1, 2% year 2) encourages longer holding",
        "Earlier: different loads by investor class; loads funded AMC selling expenses",
        "Now: no distinction by subscription amount; new/higher load only for prospective investments; parity at portfolio level",
        "<b>No exit load on bonus units and IDCW-reinvestment units</b>",
        "Exit load credited back to the scheme immediately"))
    sub("Accounting & reporting requirements", 4,
      L("Scheme accounts distinct from AMC; different auditors",
        "Norms on when interest, dividend, bonus, rights are booked",
        "NAV to <b>4 decimals</b>: index funds, liquid funds, other debt funds",
        "NAV to <b>at least 2 decimals</b>: equity and balanced funds",
        "Units may be held in fractions; exchanges may restrict to whole units"))
    sub("Segregated portfolio: NAV, TER, pricing", 4,
      L("No investment &amp; advisory fee on segregated portfolio; other TER pro-rata only upon recovery",
        "NAV of segregated portfolio declared <b>daily</b>",
        "Disclosed in scheme documents, monthly &amp; half-yearly portfolios, annual report") +
      K("Credit event basis: SEBI circular 28 Dec 2018","Unrated debt of issuer with no rated debt: allowed (7 Nov 2019) only on actual default of interest or principal","Detail in Ch 10"))
