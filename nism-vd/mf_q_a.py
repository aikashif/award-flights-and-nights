"""MF quiz part A: Ch9 Investor Services, Ch12 Scheme Selection."""

def add(Q, inr, num):
    # ============================================================ CH 9 INVESTOR SERVICES
    C = 9
    S = lambda *a: Q(C, "S", *a)
    H = lambda *a: Q(C, "H", *a)
    S("What is the maximum period for which an NFO (other than ELSS) can remain open?",
      "15 days", "SEBI caps NFO subscription at 15 days. ELSS is the exception.",
      ("30 days", "That's the exit window for fundamental attribute changes."),
      ("7 days", "Too short; the cap is 15 days."),
      ("45 days", "No such NFO limit."))
    S("Within how many business days of NFO closure must units be allotted?",
      "5 business days", "Allotment (and refunds, if any) must be done within 5 business days of the NFO closing.",
      ("3 business days", "That's the redemption payout timeline."),
      ("7 business days", "That's the IDCW payout timeline."),
      ("15 days", "That's the NFO open period."))
    S("Redemption proceeds must be sent to the investor within:",
      "3 working days", "SEBI requires redemption payment within 3 working days of the request (some exceptions for overseas schemes).",
      ("7 working days", "That's for IDCW."),
      ("10 working days", "That was the old rule; it's now 3 working days."),
      ("5 business days", "That's NFO allotment."))
    S("IDCW must be paid to unitholders within how many working days of the record date?",
      "7 working days", "IDCW payout deadline is 7 working days from the record date.",
      ("3 working days", "That's redemption."),
      ("15 days", "Not the IDCW rule."),
      ("30 days", "Too long."))
    S("If an AMC delays redemption or IDCW payment beyond the deadline, it must pay the investor interest at:",
      "15% per annum", "Delay attracts interest at 15% p.a. for the delay period, paid by the AMC.",
      ("The scheme's YTM", "No — a fixed 15% p.a."),
      ("The bank savings rate", "Too low; the rule is 15% p.a."),
      ("Nothing, as delays are allowed", "Delays carry a penalty interest."))
    S("For an equity scheme, a purchase application with funds realised before 3:00 pm gets:",
      "The NAV of the same day", "Equity/debt: cut-off 3 pm. Same-day NAV if funds are realised before cut-off.",
      ("The previous day's NAV", "That's for liquid/overnight purchases."),
      ("The next day's NAV", "Only if after cut-off or funds realise later."),
      ("The NFO price of ₹10", "Ongoing purchases are at NAV."))
    S("What is the cut-off time for purchases in liquid and overnight funds?",
      "1:30 pm", "Liquid/overnight purchase cut-off is 1:30 pm; NAV of the day before funds are realised.",
      ("3:00 pm", "That's for equity/debt purchases and all redemptions."),
      ("12:00 noon", "Not the rule."),
      ("5:00 pm", "Not the rule."))
    S("A liquid fund purchase with funds realised before 1:30 pm on Wednesday gets the NAV of:",
      "Tuesday", "Liquid/overnight purchases get the NAV of the day before the day funds are realised.",
      ("Wednesday", "That's the equity rule."),
      ("Thursday", "That's if realised after cut-off."),
      ("The previous Friday", "No."))
    S("For any mutual fund purchase, units are allotted at the applicable NAV based on:",
      "The time the funds are realised in the scheme's account", "Since Feb 2021, NAV applies on realisation of funds for all purchase amounts.",
      ("The time the cheque is signed", "No."),
      ("The time the application is printed", "No."),
      ("The NFO date", "No."))
    S("KYC for mutual funds is done:",
      "Once, through a KYC Registration Agency (KRA), and is valid across intermediaries", "One-time KYC with a KRA; other MFs and intermediaries rely on it.",
      ("Separately for each AMC", "KYC is centralised via KRAs."),
      ("Every year", "It is one-time (updated when details change)."),
      ("Only for investments above ₹10 lakh", "KYC is needed for all investors (except PEKRN micro-investments without PAN)."))
    S("Which document is mandatory for KYC?",
      "PAN", "PAN is mandatory for KYC (with a few exceptions like PEKRN micro-investments and Sikkim residents).",
      ("Passport", "Optional as address proof."),
      ("Voter ID", "Optional as address proof."),
      ("Driving licence", "Optional as address proof."))
    S("An investor without PAN can invest under the micro-investment (PEKRN) route up to:",
      "₹50,000 per year", "Micro investments including micro-SIP: up to ₹50,000 per year per investor without PAN.",
      ("₹10,000 per year", "Limit is ₹50,000."),
      ("₹1 lakh per year", "Limit is ₹50,000."),
      ("No limit", "There is a ₹50,000 limit."))
    S("In a minor's folio, who can be a joint holder?",
      "No one — the minor must be the sole holder", "A minor's folio is single-holder; the guardian operates it.",
      ("The guardian", "Guardian operates the folio but is not a joint holder."),
      ("Either parent", "No joint holding allowed."),
      ("A sibling", "No joint holding allowed."))
    S("When a minor turns 18, what must happen to the folio?",
      "Status changes to major with the new major's KYC and bank details", "Until the change, transactions are stopped; the major must complete KYC and update details.",
      ("It is closed and redeemed automatically", "No; status is changed."),
      ("The guardian continues to operate it", "Guardian's authority ends at majority."),
      ("Nothing changes", "Status must be changed."))
    S("Who can make a nomination in a mutual fund folio?",
      "Individuals holding units singly or jointly", "Nomination is for individual holders; non-individuals and POA holders can't nominate.",
      ("Companies and trusts", "Non-individuals can't nominate."),
      ("Power of attorney holders", "A POA holder can't nominate on the investor's behalf."),
      ("Only joint holders", "Single holders can nominate too (and must, or opt out)."))
    S("A nominee in a mutual fund folio is best described as:",
      "A trustee who receives the units for the legal heirs", "Units go to the nominee on the holder's death; legal heirs may still claim from the nominee.",
      ("The legal owner beyond all heirs", "The nominee holds for the legal heirs."),
      ("A joint holder", "A nominee is not a joint holder."),
      ("The distributor", "No."))
    S("In a joint folio, if one holder dies, the units go to:",
      "The surviving joint holder(s)", "Transmission to surviving holders comes first; nominee comes in only on death of all holders.",
      ("The nominee", "Nominee gets units only on death of all joint holders."),
      ("The legal heirs of the deceased", "Survivors get the units first."),
      ("The AMC", "No."))
    S("How many holders can a mutual fund folio have at most?",
      "3", "Up to 3 holders in a folio.",
      ("2", "Up to 3 allowed."),
      ("4", "Max is 3."),
      ("10", "That's the nominee limit."))
    S("Which payment is a 'third-party payment' that is NOT allowed?",
      "A friend pays from their account for your purchase", "Third-party payments are banned except for listed cases.",
      ("A parent pays ₹30,000 for a minor child's purchase", "Allowed exception (≤ ₹50,000 per transaction)."),
      ("An employer deducts SIP from salary on the employee's behalf", "Allowed exception."),
      ("A custodian pays for an FPI client", "Allowed exception."))
    S("Up to how much can an investor invest in cash per mutual fund in a financial year (subject to KYC)?",
      "₹50,000", "Cash investments are allowed up to ₹50,000 per investor per MF per FY.",
      ("₹2 lakh", "Too high."),
      ("₹10,000", "Too low."),
      ("No cash allowed", "Cash is allowed within the limit."))
    S("A Systematic Investment Plan (SIP) means:",
      "Investing a fixed amount at regular intervals", "SIP = regular fixed investment; gives rupee-cost averaging.",
      ("Withdrawing a fixed amount regularly", "That's SWP."),
      ("Moving money from one scheme to another regularly", "That's STP."),
      ("Investing a lump sum once a year", "Not SIP."))
    S("A Systematic Withdrawal Plan (SWP) is mainly used to:",
      "Get regular cash flow from an existing investment", "SWP redeems a fixed amount at regular intervals.",
      ("Invest regularly", "That's SIP."),
      ("Switch between plans", "That's a switch."),
      ("Avoid all tax", "Each SWP redemption can have capital gains."))
    S("A Systematic Transfer Plan (STP) is typically used to:",
      "Move a lump sum gradually from a liquid/debt fund into an equity fund", "STP phases entry into equity while the balance earns in a debt fund.",
      ("Withdraw money to a bank account", "That's SWP."),
      ("Buy shares directly", "STP moves money between MF schemes."),
      ("Pledge units", "Not STP."))
    S("Rupee-cost averaging through SIP means:",
      "More units are bought when NAV is low and fewer when NAV is high", "A fixed rupee amount buys more units at low NAV, so average cost ≤ average NAV.",
      ("Units are always bought at the lowest NAV", "SIP doesn't time the market."),
      ("The NAV is averaged by the AMC", "NAV is market-driven."),
      ("Returns are guaranteed", "No guarantee."))
    S("A switch from one scheme to another of the same AMC is treated for tax as:",
      "A redemption from one scheme and a purchase in the other", "Switch = sale + purchase, so capital gains apply.",
      ("No transaction at all", "It is a transfer for tax."),
      ("A gift", "No."),
      ("Only a purchase", "It's both."))
    S("The Consolidated Account Statement (CAS) for a month with any transaction is sent by:",
      "The 15th of the following month", "Monthly CAS by the 15th of next month for months with transactions.",
      ("The 5th of the following month", "No."),
      ("The end of the quarter", "No."),
      ("Once a year", "No."))
    S("Which of these appears in the CAS?",
      "Commission paid to the distributor and the scheme's TER", "CAS shows holdings, transactions, commission paid and TER.",
      ("The fund manager's salary", "Not in CAS."),
      ("The AMC's profit", "Not in CAS."),
      ("Other investors' holdings", "Never."))
    S("Who maintains investor records such as purchases, redemptions and statements?",
      "Registrar and Transfer Agent (RTA)", "RTAs (e.g. CAMS, KFintech) keep investor records.",
      ("Custodian", "Custodian holds securities."),
      ("Trustees", "Trustees supervise."),
      ("SEBI", "Regulator."))
    S("Investors can hold mutual fund units in demat form. This means:",
      "Units are credited to a demat account through a depository participant", "Demat holding is optional for most schemes; ETFs must be in demat.",
      ("Units must be sold on the exchange only", "Demat units can usually also be redeemed via the AMC/DP."),
      ("Units are converted into shares", "No."),
      ("No account statement is needed", "Depository sends statements."))
    S("A tax status 'NRI' investor investing on a repatriable basis must pay from:",
      "An NRE account (or FCNR)", "Repatriable investments come from NRE/FCNR accounts.",
      ("An NRO account", "NRO is non-repatriable."),
      ("Cash", "No."),
      ("A minor's account", "No."))
    S("Which investor category is NOT allowed to invest in Indian mutual funds?",
      "Overseas Corporate Bodies (OCBs)", "OCBs have been barred since 2003.",
      ("NRIs", "Allowed."),
      ("FPIs", "Allowed."),
      ("HUFs", "Allowed through the Karta."))
    # Ch9 harder
    H("An investor submits a ₹5 lakh equity fund purchase at 2:30 pm Monday by NEFT, but the money reaches the scheme's account at 4:00 pm Monday. Which NAV applies?",
      "Tuesday's NAV", "NAV depends on realisation of funds. Funds arrived after the 3 pm cut-off, so next business day's NAV.",
      ("Monday's NAV", "The application was early, but funds realised after cut-off."),
      ("Friday's NAV", "No backdating."),
      ("Wednesday's NAV", "Too late; next business day after realisation."))
    H("A liquid fund redemption request is received at 2:45 pm on Thursday (Friday is a business day). Which NAV applies?",
      "Thursday's NAV (the day before the next business day)", "Liquid redemption: cut-off 3 pm, NAV of the day before the next business day = Thursday.",
      ("Friday's NAV", "That would be for requests after cut-off."),
      ("Wednesday's NAV", "That's the purchase rule logic misapplied."),
      ("Monday's NAV", "No."))
    H("A grandparent wants to pay ₹40,000 from their own account for a grandchild's (minor) folio. Is this allowed?",
      "Yes — it is a permitted third-party payment for a minor up to ₹50,000 per transaction, with declarations",
      "Parents/grandparents/relatives may pay for a minor up to ₹50,000 per transaction with KYC and a declaration.",
      ("No — all third-party payments are banned", "This is a listed exception."),
      ("Yes, without any limit", "There is a ₹50,000 per transaction cap."),
      ("Only if paid in cash", "Cash isn't the point; the exception covers bank payments."))
    H("A single holder dies without a nominee. The units are worth ₹12 lakh. To whom and how are they transmitted?",
      "To the legal heir(s), with documents such as succession certificate or probate as required", "No nominee/joint holder → legal heirs; higher values need stronger legal documents.",
      ("To the distributor", "Never."),
      ("To the AMC as unclaimed", "Heirs can claim."),
      ("To the eldest child automatically", "Legal heirs as per law/will."))
    H("An investor with a joint folio (A and B, 'either or survivor') and nominee C. A dies. What happens?",
      "B continues as sole holder; C gets the units only if B also dies", "Survivor takes precedence; nominee comes in after all holders die.",
      ("C gets A's half", "Units aren't split for a nominee while a joint holder survives."),
      ("Units are redeemed and paid to C", "No."),
      ("The folio is frozen till courts decide", "Survivor continues."))
    H("An investor wants ₹6 lakh moved into an equity fund over 12 months without timing the market and while earning on the idle balance. Best option?",
      "Invest in a liquid fund and set up an STP into the equity fund", "STP from liquid to equity phases the entry while the balance earns liquid returns.",
      ("SWP from the equity fund", "SWP withdraws money."),
      ("Lump sum in equity today", "Doesn't phase the entry."),
      ("SIP from a savings account in 12 instalments", "Works, but idle money earns only savings interest."))
    H("Why does SWP often give better post-tax cash flow than IDCW for a retired investor?",
      "Only the gains part of each SWP redemption is taxed; IDCW is fully taxed at slab", "SWP redemptions contain capital + gain; tax only on gain portion.",
      ("SWP is tax-free", "Gains in SWP are taxed."),
      ("IDCW is guaranteed", "IDCW is not guaranteed."),
      ("SWP has no exit load ever", "Exit load can apply depending on scheme rules."))
    H("A distributor's client invests via SIP. NAVs on 3 SIP dates: ₹10, ₹8, ₹12; ₹1,200 each time. What is the average cost per unit?",
      "₹9.73", "Units = 120 + 150 + 100 = 370. Cost ₹3,600 ÷ 370 = ₹9.73 (below the average NAV of ₹10).",
      ("₹10.00", "That's the simple average NAV, not average cost."),
      ("₹12.00", "That's the last NAV."),
      ("₹8.00", "That's the lowest NAV."))
    H("An NRI investor wants to invest in an Indian MF on a non-repatriable basis. Which account and statement is correct?",
      "Pay from an NRO account; proceeds are generally not freely repatriable", "Non-repatriable = NRO.",
      ("Pay from NRE; proceeds non-repatriable", "NRE is repatriable."),
      ("Pay in foreign currency cash", "No."),
      ("NRIs can't invest", "They can."))
    H("Which of these is NOT a reason for an AMC to reject a purchase application?",
      "The investor chose the direct plan", "Choosing direct is the investor's right.",
      ("PAN/KYC not complied", "Valid reason."),
      ("Third-party cheque without exception", "Valid reason."),
      ("Cheque bounced", "Valid reason."))
    H("An investor changes their bank mandate and requests redemption the same day. What protects them against fraud?",
      "AMCs verify the new bank details and may pay to the old/verified account during a cooling period", "Bank change requests are verified; payouts follow safeguards.",
      ("Redemption is cancelled automatically", "Not cancelled."),
      ("Money is paid in cash", "Never cash for redemption."),
      ("Nothing; changes are instant", "Safeguards exist."))
    H("An investor holds units in demat and also in a statement-of-account form for the same scheme. Which statement is TRUE?",
      "Demat units show in the depository statement; SOA units in the CAS/RTA statement — both are valid holdings", "Both forms co-exist.",
      ("Only demat units are valid", "SOA units are valid."),
      ("Demat units can't be redeemed", "They can, via DP/exchange or AMC."),
      ("SOA units must be converted", "Optional."))
    H("A minor's folio has a monthly SIP running. The minor turns 18 next month. What happens to the SIP?",
      "SIPs for minors are registered only till the date of majority; it stops unless the major updates status", "SIP end is capped at majority.",
      ("It continues automatically for 10 years", "No."),
      ("The guardian becomes the holder", "No."),
      ("It converts into an SWP", "No."))
    H("Which combination correctly lists the KYC status categories used by KRAs?",
      "Validated, Registered, On hold", "KRAs classify records by verification level.",
      ("Approved, Rejected, Pending", "Not the KRA categories."),
      ("Gold, Silver, Bronze", "No."),
      ("Active, Dormant, Closed", "Those are account states."))
    H("In a liquid fund, an investor redeems after 3 days. What applies?",
      "A graded exit load for redemptions within 7 days", "Liquid funds carry a small graded exit load for days 1–6.",
      ("No load ever in liquid funds", "There is a graded load up to day 6."),
      ("1% exit load", "Too high; it's a small graded load."),
      ("Redemption not allowed for 7 days", "Redemption is allowed."))
    H("Which of these requires a fresh KYC/status update rather than just a change request?",
      "A minor becoming a major", "The new major must do their own KYC.",
      ("Change of mobile number", "Simple update."),
      ("Change of email", "Simple update."),
      ("Adding a nominee", "Simple form."))
    H("An investor's redemption is paid on day 6 (deadline day 3). Redemption value ₹2,00,000. Approximate interest due for 3 days' delay?",
      "About ₹247", "₹2,00,000 × 15% × 3/365 ≈ ₹247.",
      ("About ₹740", "That's 9 days."),
      ("About ₹82", "That's 1 day."),
      ("About ₹30,000", "That's a full year at 15%."))
    H("Unclaimed redemption/IDCW amounts are:",
      "Deployed in a separate plan; after 3 years investors get the value then, and the balance goes to investor education", "SEBI rules for unclaimed amounts.",
      ("Taken by the AMC as income", "Never."),
      ("Paid to the distributor", "Never."),
      ("Forfeited after 1 year", "No."))
    H("Which statement about nomination opt-out is correct?",
      "New single-holder investors must either nominate or sign an explicit opt-out declaration", "Opt-out is allowed but must be declared.",
      ("Nomination is optional and can be left blank", "A declaration is needed."),
      ("Only joint holders must nominate", "Single holders must decide."),
      ("Opt-out is not allowed", "It is allowed with declaration."))

    # ============================================================ CH 12 SCHEME SELECTION
    C = 12
    S = lambda *a: Q(C, "S", *a)
    H = lambda *a: Q(C, "H", *a)
    for cat, rule, w in [
        ("large cap fund", "At least 80% in large cap stocks", [("At least 65% in large cap stocks", "65% is mid/small cap."), ("At least 35% each in large and mid cap", "That's large & mid cap."), ("Any market cap", "That's flexi cap.")]),
        ("mid cap fund", "At least 65% in mid cap stocks", [("At least 80% in mid cap stocks", "80% is for large cap."), ("At least 25% in mid cap", "That's multi cap."), ("Only mid cap stocks, 100%", "Minimum is 65%.")]),
        ("small cap fund", "At least 65% in small cap stocks", [("At least 80% in small cap stocks", "80% is large cap."), ("At least 25% in small cap", "That's multi cap."), ("At most 30 stocks", "That's focused.")]),
        ("multi cap fund", "At least 25% each in large, mid and small cap", [("At least 65% equity in any market cap", "That's flexi cap."), ("At least 35% each in large and mid cap", "That's large & mid cap."), ("At least 80% in large cap", "That's large cap.")]),
        ("flexi cap fund", "At least 65% in equity, across market caps freely", [("At least 25% each in large, mid and small", "That's multi cap."), ("At least 80% in one sector", "That's sectoral."), ("At most 30 stocks", "That's focused.")]),
        ("large & mid cap fund", "At least 35% each in large cap and mid cap", [("At least 25% each in large, mid, small", "That's multi cap."), ("At least 80% in large cap", "That's large cap."), ("At least 65% in mid cap", "That's mid cap.")]),
        ("focused fund", "At most 30 stocks", [("At least 80% in large cap", "That's large cap."), ("At most 10 stocks", "Limit is 30."), ("At least 65% in one sector", "Sectoral is 80%.")]),
        ("ELSS", "At least 80% in equity with a 3-year lock-in", [("At least 65% in equity with a 5-year lock-in", "5-yr lock-in is for solution-oriented."), ("No lock-in", "ELSS has 3 years."), ("At least 80% in debt", "ELSS is equity.")]),
        ("sectoral/thematic fund", "At least 80% in the chosen sector or theme", [("At least 65% in the sector", "It's 80%."), ("At most 30 stocks", "That's focused."), ("Any allocation", "No.")]),
    ]:
        S(f"Under SEBI's categorisation, a {cat} must invest:", rule, "SEBI scheme categorisation (Oct 2017).", *w)
    for cat, rule, w in [
        ("overnight fund", "Securities with 1-day maturity", [("Up to 91 days maturity", "That's liquid."), ("Macaulay duration 3–6 months", "That's ultra short."), ("Up to 1 year maturity", "That's money market.")]),
        ("liquid fund", "Debt and money market securities with maturity up to 91 days", [("1-day securities only", "That's overnight."), ("Macaulay duration 1–3 years", "That's short duration."), ("Up to 1 year maturity", "That's money market.")]),
        ("ultra short duration fund", "Macaulay duration of 3 to 6 months", [("6 to 12 months", "That's low duration."), ("1 to 3 years", "That's short duration."), ("Up to 91 days maturity", "That's liquid.")]),
        ("short duration fund", "Macaulay duration of 1 to 3 years", [("3 to 4 years", "That's medium."), ("6 to 12 months", "That's low duration."), ("Over 7 years", "That's long duration.")]),
        ("long duration fund", "Macaulay duration over 7 years", [("4 to 7 years", "That's medium to long."), ("3 to 4 years", "That's medium."), ("Any duration", "That's dynamic bond.")]),
        ("corporate bond fund", "At least 80% in AA+ and above rated corporate bonds", [("At least 65% in AA and below", "That's credit risk."), ("At least 80% in G-secs", "That's gilt."), ("At least 80% in bank/PSU debt", "That's banking & PSU.")]),
        ("credit risk fund", "At least 65% in corporate bonds rated AA and below", [("At least 80% in AA+ and above", "That's corporate bond fund."), ("At least 80% in G-secs", "That's gilt."), ("At least 65% in floating rate", "That's floater.")]),
        ("gilt fund", "At least 80% in government securities", [("At least 80% in AA+ bonds", "Corporate bond."), ("At least 65% in G-secs", "It's 80%."), ("Any debt", "No.")]),
        ("floater fund", "At least 65% in floating rate instruments", [("At least 80% in floating rate", "It's 65%."), ("At least 80% in G-secs", "Gilt."), ("Duration over 7 years", "Long duration.")]),
    ]:
        S(f"Under SEBI's categorisation, a {cat} invests in:", rule, "SEBI debt scheme categories.", *w)
    for cat, rule, w in [
        ("conservative hybrid fund", "10–25% equity, rest debt", [("40–60% equity", "Balanced hybrid."), ("65–80% equity", "Aggressive hybrid."), ("0–100% equity", "BAF.")]),
        ("aggressive hybrid fund", "65–80% equity", [("10–25% equity", "Conservative."), ("40–60% equity", "Balanced."), ("At least 25% each in 3 assets", "No.")]),
        ("balanced advantage / dynamic asset allocation fund", "Equity–debt mix changed dynamically, 0–100%", [("Fixed 50:50", "Not fixed."), ("65–80% equity", "Aggressive."), ("At least 65% arbitrage", "Arbitrage fund.")]),
        ("multi-asset allocation fund", "At least 3 asset classes, minimum 10% in each", [("At least 2 asset classes, 25% each", "Wrong numbers."), ("Only equity and debt", "Needs 3."), ("At least 65% arbitrage", "No.")]),
        ("equity savings fund", "At least 65% equity (incl. hedged) and at least 10% debt", [("10–25% equity", "Conservative hybrid."), ("At least 80% equity", "No."), ("Only arbitrage", "No.")]),
    ]:
        S(f"A {cat} has:", rule, "SEBI hybrid categories.", *w)
    S("Solution-oriented schemes (retirement and children's funds) have a lock-in of:",
      "5 years (or till retirement / child turns 18, whichever is earlier)", "Both have 5-year lock-in with the stated earlier-of condition.",
      ("3 years", "That's ELSS."), ("1 year", "No."), ("No lock-in", "They have one."))
    S("An investor needs money for an emergency at short notice with minimal risk. Best choice:",
      "Liquid or overnight fund", "Very short duration, low risk, quick redemption.",
      ("Small cap fund", "High volatility."), ("Long duration gilt fund", "High interest rate risk."), ("ELSS", "3-year lock-in."))
    S("An investor expects interest rates to fall sharply. Which debt fund benefits most?",
      "Long duration / gilt fund", "Longer duration = bigger price gain when rates fall.",
      ("Overnight fund", "Almost no duration."), ("Floater fund", "Coupons reset lower; little price gain."), ("Liquid fund", "Tiny duration."))
    S("An investor expects interest rates to rise. Which debt fund suits best?",
      "Floater or short duration fund", "Low duration limits price loss; floaters reset coupons upward.",
      ("Long duration fund", "Biggest losses when rates rise."), ("Gilt 10-year constant duration", "Duration ~10 years."), ("Dynamic bond fund locked long", "Still exposed."))
    S("Which plan is best for an investor who needs no advice and wants the lowest cost?",
      "Direct plan", "No distributor commission → lower TER → higher NAV.",
      ("Regular plan", "Includes distribution cost."), ("IDCW option", "Option, not plan."), ("NFO", "Not a plan."))
    S("Which option is generally better for long-term wealth creation and tax deferral?",
      "Growth option", "Gains compound in NAV; tax only on redemption.",
      ("IDCW payout", "Taxed at slab each time."), ("IDCW reinvestment", "Still taxed as IDCW."), ("Bonus option", "Not standard."))
    S("Compared with an index fund, an ETF:",
      "Trades on the exchange at market prices and needs a demat account", "ETFs trade intraday; index funds deal with AMC at NAV.",
      ("Is bought from the AMC at end-of-day NAV only", "That's the index fund."), ("Has no tracking error", "Both have some."), ("Is always actively managed", "ETFs here are passive."))
    S("A first-time equity investor nervous about market falls may be suited to:",
      "Balanced advantage fund", "BAF adjusts equity exposure by valuation, reducing volatility.",
      ("Small cap fund", "High volatility."), ("Sectoral fund", "Concentrated."), ("Credit risk fund", "Debt with credit risk."))
    S("Who should invest in sectoral/thematic funds?",
      "Investors who understand the sector and can accept high concentration risk", "Concentration makes them high risk.",
      ("All beginners", "Not suitable."), ("Retirees needing income", "Unsuitable."), ("Emergency savers", "Unsuitable."))
    S("An investor wants to save tax under Sec 80C with equity exposure and the shortest lock-in. Choice:",
      "ELSS", "3-year lock-in, shortest among 80C products.",
      ("PPF", "15 years."), ("Retirement fund", "5-year lock-in, not 80C unless notified."), ("Liquid fund", "No 80C."))
    S("Target maturity funds are best described as:",
      "Passive debt funds that hold bonds maturing near a fixed date", "Defined maturity; roll-down reduces rate risk if held to maturity.",
      ("Equity funds with a target return", "No target return."), ("Close-ended equity funds", "No."), ("Guaranteed-return schemes", "No guarantee."))
    S("Which measure tells you a debt fund's sensitivity to interest rate changes?",
      "Modified duration", "%ΔNAV ≈ −MD × Δyield.",
      ("YTM", "Yield, not sensitivity."), ("Expense ratio", "Cost."), ("Beta", "Equity measure."))
    S("When comparing two large cap funds, the fairest comparison uses:",
      "Same category, same period, risk-adjusted returns and costs", "Compare like with like.",
      ("A large cap vs a small cap fund's returns", "Different risk."), ("NAV levels", "NAV level is meaningless."), ("Fund age only", "Not enough."))
    S("An investor with a 1-year horizon wants equity-like taxation with low risk. Suitable choice:",
      "Arbitrage fund", "Arbitrage funds hedge equity; taxed as equity; low volatility.",
      ("Small cap fund", "Too risky."), ("Long duration fund", "Debt tax, rate risk."), ("ELSS", "Lock-in 3 years."))
    # Ch12 harder
    H("A 28-year-old with stable income, 20+ year goal, high risk appetite. Most suitable core holding?",
      "Flexi cap or index fund with long-term SIP", "Long horizon + high capacity → equity core.",
      ("Liquid fund", "Too conservative."), ("Conservative hybrid", "Too conservative for horizon."), ("Credit risk fund", "Debt with credit risk; not core equity."))
    H("A 62-year-old retiree needs monthly income and capital safety. Most suitable approach?",
      "Short-duration/conservative hybrid fund with an SWP", "Low risk + regular cash flow via SWP.",
      ("Small cap fund with IDCW", "High risk; IDCW not assured."), ("Sectoral fund", "Concentrated."), ("Long duration gilt", "Rate risk for income need."))
    H("Two debt funds: A has YTM 7.8% and MD 1.5; B has YTM 8.6% and MD 1.6 with mostly A-rated paper. What does B's higher YTM most likely reflect?",
      "Higher credit risk", "Similar duration, higher yield → lower credit quality.",
      ("Better fund management", "Yield gap is from risk."), ("Lower interest rate risk", "Durations are similar."), ("Guaranteed higher return", "YTM isn't guaranteed."))
    H("An investor will need money in exactly 3 years and wants predictable debt returns. Best fit?",
      "Target maturity fund maturing in about 3 years", "Held to maturity, return ≈ YTM at entry (minus costs).",
      ("Long duration fund", "Mismatch."), ("Small cap fund", "Too volatile."), ("Overnight fund", "Reinvestment risk; lower yield."))
    H("Which is the BIGGEST red flag when selecting a small cap fund?",
      "Very large AUM relative to the liquidity of its holdings", "Large small-cap AUM creates liquidity risk in redemptions.",
      ("Moderate expense ratio", "Normal."), ("Fund manager with 10 years' tenure", "Positive."), ("Benchmark is Nifty Smallcap 250 TRI", "Correct benchmark."))
    H("An investor holds 6 large cap funds. What is the main problem?",
      "Heavy portfolio overlap with little extra diversification", "Same category funds hold similar stocks.",
      ("Too little diversification across stocks", "It's over-diversified/duplicated."), ("Tax is higher", "Not the main issue."), ("Large cap is illegal", "No."))
    H("A fund beat its benchmark by 2% but had double the benchmark's volatility. What should you check?",
      "Risk-adjusted measures such as Sharpe ratio", "Excess return may just reflect excess risk.",
      ("Only the NAV", "Meaningless."), ("Fund launch date", "Not the issue."), ("AUM only", "Not enough."))
    H("An investor chooses IDCW payout from an equity fund 'for regular income'. What should a distributor point out?",
      "IDCW is not assured, comes from the investor's own capital/gains, and is taxed at slab; an SWP may suit better", "IDCW = capital withdrawal.",
      ("IDCW is guaranteed monthly", "Not guaranteed."), ("IDCW is tax-free", "Taxed at slab."), ("IDCW increases NAV", "NAV falls by IDCW."))
    H("An investor wants international diversification. What extra risk must be explained?",
      "Currency risk (INR vs foreign currency) and overseas investment limits", "International funds add currency risk.",
      ("No risk because markets are diversified", "Still risky."), ("Credit risk only", "Not the main extra risk."), ("Lock-in of 5 years", "No such lock-in."))
    H("BAF vs aggressive hybrid: key difference?",
      "BAF changes equity exposure dynamically (0–100%); aggressive hybrid keeps 65–80% equity", "Dynamic vs fixed band.",
      ("BAF is debt-only", "No."), ("Aggressive hybrid has no equity", "It has 65–80%."), ("They are identical", "No."))
    H("A scheme's PRC is B-III. What does it tell you?",
      "Moderate credit risk and relatively high interest rate risk (any duration)", "B = moderate credit; III = high interest rate risk.",
      ("Lowest credit and rate risk", "That's A-I."), ("High credit risk, low rate risk", "That's C-I."), ("It is an equity fund", "PRC is for debt."))
    H("Which combination best suits a 2-year goal for a moderate-risk investor?",
      "Short duration / banking & PSU fund, perhaps with some conservative hybrid", "2-yr horizon → short-to-medium debt.",
      ("Pure small cap", "Too risky for 2 years."), ("Overnight fund only", "Too low return over 2 years."), ("Long duration gilt", "Rate risk mismatch."))
    H("An investor asks for the 'cheapest' NFO at ₹10 vs an existing fund at NAV ₹150. Correct advice?",
      "NAV level doesn't make a fund cheap or expensive; compare strategy, portfolio and costs", "NAV is just accumulated value.",
      ("Buy the NFO; more units means more return", "Units count doesn't matter."), ("Buy the ₹150 fund; higher NAV is better", "NAV level isn't quality."), ("NFOs are always better", "No."))
    H("Why are passive funds often preferred for large cap exposure?",
      "Few active large cap funds consistently beat the index after costs, and passive costs are low", "Efficient large cap market + low TER.",
      ("Passive funds have no risk", "They have market risk."), ("Passive funds guarantee index return plus 2%", "No."), ("Large cap active funds are banned", "No."))
    H("Which situation best fits a credit risk fund?",
      "An informed investor seeking higher yield and accepting default risk for a 3+ year horizon", "Credit risk funds suit risk-aware investors.",
      ("Emergency fund", "Unsuitable."), ("Retiree's only income source", "Too risky."), ("Investor who can't tolerate any NAV fall", "Unsuitable."))
    H("An investor's risk appetite is high but risk capacity is low (no savings, many dependants). What should guide product choice?",
      "The lower of the two — risk capacity", "Recommend within the lower of appetite and capacity.",
      ("The higher — appetite", "Unsafe."), ("Past returns", "No."), ("Whatever the investor asks", "Suitability matters."))
    H("Which is the most suitable comparison for an index fund's quality?",
      "Tracking error and expense ratio", "Index funds aim to match the index cheaply.",
      ("Alpha generated", "Passive funds don't target alpha."), ("Number of stocks vs a flexi cap", "Irrelevant."), ("NAV level", "Meaningless."))
    H("An investor holds a gilt fund and RBI unexpectedly raises rates by 0.50%. The fund's MD is 8. Approximate NAV impact?",
      "About −4%", "−MD × Δy = −8 × 0.5% = −4%.",
      ("About +4%", "Rates up → NAV down."), ("About −0.5%", "Ignores duration."), ("No impact; G-secs have no risk", "No credit risk, but rate risk."))
    H("Which fund is most suitable for parking money for 10 days?",
      "Overnight or liquid fund", "Very short horizon → overnight/liquid; check liquid's graded load for < 7 days.",
      ("Short duration fund", "Too long duration for 10 days."), ("Equity savings fund", "Equity exposure."), ("ELSS", "Lock-in."))
    H("Two flexi cap funds have the same 5-year CAGR. Fund X has lower standard deviation and lower downside capture. Which is better on risk?",
      "Fund X", "Same return with lower risk = better risk-adjusted performance.",
      ("Fund Y", "Higher risk for same return."), ("Both equal", "Risk differs."), ("Can't say without NAV", "NAV level doesn't matter."))
