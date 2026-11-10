from summary_lib import *

def add(chap, sub):
    chap(3, "Primary Markets", "20", 5)
    sub("Primary market — nature", 5,
      L("Issuers raise equity/debt from investors who buy <b>from the issuer</b>; 'new issue market'; 'going public'",
        "Private placement to a syndicate of institutions is also primary market (debt PP ≈ PE/VC deals but with debt)",
        "Issuer must work with a <b>merchant banker</b>: readiness, structuring, pricing, investor targeting, whole process, for a fee; may use syndicate / underwriting; distribution via brokers",
        "Securities (vs one-to-one deals) give outside investors regulatory protection, disclosure and exit via listing") +
      T(["Segment","Regulator"],
        [["Equity primary market","SEBI"],["Govt securities","RBI (auction, predefined calendar; banks, PDs)"],["Corporate bonds","SEBI (public or private placement)"],
         ["ADRs/GDRs","SEBI eligibility + <b>FEMA</b> foreign holding limits"]]))
    sub("Functions of the primary market", 5,
      T(["Function","Point"],
        [["Tap larger markets","Move beyond promoters/banks; e.g. GDR in Euro markets"],["Competitive pricing","Price by demand/supply; G-secs by auction"],
         ["Diversify ownership","Ownership and management separate; independent directors → better governance"],
         ["Better disclosure","Adequate, relevant, accurate, verifiable information"],
         ["Evaluation by investors","Extra scrutiny beyond auditors and regulators (analysts, media, activists)"],
         ["Exit for early investors","Promoters, PE, insiders sell at a profit"],
         ["Liquidity","Public issue must be listed → secondary trading"],["Regulatory supervision","Fair process, information, defined rights — no assurance of return"]]))
    sub("Primary vs secondary; market cycles", 4,
      L("Secondary trades don't change the issuer's capital; its prices guide primary pricing",
        "<b>Bull market</b> → more IPOs at higher, issuer-friendly prices; <b>bear market</b> → hard to get subscription"))
    sub("Primary market intermediaries", 5,
      T(["Intermediary","Role"],
        [["Merchant banker","Pricing advice, offer document, listing application, advertising, allotment; also underwriter for a commission"],
         ["Book Running Lead Manager (BRLM)","Due diligence, drafting/vetting prospectus, compliance, marketing; post-issue: basis of allotment, escrow, coordinate bankers &amp; registrars"],
         ["Registrar (RTA)","Records of applications &amp; money; helps basis of allotment; despatches allotment letters, refunds; STAs keep holdings, transfers, redemption, act as DPs"],
         ["Bankers to the issue","Accept applications + money, refund unsuccessful; daily records"],
         ["Brokers to the issue","Procure subscriptions; link investors and issuer"],
         ["Depository &amp; DP","Electronic holding by book entry; depository = <b>registered owner</b>, investor = <b>beneficial owner</b>; DP does dematerialisation"],
         ["Debenture trustee","Appointed <b>before</b> debt issue; checks secured assets suffice; calls meeting if <b>one-tenth</b> of holders ask or on default"],
         ["Portfolio manager","Discretionary (independent per client needs) or non-discretionary (as client directs)"],
         ["Primary dealer","<b>RBI</b>-licensed underwriters of G-secs; commission; resell in secondary market"]]) +
      K("All registered with <b>SEBI</b> except primary dealers (authorised by <b>RBI</b>)"))
    sub("Types of issues", 5,
      T(["Type","To whom"],
        [["Public issue","Anyone eligible"],["Private placement","Select institutions / eligible investors — wholesale"],
         ["Preferential issue","Identified investors on preferential terms: promoters, strategic investors, employees"],
         ["Rights issue","Existing holders on cut-off date buy more at set price"],["Bonus issue","Existing holders get shares <b>free</b>"]]) +
      K("A public issue often combines preferential, rights and private placement portions before retail opens"))
    sub("Types of issuers", 5,
      T(["Issuer","Securities","Notes"],
        [["Central, state, local govts","G-secs, T-bills, <b>Sovereign Gold Bonds</b>","No equity · only <b>Central Govt issues T-bills</b> · govt guarantee · domestic only"],
         ["PSUs","Equity, bonds","Disinvestment; bonds may carry tax concessions"],
         ["Private companies","Equity, preference, bonds, convertibles, CP, securitised paper","High reliance on markets; may issue abroad"],
         ["Banks, NBFCs, FIs","Equity, preference, bonds, convertibles, securitised paper, CP, CDs","Banks rely less on markets (deposits); Tier-2 capital via long bonds &amp; preference; may issue abroad"],
         ["Mutual funds","Units","Specific schemes; closed-end or open-ended; <b>domestic only</b>"],
         ["REITs, InvITs","Units","Specific schemes"]]) +
      K("From <b>1 Jan 2026</b> REIT units count as <b>equity-related</b> for MF investment; InvITs stay hybrid"))
    sub("Types of investors", 5,
      K("AOP · banks · companies · LLPs · FIs · MFs · insurers · FPIs · HUFs · minors via guardians · NRIs · PIOs · societies &amp; clubs · resident individuals · partnership firms · trusts") +
      T(["Category","Rule"],
        [["Retail Individual Investor (RII)","≤ <b>₹2 lakh</b> per issue"],["Non-Institutional Buyer (NIB)","&gt; ₹2 lakh per issue"],
         ["QIB","Institutions; internal governing-body approval; authorised staff transact"]]) +
      K("Debt markets dominated by institutions; equity has more retail","Foreign investors follow FX rules","Eligible investor categories stated in offer document"))
    sub("Regulatory framework", 5,
      L("Laws: <b>Companies Act 2013 · SCRA 1956 · SEBI (ICDR) Regs 2018 · Government Securities Act 2006 · Government Securities Regulations 2007</b>",
        "G-sec primary issue: <b>not under SEBI</b> (G-Sec Act &amp; Regs); CDs and CPs governed by RBI",
        "Cover: eligibility, disclosures, reservations, offer methods, timelines, use of funds, promoter accountability, ongoing evaluation and exit",
        "Issuer can't be a sole proprietorship, partnership or AOP; equity needs a <b>limited company</b> (MCA registration)",
        "Deposit-taking banks/FIs/NBFCs need RBI approval; MFs must be SEBI-registered",
        "Instruments must be securities (SCRA) or deposits (Banking Regulation Act 1949 / Companies (Acceptance of Deposits) Rules 1975)"))
    sub("IPO eligibility (ICDR)", 5,
      T(["Test (restated, consolidated)","Requirement"],
        [["Net tangible assets","≥ <b>₹3 crore</b> in each of preceding 3 full years; ≤ 50% monetary (else committed to use; limit waived if entirely OFS)"],
         ["Average operating profit","≥ <b>₹15 crore</b> over preceding 3 years, profit in <b>each</b> year"],
         ["Net worth","≥ <b>₹1 crore</b> in each of preceding 3 years"],
         ["Name change in last 1 yr","≥ 50% of last year's revenue from activity in new name"]]) +
      K("Fails the tests → only via <b>book building</b> with ≥ <b>75%</b> of net offer to QIBs, else full refund",
        "SR (superior voting) shares to promoters/founders → may IPO only ordinary shares on Main Board (main board = nationwide terminals, not SME exchange)"))
    sub("Promoters' contribution & lock-in", 5,
      T(["Item","Rule"],
        [["Minimum contribution","≥ <b>20%</b> of post-issue capital"],
         ["Shortfall","Up to <b>10%</b> of post-issue capital may come from AIFs, FVCIs, SCBs, PFIs, IRDAI insurers, non-individual holders with ≥ 5%, or promoter-group entities — without being promoters"],
         ["No identifiable promoter","Requirement does not apply"],["Form","Equity (incl. SR shares) or convertible securities"],
         ["Lock-in: minimum contribution","<b>18 months</b>; <b>3 years</b> if most proceeds (excl. OFS) go to capex"],
         ["Lock-in: excess holding","<b>6 months</b>; <b>1 year</b> if mainly capex"]]) +
      K("Capex = civil work, misc fixed assets, land, building, plant &amp; machinery"))
    sub("Minimum offer to public", 5,
      T(["Post-issue capital at offer price","Minimum public offer"],
        [["≤ ₹1,600 crore","<b>25%</b>"],["₹1,600 – 4,000 crore","Shares worth <b>₹400 crore</b>"],["₹4,000 – 50,000 crore","<b>10%</b> (SCR Amendment Rules 2026)"]]) +
      K("Companies in the last two slabs must reach <b>25%</b> public holding within <b>3 years</b> of listing",
        "Issuer with SR shares must list SR shares on the same exchange as ordinary shares"))
    sub("Issue period, underwriting, demat, IPO grading", 5,
      T(["Rule","Detail"],
        [["Issue period","Min <b>3</b>, max <b>10</b> working days"],["Price band revised","Extend by ≥ 3 working days (within max)"],
         ["Force majeure / bank strike","Extend by ≥ 1 working day, reasons in writing"],
         ["Minimum subscription","<b>90%</b> of net offer, else refund all within <b>4 days</b> of closure"],
         ["Underwriting","Fixed price: optional (SEBI merchant bankers/brokers); book built: <b>mandatory</b> by lead managers &amp; syndicate — but the 75% QIB portion can't be underwritten"],
         ["Demat","Agreement with <b>all depositories</b> required"],
         ["IPO grading","Optional; by SEBI-registered CRAs; <b>1 (poor) to 5 (strong)</b> fundamentals; not a view on price; publish all grades"]]))
    sub("IPO: fresh issue vs offer for sale", 5,
      T(["","Fresh issue","Offer for sale (OFS)"],
        [["Shares","New shares issued","Existing holders sell"],["Share capital","Rises","Unchanged"],["Money goes to","Company","Selling shareholders"],
         ["Example (1,000 shares, X &amp; Y 500 each)","Issue 500 → 1,500 shares; X, Y 33.33% each","Each sells 250 → X, Y 25% each, public 50%; capital stays ₹10,000"]]) +
      K("PSU disinvestment = OFS (proceeds to govt)","An IPO may combine both"))
    sub("Further public offer (FPO)", 4,
      L("Company already listed raises more from public",
        "Eligibility: no name change in last 1 year, or ≥ 50% revenue from new-name activity; else book building with ≥ 75% to QIBs",
        "Uses: growth capital, retire debt; OFS-based FPO to raise public shareholding or after promoter lock-in ends"))
    sub("Fixed price vs book building", 5,
      T(["","Fixed price","Book built"],
        [["Price","Set by issuer with lead manager; known at application","Discovered by bids within floor price or price band"],
         ["Bidding","—","Bid price and quantity; retail may revise while open"],
         ["Allotment","At fixed price","At <b>cut-off price</b>; bids at or above cut-off succeed"]]))
