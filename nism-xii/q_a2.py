"""Series XII quiz part A2: top-up for Ch1 and Ch2."""

def add(Q, inr, num):
    Q(1, "H", "Which pair is matched correctly?",
      "IRDAI — IRDA Act 1999; PFRDA — PFRDA Act 2013", "Insurance 1999, pensions 2013.",
      ("IRDAI — 2013; PFRDA — 1999", "Reversed."),
      ("IBBI — 2020; IFSCA — 2016", "Reversed: IBBI 2016, IFSCA 2020."),
      ("SEBI — 1956; RBI — 1992", "SEBI Act 1992; SCRA 1956."))
    C = 2
    S = lambda *a: Q(C, "S", *a)
    H = lambda *a: Q(C, "H", *a)
    S("Governments raise long-term capital by issuing:",
      "Only debt securities", "Governments never issue equity.",
      ("Equity and debt", "No equity."),
      ("Only equity", "No."),
      ("Depository receipts", "No."))
    S("Equity capital is also called risk capital because:",
      "Investors accept no fixed return and bear the business risk", "Workbook.",
      ("It must be repaid on a fixed date", "Debt."),
      ("It is secured on assets", "No."),
      ("It carries a fixed dividend", "No."))
    S("Promoters holding 5,100 of 10,000 shares have a:",
      "51% majority stake", "Stake = proportionate holding.",
      ("5.1% stake", "No."),
      ("Minority stake", "No."),
      ("Controlling stake of 100%", "No."))
    S("Large public companies are managed by:",
      "The board of directors and professional management", "Ownership and management separate.",
      ("All shareholders jointly", "Not feasible."),
      ("SEBI-appointed directors", "No."),
      ("Debenture trustees", "No."))
    S("Lenders protect their interests by covenants that may:",
      "Restrict further borrowing or unrelated diversification", "Control feature of debt.",
      ("Give them voting rights", "No."),
      ("Fix dividends to equity", "No."),
      ("Let them appoint the CEO", "No."))
    S("Floating-rate debt interest is reset with reference to a benchmark such as:",
      "MIBOR", "Workbook example.",
      ("The issuer's share price", "No."),
      ("The Sensex", "No."),
      ("Inflation in the US", "No."))
    S("A puttable bond gives:",
      "The investor the right to seek early redemption", "Useful when rates rise.",
      ("The issuer the right to redeem early", "Callable."),
      ("Conversion into equity", "Convertible."),
      ("Coupons that step up", "Step-up."))
    S("In a step-up bond, the coupon:",
      "Rises over time", "Low burden early.",
      ("Falls over time", "No."),
      ("Is deferred for 1–3 years", "Deferred interest bond."),
      ("Floats with MIBOR", "Floater."))
    S("Securities with maturity up to one year trade in the:",
      "Money market", "Longer ones in capital markets.",
      ("Capital market", "No."),
      ("Derivatives market", "No."),
      ("Primary market only", "No."))
    S("Certificates of deposit are issued by:",
      "Banks", "Short-term tradable deposits.",
      ("Companies", "CP."),
      ("Central Government", "T-bills."),
      ("Mutual funds", "No."))
    S("Fixed-coupon G-secs pay interest:",
      "Semi-annually", "Dated securities.",
      ("Monthly", "No."),
      ("Annually", "No."),
      ("At maturity only", "No."))
    S("The RBI publishes a G-sec issuance calendar every:",
      "Six months", "Half-yearly calendar.",
      ("Month", "No."),
      ("Year", "No."),
      ("Quarter", "No."))
    S("Interest from tax-free bonds issued by authorised PSUs is:",
      "Not taxable for the investor", "Workbook.",
      ("Taxed at 10%", "No."),
      ("Taxed as capital gains", "No."),
      ("Taxable after 3 years", "No."))
    S("Green debt securities fund:",
      "Renewable energy, clean transport and similar sustainable projects", "Part of ESG investing.",
      ("Only government deficits", "No."),
      ("Working capital", "No."),
      ("Share buybacks", "No."))
    S("Which is a benefit of debt for investors?",
      "Fixed income as a legal right", "And fixed tenor.",
      ("Unlimited upside", "Equity."),
      ("Voting rights", "No."),
      ("Protection against inflation", "Debt is vulnerable to inflation."))
    S("Debt instruments in India are issued for maturities from:",
      "7 days to 30 years", "Most common: 90 days to 7 years.",
      ("1 day to 5 years", "No."),
      ("1 year to 40 years", "G-sec range."),
      ("91 days to 364 days", "T-bills."))
    S("Intrinsic value of a share is:",
      "The discounted value of its future benefits", "Workbook definition.",
      ("Its face value", "No."),
      ("Its book value", "No."),
      ("Its last traded price", "That's price."))
    S("Sell-side research is done by:",
      "Broking houses", "Buy-side = institutional investors.",
      ("Mutual funds", "Buy-side."),
      ("Insurance companies", "Buy-side."),
      ("SEBI", "No."))
    S("YTM is the rate that:",
      "Equates the present value of a bond's cash flows to its price", "Standard yield quote.",
      ("Equals coupon ÷ price", "Current yield."),
      ("Equals coupon ÷ face value", "Coupon rate."),
      ("Is set by RBI", "No."))
    H("Which combination is TRUE for an equity investor's returns?",
      "Dividends plus change in market value", "Two forms of return.",
      ("Coupon plus principal", "Debt."),
      ("Fixed dividend plus bonus", "No."),
      ("Interest plus capital gains tax refund", "No."))
    H("Why are ETFs and MFs suited to retail commodity exposure?",
      "They avoid storage and insurance costs of physical holding", "Financialisation of commodities.",
      ("They guarantee commodity returns", "No."),
      ("They have no price risk", "No."),
      ("They are exempt from SEBI", "No."))
    H("Which is TRUE of ZCZP risk?",
      "It may 'default' if promised social impact isn't delivered", "Workbook point.",
      ("It defaults if interest isn't paid", "No interest."),
      ("It has credit rating of AAA always", "No."),
      ("It carries currency risk", "No."))
    H("The EGR ecosystem stages are:",
      "Creation, trading on Gold Exchange, conversion into physical gold", "Workbook.",
      ("Mining, refining, export", "No."),
      ("Import, storage, sale", "No."),
      ("Issue, coupon, maturity", "No."))
    H("Which SEBI regulation supports the EGR ecosystem?",
      "SEBI (Vault Managers) Regulations, 2022", "With SOPs for vault managers and depositories.",
      ("SEBI (Custodian) Regulations, 1996", "No."),
      ("SEBI (ICDR) 2018", "No."),
      ("SEBI (MF) Regulations, 1996", "No."))
    H("A 10-year 9.75% callable bond with call after 5 years and one day is called back when rates fall. The investor:",
      "Must reinvest at lower rates", "Call risk.",
      ("Gains extra coupons", "No."),
      ("Gets a higher redemption premium always", "Not stated."),
      ("Faces no risk", "No."))
    H("Why are T-bills and CMBs called zero coupon?",
      "They are issued at a discount and redeemed at par with no interim coupon", "Return = discount.",
      ("They pay zero return", "No."),
      ("Coupons are tax-free", "No."),
      ("They pay coupon only at maturity", "No coupon at all."))
    H("Which approach starts with a stock's business potential and then checks industry and macro?",
      "Bottom-up", "Top-down starts with macro.",
      ("Top-down", "No."),
      ("Technical", "No."),
      ("Relative valuation", "No."))
    H("Why can DCF valuations of the same stock differ widely between analysts?",
      "Different cash-flow estimates and discount rates", "Two key assumption sets.",
      ("Different face values", "No."),
      ("Different exchanges", "No."),
      ("DCF uses only market price", "No."))
