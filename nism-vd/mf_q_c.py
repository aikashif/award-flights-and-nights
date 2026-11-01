"""MF quiz part C: Ch1, Ch6, Ch11, Ch2, Ch3, Ch8."""

def add(Q, inr, num):
    # ============================================================ CH 1 INVESTMENT LANDSCAPE
    C = 1
    S = lambda *a: Q(C, "S", *a)
    H = lambda *a: Q(C, "H", *a)
    S("Saving differs from investing because investing:",
      "Deploys money into assets to earn a return", "Saving = setting aside; investing = putting it to work.",
      ("Means keeping cash at home", "That's saving (badly)."), ("Has no risk", "Investing carries risk."), ("Is only for the rich", "No."))
    S("Which risk means your return fails to keep pace with rising prices?",
      "Inflation risk", "Purchasing power erosion.",
      ("Credit risk", "Default."), ("Liquidity risk", "Selling difficulty."), ("Business risk", "Company-specific."))
    S("Bond prices fall when interest rates rise. This is:",
      "Interest rate risk", "Rates ↑ → prices ↓.",
      ("Reinvestment risk", "Opposite effect."), ("Credit risk", "Default."), ("Inflation risk", "No."))
    S("The risk that a bond issuer fails to pay interest or principal is:",
      "Credit (default) risk", "Issuer default.",
      ("Market risk", "Systematic."), ("Liquidity risk", "No."), ("Exchange rate risk", "No."))
    S("Which risk cannot be removed by diversification?",
      "Systematic (market) risk", "Affects the whole market.",
      ("Company-specific risk", "Diversifiable."), ("Concentration risk", "Diversifiable."), ("Business risk", "Diversifiable."))
    S("Which asset class gives ownership in a business?",
      "Equity", "Shareholders own the company.",
      ("Debt", "Lenders."), ("Gold", "Commodity."), ("Bank FD", "Deposit."))
    S("Which is a money market instrument?",
      "Treasury bill", "T-bills ≤ 364 days.",
      ("Equity share", "No."), ("10-year G-sec", "Long-term."), ("REIT unit", "No."))
    S("Commercial paper is issued by:",
      "Companies", "Short-term unsecured promissory note.",
      ("Banks", "Banks issue CDs."), ("RBI", "No."), ("Mutual funds", "No."))
    S("Strategic asset allocation means:",
      "A long-term mix of assets based on goals and risk profile", "Long-term policy mix.",
      ("Short-term tilts on market views", "Tactical."), ("Changing mix daily", "No."), ("Investing only in equity", "No."))
    S("Rebalancing a portfolio means:",
      "Bringing asset weights back to the target allocation", "Sell what grew, buy what lagged.",
      ("Selling everything", "No."), ("Adding a new asset class", "No."), ("Changing the goal", "No."))
    S("'Herd mentality' bias means:",
      "Following what others are doing", "Behavioural bias.",
      ("Holding losers too long", "Loss aversion."), ("Sticking to a past price", "Anchoring."), ("Seeking only supporting info", "Confirmation bias."))
    S("Holding on to losing investments to avoid booking a loss reflects:",
      "Loss aversion", "Losses hurt more than equal gains please.",
      ("Overconfidence", "No."), ("Herding", "No."), ("Recency bias", "No."))
    S("Risk capacity depends on:",
      "Age, income, wealth, dependants and time horizon", "Ability to take risk.",
      ("Only how the investor feels", "That's appetite."), ("Past fund returns", "No."), ("The distributor's view", "No."))
    S("A risk profile questionnaire helps classify an investor as:",
      "Conservative, moderate or aggressive", "Risk profiling.",
      ("Rich or poor", "No."), ("Resident or NRI", "Tax status."), ("Active or passive", "No."))
    S("Which asset is generally the most liquid?",
      "Liquid mutual fund / savings account", "Quick, low-cost conversion to cash.",
      ("Real estate", "Illiquid."), ("Unlisted shares", "Illiquid."), ("Private equity", "Illiquid."))
    for n, i in [(10, 6), (8, 7)]:
        H(f"Nominal return is {n}% and inflation is {i}%. Exact real return?",
          f"{((1+n/100)/(1+i/100)-1)*100:.2f}%", f"(1 + {n/100})/(1 + {i/100}) − 1.",
          (f"{n-i:.2f}%", "That's the approximation."), (f"{n+i:.2f}%", "Added."), (f"{n/i:.2f}%", "Divided."))
    for r in [8, 12]:
        H(f"Using the rule of 72, how many years does money take to double at {r}% a year?",
          f"About {72/r:.0f} years", f"72 ÷ {r} = {72/r:.0f}.",
          (f"About {100/r:.1f} years", "That's a rule of 100."), (f"About {r} years", "No."), (f"About {72*r/100:.1f} years", "Multiplied."))
    H("An investor anchors to a stock's ₹1,000 peak and won't sell at ₹700 despite poor prospects. Which bias?",
      "Anchoring", "Fixed on a past reference price.",
      ("Herding", "No."), ("Recency", "No."), ("Mental accounting", "No."))
    H("Which pair of risks move in opposite directions when rates change?",
      "Interest rate (price) risk and reinvestment risk", "Rates ↑: price falls but reinvestment improves.",
      ("Credit and liquidity risk", "No."), ("Market and business risk", "No."), ("Inflation and currency risk", "No."))
    H("A 35-year-old with high appetite but low capacity (no emergency fund, big EMIs). What should a distributor do first?",
      "Build an emergency fund and recommend within the lower risk capacity", "Suitability.",
      ("Recommend small caps as asked", "Ignores capacity."), ("Recommend sectoral funds", "Too risky."), ("Recommend nothing", "Can help."))
    H("Tactical asset allocation differs from strategic allocation because it:",
      "Makes short-term tilts based on market views", "Tactical vs strategic.",
      ("Never changes", "Strategic is long-term."), ("Ignores the investor", "No."), ("Is required by SEBI", "No."))
    H("Which instrument is issued at a discount and redeemed at face value?",
      "Treasury bill", "Discount instrument; return = discount.",
      ("Equity share", "No."), ("Floating rate bond", "Pays coupon."), ("Fixed deposit", "Pays interest."))
    H("An investor counts last year's bonus as 'free money' and takes high risks with it. Which bias?",
      "Mental accounting", "Treating money differently by source.",
      ("Anchoring", "No."), ("Confirmation bias", "No."), ("Herding", "No."))

    # ============================================================ CH 6 DISTRIBUTION
    C = 6
    S = lambda *a: Q(C, "S", *a)
    H = lambda *a: Q(C, "H", *a)
    S("To distribute mutual funds, an individual needs:",
      "NISM certification and an AMFI Registration Number (ARN)", "Certification + registration.",
      ("Only a bank account", "No."), ("SEBI IA registration", "That's for advisers."), ("A stock broker licence", "No."))
    S("The ARN is valid for:",
      "3 years, renewable through CPE", "Renew before expiry.",
      ("1 year", "No."), ("Lifetime", "No."), ("10 years", "No."))
    S("EUIN is required for:",
      "Each employee/salesperson of a distributor who interacts with investors", "Employee Unique Identification Number.",
      ("Each investor", "No."), ("Each AMC", "No."), ("Each scheme", "No."))
    S("Upfront commission to distributors is:",
      "Not allowed; only trail commission is paid", "Banned since Oct 2018.",
      ("Allowed up to 1%", "No."), ("Allowed for SIPs", "No."), ("Paid by investors", "No."))
    S("Distributor commission in a regular plan is paid:",
      "By the AMC out of the scheme's TER", "Regular plan TER includes distribution cost.",
      ("By investors separately", "No."), ("By SEBI", "No."), ("Through entry load", "Abolished."))
    S("An investor wants to change their distributor. They need:",
      "No NOC from the old distributor", "Investor can change freely.",
      ("NOC from old distributor", "Not required."), ("SEBI approval", "No."), ("To redeem first", "No."))
    S("A SEBI-registered investment adviser (RIA) is paid by:",
      "The client, as a fee", "RIAs don't take commission.",
      ("AMC commission", "That's MFD."), ("Exit loads", "No."), ("SEBI", "No."))
    S("RIAs typically recommend which plan?",
      "Direct plans", "No commission involved.",
      ("Regular plans", "MFD."), ("Only NFOs", "No."), ("Only ETFs", "No."))
    S("Which is a channel for buying mutual funds through stock exchanges?",
      "NSE NMF II / BSE StAR MF", "Exchange platforms.",
      ("NDS-OM", "G-sec platform."), ("SCORES", "Grievance."), ("NACH", "Mandate system."))
    S("MF Utilities (MFU) and MF Central are:",
      "Common platforms to transact across multiple AMCs", "Shared infrastructure.",
      ("SEBI departments", "No."), ("AMCs", "No."), ("Rating agencies", "No."))
    S("Incidental advice by a distributor means:",
      "Advice given as part of selling, without charging a fee", "MFDs can't charge advisory fees.",
      ("Fee-based financial planning", "RIA."), ("Portfolio management", "PMS."), ("Tax filing", "No."))
    S("Which distributor practice is prohibited?",
      "Rebating commission to investors", "Not allowed.",
      ("Risk profiling clients", "Required."), ("Disclosing commission", "Required."), ("Updating KYC", "Required."))
    S("Distributors must disclose to investors:",
      "Commissions they earn from the schemes they recommend", "Transparency.",
      ("Their personal portfolio", "No."), ("AMC profits", "No."), ("Other clients' details", "Never."))
    S("A bank employee selling MFs must have:",
      "NISM certification and an EUIN under the bank's ARN", "Bank as corporate distributor.",
      ("Nothing; banks are exempt", "No."), ("An RIA licence", "No."), ("A separate ARN for each branch", "No."))
    S("The NISM certification for new cadre distributors who sell simple products is:",
      "Series V-B", "Mutual Fund Foundation.",
      ("Series V-A", "Full MFD."), ("Series VIII", "Equity derivatives."), ("Series X-A", "Investment adviser."))
    # harder
    H("Which of these triggers AMC due diligence of a distributor?",
      "Presence in more than 20 locations", "Due diligence criteria.",
      ("Having 10 clients", "No."), ("Selling only debt funds", "No."), ("ARN issued last month", "No."))
    H("A distributor switches a client from Fund A to similar Fund B every few months for higher trail. This is:",
      "Churning — prohibited mis-selling", "Code of conduct breach.",
      ("Rebalancing", "Not with similar funds."), ("Allowed if client signs", "Still unethical."), ("Mandatory review", "No."))
    H("What happens to trail commission when an investor moves from a regular plan to a direct plan of the same scheme?",
      "Trail stops on the switched units; it's a redemption + purchase for tax", "Direct plan = no commission.",
      ("Trail continues", "No."), ("Trail doubles", "No."), ("Nothing; not allowed", "Allowed."))
    H("Which statement about execution-only platforms (EOPs) is correct?",
      "They facilitate transactions in direct plans without giving advice", "EOPs deal in direct plans.",
      ("They sell regular plans with advice", "That's an MFD."), ("They manage portfolios", "PMS."), ("They are exempt from KYC", "No."))
    H("A distributor's ARN expires and is not renewed. What happens?",
      "Cannot sell or earn commission on new business until renewed", "Valid ARN needed.",
      ("Nothing changes", "No."), ("Investors' units are frozen", "No."), ("AMC takes over clients", "No."))
    H("Why must a distributor risk-profile a client before recommending?",
      "To ensure product suitability and avoid mis-selling", "Code of conduct.",
      ("To calculate commission", "No."), ("For tax filing", "No."), ("To choose the RTA", "No."))
    H("Which combination is NOT allowed for one individual?",
      "Being an MFD earning commission and an RIA charging fees to the same/different clients", "SEBI separation.",
      ("Being an MFD with NISM certification", "Allowed."), ("Being an RIA using direct plans", "Allowed."), ("Being an MFD selling via exchange platforms", "Allowed."))
    H("Commissions paid to a distributor are visible to the investor in:",
      "The Consolidated Account Statement (CAS)", "CAS discloses commission.",
      ("The factsheet only", "No."), ("Never", "Disclosed."), ("SEBI annual report", "No."))
    H("An investor wants advice for a fee and lowest-cost products. Best route?",
      "SEBI-registered investment adviser using direct plans", "Fee-only advice.",
      ("MFD with regular plans", "Commission model."), ("Stock broker tips", "No."), ("NFO marketing", "No."))
    H("A corporate distributor's employee sells without an EUIN. The problem?",
      "Accountability for advice can't be traced to the salesperson", "EUIN purpose.",
      ("No problem", "There is."), ("Transaction is invalid always", "Can be 'execution-only' with declaration."), ("Investor pays more", "No."))

    # ============================================================ CH 11 SCHEME PERFORMANCE
    C = 11
    S = lambda *a: Q(C, "S", *a)
    H = lambda *a: Q(C, "H", *a)
    for rp, rf, sd in [(15, 7, 16), (12, 6, 8), (18, 7, 22)]:
        sh = (rp-rf)/sd
        S(f"A fund returned {rp}% with standard deviation {sd}%. Risk-free rate is {rf}%. Sharpe ratio?",
          f"{sh:.2f}", f"(Rp − Rf) ÷ σ = ({rp} − {rf}) ÷ {sd} = {sh:.2f}.",
          (f"{rp/sd:.2f}", "You forgot to subtract Rf."), (f"{(rp-rf)*sd/100:.2f}", "Multiplied."), (f"{(rp+rf)/sd:.2f}", "Rf is subtracted."))
    for rp, rf, b in [(14, 6, 1.2), (11, 5, 0.8)]:
        tr = (rp-rf)/b
        S(f"A fund returned {rp}% with beta {b}. Risk-free rate {rf}%. Treynor ratio?",
          f"{tr:.2f}", f"(Rp − Rf) ÷ β = ({rp} − {rf}) ÷ {b} = {tr:.2f}.",
          (f"{(rp-rf)*b:.2f}", "Multiplied by beta."), (f"{rp/b:.2f}", "Forgot Rf."), (f"{rp-rf:.2f}", "Forgot beta."))
    S("Total Return Index (TRI) benchmarks include:",
      "Price changes plus dividends reinvested", "TRI mandatory since 2018.",
      ("Only price changes", "That's price return index."), ("Only dividends", "No."), ("Fund expenses", "No."))
    S("Tracking error is mainly used to evaluate:",
      "Index funds and ETFs", "Deviation from index.",
      ("Credit risk funds", "No."), ("Arbitrage funds", "No."), ("Liquid funds", "No."))
    S("For index funds, a lower tracking error means:",
      "Better index replication", "Lower = closer to index.",
      ("Worse performance", "Opposite."), ("Higher risk", "No."), ("Higher alpha", "Passive funds don't target alpha."))
    S("Sharpe ratio uses which risk measure?",
      "Standard deviation", "Total risk.",
      ("Beta", "Treynor."), ("Duration", "Debt."), ("Downside deviation", "Sortino."))
    S("Treynor ratio uses which risk measure?",
      "Beta", "Market risk.",
      ("Standard deviation", "Sharpe."), ("Tracking error", "Information ratio."), ("Credit rating", "No."))
    S("Alpha in simple terms is:",
      "Fund return minus benchmark return", "Excess return.",
      ("Fund return minus risk-free rate", "Excess over Rf."), ("Beta × market return", "No."), ("Expense ratio", "No."))
    S("Fund performance should be compared with:",
      "Its benchmark and peer funds in the same category", "Like-for-like.",
      ("Any fund with higher return", "No."), ("Bank FD only", "No."), ("Gold prices", "No."))
    S("Which is a qualitative factor in judging a fund?",
      "Fund manager's experience and investment process", "Qualitative.",
      ("Sharpe ratio", "Quantitative."), ("Beta", "Quantitative."), ("Tracking error", "Quantitative."))
    S("R-squared close to 100% means the fund's returns:",
      "Are largely explained by the benchmark", "Index-like behaviour.",
      ("Beat the benchmark", "No."), ("Are random", "No."), ("Have no risk", "No."))
    S("A reliable source of scheme performance data is:",
      "The AMC factsheet and AMFI website", "Official sources.",
      ("Social media tips", "No."), ("WhatsApp forwards", "No."), ("Unverified blogs", "No."))
    # harder
    for rp, rf, b, rm in [(16, 6, 1.1, 14), (12, 5, 0.9, 13)]:
        exp = rf + b*(rm-rf); ja = rp - exp
        H(f"Fund return {rp}%, beta {b}, market return {rm}%, risk-free {rf}%. Jensen's alpha?",
          f"{ja:+.1f}%", f"Expected (CAPM) = {rf} + {b} × ({rm} − {rf}) = {exp:.1f}%. Alpha = {rp} − {exp:.1f} = {ja:+.1f}%.",
          (f"{rp-rm:+.1f}%", "That's simple excess over market, not Jensen's."), (f"{rp-rf:+.1f}%", "Excess over Rf."), (f"{-ja:+.1f}%", "Sign reversed."))
    H("Fund A: Sharpe 0.8, Fund B: Sharpe 0.5, same category. Which is better risk-adjusted?",
      "Fund A", "Higher Sharpe = more return per unit of risk.",
      ("Fund B", "Lower Sharpe."), ("Equal", "No."), ("Need NAV levels", "No."))
    H("When is Treynor ratio more appropriate than Sharpe?",
      "For a well-diversified portfolio where unsystematic risk is negligible", "Treynor uses beta.",
      ("For a concentrated portfolio", "Sharpe better."), ("For liquid funds", "No."), ("Never", "It has uses."))
    H("Information ratio is:",
      "Excess return over benchmark ÷ tracking error", "Consistency of outperformance.",
      ("Return ÷ beta", "Treynor."), ("Return ÷ SD", "Sharpe-like."), ("Beta ÷ alpha", "No."))
    H("A fund has upside capture 110% and downside capture 80%. This means:",
      "It gains more than the benchmark in rises and falls less in declines", "Good asymmetric profile.",
      ("It falls more than the benchmark", "Downside 80% = falls less."), ("It's an index fund", "No."), ("It has no risk", "No."))
    H("Index fund A tracking difference −0.3%, tracking error 0.1%; fund B −0.2%, TE 0.8%. Which tracks better day to day?",
      "Fund A (lower tracking error)", "TE measures consistency of tracking.",
      ("Fund B", "Higher TE."), ("Both same", "No."), ("Can't tell", "TE answers it."))
    H("Why is comparing a mid cap fund's return with Nifty 50 TRI misleading?",
      "Different investment universe and risk; mid cap should be compared with a mid cap index", "Benchmark must match universe.",
      ("Nifty 50 is not published", "It is."), ("TRI is always lower", "No."), ("It isn't misleading", "It is."))
    H("A fund's 1-year return is top quartile but its 5-year rolling return is bottom quartile. Conclusion?",
      "Recent performance isn't consistent; look at longer, rolling data", "Consistency matters.",
      ("It's the best fund", "Recency bias."), ("Buy immediately", "No."), ("Rolling returns don't matter", "They do."))
    H("Sortino ratio is preferred over Sharpe when:",
      "An investor cares mainly about downside volatility", "Sortino uses downside deviation.",
      ("Returns are all positive", "Not the reason."), ("The fund is an ETF", "No."), ("Beta is high", "No."))

    # ============================================================ CH 2 CONCEPT & ROLE
    C = 2
    S = lambda *a: Q(C, "S", *a)
    H = lambda *a: Q(C, "H", *a)
    S("A mutual fund in India is set up as a:",
      "Trust", "SEBI-registered trust.",
      ("Company", "AMC is a company; MF is a trust."), ("Partnership", "No."), ("Co-operative", "No."))
    S("An open-ended scheme:",
      "Allows purchase and redemption on any business day at NAV", "Continuous liquidity.",
      ("Has a fixed maturity and must be listed", "Close-ended."), ("Opens only at intervals", "Interval."), ("Has no NAV", "No."))
    S("A close-ended scheme must be:",
      "Listed on a stock exchange", "For investor exit before maturity.",
      ("Open for daily redemption", "Open-ended."), ("Unlisted", "No."), ("Sold only in NFO and never traded", "Listed."))
    S("A passive fund aims to:",
      "Replicate an index", "Index fund/ETF.",
      ("Beat the index by stock picking", "Active."), ("Guarantee returns", "No."), ("Hold only cash", "No."))
    S("Which is an advantage of mutual funds?",
      "Professional management and diversification", "Core advantages.",
      ("Guaranteed returns", "No."), ("Customised portfolio for each investor", "Limitation."), ("No costs", "There are costs."))
    S("Which is a limitation of mutual funds?",
      "No customisation of the portfolio for individual investors", "Limitation.",
      ("Daily NAV", "Advantage."), ("Diversification", "Advantage."), ("SEBI regulation", "Advantage."))
    S("A Fund of Funds (FoF) invests in:",
      "Units of other mutual fund schemes", "Two layers of cost.",
      ("Shares directly", "No."), ("Only gold", "Gold FoF is one type."), ("Bank deposits", "No."))
    S("The first mutual fund in India was:",
      "Unit Trust of India (UTI), set up in 1963", "UTI Act 1963; US-64 first scheme.",
      ("SBI Mutual Fund", "First non-UTI, 1987."), ("Kothari Pioneer", "First private, 1993."), ("LIC MF", "No."))
    S("The first private sector mutual fund in India was:",
      "Kothari Pioneer (1993)", "Private sector entry 1993.",
      ("UTI", "Public."), ("SBI MF", "Public sector, 1987."), ("HDFC MF", "Later."))
    S("UTI was split into UTI MF and SUUTI in:",
      "2003", "Phase IV.",
      ("1987", "Public sector entry."), ("1993", "Private entry."), ("2009", "Entry load ban."))
    S("An ETF differs from an index fund mainly because an ETF:",
      "Trades on the stock exchange during market hours", "Exchange traded; demat.",
      ("Is actively managed", "Usually passive."), ("Has no NAV", "Has NAV and iNAV."), ("Can't be sold", "No."))
    S("'Mutual Funds Sahi Hai' is:",
      "AMFI's investor awareness campaign (2017)", "Industry campaign.",
      ("A SEBI regulation", "No."), ("A scheme name", "No."), ("A tax rule", "No."))
    # harder
    H("Why may a close-ended scheme trade at a discount to its NAV on the exchange?",
      "Low liquidity and demand on the exchange", "Exchange price ≠ NAV.",
      ("SEBI fixes a discount", "No."), ("NAV is wrong", "No."), ("Exit load", "No."))
    H("Which feature makes MF returns 'pass-through'?",
      "Gains and losses belong to unitholders; the AMC only earns fees", "Investors bear results.",
      ("AMC guarantees returns", "No."), ("Trustees keep profits", "No."), ("Sponsors absorb losses", "No."))
    H("An FoF investing in overseas funds carries which extra cost feature?",
      "Two layers of expenses (FoF + underlying fund)", "Double cost.",
      ("No expenses", "No."), ("Lower tax always", "No."), ("Guaranteed currency gain", "No."))
    H("Which classification is by structure, not asset class?",
      "Open-ended, close-ended, interval", "Structure types.",
      ("Equity, debt, hybrid", "Asset class."), ("Active, passive", "Management style."), ("Growth, IDCW", "Options."))
    H("Why are mutual funds called tax-efficient compared with direct trading?",
      "No tax is paid inside the fund on its trades; investors pay only on redemption", "Tax deferral.",
      ("MFs are tax-free", "No."), ("All gains are exempt", "No."), ("No STT ever", "No."))
    H("Interval schemes are a mix of:",
      "Open-ended and close-ended features", "Periodic liquidity + listing.",
      ("Equity and debt", "That's hybrid."), ("Active and passive", "No."), ("Direct and regular", "Plans."))
    H("A fund's AUM rises because markets went up, with no new investment. This is:",
      "Mark-to-market appreciation", "AUM = NAV × units.",
      ("New subscriptions", "None."), ("NFO", "No."), ("Exit loads", "No."))
    H("The SEBI rule of 'one scheme per category per AMC' does NOT apply to:",
      "Index funds, ETFs, FoFs and sectoral/thematic funds", "Exceptions.",
      ("Large cap funds", "Applies."), ("Liquid funds", "Applies."), ("ELSS", "Applies."))

    # ============================================================ CH 3 LEGAL STRUCTURE
    C = 3
    S = lambda *a: Q(C, "S", *a)
    H = lambda *a: Q(C, "H", *a)
    S("Who sets up a mutual fund (like a promoter)?",
      "Sponsor", "Sponsor creates trust and AMC.",
      ("Trustees", "They supervise."), ("AMC", "Manages."), ("Custodian", "Holds assets."))
    S("Who manages the investments of a mutual fund?",
      "Asset Management Company (AMC)", "AMC manages money.",
      ("Trustees", "Supervise."), ("Custodian", "Safekeeping."), ("RTA", "Records."))
    S("Who protects unitholders' interests and supervises the AMC?",
      "Trustees", "Guardians of investors.",
      ("Sponsor", "Promoter."), ("Distributor", "Sells."), ("RTA", "Records."))
    S("Who holds the securities of a mutual fund in safekeeping?",
      "Custodian", "Safekeeping and settlement.",
      ("AMC", "Manages, doesn't hold."), ("RTA", "Records."), ("SEBI", "Regulator."))
    S("Minimum net worth of an AMC is:",
      "₹50 crore", "Must be maintained at all times.",
      ("₹10 crore", "Old figure."), ("₹100 crore", "No."), ("₹5 crore", "No."))
    S("A sponsor must contribute at least what % of the AMC's net worth?",
      "40%", "Sponsor stake.",
      ("26%", "No."), ("51%", "No."), ("10%", "No."))
    S("At least what proportion of trustees must be independent?",
      "Two-thirds", "2/3 independent.",
      ("One-half", "AMC board rule."), ("One-third", "No."), ("All", "No."))
    S("At least what proportion of an AMC's board must be independent?",
      "50%", "AMC board.",
      ("Two-thirds", "Trustees."), ("One-third", "No."), ("None", "No."))
    S("AMFI is best described as:",
      "The industry association of mutual funds (not an SRO)", "Set up 1995.",
      ("The regulator", "SEBI."), ("A government ministry", "No."), ("A stock exchange", "No."))
    # harder
    H("Which agreement appoints the AMC to manage the fund?",
      "Investment Management Agreement (IMA) between trustees and AMC", "IMA.",
      ("Trust deed between sponsor and AMC", "Trust deed is sponsor + trustees."), ("Custody agreement", "Custodian."), ("Distribution agreement", "Distributors."))
    H("Under the traditional route, which is a sponsor eligibility condition?",
      "Profit in at least 3 of the last 5 years, including the latest", "Track record.",
      ("Losses allowed in all years", "No."), ("Only foreign sponsors", "No."), ("Net worth of ₹1 crore", "Too low."))
    H("Why must the custodian be independent of the sponsor?",
      "To avoid conflict of interest in safekeeping investors' assets", "Independence.",
      ("To reduce fees", "No."), ("To speed up NAV", "No."), ("SEBI owns custodians", "No."))
    H("Who appoints the AMC, and who can remove it?",
      "Trustees appoint; trustees (with SEBI/unitholder approval) can remove", "Trustee powers.",
      ("Sponsor alone", "Through trustees."), ("Distributors", "No."), ("RTA", "No."))
    H("How often must trustees meet at a minimum?",
      "Six times a year (about once every two months)", "Trustee meetings.",
      ("Once a year", "No."), ("Every week", "No."), ("Only when SEBI asks", "No."))
    H("Which regulator besides SEBI may oversee a bank-sponsored mutual fund's sponsor?",
      "RBI", "Bank sponsors are RBI-regulated.",
      ("IRDAI", "Insurance."), ("PFRDA", "Pensions."), ("CCI", "Competition."))

    # ============================================================ CH 8 TAXATION
    C = 8
    S = lambda *a: Q(C, "S", *a)
    H = lambda *a: Q(C, "H", *a)
    S("An equity-oriented fund for tax must invest at least what % in domestic listed equity?",
      "65%", "Equity-oriented definition.",
      ("80%", "ELSS minimum."), ("35%", "Old debt cut-off."), ("50%", "No."))
    S("STCG on equity-oriented funds (held ≤12 months) is taxed at (after 23 July 2024):",
      "20%", "Section 111A.",
      ("15%", "Old rate."), ("12.5%", "LTCG rate."), ("Slab rate", "Debt."))
    S("LTCG on equity-oriented funds (held >12 months) is taxed at:",
      "12.5% on gains above ₹1.25 lakh a year", "Section 112A.",
      ("10% above ₹1 lakh", "Old rule."), ("20% with indexation", "Old non-equity rule."), ("Nil", "Taxable."))
    S("Capital gains on debt funds bought on or after 1 April 2023 are taxed:",
      "At slab rate, whatever the holding period", "Specified MF rules.",
      ("At 12.5% after 24 months", "Not for these."), ("At 20% with indexation", "Old rule."), ("Tax-free", "No."))
    S("IDCW received from mutual funds is taxed:",
      "In the investor's hands at the slab rate", "Since 1 Apr 2020 (DDT abolished).",
      ("Tax-free", "No."), ("At 10% flat", "That's TDS, not tax rate."), ("Only for NRIs", "No."))
    S("ELSS investments qualify for deduction under:",
      "Section 80C, up to ₹1.5 lakh (old regime)", "80C.",
      ("Section 80D", "Health insurance."), ("Section 10(10D)", "Insurance maturity."), ("Section 24", "Home loan interest."))
    S("A long-term capital loss can be set off against:",
      "Long-term capital gains only", "LTCL vs LTCG only.",
      ("Any income", "No."), ("Salary", "No."), ("STCG only", "No."))
    S("Unabsorbed capital losses can be carried forward for:",
      "8 assessment years", "If return filed on time.",
      ("4 years", "No."), ("Indefinitely", "No."), ("1 year", "No."))
    S("Switching from a regular plan to the direct plan of the same scheme is:",
      "Treated as redemption — capital gains may arise", "Transfer for tax.",
      ("Tax-free", "No."), ("Not allowed", "Allowed."), ("Taxed as IDCW", "No."))
    # harder
    for g in [300000, 180000]:
        tax = max(0, g-125000)*0.125
        H(f"An investor has LTCG of {inr(g)} from equity funds in a year (no other equity gains). Tax (before cess)?",
          inr(tax), f"(Gain − 1,25,000) × 12.5% = {inr(tax)}.",
          (inr(g*0.125), "Forgot the ₹1.25 lakh exemption."), (inr(max(0,g-100000)*0.10), "Old rule (10% above ₹1 lakh)."), (inr(g*0.20), "STCG rate."))
    H("Dividend stripping rules ignore the loss if units are bought within 3 months before the record date and sold within:",
      "9 months after the record date", "Sec 94(7).",
      ("3 months", "No."), ("12 months", "No."), ("1 month", "No."))
    H("TDS on IDCW for resident investors applies at 10% when IDCW in a year from one AMC exceeds:",
      "₹10,000 (from April 2025; earlier ₹5,000)", "Sec 194K.",
      ("₹1 lakh", "No."), ("₹50,000", "No."), ("No TDS for residents", "There is."))
    H("For SIP units, the holding period for capital gains is counted:",
      "Separately for each instalment, on a first-in-first-out basis", "Each SIP is a purchase.",
      ("From the first SIP date for all units", "No."), ("From the last SIP date", "No."), ("Not counted", "No."))
    H("Equity bought before 1 Feb 2018 gets grandfathering. Cost of acquisition is:",
      "Higher of actual cost and (lower of FMV on 31 Jan 2018 and sale price)", "Grandfathering formula.",
      ("Actual cost only", "No."), ("FMV on 31 Jan 2018 always", "Partly."), ("Sale price", "No."))
