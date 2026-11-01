"""MF quiz part B: Ch7 NAV/TER/pricing, Ch4 Regulatory framework, Ch5 Scheme info, Ch10 Risk & return."""

def add(Q, inr, num):
    # ============================================================ CH 7 NAV, TER, PRICING
    C = 7
    S = lambda *a: Q(C, "S", *a)
    H = lambda *a: Q(C, "H", *a)
    for A, L, U in [(110, 10, 5), (252, 12, 16), (75.5, 3.5, 4.8)]:
        nav = (A - L) / U
        S(f"A scheme has assets of ₹{A} crore, liabilities of ₹{L} crore and {U} crore units outstanding. What is its NAV?",
          f"₹{nav:.2f}", f"NAV = (Assets − Liabilities) ÷ Units = ({A} − {L}) ÷ {U} = ₹{nav:.2f}.",
          (f"₹{A/U:.2f}", "You forgot to subtract liabilities."),
          (f"₹{(A+L)/U:.2f}", "Liabilities are subtracted, not added."),
          (f"₹{U/(A-L)*10:.2f}", "Formula inverted."))
    for nav, load in [(50, 1), (24.80, 0.5), (132.40, 2)]:
        rp = nav * (1 - load/100)
        S(f"NAV is ₹{nav:.2f} and the exit load is {load}%. What is the repurchase (redemption) price?",
          f"₹{rp:.2f}", f"Repurchase price = NAV × (1 − exit load) = {nav:.2f} × {1-load/100:.3f} = ₹{rp:.2f}.",
          (f"₹{nav*(1+load/100):.2f}", "Load is deducted on exit, not added."),
          (f"₹{nav:.2f}", "You ignored the exit load."),
          (f"₹{nav-load:.2f}", "Load is a %, not rupees."))
    S("Entry load on mutual fund schemes was abolished in:",
      "August 2009", "SEBI banned entry loads from 1 Aug 2009.",
      ("April 2020", "That's when DDT ended."), ("October 2018", "That's when upfront commission was banned."), ("It still exists", "It's abolished."))
    S("Exit load collected by a scheme goes to:",
      "The scheme (credited back to it)", "Exit load is credited to the scheme, benefiting remaining investors.",
      ("The AMC as income", "Not since 2012."), ("The distributor", "No."), ("SEBI", "No."))
    S("The sale price of units in an open-ended scheme (ongoing purchase) is:",
      "The applicable NAV", "No entry load, so sale price = NAV.",
      ("NAV plus 2.25%", "No entry load."), ("Face value ₹10", "Only at NFO."), ("NAV minus exit load", "That's repurchase price."))
    S("Who bears the NFO expenses of a new scheme?",
      "The AMC", "NFO expenses are borne by the AMC, not the scheme.",
      ("The scheme's investors", "Not allowed."), ("The distributor", "No."), ("SEBI", "No."))
    S("Listed equity shares held by a scheme are valued at:",
      "The closing price on the principal stock exchange", "Traded equity is marked to the closing price.",
      ("Purchase cost", "Mark-to-market applies."), ("Face value", "No."), ("The fund manager's estimate", "Only for non-traded securities, under policy."))
    S("Debt and money market securities in a scheme are valued:",
      "At prices provided by valuation agencies (fully marked to market)", "Debt valuation uses agency prices; amortisation was removed.",
      ("At cost, amortised", "Amortisation no longer used."), ("At face value", "No."), ("Using the last coupon", "No."))
    S("Total Expense Ratio (TER) is charged:",
      "As a percentage of daily net assets, accrued daily in the NAV", "TER is accrued daily; NAV is net of expenses.",
      ("Once a year from investors' bank accounts", "No."), ("Only at redemption", "No."), ("Only in NFO", "No."))
    S("Why is the direct plan NAV higher than the regular plan NAV of the same scheme?",
      "Direct plan has a lower TER because no distributor commission is paid", "Same portfolio, lower cost → higher NAV.",
      ("Direct plan holds better stocks", "Same portfolio."), ("Regular plan pays exit load daily", "No."), ("Direct plans are older", "No."))
    S("The maximum TER for an index fund or ETF is:",
      "1.00% of daily net assets", "Index funds/ETFs: TER cap 1%.",
      ("2.25%", "Equity first slab."), ("2.00%", "Debt first slab."), ("0.10%", "Too low as a cap."))
    S("For an equity-oriented scheme, the TER cap on the first ₹500 crore of daily net assets is:",
      "2.25%", "Equity first slab: 2.25%. Debt: 2.00%.",
      ("2.00%", "That's debt."), ("1.00%", "Index/ETF."), ("2.50%", "Older cap."))
    S("Stamp duty on mutual fund purchases is:",
      "0.005% of the purchase amount", "Since 1 July 2020; applies to purchases, switch-ins and IDCW reinvestment.",
      ("0.001% on redemption", "That's STT on equity fund redemption."), ("0.1%", "Too high."), ("Nil", "It applies."))
    S("STT on redemption of equity-oriented fund units is:",
      "0.001%, paid by the seller", "Equity fund redemption STT 0.001%.",
      ("0.005%", "That's stamp duty."), ("0.1%", "Too high."), ("Nil", "It applies."))
    S("After an IDCW of ₹2 per unit, the NAV of the scheme:",
      "Falls by about ₹2 per unit", "IDCW is paid from NAV; investor's wealth is unchanged before tax.",
      ("Rises by ₹2", "No."), ("Stays the same", "It falls by the payout."), ("Falls by ₹10", "No."))
    S("AUM of a scheme equals:",
      "NAV × units outstanding", "AUM = total market value of net assets.",
      ("NAV ÷ units", "No."), ("Face value × units", "No."), ("Units ÷ NAV", "No."))
    # harder
    for nav, idcw, units in [(15.00, 1.00, 1000), (42.50, 2.50, 400)]:
        H(f"An investor holds {units} units at NAV ₹{nav:.2f}. An IDCW of ₹{idcw:.2f} per unit is paid. Ignoring tax, what is the investor's total wealth just after (units + cash)?",
          inr(units*nav, 0), f"Units now worth {units} × {nav-idcw:.2f} = {inr(units*(nav-idcw))}, cash {inr(units*idcw)}. Total = {inr(units*nav)} — unchanged.",
          (inr(units*(nav+idcw)), "IDCW doesn't add wealth; NAV falls."),
          (inr(units*(nav-idcw)), "You forgot the cash received."),
          (inr(units*idcw), "That's only the cash."))
    H("A scheme has daily net assets of ₹800 crore (equity). Under the slab structure, the TER cap is applied as:",
      "2.25% on the first ₹500 crore and 2.00% on the next ₹300 crore", "Slabs apply incrementally, like tax brackets.",
      ("2.25% on the full ₹800 crore", "Slabs reduce the rate above ₹500 cr."), ("2.00% on the full ₹800 crore", "First ₹500 cr gets 2.25%."), ("1.75% on all", "That's a later slab."))
    H("Investor A buys an equity fund on day 1. Exit load: 1% if redeemed within 365 days. He redeems ₹1,00,000 worth on day 200. How much load is deducted and where does it go?",
      "₹1,000, credited to the scheme", "1% × ₹1,00,000 = ₹1,000; exit load goes back to the scheme.",
      ("₹1,000, paid to the AMC", "Credited to scheme."), ("Nil, as load applies only on NFO units", "Load applies within 365 days."), ("₹1,000, paid to the distributor", "No."))
    H("Why is 'equalisation reserve' used in mutual fund accounting?",
      "So that distributable income per unit isn't diluted when new investors buy in", "Part of sale price goes to equalisation reserve to keep income per unit fair.",
      ("To pay exit loads", "No."), ("To meet NFO expenses", "AMC bears those."), ("To pay SEBI fees", "No."))
    H("Which of these is NOT charged within the TER limit (it's over and above)?",
      "GST on investment management fees", "GST on management fee is allowed over and above TER limits.",
      ("Distribution commission", "Within TER."), ("Audit fees", "Within TER."), ("RTA fees", "Within TER."))
    H("A scheme's NAV moves from ₹20.00 to ₹20.05 in a day with no market movement. Most likely reason?",
      "Accrued income (interest/dividends) net of daily expenses", "Daily accrual of income less expenses changes NAV.",
      ("New investors bought units", "Purchases at NAV don't change NAV."), ("Redemptions", "Redemptions at NAV don't change NAV (except exit load)."), ("NAV is random", "No."))
    H("Why do purchases and redemptions at NAV NOT change the NAV of an open-ended scheme?",
      "Units are issued/cancelled at NAV, so assets and units change in the same proportion", "Assets and units move together.",
      ("Because SEBI fixes NAV", "Market sets it."), ("Because units have face value", "Irrelevant."), ("Because AMC absorbs flows", "No."))
    H("A liquid fund investor redeems on day 2. NAV ₹3,000; graded exit load 0.0065%. Redemption of 100 units. Load deducted?",
      "₹19.50", "100 × 3,000 × 0.0065% = ₹19.50.",
      ("₹195", "Off by 10."), ("₹1.95", "Off by 10."), ("Nil", "Graded load applies on day 2."))
    H("Which statement about swing pricing is correct?",
      "In market dislocation, NAV of open-ended debt schemes is adjusted so exiting investors bear liquidity costs", "Protects remaining investors.",
      ("It applies to equity funds daily", "Debt schemes in stress."), ("It raises NAV for redeeming investors", "Lowers effective exit NAV."), ("It is optional for investors to choose", "No."))
    H("An investor invests ₹1,00,000 in a fund (stamp duty applies). How many rupees actually buy units?",
      "₹99,995", "Stamp duty 0.005% = ₹5 → ₹99,995 invested.",
      ("₹1,00,000", "Stamp duty is deducted."), ("₹99,500", "That's 0.5%."), ("₹99,950", "That's 0.05%."))
    H("Brokerage paid by schemes on cash market equity trades is capped (beyond which it must come from TER) at about:",
      "0.12% of trade value", "Cash market brokerage cap 0.12%; derivatives 0.05%.",
      ("0.05%", "Derivatives."), ("1%", "Too high."), ("2.25%", "That's a TER slab."))
    H("Two plans of the same scheme: regular TER 1.8%, direct TER 0.8%. Ignoring compounding, over 5 years how much more will the direct plan earn?",
      "About 5 percentage points", "1% a year × 5 years ≈ 5% (more with compounding).",
      ("About 1 percentage point", "That's one year."), ("No difference", "TER difference compounds."), ("About 10 percentage points", "Too high."))

    # ============================================================ CH 4 LEGAL & REGULATORY FRAMEWORK
    C = 4
    S = lambda *a: Q(C, "S", *a)
    H = lambda *a: Q(C, "H", *a)
    S("Mutual funds in India are mainly governed by:",
      "SEBI (Mutual Funds) Regulations, 1996", "Primary regulation for MFs.",
      ("Companies Act, 2013", "Applies to AMC as company, not MF rules."), ("RBI Act, 1934", "No."), ("Indian Contract Act", "No."))
    S("A scheme can invest at most what % of its NAV in the equity shares of a single company (non-index, non-sector fund)?",
      "10%", "Single-company equity cap is 10% of NAV.",
      ("25%", "Too high."), ("5%", "Too low."), ("100%", "No."))
    S("All schemes of an AMC together can hold at most what % of a company's paid-up voting capital?",
      "10%", "AMC-level cap: 10% of voting rights.",
      ("25%", "Too high."), ("49%", "No."), ("5%", "No."))
    S("Mutual fund schemes may borrow only to:",
      "Meet temporary liquidity needs for redemption or IDCW (max 20% of net assets, 6 months)", "Borrowing is restricted.",
      ("Buy more securities", "Not allowed."), ("Pay AMC fees", "No."), ("Launch an NFO", "No."))
    S("Which right does a mutual fund unitholder have?",
      "Receive redemption proceeds within the set timeline, with interest if delayed", "Investor right.",
      ("A guaranteed return", "No guarantee."), ("Choose the fund manager", "No."), ("Sue for poor performance", "Not a right."))
    S("When fundamental attributes of a scheme change, investors get:",
      "A 30-day window to exit at NAV without exit load", "Exit option without load.",
      ("Compensation for losses", "No."), ("Free units", "No."), ("Nothing", "They get an exit window."))
    S("An investor's first point of complaint about a mutual fund service issue is:",
      "The AMC / RTA (investor relations officer)", "Start with AMC; escalate to SCORES, then ODR.",
      ("Supreme Court", "Last resort."), ("AMFI", "Not the investor grievance forum."), ("Stock exchange", "No."))
    S("SEBI's online grievance redressal system is called:",
      "SCORES", "SEBI Complaints Redress System.",
      ("NACH", "Payment mandate system."), ("NDS-OM", "G-sec trading."), ("MFU", "Transaction platform."))
    S("If SCORES doesn't resolve a complaint, the investor can go to:",
      "SMART ODR (online dispute resolution)", "ODR: conciliation, then arbitration.",
      ("AMFI tribunal", "No such thing."), ("RBI ombudsman", "Not for MFs."), ("Nothing further", "ODR is available."))
    S("The standard warning in mutual fund ads is:",
      "'Mutual Fund investments are subject to market risks, read all scheme related documents carefully.'", "Mandatory warning.",
      ("'Returns are guaranteed by SEBI'", "False."), ("'Past performance guarantees future returns'", "False."), ("'Invest at your own risk'", "Not the prescribed text."))
    S("The AMFI Code of Conduct for intermediaries requires distributors to:",
      "Disclose commissions and recommend suitable products", "Suitability + disclosure.",
      ("Guarantee returns", "Not allowed."), ("Rebate commission to clients", "Not allowed."), ("Churn portfolios", "Prohibited."))
    S("Rebating part of commission to investors by a distributor is:",
      "Not allowed", "Rebating is prohibited.",
      ("Allowed up to 50%", "No."), ("Allowed for large investors", "No."), ("Mandatory", "No."))
    S("Churning by a distributor means:",
      "Frequent switching of clients' investments to earn more commission", "Prohibited.",
      ("Rebalancing as per plan", "Legitimate."), ("SIP top-up", "Legitimate."), ("Nomination update", "No."))
    S("A segregated portfolio (side pocket) is created when:",
      "A debt security in the portfolio suffers a credit event (e.g. downgrade below investment grade)", "Bad paper separated from main portfolio.",
      ("NAV rises sharply", "No."), ("A new fund manager joins", "No."), ("AUM crosses ₹1,000 crore", "No."))
    S("Can an individual act as both mutual fund distributor and SEBI-registered investment adviser?",
      "No — SEBI requires separation of the two activities", "IA Regulations 2020 separation.",
      ("Yes, freely", "Not allowed."), ("Yes, with AMFI approval", "No."), ("Only for direct plans", "No."))
    S("Mutual funds can invest in derivatives up to (gross exposure, excluding hedging):",
      "100% of net assets", "Gross derivative exposure cap.",
      ("25%", "That's the SIF short limit."), ("10%", "No."), ("200%", "No."))
    S("Inter-scheme investment (one scheme in another of the same AMC) is limited to:",
      "5% of the investing scheme's NAV, with no management fee", "Limits and no double fee.",
      ("25%", "Too high."), ("No limit", "There is a limit."), ("Not allowed at all", "Allowed within limit."))
    S("Under the investor rights framework, unitholders can wind up a scheme or change the AMC if:",
      "75% of unitholders pass a resolution", "Special majority.",
      ("51% vote", "Needs 75%."), ("Any one investor asks", "No."), ("Only SEBI decides", "Investors also have the power."))
    # harder
    H("The minimum investment in a Specialized Investment Fund (SIF) per investor (non-accredited) is:",
      "₹10 lakh across all SIF strategies of the AMC", "SIF threshold, PAN level.",
      ("₹50 lakh", "That's PMS."), ("₹1 crore", "That's AIF."), ("₹5,000", "Regular MF."))
    H("A SIF can take unhedged short exposure through derivatives up to:",
      "25% of net assets", "SIF short cap.",
      ("100%", "Gross derivatives cap for MFs."), ("10%", "No."), ("50%", "No."))
    H("Which risk-labelling system do SIFs use?",
      "Risk band levels 1 to 5", "SIF uses a risk band, not the 6-level riskometer.",
      ("6-level riskometer", "That's for MF schemes."), ("PRC matrix only", "Debt MF."), ("Credit rating", "No."))
    H("An AMC wants to launch SIFs through the regular route. Which is part of its eligibility?",
      "Operations of at least 3 years with average AUM of at least ₹10,000 crore in the last 3 years", "Regular route criteria.",
      ("AUM of ₹100 crore", "Too low."), ("Only foreign AMCs", "No."), ("No conditions", "There are conditions."))
    H("A debt scheme rated AA holding: what's the single-issuer limit (without trustee extension)?",
      "8% of NAV", "AAA 10%, AA 8%, A & below 6%; +2% with trustee approval.",
      ("10%", "That's AAA."), ("6%", "That's A and below."), ("15%", "No."))
    H("Which body is responsible for AMC compliance oversight at the fund level, protecting investors?",
      "Trustees", "Trustees supervise the AMC.",
      ("Distributors", "No."), ("RTA", "No."), ("Custodian", "Holds assets only."))
    H("A distributor shows a client a fund's 1-year return of 45% without benchmark or other periods. What's wrong?",
      "Performance must be shown with benchmark and standard periods, not cherry-picked", "Advertising/performance norms.",
      ("Nothing; high returns can be highlighted alone", "Misleading."), ("Only 6-month returns are allowed", "No."), ("Returns can never be shown", "They can, with norms."))
    H("An AMC must do due diligence on a distributor who:",
      "Earns over ₹1 crore commission a year across the industry", "One of the due diligence triggers.",
      ("Has one client", "No."), ("Has ARN for 1 year", "No."), ("Sells only liquid funds", "No."))
    H("In a side-pocketed scheme, what happens to fresh subscriptions?",
      "Allowed only in the main portfolio; the segregated portfolio is closed to new money", "Segregated units are not available for subscription.",
      ("Allowed in both", "No."), ("All subscriptions stop permanently", "Main portfolio continues."), ("Only segregated portfolio is open", "No."))
    H("Which grievance escalation order is correct?",
      "AMC → SCORES → SMART ODR", "Escalation path.",
      ("SMART ODR → AMC → SCORES", "Wrong order."), ("AMFI → SEBI → AMC", "No."), ("Court → AMC → SCORES", "No."))
    H("A distributor uses the term 'Independent Financial Adviser' while earning commissions. Under SEBI rules this is:",
      "Not allowed — MFDs must not call themselves independent or advisers", "Use 'Mutual Fund Distributor'.",
      ("Allowed if ARN is valid", "No."), ("Allowed for corporate distributors", "No."), ("Required", "No."))
    H("Which is an investor's obligation rather than a right?",
      "Keeping KYC, contact and bank details updated", "Investor obligation.",
      ("Getting redemption on time", "Right."), ("Getting annual report", "Right."), ("Exit on attribute change", "Right."))

    # ============================================================ CH 5 SCHEME RELATED INFORMATION
    C = 5
    S = lambda *a: Q(C, "S", *a)
    H = lambda *a: Q(C, "H", *a)
    S("Which document contains scheme-specific details like objective, asset allocation and risks?",
      "Scheme Information Document (SID)", "SID is scheme-specific.",
      ("SAI", "Fund-house level."), ("KIM", "Abridged SID."), ("CAS", "Account statement."))
    S("Which document contains fund-house level information such as sponsor, AMC and trustee details?",
      "Statement of Additional Information (SAI)", "SAI is common to all schemes.",
      ("SID", "Scheme-level."), ("KIM", "Summary."), ("Factsheet", "Monthly data."))
    S("Which document must accompany every application form?",
      "Key Information Memorandum (KIM)", "KIM is the abridged SID with the form.",
      ("SAI", "Not attached."), ("Annual report", "No."), ("Trust deed", "No."))
    S("Together, which documents make up the full offer document?",
      "SID + SAI", "Offer document = SID and SAI.",
      ("KIM + CAS", "No."), ("Factsheet + KIM", "No."), ("Trust deed + IMA", "Constitutional documents."))
    S("Changes to an SID between updates are communicated through:",
      "An addendum", "Addendum carries interim changes.",
      ("A new NFO", "No."), ("A press release only", "No."), ("Nothing", "Must be disclosed."))
    S("Which is a fundamental attribute of a scheme?",
      "Investment objective", "Fundamental: type, objective, asset allocation, terms.",
      ("Fund manager's name", "Not fundamental."), ("Scheme logo", "No."), ("Distributor list", "No."))
    S("NAV of most schemes must be published on AMC and AMFI websites by:",
      "11 pm on every business day", "Daily NAV disclosure deadline.",
      ("9 am next day", "That's for some FoFs (10 am)."), ("End of week", "Daily."), ("End of month", "Daily."))
    S("Portfolio of all schemes must be disclosed at least:",
      "Monthly", "Monthly portfolio disclosure; debt schemes fortnightly.",
      ("Yearly", "Too infrequent."), ("Daily", "NAV is daily, not portfolio."), ("Quarterly only", "Monthly now."))
    S("Debt schemes must also disclose their portfolio:",
      "Fortnightly", "Debt schemes: fortnightly disclosure.",
      ("Weekly", "No."), ("Daily", "No."), ("Half-yearly only", "No."))
    S("NFO units of most schemes are offered at:",
      "₹10 face value", "Typical NFO price.",
      ("₹100", "No."), ("Current NAV of another scheme", "No."), ("₹1,000", "No."))
    S("An open-ended scheme must have at least how many investors?",
      "20 investors, with no single investor above 25%", "Minimum investor rule.",
      ("2 investors", "No."), ("100 investors", "No."), ("No minimum", "There is."))
    S("IDCW stands for:",
      "Income Distribution cum Capital Withdrawal", "Renamed from 'dividend' option in 2021.",
      ("Interest and Dividend Capital Wealth", "No."), ("Investor Dividend Cash Withdrawal", "No."), ("Income Deferred Capital Wealth", "No."))
    S("In the IDCW reinvestment option:",
      "IDCW is used to buy more units of the same scheme", "No cash payout.",
      ("IDCW is paid in cash", "That's payout."), ("IDCW goes to another scheme", "That's IDCW transfer."), ("NAV never falls", "NAV falls by IDCW."))
    S("Annual report of schemes must be published within:",
      "4 months from the end of the financial year", "Annual report timeline.",
      ("1 month", "That's half-yearly unaudited."), ("12 months", "No."), ("2 years", "No."))
    S("Close-ended schemes must be:",
      "Listed on a stock exchange", "Listing gives investors an exit.",
      ("Redeemable daily with the AMC", "That's open-ended."), ("Sold only to institutions", "No."), ("Unlisted", "No."))
    S("Interval schemes allow purchase and redemption:",
      "Only during specified transaction periods", "Interval schemes open periodically.",
      ("Every business day", "Open-ended."), ("Never", "No."), ("Only at maturity", "Close-ended."))
    S("Which is NOT normally in the KIM?",
      "Detailed legal information about the sponsor's other businesses", "That sits in SAI.",
      ("Investment objective", "In KIM."), ("Loads", "In KIM."), ("Riskometer", "In KIM."))
    S("TER of each scheme must be disclosed on the AMC website:",
      "Daily, with prior notice to investors before any increase", "TER disclosure.",
      ("Once in 5 years", "No."), ("Never", "No."), ("Only in NFO", "No."))
    # harder
    H("An AMC wants to change a scheme from 'large cap' to 'mid cap'. What must happen?",
      "Treated as a fundamental attribute change: trustee approval, SEBI comments, notice and 30-day exit at NAV without load", "Category change alters objective/allocation.",
      ("Just update the website", "Not enough."), ("No action needed", "Fundamental."), ("Investors must reinvest", "No."))
    H("Which change is NOT a fundamental attribute change?",
      "Change of fund manager", "Fund manager change is disclosed but not fundamental.",
      ("Change in asset allocation pattern", "Fundamental."), ("Change from open-ended to close-ended", "Fundamental."), ("Change in investment objective", "Fundamental."))
    H("A scheme's NFO raises money from 15 investors only. What follows?",
      "The scheme must meet the 20-investor rule within the allowed time or refund/close", "Minimum investor requirement.",
      ("It launches anyway", "Rule applies."), ("SEBI buys units", "No."), ("AMC invests to make up", "No."))
    H("One investor holds 30% of an open-ended scheme's corpus. Under the 20-25 rule:",
      "The excess over 25% must be brought down within the stipulated time (else redeemed)", "No single investor above 25%.",
      ("Allowed if KYC is complete", "No."), ("Allowed for 1 year", "No; specific rebalancing period."), ("SEBI must approve", "No."))
    H("Why does the SID carry a product label like 'This product is suitable for investors seeking...'?",
      "To help investors judge suitability with the riskometer", "Product labelling norms.",
      ("To guarantee returns", "No."), ("For tax purposes", "No."), ("Required by stock exchange only", "No."))
    H("Which disclosure helps investors see a debt scheme's maximum credit and interest rate risk?",
      "Potential Risk Class (PRC) matrix", "PRC shows max risk.",
      ("Riskometer only", "Shows current risk level."), ("Expense ratio", "Cost."), ("NAV", "No."))
    H("A scheme declares IDCW. An investor in the growth option of the same scheme:",
      "Gets nothing; growth option NAV is unaffected by the IDCW option's payout", "Options have separate NAVs.",
      ("Gets the same IDCW", "No."), ("Sees NAV fall too", "Separate NAV."), ("Is switched to IDCW", "No."))
    H("Which is the correct statement about the SAI?",
      "It is updated within 3 months of FY end and changes in between are via addendum", "SAI update norm.",
      ("It is updated daily", "No."), ("It is scheme-specific", "No, fund-house level."), ("It replaces the SID", "No."))
    H("When can an open-ended scheme reopen for continuous sale after the NFO?",
      "Within 5 business days of allotment", "Continuous offer starts quickly.",
      ("After 1 year", "No."), ("Only after SEBI approval again", "No."), ("Never", "It reopens."))
    H("An investor reads 'monthly portfolio disclosure within 10 days of month end'. This helps investors:",
      "Check the scheme is following its stated objective and allocation", "Transparency tool.",
      ("Guarantee returns", "No."), ("Avoid tax", "No."), ("Time their trades exactly", "No."))
    H("Which document would you check for the scheme's benchmark and fund manager's other schemes?",
      "SID", "SID covers benchmark and fund manager details.",
      ("SAI", "Fund-house info."), ("CAS", "No."), ("Trust deed", "No."))
    H("A scheme states 'NAV of FoF (overseas)'. By when is its NAV published?",
      "By 10 am the next business day", "Overseas FoF NAV timing exception.",
      ("By 11 pm same day", "Domestic schemes."), ("Weekly", "No."), ("Monthly", "No."))

    # ============================================================ CH 10 RISK, RETURN & PERFORMANCE
    C = 10
    S = lambda *a: Q(C, "S", *a)
    H = lambda *a: Q(C, "H", *a)
    for a, b in [(10, 15), (25, 22), (120, 150)]:
        r = (b - a) / a * 100
        S(f"NAV moves from ₹{a} to ₹{b}. What is the absolute return?",
          f"{r:+.1f}%", f"(End − Start) ÷ Start = ({b} − {a}) ÷ {a} = {r:+.1f}%.",
          (f"{(b-a)/b*100:+.1f}%", "You divided by the end NAV."),
          (f"{b-a:+.1f}%", "That's the rupee change, not %."),
          (f"{-r:+.1f}%", "Sign reversed."))
    for a, b, n in [(10, 15, 3), (100, 200, 5), (50, 72, 2)]:
        c = ((b / a) ** (1/n) - 1) * 100
        S(f"NAV grows from ₹{a} to ₹{b} in {n} years. What is the CAGR?",
          f"{c:.2f}%", f"CAGR = ({b}/{a})^(1/{n}) − 1 = {c:.2f}%.",
          (f"{(b/a-1)*100/n:.2f}%", "That's simple average, not compound."),
          (f"{(b/a-1)*100:.2f}%", "That's absolute return."),
          (f"{c*n:.2f}%", "Don't multiply CAGR by years."))
    for a, b, d in [(20, 21, 73), (50, 51.5, 146)]:
        ab = (b-a)/a*100; ann = ab*365/d
        S(f"NAV rises from ₹{a} to ₹{b} in {d} days. What is the annualised simple return?",
          f"{ann:.1f}%", f"Absolute {ab:.1f}% × 365/{d} = {ann:.1f}%.",
          (f"{ab:.1f}%", "Not annualised."), (f"{ab*d/365:.2f}%", "Inverted factor."), (f"{ann/2:.1f}%", "Wrong factor."))
    S("SEBI norms say returns for periods under 1 year must be shown as:",
      "Simple (absolute) returns", "<1 yr simple; ≥1 yr CAGR.",
      ("CAGR", "For ≥1 year."), ("XIRR only", "No."), ("Annualised compound", "No."))
    S("Which return measure is used for SIP investments?",
      "XIRR", "XIRR handles multiple cash flows on different dates.",
      ("Absolute return", "Ignores timing."), ("Point-to-point CAGR", "Single cash flow."), ("Current yield", "Bond measure."))
    S("Rolling returns are useful because they:",
      "Show consistency of returns across many start dates", "Reduce start/end date bias.",
      ("Guarantee future returns", "No."), ("Show only the best period", "Opposite."), ("Remove all risk", "No."))
    S("Standard deviation of a fund's returns measures:",
      "Total volatility", "SD = total risk.",
      ("Market risk only", "That's beta."), ("Credit risk", "Debt measure."), ("Expense ratio", "Cost."))
    S("A fund with beta 1.3 is expected to:",
      "Move about 30% more than the market", "β > 1 = more volatile than market.",
      ("Move 30% less than the market", "That's β 0.7."), ("Not move with the market", "β 0."), ("Earn 1.3% more", "Beta isn't return."))
    S("How many levels does the mutual fund riskometer have?",
      "6", "Low, Low to Moderate, Moderate, Moderately High, High, Very High.",
      ("5", "SIF risk band has 5."), ("3", "No."), ("10", "No."))
    S("The riskometer of a scheme is reviewed:",
      "Monthly", "Monthly evaluation based on portfolio.",
      ("Once at NFO only", "No."), ("Yearly", "No."), ("Daily", "No."))
    S("Which is the main risk in a long duration debt fund?",
      "Interest rate risk", "Long duration → big price change with rates.",
      ("Credit risk", "Depends on holdings; main is rate risk."), ("Currency risk", "No."), ("Equity market risk", "No."))
    S("Which is the main additional risk in an international fund?",
      "Currency risk", "INR vs foreign currency moves.",
      ("Credit risk", "Not main."), ("Interest rate risk", "Not main."), ("No additional risk", "There is."))
    S("In the PRC matrix, the safest cell is:",
      "A-I", "A = low credit risk; I = low interest rate risk.",
      ("C-III", "Riskiest."), ("B-II", "Moderate."), ("A-III", "High rate risk."))
    # harder
    H("A debt scheme has PRC class C-III. It means:",
      "Relatively high credit risk and relatively high interest rate risk", "C = high credit; III = high rate risk.",
      ("Lowest risk", "That's A-I."), ("Only high credit risk", "Also high rate risk."), ("Equity fund", "PRC is debt."))
    H("Interest rate class I in the PRC matrix means the scheme's Macaulay duration is at most:",
      "1 year", "Class I ≤ 1 yr; II ≤ 3 yrs; III any.",
      ("3 years", "Class II."), ("7 years", "No."), ("Any", "Class III."))
    H("A fund's portfolio has MD 4. Yields fall by 0.75%. Approximate NAV change?",
      "+3.0%", "−MD × Δy = −4 × (−0.75%) = +3%.",
      ("−3.0%", "Yields fell → NAV up."), ("+0.75%", "Ignores duration."), ("+4.75%", "Added, not multiplied."))
    H("A fund returns 18% with SD 20%; another returns 15% with SD 10%. On return per unit of total risk:",
      "The second fund is better", "18/20 = 0.9 vs 15/10 = 1.5 (ignoring Rf).",
      ("The first is better because return is higher", "Ignores risk."), ("Both equal", "No."), ("Can't compare", "Can."))
    H("Which risk is reduced by diversification?",
      "Unsystematic (company-specific) risk", "Systematic risk stays.",
      ("Systematic (market) risk", "Can't diversify away."), ("Inflation risk", "No."), ("Interest rate risk on all bonds", "No."))
    H("Reinvestment risk is highest when:",
      "Interest rates fall and coupons must be reinvested at lower rates", "Reinvestment risk.",
      ("Rates rise", "That helps reinvestment."), ("Bond is zero-coupon held to maturity", "No coupons to reinvest."), ("Equity markets fall", "Different risk."))
    H("Why can a liquid fund still lose value?",
      "Credit events in money market paper or sharp spikes in short-term rates", "Low but not zero risk.",
      ("It can't lose value", "It can."), ("Because of equity exposure", "No equity."), ("Because of currency risk", "No."))
    H("A small cap fund with very high AUM faces which specific risk?",
      "Liquidity risk when selling holdings during redemptions", "Small caps are less liquid.",
      ("Credit risk", "Debt."), ("Duration risk", "Debt."), ("Currency risk", "No."))
    H("An investor got 12% CAGR when inflation averaged 6%. Real return (exact)?",
      "About 5.66%", "(1.12/1.06) − 1 = 5.66%.",
      ("6%", "Approximation, not exact."), ("18%", "Added."), ("2%", "Divided."))
    H("Why is total return (TRI) a fairer benchmark than price return index?",
      "Funds receive and reinvest dividends; TRI includes dividends too", "Like-for-like comparison.",
      ("TRI is lower so funds look better", "Opposite."), ("TRI ignores dividends", "It includes them."), ("Price index is not published", "It is."))
    H("Riskometer change from 'High' to 'Very High' must be:",
      "Communicated to investors (e.g. via email/SMS) and disclosed", "Changes are communicated.",
      ("Kept secret", "No."), ("Approved by each investor", "No."), ("Ignored", "No."))
    H("Which measure reflects only 'bad' volatility?",
      "Downside deviation (semi-variance)", "Used in Sortino ratio.",
      ("Standard deviation", "Both directions."), ("Beta", "Market sensitivity."), ("R-squared", "Fit to benchmark."))
