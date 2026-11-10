"""Series XII quiz part A: Ch1 Securities Markets, Ch2 Securities & Investing."""

def add(Q, inr, num):
    # ============================================================ CH 1
    C = 1
    S = lambda *a: Q(C, "S", *a)
    H = lambda *a: Q(C, "H", *a)
    S("Under which Act and section is the term 'securities' defined?",
      "Section 2(h) of the Securities Contracts (Regulation) Act, 1956", "SCRA 1956, Section 2(h) defines securities.",
      ("Section 2 of the SEBI Act, 1992", "SEBI Act sets up SEBI; the definition is in SCRA."),
      ("Section 10 of the Companies Act, 2013", "Companies Act does not hold this definition."),
      ("Section 2(h) of the Depositories Act, 1996", "Wrong Act."))
    S("Which of these is NOT a security under SCRA?",
      "A unit linked insurance policy (ULIP)", "MF units are securities, but ULIPs (insurance + investment) are expressly excluded.",
      ("Units of a mutual fund scheme", "These are securities."),
      ("Government securities", "These are securities."),
      ("Security receipts under SARFAESI", "These are securities."))
    S("Which of these is a security?",
      "A certificate of deposit issued by a bank", "A CD is transferable — a security. A bank FD is a bilateral contract.",
      ("A bank fixed deposit", "Bilateral, not transferable."),
      ("An insurance policy", "A contract, not a security."),
      ("A chit fund subscription", "Not a security."))
    S("Electronic Gold Receipts were declared 'securities' by the Central Government in:",
      "December 2021", "Gazette notification dated 24 December 2021.",
      ("July 2022", "That is the ZCZP instrument."),
      ("June 2020", "Regulatory sandbox framework date."),
      ("January 2023", "No such notification."))
    S("Zero Coupon Zero Principal instruments are issued by:",
      "Not-for-profit organisations registered on a Social Stock Exchange", "ZCZPs fund social projects; listed on the SSE segment.",
      ("Central Government for social schemes", "Not issued by govt."),
      ("Banks for priority-sector lending", "No."),
      ("Mutual funds as social-impact schemes", "No."))
    S("The primary market is also called the:",
      "New issue market", "Issuers sell securities for the first time.",
      ("Stock market", "That's the secondary market."),
      ("Money market", "Short-term debt market."),
      ("After market", "Not used for primary market."))
    S("The secondary market's main contribution is that it:",
      "Makes financial assets marketable", "Primary market creates assets; secondary market makes them marketable.",
      ("Creates new financial assets", "That's the primary market."),
      ("Raises fresh capital for issuers", "Secondary trades don't give issuers new capital."),
      ("Sets interest rates for the economy", "That's RBI policy."))
    S("The role of stock exchanges in the primary market is limited to:",
      "Listing of securities", "Workbook: exchanges' primary-market role is limited to listing.",
      ("Pricing the issue", "Done by issuer and lead manager / book building."),
      ("Underwriting the issue", "Done by merchant bankers and brokers."),
      ("Approving the prospectus", "SEBI observes; RoC files."))
    S("Which intermediary serves BOTH primary and secondary markets as infrastructure?",
      "Registrars and transfer agents", "RTAs, custodians and depositories serve both markets.",
      ("Merchant bankers", "Mainly primary market."),
      ("Underwriters", "Primary market."),
      ("Bankers to an issue", "Primary market."))
    S("A mutual fund that collects money and issues units is a/an:",
      "Issuer", "Workbook sample question: MF issues units → issuer.",
      ("Regulator", "No."),
      ("Intermediary only", "The workbook answer is issuer."),
      ("Custodian", "No."))
    S("Which entity does NOT issue equity capital?",
      "Government agencies", "Governments and their agencies issue only debt.",
      ("Public sector companies", "They can (disinvestment)."),
      ("Banks", "They can issue equity."),
      ("Private companies", "They issue equity."))
    S("Which regulation lists intermediaries such as merchant bankers, DPs, CRAs and KRAs?",
      "SEBI (Intermediaries) Regulations, 2008", "Roles and responsibilities of intermediaries are in these regulations.",
      ("SEBI (ICDR) Regulations, 2018", "Covers issues of capital."),
      ("SEBI (LODR) Regulations, 2015", "Listing obligations."),
      ("SCRA 1956", "Defines securities, regulates exchanges."))
    S("Who are registered with exchanges as agents of brokers (earlier called sub-brokers)?",
      "Authorised persons", "APs extend brokers' reach.",
      ("Depository participants", "Agents of depositories."),
      ("Custodians", "Serve institutions."),
      ("Clearing members", "Settle trades."))
    S("A depository participant is an agent of:",
      "The depository", "DPs act as agents of depositories.",
      ("The stock exchange", "No."),
      ("SEBI", "No."),
      ("The issuer company", "No."))
    S("Underwriters in the government bond market are called:",
      "Primary dealers", "Primary dealers underwrite G-sec issues for RBI.",
      ("Merchant bankers", "Corporate issues."),
      ("Gilt brokers", "No."),
      ("Treasury agents", "No."))
    S("Which intermediary does NOT pool clients' money and issues no security?",
      "Portfolio manager", "AMCs pool and issue units; portfolio managers manage individual portfolios.",
      ("Asset management company", "Pools money, issues units."),
      ("Collective investment scheme", "Pools money."),
      ("REIT", "Pools money, issues units."))
    S("KYC done once with a SEBI-registered intermediary is:",
      "Valid across all SEBI-registered intermediaries", "Uniform KYC held by KRAs is valid across the capital market.",
      ("Valid only with that intermediary", "No."),
      ("Valid for one year only", "No expiry rule like this."),
      ("Valid only for mutual funds", "No."))
    S("KRAs validate PAN against the:",
      "Income Tax database", "Aadhaar via UIDAI; mobile/email via OTP; PAN via Income Tax database.",
      ("UIDAI database", "That's for Aadhaar."),
      ("CKYC registry", "Not stated."),
      ("Bank records", "No."))
    S("SEBI was set up under the:",
      "SEBI Act, 1992", "Statutory body under the SEBI Act 1992; under Ministry of Finance.",
      ("SCRA, 1956", "No."),
      ("Companies Act, 1956", "No."),
      ("Depositories Act, 1996", "No."))
    S("Which department of the Ministry of Finance regulates capital markets?",
      "Department of Economic Affairs", "DEA → capital markets; DFS → banks, insurance, pension.",
      ("Department of Financial Services", "Banks, insurance, pension."),
      ("Department of Revenue", "Taxes."),
      ("Department of Expenditure", "No."))
    S("Who regulates the money market and foreign exchange market?",
      "RBI", "Workbook sample question — True.",
      ("SEBI", "Capital markets."),
      ("IRDAI", "Insurance."),
      ("PFRDA", "Pensions."))
    S("IFSCA is headquartered at:",
      "GIFT City, Gandhinagar", "Set up 2020 under IFSCA Act 2019.",
      ("BKC, Mumbai", "SEBI HQ area."),
      ("New Delhi", "No."),
      ("Ahmedabad city", "GIFT City is in Gandhinagar."))
    S("A poor monsoon causes fertiliser company share prices to fall. This shows the market's role of:",
      "Information signalling through prices", "Prices reflect new information quickly.",
      ("Liquidity", "No."),
      ("Generating productive investments", "No."),
      ("Orderly transfer of funds", "No."))
    S("A company issues commercial paper instead of taking a bank loan. This trend is called:",
      "Financial disintermediation", "Securities markets reduce dependence on banks.",
      ("Price discovery", "No."),
      ("Dematerialisation", "No."),
      ("Securitisation", "No."))
    S("Which is NOT one of the 5 cyber resiliency goals of CSCRF?",
      "Insure", "Goals: Anticipate, Withstand, Contain, Recover, Evolve.",
      ("Anticipate", "It is a goal."),
      ("Contain", "It is a goal."),
      ("Evolve", "It is a goal."))
    S("Under CSCRF, cyber incidents must be reported through:",
      "The SEBI incident reporting portal", "Respond function: report via SEBI portal.",
      ("SCORES", "Investor complaints."),
      ("The ODR portal", "Disputes."),
      ("The stock exchange website", "No."))
    S("In the Innovation Sandbox, testing is done:",
      "Offline, isolated from the live market", "Innovation sandbox = offline; regulatory sandbox = live.",
      ("Live with real customers", "That's regulatory sandbox."),
      ("Only on SEBI's servers", "No."),
      ("Only by SEBI-registered brokers", "Open to FinTechs, start-ups, individuals."))
    S("The term 'regulatory sandbox' was coined by:",
      "UK Financial Conduct Authority in 2015", "Adopted by 20+ countries since.",
      ("SEBI in 2020", "SEBI's framework came in 2020."),
      ("US SEC in 2008", "No."),
      ("Monetary Authority of Singapore in 2016", "No."))
    S("Regulatory sandbox relaxations can NEVER be given from:",
      "KYC, AML and investor protection rules", "These are never relaxed.",
      ("Capital adequacy norms", "May be relaxed."),
      ("Reporting formats", "May be relaxed."),
      ("Registration fees", "Not the stated exclusion."))
    S("In the 19th century, Mumbai brokers met under a banyan tree in front of:",
      "Mumbai Town Hall", "Fort area, in front of the Town Hall.",
      ("Gateway of India", "No."),
      ("Victoria Terminus", "No."),
      ("Reserve Bank building", "No."))
    # ---- harder
    H("Which are 'Market Infrastructure Institutions' under CSCRF but NOT under the usual list of exchanges, depositories and clearing corporations?",
      "KRAs and Qualified RTAs", "CSCRF adds KRAs and QRTAs to the MII list.",
      ("AMCs and DPs", "Regulated entities, not MIIs."),
      ("Brokers and custodians", "Not MIIs."),
      ("CRAs and debenture trustees", "Not MIIs."))
    H("Under CSCRF, periodic audits must be done by:",
      "A CERT-In empanelled IS auditor", "Protect function.",
      ("SEBI's internal audit team", "No."),
      ("The statutory auditor", "No."),
      ("The stock exchange", "No."))
    H("A RE's CSCRF category for a financial year is decided:",
      "At the start of the year on previous year's data and stays fixed for the year", "Category doesn't change mid-year.",
      ("Every quarter", "No."),
      ("At year-end on current year data", "No."),
      ("By the RE itself at any time", "No."))
    H("Which cybersecurity function is mapped to the 'Withstand & Contain' goals?",
      "Respond", "Governance/Identify/Protect/Detect → Anticipate; Respond → Withstand & Contain; Recover → Recover.",
      ("Detect", "Anticipate."),
      ("Protect", "Anticipate."),
      ("Governance", "Anticipate."))
    H("Who approves the list of critical systems under CSCRF?",
      "The Board / Partner / Proprietor", "Identify function.",
      ("SEBI", "No."),
      ("CERT-In", "No."),
      ("The CISO alone", "No."))
    H("The Central Government may nominate how many persons to a stock exchange's governing board for recognition?",
      "Not more than three", "Recognition condition under SCRA.",
      ("Exactly one", "No."),
      ("Up to five", "No."),
      ("Half the board", "No."))
    H("Which body's members include representatives of MoF, MCA and RBI?",
      "IBBI", "Established 2016 under the Insolvency and Bankruptcy Code.",
      ("IFSCA", "Not stated this way."),
      ("PFRDA", "No."),
      ("IRDAI", "No."))
    H("IFSCA was established in ___ under the IFSCA Act of ___.",
      "2020; 2019", "Act 2019, authority set up 2020.",
      ("2019; 2020", "Reversed."),
      ("2016; 2016", "That's IBBI."),
      ("2015; 2013", "No."))
    H("Which is NOT a valid PFRDA fact?",
      "It was set up under an Act of 1999", "PFRDA Act is 2013; IRDA Act is 1999.",
      ("It regulates NPS", "True."),
      ("It registers pension intermediaries", "True."),
      ("It aims at old-age income security", "True."))
    H("SEBI's digital KYC accessibility directive for persons with disabilities is dated:",
      "May 2025", "SEBI circular 23 May 2025.",
      ("January 2022", "No."),
      ("August 2024", "That's CSCRF."),
      ("June 2020", "Sandbox."))
    H("KRAs share KYC data with each other through:",
      "Inter-operability process (IOP)", "So investors aren't asked again.",
      ("CKYC uploads", "Not stated."),
      ("NDS-OM", "G-sec trading."),
      ("SCORES", "Complaints."))
    H("SEBI (ICDR) Regulations, 2018 do NOT cover:",
      "Listing of non-convertible debt securities", "Debt is under SEBI (NCS) Regulations 2021.",
      ("Qualified Institutions Placement", "Covered."),
      ("Bonus issues", "Covered."),
      ("Indian Depository Receipts", "Covered."))
    H("SEBI (NCS) Regulations 2021 replaced which two regulations?",
      "Debt Securities Regs 2008 and NCRPS Regs 2013", "Merged and repealed on 9 Aug 2021.",
      ("ICDR 2009 and LODR 2015", "No."),
      ("Debt Securities Regs 2008 and Municipal Debt Regs 2015", "Municipal regs still exist."),
      ("CIS Regs 1999 and MF Regs 1996", "No."))
    H("Which onshore instruments did the Central Government declare as securities besides EGRs and ZCZPs?",
      "Rupee bonds of multilateral institutions like ADB and IFC", "Listed under 'other instruments' in 2(h).",
      ("Bank fixed deposits", "Not securities."),
      ("Company deposits", "Not securities."),
      ("Provident fund balances", "Not securities."))
    H("Which statement on dematerialisation is correct?",
      "Securities have been issued electronically since the mid-1990s", "Old certificates also converted.",
      ("Demat began in 2008 with SLBM", "No."),
      ("Only listed companies' debt is demat", "No."),
      ("Demat is optional for exchange trading", "Securities must be demat to trade."))
    H("Which is TRUE of custodians?",
      "They work with institutional investors and are usually large banks", "Hold securities and cash, settle, value portfolios.",
      ("They serve only retail investors", "No."),
      ("They are agents of depositories", "That's DPs."),
      ("They underwrite issues", "No."))
    H("Debenture trustees are appointed to:",
      "Protect lenders' interests", "MF trustees supervise AMCs; debenture trustees protect debenture holders.",
      ("Supervise AMCs", "That's MF trustees."),
      ("Rate the debentures", "CRAs do that."),
      ("Price the debentures", "No."))
    H("The SEBI code of conduct for intermediaries does NOT require:",
      "Guaranteeing returns to clients", "Key points: investor protection, fair service, no collusion, timely info, infrastructure.",
      ("Avoiding collusion with other intermediaries", "Required."),
      ("Timely information to clients", "Required."),
      ("Adequate infrastructure", "Required."))
    H("SEBI's penalties after investigation can include:",
      "Suspension, monetary penalty and prosecution", "Powers to penalise violators.",
      ("Only warnings", "Too weak."),
      ("Only monetary penalty", "Incomplete."),
      ("Cancellation of PAN", "No."))

    # ============================================================ CH 2
    C = 2
    S = lambda *a: Q(C, "S", *a)
    H = lambda *a: Q(C, "H", *a)
    S("Which is ranked last for profit sharing and liquidation proceeds?",
      "Equity shareholders", "Residual claim — after govt, lenders, employees and preference holders.",
      ("Lenders", "Paid before equity."),
      ("Employees", "Paid before equity."),
      ("Preference shareholders", "Paid before equity shareholders."))
    S("The reserves of a company rightfully belong to:",
      "Equity shareholders", "Retained profits belong to the owners.",
      ("Lenders", "No."),
      ("Promoters only", "All equity holders."),
      ("Employees", "No."))
    S("Analysts estimate intrinsic value at ₹50; the share trades at ₹35. The share is:",
      "Undervalued", "Intrinsic > price → undervalued.",
      ("Overvalued", "Reversed."),
      ("Fairly priced", "No."),
      ("At par", "Irrelevant."))
    S("Market interest rates rise after a 10% bond is issued at ₹100. The bond will likely quote:",
      "Below face value", "Price and yield move inversely.",
      ("Above face value", "That's when rates fall."),
      ("At face value", "No."),
      ("At a price set by the issuer", "Market decides."))
    S("The process of splitting surplus between equity and debt is called:",
      "Asset allocation", "Based on return, horizon, risk appetite, needs.",
      ("Diversification within a sector", "Second level, not this."),
      ("Rebalancing", "Related but not the term."),
      ("Hedging", "No."))
    S("Equity shares with higher dividend but fewer votes are called:",
      "DVR shares", "Differential voting rights shares.",
      ("Preference shares", "No voting, fixed dividend."),
      ("Bonus shares", "Free shares."),
      ("Sweat equity", "Not covered."))
    S("Unpaid preference dividend carried to later years applies to:",
      "Cumulative preference shares", "If terms allow.",
      ("Redeemable preference shares", "Not this feature."),
      ("Participating preference shares", "Not covered."),
      ("Convertible preference shares", "No."))
    S("Which is TRUE of preference shares vs debentures?",
      "Preference dividend is paid from profit after tax; debenture interest is a pre-tax expense", "Key difference.",
      ("Preference shares are usually secured", "Not a borrowing; unsecured."),
      ("Preference holders are creditors", "They are shareholders."),
      ("Debenture holders get voting rights", "No."))
    S("Typical face values of equity shares in India include:",
      "₹1, ₹2, ₹5 or ₹10", "Workbook list.",
      ("₹100 only", "No."),
      ("₹1,000", "Debt instruments often."),
      ("Any value set by SEBI", "No."))
    S("10,000 shares of FV ₹2 each give equity capital of:",
      "₹20,000", "10,000 × 2.",
      ("₹1,00,000", "That's FV ₹10."),
      ("₹2,00,000", "No."),
      ("₹10,000", "No."))
    S("In India, a bond usually refers to debt of:",
      "Government or public sector", "Private corporate debt = debenture; terms now interchangeable.",
      ("Private companies only", "Debenture."),
      ("Banks only", "No."),
      ("Foreign issuers", "No."))
    S("A zero coupon bond with a long maturity issued at a big discount is a:",
      "Deep discount bond", "Workbook term.",
      ("Step-up bond", "Rising coupons."),
      ("Amortising bond", "Principal over life."),
      ("Callable bond", "Issuer option."))
    S("A bond that lets the ISSUER redeem early is:",
      "Callable", "Issuer calls when rates fall.",
      ("Puttable", "Investor's option."),
      ("Amortising", "No."),
      ("Convertible", "No."))
    S("Home loans where each instalment includes principal and interest resemble:",
      "Amortising bonds", "Principal repaid over life.",
      ("Zero coupon bonds", "No."),
      ("Perpetual bonds", "No."),
      ("Deferred interest bonds", "No."))
    S("Treasury bills are issued for:",
      "91, 182 and 364 days", "Via RBI auctions.",
      ("30, 60 and 90 days", "No."),
      ("1, 3 and 5 years", "No."),
      ("7 days to 1 year", "That's CP/CD range."))
    S("The most popular maturity for commercial paper is:",
      "90 days", "CP up to 364 days; 90-day most popular.",
      ("7 days", "No."),
      ("364 days", "Maximum, not most popular."),
      ("180 days", "No."))
    S("Money market securities are generally:",
      "Issued at a discount and redeemed at par", "Zero-coupon structure.",
      ("Issued at par with semi-annual coupons", "That's dated G-secs."),
      ("Floating rate", "No."),
      ("Unlisted equity", "No."))
    S("What share of long-term debt market trading is in G-secs?",
      "Over 90%", "Concentrated in benchmark securities.",
      ("About 50%", "No."),
      ("About 70%", "That's financial sector's share of bond issuance."),
      ("Under 30%", "No."))
    S("Capital gains bonds that save tax are issued under Section:",
      "54EC", "By NHAI, NABARD, NHB etc.",
      ("80C", "ELSS etc."),
      ("10(10D)", "No."),
      ("80D", "No."))
    S("Masala bonds are:",
      "Rupee bonds issued abroad by Indian companies", "Currency risk on foreign investors.",
      ("Dollar bonds issued in India", "No."),
      ("Green bonds of PSUs", "No."),
      ("Tax-free municipal bonds", "No."))
    S("The first masala bond was issued by:",
      "IFC, listed on the London Stock Exchange", "Workbook fact.",
      ("SBI, listed on NSE", "No."),
      ("ADB, listed on SGX", "No."),
      ("RBI, listed in Dubai", "No."))
    S("Bharat Bond ETF tracks an index of:",
      "AAA-rated PSU bonds", "Nifty Bharat Bond Index; 5- and 11-year series.",
      ("G-secs", "No."),
      ("AA corporate bonds", "No."),
      ("Bank CDs", "No."))
    S("Which risk do G-secs NOT carry?",
      "Default (credit) risk", "Govt can tax, borrow or print money.",
      ("Interest rate risk", "They do."),
      ("Inflation risk", "They do."),
      ("Reinvestment risk", "Coupon bonds do."))
    S("ADRs are listed in:",
      "The USA", "GDRs elsewhere abroad; IDRs in India.",
      ("India", "IDRs."),
      ("Europe only", "GDRs."),
      ("Any country", "No."))
    S("DR holders get:",
      "Dividends and capital appreciation, but no voting rights", "Workbook point.",
      ("Voting rights only", "No."),
      ("Fixed interest", "No."),
      ("Full shareholder rights", "No votes."))
    S("Minimum maturity of an FCCB is:",
      "5 years", "Workbook rule.",
      ("3 years", "No."),
      ("1 year", "No."),
      ("10 years", "No."))
    S("Investors in warrants pay upfront:",
      "25% of the consideration", "Balance on exercise; forfeited if not exercised.",
      ("10%", "No."),
      ("50%", "No."),
      ("Nothing", "No."))
    S("Which commodities are 'bullion'?",
      "Gold and silver", "Base metals are copper, zinc etc.",
      ("Copper and zinc", "Base metals."),
      ("Crude oil and gas", "Energy."),
      ("Wheat and sugar", "Soft commodities."))
    S("PE ratio is:",
      "Market price per share ÷ EPS", "Valuation multiple.",
      ("EPS ÷ market price", "Earnings yield."),
      ("Market price ÷ book value", "PBV."),
      ("DPS ÷ market price", "Dividend yield."))
    S("A 40% dividend on FV ₹10 when price is ₹200 gives dividend yield of:",
      "2%", "Dividend ₹4; 4/200 = 2%.",
      ("40%", "That's on face value."),
      ("4%", "No."),
      ("20%", "No."))
    S("Top-down analysis begins with:",
      "Macro factors", "Then sectors, then stocks.",
      ("Individual stock selection", "Bottom-up."),
      ("Technical charts", "No."),
      ("Peer valuation", "No."))
    S("Current yield of a 12% bond priced at ₹109.50 is about:",
      "10.95%", "12 ÷ 109.5.",
      ("12%", "Coupon."),
      ("13.14%", "No."),
      ("9.50%", "No."))
    S("Studying price and volume charts is:",
      "Technical analysis", "Fundamental uses financial statements.",
      ("Fundamental analysis", "No."),
      ("DCF valuation", "No."),
      ("EIC analysis", "Fundamental framework."))
    S("Which investment suits 'capital preservation' best?",
      "Cash, bank deposits, ultra-short-term funds", "Workbook table.",
      ("Equity funds", "Growth."),
      ("Real estate", "Growth/income."),
      ("Gold", "Growth."))
    S("Futures and options are settled on a predetermined date called the:",
      "Expiry date", "Short shelf life.",
      ("Record date", "Corporate action."),
      ("Strike date", "No such term."),
      ("Pay-in date", "Settlement step."))
    S("With 10% margin on a ₹100 stock, a trader controls 10 shares with ₹100. Leverage is:",
      "10 times", "₹1,000 exposure on ₹100.",
      ("100 times", "No."),
      ("2 times", "No."),
      ("1 time", "No."))
    S("Commodity options in India are options on:",
      "Commodity futures", "Spot markets are state-regulated.",
      ("Spot commodities", "No."),
      ("Commodity ETFs", "No."),
      ("Commodity indices only", "No."))
    S("Individual stock futures and options in India are settled by:",
      "Physical delivery", "Index F&O are cash-settled.",
      ("Cash", "Index F&O."),
      ("Either, at buyer's choice", "No."),
      ("Rollover", "No."))
    S("ZCZP instruments give the funder:",
      "No financial return, only a social return", "Default if social impact not delivered.",
      ("Zero coupon but principal back", "No principal either."),
      ("Tax-free interest", "No."),
      ("Equity in the NPO", "No."))
    S("Structured products are most suitable for:",
      "HNIs with high risk appetite", "Complex, customised, illiquid.",
      ("Retail investors", "MFs suit them."),
      ("Retirees seeking income", "No."),
      ("Banks only", "No."))
    S("Distressed securities attract hedge funds mainly because:",
      "Banks, MFs and insurers must exit them, pushing prices to steep discounts", "Regulatory limits on low-rated holdings.",
      ("They are guaranteed by government", "No."),
      ("They pay fixed high coupons", "Not the reason."),
      ("They are listed only abroad", "No."))
    # ---- harder
    H("Borrowing at 12% and earning 14% on assets: who gets the extra 2%?",
      "Equity investors", "Lenders get only promised 12%.",
      ("Lenders", "No."),
      ("Government as tax", "No."),
      ("Split equally", "No."))
    H("Which factor favours EQUITY financing for an issuer?",
      "A services business with few assets to pledge", "No collateral → equity.",
      ("Stable profits to pay interest", "Favours debt."),
      ("Owners unwilling to dilute", "Favours debt."),
      ("Short-term working capital need", "Favours debt."))
    H("Which statement on convertible debentures is correct?",
      "Coupon is usually lower than pure debt because of conversion upside", "Issuer benefit; but existing holders diluted.",
      ("Interest continues after conversion", "Stops on conversion."),
      ("PCDs convert fully into equity", "That's FCD."),
      ("OCDs convert at issuer's option", "Holder's option."))
    H("Which is TRUE of IDRs?",
      "Available only to resident Indians, not FPIs", "SEBI guidelines.",
      ("Underlying is Indian shares listed abroad", "That's ADR/GDR."),
      ("Have no lock-in", "Lock-in on conversion exists."),
      ("Listed only on NYSE", "No."))
    H("FCCB issue expenses are capped at:",
      "4% for public issue, 2% for private placement", "Workbook.",
      ("2% public, 4% private", "Reversed."),
      ("1% for both", "No."),
      ("No cap", "No."))
    H("FCCBs are regulated by RBI under:",
      "FEMA and the 1993 FCCB & Depository Receipt Scheme", "Workbook.",
      ("SEBI ICDR 2018", "No."),
      ("Companies Act 1956", "No."),
      ("SCRA 1956", "No."))
    H("ABC trades at ₹180; 4,00,000 warrants at ₹220. Upfront payment is:",
      "₹2.20 crore", "25% × 4,00,000 × 220.",
      ("₹8.80 crore", "Full value."),
      ("₹1.80 crore", "Wrong price."),
      ("₹0.88 crore", "No."))
    H("Why do commodities diversify an equity-debt portfolio?",
      "They hedge inflation, so have low correlation with equity and debt", "Inflation hurts equity and debt.",
      ("They have no price risk", "False."),
      ("They pay fixed income", "No."),
      ("They are always liquid", "No."))
    H("Shares of a steel company are not a pure commodity play because of:",
      "Company-specific risks like debt, imports policy and competition", "Workbook example.",
      ("Steel prices being fixed", "No."),
      ("Absence of listing", "No."),
      ("SEBI ban on such shares", "No."))
    H("Book value per share is limited because:",
      "Assets are at cost less depreciation, not inflation-adjusted", "Doesn't show realisable value.",
      ("It includes market price", "No."),
      ("It excludes reserves", "Includes them."),
      ("It changes daily", "No."))
    H("In a bull market, dividend yields typically:",
      "Fall", "Prices rise faster.",
      ("Rise", "Bear market."),
      ("Stay constant", "No."),
      ("Turn negative", "Impossible."))
    H("Amit's 5-year 10% annual bond at 8% yield is worth about:",
      "₹107.98", "Sum of discounted flows.",
      ("₹100.00", "Only if yield = coupon."),
      ("₹92.42", "That's when yield > coupon."),
      ("₹110.00", "No."))
    H("A bond bought below face value has a yield:",
      "Higher than the coupon", "Discount adds return.",
      ("Lower than the coupon", "Premium case."),
      ("Equal to the coupon", "Only at par."),
      ("Of zero", "No."))
    H("Credit spreads usually:",
      "Widen in recessions and narrow in booms", "Risk perception changes.",
      ("Narrow in recessions", "Reversed."),
      ("Never change", "No."),
      ("Depend only on G-sec supply", "No."))
    H("When the interest rate cycle peaks, a debt investor should tilt toward:",
      "Gilt funds / long-dated G-secs", "Lock high yields before prices rise.",
      ("Credit risk funds", "Keep lowest in recession."),
      ("Liquid funds only", "No."),
      ("Overnight funds", "No."))
    H("Investors who can't judge interest rate moves are advised to use:",
      "Dynamic bond funds", "Workbook advice.",
      ("Credit risk funds", "No."),
      ("10-year gilt funds", "No."),
      ("Equity savings funds", "No."))
    H("Which is TRUE of relative valuation?",
      "It can carry valuation errors already in market prices", "Limitation.",
      ("It needs a discount rate", "DCF does."),
      ("It ignores market price", "Uses it."),
      ("It is harder to tweak than DCF", "Easier."))
    H("Which is NOT a feature of exchange-traded derivatives as per the workbook?",
      "They are fully funded instruments", "They are under-funded (margin only).",
      ("Contracts designed by exchanges, approved by regulator", "True."),
      ("Leveraged", "True."),
      ("Often more liquid than cash markets", "True."))
    H("Which currency pair is a cross-currency pair in Indian exchanges?",
      "EURUSD", "INR pairs: USDINR, EURINR, GBPINR, JPYINR.",
      ("USDINR", "INR pair."),
      ("GBPINR", "INR pair."),
      ("JPYINR", "INR pair."))
    H("Interest rate options in India are available on:",
      "Government securities", "IRF on G-secs, T-bills, MIBOR; IRO on G-secs.",
      ("MIBOR", "Futures only."),
      ("T-bills", "Futures only."),
      ("Corporate bonds", "No."))
    H("Which debt risk do investors who take regular payouts face?",
      "Reinvestment risk", "Coupons may be reinvested at lower rates.",
      ("Call risk", "Callable bonds."),
      ("Liquidity risk", "Different."),
      ("Default risk", "Different."))
    H("Why do unsecured company FDs pay more than secured bonds?",
      "Higher default risk — no recourse to assets", "Secured debt has lower risk.",
      ("They are tax-free", "No."),
      ("They are liquid", "No liquidity."),
      ("They are govt guaranteed", "No."))
    H("LMN NCD Series V (3-year cumulative) redeems ₹1,000 at:",
      "₹1,368.02", "Box 2.3.",
      ("₹1,295.40", "No."),
      ("₹1,000", "No."),
      ("₹1,100", "No."))
    H("Which instrument is in the money market but creates NO security?",
      "Inter-corporate deposits", "Call, term and ICDs excluded from securities.",
      ("Commercial paper", "Security."),
      ("Certificate of deposit", "Security."),
      ("Treasury bill", "Security."))
    H("Tri-party repo trades differ from regular repo because they:",
      "Are settled through a central counterparty", "CCIL/exchange guarantees.",
      ("Use only equity collateral", "No."),
      ("Have no margins", "CCP collects margins."),
      ("Are bilateral", "Regular repo is."))
    H("Exchange basket repo contracts on corporate bonds have tenor of:",
      "1 to 7 days", "Workbook.",
      ("1 to 30 days", "No."),
      ("Overnight only", "No."),
      ("Up to 1 year", "No."))
    H("Who selects securities eligible for exchange tri-party repo?",
      "The clearing corporation", "Workbook.",
      ("SEBI", "No."),
      ("RBI", "No."),
      ("The borrower", "No."))
    H("G-secs can have tenors of:",
      "1 to 40 years", "Workbook.",
      ("1 to 10 years", "No."),
      ("91 days to 30 years", "No."),
      ("5 to 50 years", "No."))
    H("Financial sector share of total corporate bond issuance is around:",
      "70%", "Manufacturing ~30%.",
      ("30%", "Manufacturing."),
      ("90%", "That's G-sec trading share."),
      ("50%", "No."))
    H("Which describes a 'sponsored' DR issue?",
      "Existing shareholders' shares are converted into DRs", "Fresh shares otherwise.",
      ("Company issues fresh shares for DRs", "Not sponsored."),
      ("Govt sponsors the DR", "No."),
      ("A bank sponsors and guarantees", "No."))
    H("Two-way fungibility of DRs means:",
      "Shares can become DRs and DRs can become shares", "Subject to regulation.",
      ("DRs trade on two exchanges", "No."),
      ("DRs pay two dividends", "No."),
      ("DRs can be in two currencies", "No."))
