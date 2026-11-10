"""Series XII quiz part D: Ch5 Mutual Funds."""

def add(Q, inr, num):
    C = 5
    S = lambda *a: Q(C, "S", *a)
    H = lambda *a: Q(C, "H", *a)
    S("NAV of a mutual fund primarily reflects:",
      "Current market value of the fund's portfolio", "Workbook sample answer.",
      ("AMC's expenses", "Deducted, but not the main driver."),
      ("Dividends payable", "No."),
      ("Income of constituents", "No."))
    S("To buy ETF units on the exchange, an investor deals with ___ and gets units in ___.",
      "Brokers; demat account", "Exchange-traded like shares.",
      ("Distributors; account statement", "Regular MFs."),
      ("AMC; account statement", "Only above ₹25 crore direct."),
      ("Distributor; demat account", "No."))
    S("KYC for a mutual fund folio must be done by:",
      "All holders, including minors", "Workbook sample answer.",
      ("First holder only", "No."),
      ("All holders except minors", "No."),
      ("First and second holders only", "No."))
    S("Investing a fixed amount periodically is a:",
      "Systematic Investment Plan", "Rupee cost averaging.",
      ("Systematic Withdrawal Plan", "Redemptions."),
      ("Systematic Transfer Plan", "Between schemes."),
      ("Dividend reinvestment plan", "No."))
    S("Mutual funds must disclose NAV:",
      "Daily", "Every business day.",
      ("Weekly", "No."),
      ("Monthly", "Factsheet."),
      ("Quarterly", "IDF NAV."))
    S("SEBI's broad MF categories are:",
      "Equity, Debt, Hybrid, Life Cycle Funds, Others", "Five groups (2026 circular).",
      ("Equity, Debt, Hybrid, Solution-oriented, Others", "Old grouping."),
      ("Equity, Debt, Gold, Index", "No."),
      ("Open, Closed, Interval", "Structure, not category."))
    S("Only one scheme per category is allowed EXCEPT for:",
      "Index funds/ETFs, FoFs and sectoral/thematic funds", "Workbook.",
      ("Liquid and overnight funds", "One each."),
      ("ELSS", "One."),
      ("Large cap funds", "One."))
    S("Three investors put ₹10,000, ₹20,000, ₹30,000. Portfolio grows to ₹72,000. The second investor's holding is:",
      "₹24,000", "Ratio 1:2:3.",
      ("₹20,000", "Original."),
      ("₹36,000", "Third."),
      ("₹12,000", "First."))
    S("Unit capital of a scheme with 6,000 units of FV ₹10 is:",
      "₹60,000", "Units × FV.",
      ("₹72,000", "Market value."),
      ("₹74,400", "Net assets."),
      ("₹6,000", "No."))
    S("Portfolio ₹72,000 + income ₹3,000 − expenses ₹600, 6,000 units. NAV is:",
      "₹12.40", "74,400 ÷ 6,000.",
      ("₹12.00", "Ignores income/expenses."),
      ("₹12.50", "Ignores expenses."),
      ("₹10.00", "Face value."))
    S("Valuing portfolio securities at current market prices daily is:",
      "Marking to market", "MTM.",
      ("Book valuation", "No."),
      ("Amortisation", "No."),
      ("Accrual", "No."))
    S("Exit load is calculated as a percentage of:",
      "NAV", "Reduced from NAV.",
      ("Face value", "No."),
      ("Purchase amount", "No."),
      ("AUM", "No."))
    S("NAV ₹12, exit load 1%. Redemption price is:",
      "₹11.88", "12 − 0.12.",
      ("₹12.12", "Added instead."),
      ("₹11.00", "No."),
      ("₹12.00", "No load applied."))
    S("Entry loads in mutual funds are:",
      "Prohibited by SEBI", "Workbook.",
      ("Capped at 2.25%", "Old."),
      ("Allowed for regular plans", "No."),
      ("Allowed only for NFOs", "No."))
    S("Mutual fund expenses are charged as a percentage of:",
      "Daily average net assets", "Already reflected in NAV.",
      ("Face value", "No."),
      ("Unit capital", "No."),
      ("Investor's purchase amount", "No."))
    S("Income of a SEBI-registered mutual fund is:",
      "Fully exempt from tax (pass-through)", "Taxed in investors' hands.",
      ("Taxed at corporate rate", "No."),
      ("Taxed at 10%", "No."),
      ("Taxed only on dividends", "No."))
    S("Closed-end scheme units are:",
      "Mandatorily listed on stock exchanges", "Fund buys back only at maturity.",
      ("Never listed", "No."),
      ("Sold back to fund daily", "Open-ended."),
      ("Optionally listed", "Mandatory."))
    S("Interval funds allow transactions with the fund:",
      "Only during specified transaction periods", "e.g. 3 days a quarter.",
      ("Every business day", "Open-ended."),
      ("Only at maturity", "Closed-end."),
      ("Never", "No."))
    S("In the growth option, gains are:",
      "Retained in the fund and reflected in NAV", "Realised by selling units.",
      ("Paid out as dividends", "IDCW payout."),
      ("Reinvested as new units", "IDCW reinvestment."),
      ("Paid to the AMC", "No."))
    S("The dividend option was renamed:",
      "Income Distribution cum Capital Withdrawal (IDCW)", "SEBI 5 Oct 2020.",
      ("Systematic Dividend Plan", "No."),
      ("Profit Distribution Option", "No."),
      ("Income Plan", "No."))
    S("Trustees of a mutual fund must meet at least:",
      "6 times a year", "Workbook.",
      ("4 times a year", "No."),
      ("Once a year", "No."),
      ("Monthly", "No."))
    S("Investor money in a mutual fund is held by:",
      "A custodian", "Not the AMC's bank account.",
      ("The AMC", "No."),
      ("The distributor", "No."),
      ("SEBI", "No."))
    S("Commission paid periodically on assets as long as the investor stays is:",
      "Trail commission", "Full trail model.",
      ("Upfront commission", "Not allowed (except SIP upfronting of trail)."),
      ("Entry load", "Prohibited."),
      ("Brokerage", "Securities trades."))
    S("Investor records for most funds are serviced by:",
      "R&T agents", "Folio-level records.",
      ("Custodians", "Securities and funds."),
      ("Auditors", "Accounts."),
      ("Brokers", "Trades."))
    S("A multi cap fund must invest at least ___ in equity, with ≥25% each in large, mid and small caps.",
      "75%", "Workbook 2026.",
      ("65%", "Flexi cap."),
      ("80%", "Large cap."),
      ("95%", "Index."))
    S("Large cap companies are the:",
      "1st to 100th by full market cap", "Mid 101–250; small 251+.",
      ("1st to 50th", "No."),
      ("1st to 250th", "No."),
      ("Top 500", "No."))
    S("A large cap fund invests at least ___ in large cap stocks.",
      "80%", "Workbook.",
      ("65%", "Mid/small cap."),
      ("35%", "Large & mid."),
      ("75%", "Multi cap equity."))
    S("Mid cap and small cap funds invest at least ___ in their segment.",
      "65%", "Workbook.",
      ("80%", "No."),
      ("35%", "No."),
      ("50%", "No."))
    S("A flexi cap fund must invest at least ___ in equity.",
      "65%", "Dynamic across caps.",
      ("75%", "Multi cap."),
      ("80%", "No."),
      ("50%", "No."))
    S("A focused fund can hold at most:",
      "30 stocks", "Equity ≥ 80%.",
      ("20 stocks", "No."),
      ("50 stocks", "No."),
      ("10 stocks", "No."))
    S("ELSS has a lock-in of:",
      "3 years", "Section 80C up to ₹1.5 lakh (old regime).",
      ("5 years", "No."),
      ("1 year", "No."),
      ("No lock-in", "No."))
    S("ELSS tax deduction under Section 80C is available:",
      "Only under the old tax regime", "Workbook.",
      ("Under both regimes", "No."),
      ("Only under the new regime", "No."),
      ("Unlimited", "Cap ₹1.5 lakh."))
    S("An overnight fund invests in securities with maturity of:",
      "1 day", "Workbook.",
      ("Up to 91 days", "Liquid."),
      ("Up to 1 year", "Money market."),
      ("3–6 months duration", "Ultra short."))
    S("A liquid fund invests in instruments maturing within:",
      "91 days", "Workbook.",
      ("1 day", "Overnight."),
      ("1 year", "Money market."),
      ("182 days", "No."))
    S("Ultra short term fund Macaulay duration is:",
      "3 to 6 months", "Workbook.",
      ("6 to 12 months", "Ultra short to short term."),
      ("1 to 3 years", "Short term."),
      ("Over 7 years", "Long term."))
    S("A short term debt fund has Macaulay duration of:",
      "1 to 3 years", "Workbook.",
      ("3 to 4 years", "Medium."),
      ("4 to 7 years", "Medium to long."),
      ("6 to 12 months", "Ultra short to short."))
    S("A corporate bond fund invests at least 80% in bonds rated:",
      "AA+ and above", "Credit risk fund: AA and below.",
      ("AA and below", "Credit risk."),
      ("A and above", "No."),
      ("AAA only", "No."))
    S("A credit risk fund invests at least ___ in AA and below rated bonds.",
      "65%", "Excludes AA+.",
      ("80%", "No."),
      ("50%", "No."),
      ("95%", "No."))
    S("A gilt fund invests at least ___ in G-secs.",
      "80%", "Across maturity.",
      ("65%", "No."),
      ("95%", "No."),
      ("100%", "No."))
    S("A 10-year constant maturity gilt fund keeps portfolio Macaulay duration at:",
      "10 years", "Workbook.",
      ("Over 7 years", "Long term fund."),
      ("1 to 10 years", "No."),
      ("5 years", "No."))
    S("Conservative hybrid funds hold equity of:",
      "10% to 25%", "Debt 75–90%.",
      ("40% to 60%", "Balanced."),
      ("65% to 80%", "Aggressive."),
      ("At least 65%", "Arbitrage/equity savings."))
    S("Aggressive hybrid funds hold equity of:",
      "65% to 80%", "Debt 20–35%.",
      ("40% to 60%", "Balanced."),
      ("10% to 25%", "Conservative."),
      ("At least 80%", "No."))
    S("A mutual fund may offer:",
      "Either an aggressive hybrid or a balanced hybrid fund", "Workbook.",
      ("Both aggressive and balanced hybrid", "No."),
      ("Neither", "No."),
      ("Up to three hybrid funds", "No."))
    S("Multi asset allocation funds invest in at least ___ asset classes, ≥10% each.",
      "Three", "Foreign securities not a separate class.",
      ("Two", "No."),
      ("Four", "No."),
      ("Five", "No."))
    S("Index funds and ETFs invest at least ___ in index securities.",
      "95%", "Workbook.",
      ("80%", "No."),
      ("90%", "No."),
      ("100%", "No."))
    S("Each gold ETF unit typically represents:",
      "1 gram of gold", "Workbook.",
      ("10 grams", "No."),
      ("1 ounce", "No."),
      ("1 kilogram", "No."))
    S("A fund of funds invests at least ___ in underlying funds.",
      "95%", "Workbook.",
      ("80%", "No."),
      ("65%", "No."),
      ("100%", "No."))
    S("The difference between a passive fund's return and its benchmark is:",
      "Tracking error", "Should be close to zero.",
      ("Alpha", "No."),
      ("Expense ratio", "No."),
      ("Exit load", "No."))
    S("PAN is NOT mandatory for individual MF investments up to:",
      "₹50,000 per year per mutual fund", "Lump sum + SIP.",
      ("₹2 lakh", "No."),
      ("₹10,000", "No."),
      ("₹1 lakh per year", "No."))
    S("Aadhaar-based eKYC for MFs removes the need for:",
      "Paperwork and in-person verification", "Workbook.",
      ("PAN", "No."),
      ("Bank account", "No."),
      ("Nomination", "No."))
    S("An NFO (except ELSS) can stay open for:",
      "15 days", "Workbook.",
      ("30 days", "No."),
      ("10 working days", "Public issue."),
      ("7 days", "No."))
    S("Units in an NFO must be allotted within ___ of closing.",
      "5 business days", "Workbook.",
      ("15 days", "No."),
      ("10 working days", "No."),
      ("2 days", "No."))
    S("Existing investors buy more units in the continuous offer using:",
      "A transaction slip with the folio number", "New investors use an application form.",
      ("A new application form", "New investors."),
      ("A KIM", "No."),
      ("A DIS", "No."))
    S("Which document contains statutory information about the fund house?",
      "Statement of Additional Information (SAI)", "SID = scheme; KIM = key facts.",
      ("Scheme Information Document", "Scheme."),
      ("Key Information Memorandum", "Summary."),
      ("Factsheet", "Monthly."))
    S("The riskometer appears on the front page of:",
      "NFO application form, SID and KIM (and in adverts)", "Workbook.",
      ("Only the SAI", "No."),
      ("Only the account statement", "No."),
      ("Only the annual report", "No."))
    S("A mutual fund factsheet is published:",
      "Monthly", "Shows top 10 holdings etc.",
      ("Daily", "NAV."),
      ("Quarterly", "No."),
      ("Yearly", "No."))
    S("Cash payment for MF purchases is allowed up to:",
      "₹50,000 per mutual fund house", "Workbook.",
      ("₹2 lakh", "No."),
      ("₹10,000", "No."),
      ("Not allowed", "No."))
    S("A folio can have up to ___ joint holders.",
      "Three", "All do PAN and KYC.",
      ("Two", "No."),
      ("Four", "No."),
      ("Five", "No."))
    S("Investors can register up to ___ bank accounts with a mutual fund.",
      "Five", "One is default.",
      ("Three", "No."),
      ("Ten", "No."),
      ("One", "No."))
    S("500 units redeemed at NAV ₹24 with 1% exit load gives:",
      "₹11,880", "23.76 × 500.",
      ("₹12,000", "No load."),
      ("₹12,120", "Load added."),
      ("₹11,760", "No."))
    S("A Consolidated Account Statement is sent:",
      "Monthly if there are transactions; every 6 months if none", "Workbook.",
      ("Only yearly", "No."),
      ("Weekly", "No."),
      ("Only on request", "No."))
    S("Rupee cost averaging means:",
      "More units bought when price is low, fewer when high", "SIP benefit.",
      ("Same units bought each month", "No."),
      ("Selling units at high prices", "No."),
      ("Fixed NAV for all purchases", "No."))
    S("An STP is in effect:",
      "An SWP from source scheme plus SIP into destination scheme", "Same fund house.",
      ("A switch between fund houses", "No."),
      ("A dividend transfer", "No."),
      ("A redemption only", "No."))
    S("Mutual funds are regulated under:",
      "SEBI (Mutual Funds) Regulations, 1996", "Workbook.",
      ("SEBI (ICDR) Regulations 2018", "No."),
      ("RBI Act 1934", "No."),
      ("Companies Act 2013", "No."))
    S("A mutual fund is constituted as a:",
      "Trust", "Investors' money off AMC balance sheet.",
      ("Company", "AMC is a company."),
      ("Partnership", "No."),
      ("Society", "No."))
    S("AMFI is:",
      "The industry body of mutual funds", "Best practices, code of conduct.",
      ("A SEBI department", "No."),
      ("A rating agency", "No."),
      ("A depository", "No."))
    H("A new investor buys 1,000 units at face value ₹10 when NAV is ₹12.40 (6,000 units, ₹74,400). New NAV is:",
      "₹12.05", "84,400 ÷ 7,000 — dilutes existing holders.",
      ("₹12.40", "Only if bought at NAV."),
      ("₹12.88", "Redemption at FV case."),
      ("₹10.00", "No."))
    H("An investor redeems 1,000 units at face value ₹10 when NAV is ₹12.40 (6,000 units). New NAV is:",
      "₹12.88", "64,400 ÷ 5,000.",
      ("₹12.05", "Purchase at FV case."),
      ("₹12.40", "Only at NAV."),
      ("₹11.88", "No."))
    H("Why are transactions priced at NAV?",
      "To keep parity between entering, remaining and exiting investors", "Workbook.",
      ("To maximise AMC fees", "No."),
      ("Because SEBI fixes NAV", "No."),
      ("To avoid exit loads", "No."))
    H("MFs may borrow only:",
      "For temporary liquidity needs like redemptions or dividend payment", "Not to invest.",
      ("To leverage equity portfolios", "No."),
      ("Up to 50% of AUM for investment", "No."),
      ("Never under any condition", "Temporary borrowing allowed."))
    H("Large & mid cap fund minimum allocation is:",
      "35% large cap and 35% mid cap", "Workbook.",
      ("50% each", "No."),
      ("65% combined only", "No."),
      ("25% each", "Multi cap sub-limits."))
    H("Sectoral/thematic funds may overlap with other equity schemes (except large cap) by at most:",
      "50%", "Workbook 2026.",
      ("25%", "No."),
      ("65%", "No."),
      ("No limit", "No."))
    H("Per the XII workbook, a fund house may offer:",
      "Either a value fund or a contra fund", "XII workbook rule; V-D allows both with ≤50% overlap.",
      ("Both value and contra with no limit", "No."),
      ("Neither", "No."),
      ("Value fund only", "No."))
    H("A medium term debt fund's duration under anticipated adverse situation can be:",
      "1 to 4 years", "Normal 3–4 years.",
      ("3 to 4 years only", "Normal range."),
      ("1 to 7 years", "Medium to long."),
      ("Over 7 years", "No."))
    H("Medium to long duration fund normal Macaulay duration is:",
      "4 to 7 years", "Adverse: 1–7.",
      ("3 to 4 years", "Medium."),
      ("1 to 3 years", "Short."),
      ("Over 7 years", "Long."))
    H("Ultra short to short term fund has Macaulay duration of:",
      "6 to 12 months", "New 2026 name.",
      ("3 to 6 months", "Ultra short."),
      ("1 to 3 years", "Short."),
      ("Up to 91 days", "Liquid."))
    H("Banking & PSU debt funds can also count which instruments in their 80%?",
      "Municipal bonds", "Banks, PSUs, PFIs and municipal bonds.",
      ("AA corporate bonds", "No."),
      ("Equity of banks", "No."),
      ("Foreign bonds", "No."))
    H("A floater fund invests at least 65% in floating-rate instruments, including:",
      "Fixed-rate instruments swapped into floating", "Workbook.",
      ("Equity shares", "No."),
      ("Gold ETFs", "No."),
      ("Only T-bills", "No."))
    H("Sectoral debt funds invest at least 80% in one sector's bonds rated:",
      "AA+ and above", "Feb 2026 circular.",
      ("AA and below", "No."),
      ("Any rating", "No."),
      ("A and above", "No."))
    H("Which sector is NOT listed for sectoral debt funds in the workbook?",
      "Information technology", "Listed: financial services, energy, infrastructure, housing & real estate.",
      ("Financial services", "Listed."),
      ("Energy", "Listed."),
      ("Housing & real estate", "Listed."))
    H("Balanced hybrid funds differ from aggressive hybrid in that they:",
      "Hold 40–60% equity and allow no arbitrage", "Workbook.",
      ("Must hold 65–80% equity", "Aggressive."),
      ("Invest only in debt", "No."),
      ("Can hold foreign equity only", "No."))
    H("Arbitrage funds' debt exposure is limited to:",
      "G-secs maturing under 1 year and G-sec repo", "Equity ≥ 65%.",
      ("AA+ corporate bonds", "No."),
      ("Any money market instrument", "No."),
      ("Gilt funds", "No."))
    H("Equity savings funds must hold at least ___ equity and ___ debt.",
      "65%; 10%", "Hedged/unhedged minimums in SID.",
      ("80%; 20%", "No."),
      ("40%; 40%", "Balanced."),
      ("65%; 35%", "No."))
    H("Hybrid funds may invest residual portion in InvITs EXCEPT:",
      "Arbitrage funds", "Workbook.",
      ("Balanced advantage funds", "Allowed."),
      ("Multi asset funds", "Allowed."),
      ("Aggressive hybrid funds", "Allowed."))
    H("Life Cycle Funds can be launched with tenures of:",
      "5 to 30 years in multiples of 5; max 6 open at a time", "2026 category.",
      ("1 to 10 years; max 3 open", "No."),
      ("10 to 50 years; unlimited", "No."),
      ("Exactly 20 years", "No."))
    H("Life cycle funds follow a glide path, meaning:",
      "Asset allocation turns more conservative as maturity nears", "Workbook.",
      ("Equity rises near maturity", "Reversed."),
      ("Fixed 50:50 allocation", "No."),
      ("Only debt throughout", "No."))
    H("REIT units for MF investment purposes from 1 Jan 2026 are classified as:",
      "Equity-related instruments (InvITs stay hybrid)", "SEBI circular.",
      ("Hybrid instruments", "InvITs."),
      ("Debt instruments", "No."),
      ("Money market instruments", "No."))
    H("Infrastructure Debt Fund minimum investment and unit face value are:",
      "₹1 crore; ₹10 lakh", "Closed-end, ≥ 5 years.",
      ("₹10 lakh; ₹1 lakh", "No."),
      ("₹5,000; ₹10", "No."),
      ("₹25 crore; ₹1 crore", "No."))
    H("IDF NAV must be disclosed at least:",
      "Once a quarter", "Workbook.",
      ("Daily", "Regular funds."),
      ("Monthly", "No."),
      ("Yearly", "No."))
    H("The main risk in a Fixed Maturity Plan held to maturity is:",
      "Credit (default) risk", "Rate risk vanishes as securities mature with scheme.",
      ("Interest rate risk", "No."),
      ("Currency risk", "No."),
      ("Liquidity risk of the fund house", "No."))
    H("Investors can deal directly with the AMC in ETF units only above:",
      "₹25 crore", "SEBI passive fund norms 2022.",
      ("₹1 crore", "No."),
      ("₹10 lakh", "SIF minimum."),
      ("₹50,000", "No."))
    H("Passive ELSS must track an index of equity from the top ___ companies by market cap.",
      "250", "SEBI 2022.",
      ("100", "No."),
      ("500", "No."),
      ("50", "No."))
    H("FoFs investing in ETFs value them at:",
      "The ETF's closing price on the exchange", "Workbook.",
      ("The ETF's NAV", "No."),
      ("Cost", "No."),
      ("The iNAV at 3 pm", "No."))
    H("Which is NOT an ESG fund strategy listed by SEBI?",
      "Momentum", "Listed: exclusion, integration, best-in-class & positive screening, impact, sustainable objectives, transition.",
      ("Exclusion", "Listed."),
      ("Impact investing", "Listed."),
      ("Transition", "Listed."))
    H("Upfronting of trail commission is allowed only for:",
      "SIP inflows, subject to conditions", "Full trail model otherwise.",
      ("Lump sum NFO investments", "No."),
      ("Debt fund investments", "No."),
      ("Never", "Allowed for SIPs."))
    H("After a FATCA/CRS status change, the investor must inform the fund within:",
      "30 days", "Workbook.",
      ("7 days", "No."),
      ("90 days", "No."),
      ("1 year", "No."))
    H("For a FATCA-reportable investor, the fund reports:",
      "The entire value of all folios held", "Plus beneficiaries and controlling persons.",
      ("Only the latest transaction", "No."),
      ("Only folios above ₹50,000", "No."),
      ("Nothing if NRI", "No."))
    H("Per the XII workbook, redemption proceeds must be sent within:",
      "10 working days", "IDCW 15 days; delay → 15% p.a. interest borne by AMC.",
      ("3 working days", "V-D workbook's newer figure."),
      ("15 days", "IDCW."),
      ("5 business days", "NFO allotment."))
    H("Delay interest on late redemption or IDCW payment is borne by:",
      "The AMC, not the scheme", "15% p.a.",
      ("The scheme", "No."),
      ("The investor", "No."),
      ("The distributor", "No."))
    H("Which is TRUE of the minimum SIF investment?",
      "₹10 lakh across all strategies", "SEBI amendment Dec 2024.",
      ("₹50 lakh", "PMS."),
      ("₹1 crore", "AIF/IDF."),
      ("₹5,000", "MF schemes."))
    H("An SWP of ₹5,000 meets a folio balance worth only ₹3,000 on the date. The fund:",
      "Redeems all units and closes the folio", "Workbook.",
      ("Skips the instalment", "No."),
      ("Pays ₹5,000 from its own money", "No."),
      ("Cancels the SWP without payment", "No."))
    H("Why is an SoA after the first purchase different from later ones?",
      "Later SoAs also show balance units, value, average TER and gross commission", "Workbook.",
      ("Later ones omit NAV", "No."),
      ("The first shows commission only", "No."),
      ("There is no difference", "No."))
    H("Mutual funds must vote at company meetings on:",
      "Governance, capital structure, pay, director changes, related-party deals", "SEBI 5 Mar 2021.",
      ("Only dividend declarations", "No."),
      ("Nothing — voting is optional", "No."),
      ("Only mergers", "Incomplete."))
    H("A scheme name like 'High Yield Fund' is:",
      "Not allowed — names cannot stress only returns", "SEBI Oct 2017.",
      ("Allowed for credit risk funds", "No."),
      ("Required for credit risk funds", "No."),
      ("Allowed with SEBI approval", "No."))
    H("Large/mid/small cap lists are published by AMFI every:",
      "Six months (end-June and end-December data)", "Within 5 calendar days.",
      ("Quarter", "No."),
      ("Month", "No."),
      ("Year", "No."))
