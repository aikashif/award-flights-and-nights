"""Series XII quiz part B: Ch3 Primary Markets."""

def add(Q, inr, num):
    C = 3
    S = lambda *a: Q(C, "S", *a)
    H = lambda *a: Q(C, "H", *a)
    S("A retail individual investor in a public issue invests:",
      "Not more than ₹2 lakh", "Above ₹2 lakh = non-institutional.",
      ("At least 100 shares", "No."),
      ("Not more than ₹5 lakh", "That's the UPI limit."),
      ("Not more than ₹10 lakh", "NII sub-bucket."))
    S("In an offer for sale, the money raised goes to:",
      "The selling shareholders", "Company's capital doesn't change.",
      ("The company", "Fresh issue."),
      ("The stock exchange", "No."),
      ("SEBI", "No."))
    S("Which shares must be listed on a stock exchange?",
      "All shares issued through a public offer", "Workbook sample answer.",
      ("All shares issued to promoters", "No."),
      ("Only shares above ₹10 face value", "No."),
      ("Shares as per issue terms", "Public issue listing is mandatory."))
    S("If an issue is heavily oversubscribed:",
      "Each investor gets fewer shares than applied", "Proportionate allotment.",
      ("The issue price falls", "No."),
      ("Listing price must be higher", "Not certain."),
      ("The company raises more money", "Fixed size (unless green shoe)."))
    S("Which is essential for a public issue of debt?",
      "Credit rating of the instrument", "At least one SEBI-registered CRA.",
      ("Listing of the issuer's shares", "Unlisted companies can issue."),
      ("Promoter guarantee", "No."),
      ("A minimum coupon set by SEBI", "No."))
    S("Who underwrites G-secs on behalf of RBI?",
      "Primary dealers", "RBI-licensed.",
      ("Merchant bankers", "Corporate issues."),
      ("BRLMs", "Corporate issues."),
      ("Stock exchanges", "No."))
    S("Which primary market intermediary is NOT registered with SEBI?",
      "Primary dealer", "Authorised by RBI.",
      ("Merchant banker", "SEBI."),
      ("Registrar to an issue", "SEBI."),
      ("Banker to an issue", "SEBI."))
    S("Debenture trustees must call a meeting of holders when requested by at least:",
      "One-tenth of debenture holders", "Or on default.",
      ("Half of debenture holders", "No."),
      ("One-fourth", "No."),
      ("Any single holder", "No."))
    S("A depository becomes the ___ owner and the investor the ___ owner of demat securities.",
      "Registered; beneficial", "Workbook.",
      ("Beneficial; registered", "Reversed."),
      ("Legal; nominal", "No."),
      ("Joint; sole", "No."))
    S("Issue of free additional shares to existing holders is a:",
      "Bonus issue", "No consideration.",
      ("Rights issue", "Paid at a price."),
      ("Preferential issue", "Identified investors."),
      ("Private placement", "Select investors."))
    S("Only which government issues T-bills?",
      "Central Government", "States issue dated securities only.",
      ("State governments", "No."),
      ("Municipalities", "No."),
      ("Both centre and states", "No."))
    S("Mutual fund units are issued:",
      "Only in domestic markets", "Workbook issuer table.",
      ("Only abroad", "No."),
      ("In both domestic and international markets", "No."),
      ("Only to institutions", "No."))
    S("The primary issue of G-secs is governed by:",
      "Government Securities Act 2006 and Regulations 2007", "Not under SEBI.",
      ("SEBI (ICDR) Regulations", "No."),
      ("Companies Act 2013", "No."),
      ("SEBI (NCS) Regulations", "No."))
    S("An entity raising equity from the public must be:",
      "A limited company", "Registered with MCA.",
      ("A partnership firm", "Not allowed."),
      ("A sole proprietorship", "Not allowed."),
      ("An association of persons", "Not allowed."))
    S("IPO eligibility requires average operating profit of at least ___ over preceding 3 years.",
      "₹15 crore", "With profit in each year.",
      ("₹3 crore", "Net tangible assets."),
      ("₹1 crore", "Net worth."),
      ("₹50 crore", "No."))
    S("IPO eligibility requires net tangible assets of at least ___ in each of preceding 3 years.",
      "₹3 crore", "≤ 50% monetary.",
      ("₹15 crore", "Operating profit."),
      ("₹1 crore", "Net worth."),
      ("₹10 crore", "No."))
    S("IPO eligibility requires net worth of at least ___ in each of preceding 3 years.",
      "₹1 crore", "Restated, consolidated.",
      ("₹3 crore", "NTA."),
      ("₹15 crore", "Profit."),
      ("₹5 crore", "No."))
    S("An issuer failing the profitability tests can still IPO if it allots at least ___ of net offer to QIBs.",
      "75%", "Through book building; else refund.",
      ("50%", "That's the QIB cap for eligible issuers."),
      ("35%", "Retail minimum."),
      ("90%", "Minimum subscription."))
    S("Minimum promoters' contribution in an IPO is:",
      "20% of post-issue capital", "Locked in 18 months (3 years if capex).",
      ("25% of post-issue capital", "Minimum public offer."),
      ("10% of pre-issue capital", "No."),
      ("51% of post-issue capital", "No."))
    S("Minimum promoters' contribution is locked in for:",
      "18 months (3 years if proceeds mainly for capex)", "Excess: 6 months / 1 year.",
      ("6 months", "Excess holding."),
      ("1 year", "Excess holding if capex."),
      ("3 years always", "Only if capex."))
    S("Promoter holding above the minimum contribution is locked in for:",
      "6 months (1 year if mainly capex)", "Workbook.",
      ("18 months", "Minimum contribution."),
      ("3 years", "Minimum contribution if capex."),
      ("No lock-in", "No."))
    S("Post-issue capital ≤ ₹1,600 crore → minimum public offer is:",
      "25%", "Slab 1.",
      ("10%", "₹4,000–50,000 crore slab."),
      ("Shares worth ₹400 crore", "₹1,600–4,000 crore slab."),
      ("35%", "No."))
    S("A public issue stays open for:",
      "Minimum 3 and maximum 10 working days", "Workbook.",
      ("Minimum 7 and maximum 30 days", "Rights issue."),
      ("Exactly 15 days", "MF NFO."),
      ("Minimum 1 and maximum 5 days", "No."))
    S("If the price band is revised, bidding must be extended by at least:",
      "3 working days", "Within the 10-day maximum.",
      ("1 working day", "Force majeure."),
      ("7 days", "No."),
      ("No extension needed", "No."))
    S("Minimum subscription for a public equity issue is:",
      "90% of the net offer", "Else full refund within 4 days.",
      ("75% of base issue", "Debt public issue."),
      ("100%", "No."),
      ("50%", "No."))
    S("Underwriting is mandatory in a:",
      "Book built issue", "Fixed price: optional.",
      ("Fixed price issue", "Optional."),
      ("Rights issue", "Not stated."),
      ("Private placement", "No."))
    S("IPO grading is on a scale of:",
      "1 to 5, with 5 = strong fundamentals", "Optional; not about price.",
      ("1 to 10", "No."),
      ("AAA to D", "Credit ratings."),
      ("5 to 1, with 1 = strong", "Reversed."))
    S("IPO grading is:",
      "An assessment of fundamentals, not of issue price", "Not a recommendation.",
      ("A recommendation to subscribe", "No."),
      ("Mandatory for all IPOs", "Optional."),
      ("Done by SEBI", "CRAs do it."))
    S("A further public offer is made by:",
      "A company already listed after an IPO", "FPO.",
      ("A company going public for the first time", "IPO."),
      ("Promoters selling shares privately", "No."),
      ("Mutual funds", "No."))
    S("In a fixed price issue, the price is set by:",
      "The issuer with the lead manager", "Known before application.",
      ("Bids from investors", "Book building."),
      ("SEBI", "No."),
      ("The stock exchange", "No."))
    S("In book building, successful bidders are those who bid:",
      "At or above the cut-off price", "Allotted at cut-off.",
      ("Below the floor price", "No."),
      ("At the lowest price", "No."),
      ("Only at the cap price", "No."))
    S("Retail discount to cut-off price in a book built issue cannot exceed:",
      "10%", "Workbook.",
      ("5%", "No."),
      ("15%", "Green shoe."),
      ("25%", "No."))
    S("For an issuer meeting profitability tests, retail allocation in a book built issue is:",
      "Not less than 35%", "NII ≥ 15%, QIB ≤ 50%.",
      ("Not more than 10%", "75% QIB route."),
      ("Not less than 50%", "Fixed price."),
      ("Not more than 35%", "No."))
    S("Within the QIB portion, the reservation for mutual funds is:",
      "5%", "Both allocation patterns.",
      ("10%", "QIP MF minimum."),
      ("15%", "No."),
      ("35%", "No."))
    S("In a non-book-built issue, retail gets at least:",
      "50% of net offer", "Rest to others.",
      ("35%", "Book built."),
      ("10%", "No."),
      ("75%", "No."))
    S("The draft prospectus is filed with:",
      "SEBI", "Then with RoC after changes.",
      ("Stock exchange only", "In-principle approval separately."),
      ("RBI", "No."),
      ("MCA directly first", "No."))
    S("Every application form must be accompanied by:",
      "An abridged prospectus", "Workbook step.",
      ("A red herring prospectus", "No."),
      ("A credit rating", "No."),
      ("A contract note", "No."))
    S("Payment for public issue applications must be through:",
      "ASBA only", "Retail may use UPI within ASBA.",
      ("Cheque only", "No."),
      ("Cash up to ₹50,000", "That's MF purchases."),
      ("Demand draft", "No."))
    S("Basis of allotment is finalised in consultation with:",
      "The stock exchange", "Workbook step.",
      ("SEBI", "No."),
      ("RBI", "No."),
      ("The depositories", "No."))
    S("A prospectus for a book built issue without final price is a:",
      "Red herring prospectus", "Price band or issue size shown.",
      ("Shelf prospectus", "Multiple debt issues."),
      ("Abridged prospectus", "Summary."),
      ("Letter of offer", "Rights issue."))
    S("IPO bidding on exchanges runs from:",
      "10 am to 5 pm", "LM may extend on closing day.",
      ("9:15 am to 3:30 pm", "Equity trading."),
      ("9 am to 5 pm", "Debt segment."),
      ("10 am to 3 pm", "No."))
    S("The price band must be announced at least ___ before issue opens.",
      "2 working days", "Workbook.",
      ("5 working days", "No."),
      ("1 working day", "No."),
      ("7 days", "No."))
    S("Minimum application value in a book built issue is in the range:",
      "₹10,000 – ₹15,000", "Minimum bid lot.",
      ("₹5,000 – ₹10,000", "No."),
      ("₹15,000 – ₹20,000", "No."),
      ("₹1 lakh – ₹2 lakh", "No."))
    S("Bidding at 'cut-off' means the investor:",
      "Accepts the price discovered and is always allotted (subject to oversubscription)", "Ensures acceptance.",
      ("Bids at the floor price", "No."),
      ("Cannot revise the bid", "No."),
      ("Pays nothing upfront", "No."))
    S("UPI is mandatory for individual applications up to:",
      "₹5 lakh (from 1 May 2022)", "Workbook.",
      ("₹2 lakh", "Retail limit."),
      ("₹10 lakh", "No."),
      ("₹50,000", "No."))
    S("Green shoe option allows extra allotment up to:",
      "15% of issue size", "For price stabilisation.",
      ("10%", "No."),
      ("25%", "No."),
      ("5%", "No."))
    S("The stabilising agent can intervene for:",
      "30 days from listing", "Workbook.",
      ("15 days", "No."),
      ("90 days", "No."),
      ("6 months", "No."))
    S("A rights issue stays open for:",
      "Not less than 7 and not more than 30 days", "Workbook.",
      ("3 to 10 working days", "Public issue."),
      ("Exactly 15 days", "No."),
      ("1 to 7 days", "No."))
    S("Selling your rights entitlement is called:",
      "Renunciation", "Entitlements trade on exchange.",
      ("Forfeiture", "No."),
      ("Assignment", "No."),
      ("Novation", "No."))
    S("Minimum subscription in a public issue of debt is:",
      "75% of base issue size", "Tax-free bonds exempt.",
      ("90% of net offer", "Equity."),
      ("100%", "No."),
      ("50%", "No."))
    S("Unsecured debentures issued by a company are treated as:",
      "Deposits under the Companies (Acceptance of Deposits) Rules", "Workbook.",
      ("Equity", "No."),
      ("Government securities", "No."),
      ("Commercial paper", "No."))
    S("Private placement under the Companies Act 2013 is an offer to not more than:",
      "50 persons", "Workbook.",
      ("200 persons", "No."),
      ("49 persons", "Close but wrong."),
      ("100 persons", "No."))
    S("Private placement payment must be made:",
      "Through banking channels, not cash", "Workbook.",
      ("In cash only", "No."),
      ("Through ASBA only", "No."),
      ("By demand draft to SEBI", "No."))
    S("QIP is made by a listed issuer to:",
      "Qualified institutional buyers", "Private placement basis.",
      ("Retail investors", "No."),
      ("Promoters only", "No."),
      ("Employees", "No."))
    S("In a QIP, at least ___ goes to mutual funds.",
      "10%", "Unsubscribed part to other QIBs.",
      ("5%", "Book building MF reservation."),
      ("25%", "No."),
      ("50%", "No."))
    S("To make a QIP, a company's shares must be listed for at least:",
      "1 year before notice", "Plus special resolution.",
      ("3 years", "No."),
      ("6 months", "No."),
      ("No minimum", "No."))
    S("Retail investors bid in G-sec auctions through stock exchanges as:",
      "Non-competitive bidders", "Exchange submits one consolidated bid.",
      ("Competitive bidders", "Only banks, PDs with RBI accounts."),
      ("Primary dealers", "No."),
      ("Underwriters", "No."))
    S("Non-competitive bidders in G-sec auctions are allotted at:",
      "Weighted average price/yield of competitive bids", "Workbook.",
      ("The highest yield", "No."),
      ("Face value", "No."),
      ("The cut-off price", "No."))
    S("Competitive bidding in G-sec auctions needs:",
      "A current account and SGL account with RBI", "Banks, PDs.",
      ("A demat account only", "No."),
      ("SEBI registration", "No."),
      ("A broker", "No."))
    S("The issuer of a public issue of debt must NOT be:",
      "A wilful defaulter", "Primary requirement.",
      ("A public limited company", "Must be."),
      ("Unlisted", "Unlisted allowed."),
      ("A PSU", "Allowed."))
    S("A Debenture Redemption Reserve is created by:",
      "Transferring part of profits each year until redemption", "Workbook.",
      ("Borrowing from banks", "No."),
      ("Issuing fresh equity", "No."),
      ("Collecting from investors", "No."))
    H("For post-issue capital of ₹2,000 crore at offer price, the minimum public offer is:",
      "Shares worth ₹400 crore", "₹1,600–4,000 crore slab; reach 25% in 3 years.",
      ("25%", "≤ ₹1,600 crore."),
      ("10%", "₹4,000–50,000 crore."),
      ("₹200 crore", "No."))
    H("A company with post-issue capital of ₹10,000 crore must offer at least ___ and reach 25% public holding within ___.",
      "10%; 3 years", "Slab 3.",
      ("25%; immediately", "Slab 1."),
      ("5%; 5 years", "No."),
      ("10%; 5 years", "3 years."))
    H("Which can contribute up to 10% of post-issue capital to meet promoter contribution shortfall without being promoters?",
      "AIFs, FVCIs, SCBs, PFIs, IRDAI insurers or non-individual holders with ≥5%", "ICDR 2024 amendment.",
      ("Retail investors", "No."),
      ("Mutual funds only", "Not listed this way."),
      ("Any FPI", "Not in the list."))
    H("The 50% limit on monetary assets in NTA does NOT apply when:",
      "The IPO is entirely an offer for sale", "Workbook proviso.",
      ("The issuer is a bank", "No."),
      ("The issue size is below ₹100 crore", "No."),
      ("The issue is fixed price", "No."))
    H("A company changed its name within the last year. To IPO under normal route, it needs:",
      "≥ 50% of last year's revenue from the new-name activity", "Workbook.",
      ("SEBI's special approval", "No."),
      ("A 2-year waiting period", "No."),
      ("100% revenue from new activity", "No."))
    H("If an issuer fails the profitability tests, allocation is:",
      "Retail ≤ 10%, NII ≤ 15%, QIB ≥ 75%", "Reverse pattern.",
      ("Retail ≥ 35%, NII ≥ 15%, QIB ≤ 50%", "Eligible issuer."),
      ("Retail ≥ 50%", "Fixed price."),
      ("QIB ≤ 25%", "No."))
    H("In the NII category, how is allocation split?",
      "1/3 for ₹2–10 lakh applicants; 2/3 for above ₹10 lakh", "ICDR 2022.",
      ("Half and half", "No."),
      ("2/3 for ₹2–10 lakh; 1/3 above", "Reversed."),
      ("All to above ₹10 lakh", "No."))
    H("Which portion of a book built issue cannot be underwritten?",
      "The 75% QIB portion for issuers failing the tests", "Workbook.",
      ("The retail portion", "No."),
      ("The NII portion", "No."),
      ("The green shoe portion", "Not stated."))
    H("For an underwritten issue, the 90% minimum subscription:",
      "Includes subscription by underwriters", "Workbook.",
      ("Excludes underwriters", "No."),
      ("Applies only to retail", "No."),
      ("Drops to 75%", "No."))
    H("Bids (price/shares): 144/1,000; 140/1,500; 135/2,500; 130/1,000; 120/500. Issue size 5,000. Cut-off is:",
      "₹135", "Cumulative demand hits 5,000 at 135.",
      ("₹140", "Only 2,500."),
      ("₹130", "6,000 — beyond size."),
      ("₹144", "Only 1,000."))
    H("Retail portion oversubscribed 1.52×. A bidder for 50 shares gets about:",
      "33 shares", "50 ÷ 1.52 ≈ 33.",
      ("50 shares", "No."),
      ("26 shares", "That's for 40."),
      ("20 shares", "That's for 30."))
    H("In the same 1.52× example, total shares allotted to 100 bidders of 20 shares each is:",
      "1,300", "13 × 100.",
      ("2,000", "Applied, not allotted."),
      ("1,520", "No."),
      ("700", "That's unblocked."))
    H("Green shoe proceeds are used to:",
      "Buy shares if price falls below issue price after listing", "Price stabilisation.",
      ("Pay underwriters", "No."),
      ("Fund capex", "No."),
      ("Refund retail investors", "No."))
    H("Which is a ground for SEBI to reject a draft offer document?",
      "Issue proceeds not creating tangible assets or unclear use", "Workbook list.",
      ("Price band too low", "No."),
      ("Too many retail investors", "No."),
      ("Issuer listed on BSE only", "No."))
    H("Which channel is NOT among the extra ASBA channels introduced for issues?",
      "Paying cash at the stock exchange", "Channels: online ASBA, physical ASBA, broker's linked 3-in-1 account.",
      ("Online ASBA via SCSB portal", "Valid."),
      ("Physical ASBA at SCSB branch", "Valid."),
      ("Linked trading-demat-bank account of brokers", "Valid."))
    H("Under e-IPO (since 2013), investors can bid through:",
      "Any broker of the exchange, appointed or not", "Workbook.",
      ("Only syndicate members", "No."),
      ("Only the BRLM", "No."),
      ("Only the registrar", "No."))
    H("Debt public issue: the draft offer document is filed with:",
      "Stock exchanges, then open for public comments", "Final to RoC; LM gives due diligence certificate to SEBI.",
      ("SEBI for approval", "Equity route."),
      ("RBI", "No."),
      ("Debenture trustee only", "No."))
    H("Which entity is NOT eligible to file a shelf prospectus for debt per the workbook?",
      "Any unlisted private company", "Eligible: PFIs, scheduled banks, CBDT tax-free issuers, IDFs, listed entities, eligible NBFCs/HFCs.",
      ("Public financial institutions", "Eligible."),
      ("Scheduled banks", "Eligible."),
      ("Infrastructure debt funds", "Eligible."))
    H("Which issuer is exempt from minimum subscription in a debt public issue?",
      "Issuer of CBDT-notified tax-free bonds", "Workbook.",
      ("Any PSU", "No."),
      ("Any bank", "No."),
      ("Any NBFC", "No."))
    H("EBP (per XII workbook) is mandatory for a single private debt issue of at least:",
      "₹50 crore including green shoe", "XII workbook figure.",
      ("₹20 crore", "V-D workbook's newer figure — not XII."),
      ("₹100 crore", "Bid cap."),
      ("₹500 crore", "No."))
    H("On EBP, a first-time issuer must upload documents at least ___ before opening (XII workbook).",
      "5 working days", "Others: 2 working days.",
      ("2 working days", "Repeat issuers."),
      ("1 working day", "Bidding announcement."),
      ("10 days", "No."))
    H("Maximum bid through arrangers on EBP is:",
      "Lower of ₹100 crore or 5% of base issue", "Workbook.",
      ("Higher of ₹100 crore or 5%", "No."),
      ("₹50 crore", "No."),
      ("10% of issue", "No."))
    H("EBP allotment when coupon is discovered in bidding is by:",
      "Yield-time priority", "Price-time if coupon fixed.",
      ("Price-time priority", "Coupon fixed."),
      ("Proportionate basis", "No."),
      ("Lottery", "No."))
    H("Issuers older than ___ are not automatically required to use EBP for small issues; younger issuers must.",
      "3 years", "Issuers in existence < 3 years must use EBP.",
      ("1 year", "No."),
      ("5 years", "No."),
      ("10 years", "No."))
    H("Which is TRUE of preferential allotment?",
      "It needs shareholder resolution and follows SEBI's pricing formula", "Listed companies only.",
      ("It is made by unlisted companies to the public", "No."),
      ("It needs no lock-in", "Promoter allotment locked."),
      ("It is priced by book building", "No."))
    H("QIP shares can be sold within 1 year of allotment only:",
      "On a recognised stock exchange", "Workbook.",
      ("To promoters", "No."),
      ("Through private deals", "No."),
      ("After SEBI approval", "No."))
    H("Promoters may use an OFS through QIP mainly to:",
      "Achieve minimum public shareholding of 25%", "SCR Rules 1957.",
      ("Increase their stake", "No."),
      ("Delist the company", "No."),
      ("Avoid lock-in", "No."))
    H("Which is NOT an 'eligible security' for QIP?",
      "Warrants issued alone", "Eligible: equity, NCDs with warrants, convertibles other than warrants.",
      ("Equity shares", "Eligible."),
      ("Non-convertible debt with warrants", "Eligible."),
      ("Fully convertible debentures", "Eligible."))
    H("An issuer with SR equity shares listing ordinary shares must:",
      "List the SR shares on the same exchange", "SCR Rules amendment 2020.",
      ("Convert SR shares into ordinary shares", "No."),
      ("Sell SR shares in the IPO", "No."),
      ("List SR shares abroad", "No."))
    H("In a public issue, who appoints the registrar, bankers and brokers?",
      "The lead manager in consultation with the issuer", "Workbook.",
      ("SEBI", "No."),
      ("The stock exchange", "No."),
      ("The depository", "No."))
    H("Brokers to the issue are paid commission based on:",
      "Their collection of applications", "Workbook.",
      ("The issue price", "No."),
      ("Listing gains", "No."),
      ("A fixed SEBI fee", "No."))
    H("Bankers to the issue must have branches:",
      "In the mandatory centres specified by regulations", "Workbook.",
      ("Only in Mumbai", "No."),
      ("In every district", "No."),
      ("Abroad", "No."))
    H("Which IPO fact is TRUE about a company that issued 500 fresh shares on 1,000 existing (X, Y 500 each)?",
      "X and Y each hold 33.33% after the issue", "500/1,500.",
      ("X and Y each hold 25%", "That's the OFS case."),
      ("Share capital stays ₹10,000", "OFS case."),
      ("Money goes to X and Y", "OFS case."))
    H("Why do issues cluster in bull markets?",
      "High buying interest gives better pricing for issuers", "Workbook.",
      ("SEBI relaxes rules in bull markets", "No."),
      ("Underwriting is cheaper by law", "No."),
      ("Bear markets ban IPOs", "No."))
    H("A company's prospectus information must be updated:",
      "Annually and made public", "Workbook.",
      ("Never after listing", "No."),
      ("Every quarter with SEBI", "No."),
      ("Only on FPO", "No."))
    H("Which is TRUE of the RTA's post-issue work?",
      "Rejects incomplete forms and finalises basis of allotment with LM, issuer and exchange", "Workbook.",
      ("Sets the price band", "No."),
      ("Underwrites shortfall", "No."),
      ("Approves the prospectus", "No."))
    H("For RBI's retail non-competitive bidding via exchanges, the exchange:",
      "Aggregates orders into one bid and allocates investor-wise after RBI allotment", "RBI circular Nov 2017.",
      ("Bids competitively for each investor", "No."),
      ("Buys from PDs and resells", "No."),
      ("Sends each order to RBI separately", "No."))
    H("Which securities are 'eligible' for private placement listing?",
      "Any privately placed security meeting SEBI and exchange listing rules", "Workbook.",
      ("None — private placements can't list", "They can."),
      ("Only G-secs", "No."),
      ("Only equity", "No."))
