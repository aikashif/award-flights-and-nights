from summary_lib import *

def add(chap, sub):
    chap(4, "Legal & Regulatory Framework", "7", 4)
    sub("Four financial regulators", 4,
      T(["Regulator","Regulates"],
        [["RBI","Banking system + money markets"],["SEBI","Securities markets"],["IRDAI","Insurance"],["PFRDA","Pension"]]) +
      K("All under the Ministry of Finance","Purpose: protect consumers + regulated development of markets"))
    sub("Role of SEBI", 4,
      KV([("Regulates","MFs, depositories, custodians, RTAs, credit rating agencies (among others)"),
          ("Preamble","'to protect the interests of investors in securities and to promote the development of, and to regulate the securities market…'"),
          ("'Securities'","Transferable, tradeable instruments — Sec 2(h) of SCRA, 1956"),
          ("Three aspects","Disclosures by issuers · efficiency of transactions · low transaction costs"),
          ("Also checks","Deliberate speculation · insider trading · excessive risk by MFs · inadequate collateral by debt issuers")]) +
      K("Unchecked → loss of investor trust → household savings stop flowing to capital markets"))
    sub("Regulatory reforms: MF Regulations 1996 → 2026", 3,
      K("MF Regulations first issued 1996; replaced by <b>SEBI MF Regulations 2026</b>","Covers investor services, NAV accounting, valuation, disclosures, investment norms","Master circulars on sebi.gov.in"))
    sub("22 areas covered by regulations", 4,
      T(["#","Area","Key point"],
        [["1","Scheme documents (offer document = SID + SAI)","Content, update frequency; performance vs <b>Total Return Index (TRI)</b>, not Price Return Index"],
         ["2","Registration","AMC, sponsor, trustees; mergers, change of management"],
         ["3","Conversion &amp; consolidation","Scheme mergers; one scheme per category; market-cap definitions; PRC matrix for debt"],
         ["4","New products","e.g. Infrastructure Debt Funds, ESG"],
         ["5","Risk management","Operational risk, exposure limits (true-to-label), segregated portfolios (after 2018 credit crisis); 2008 crisis: no premature redemption of FMPs, no 'liquid plus' names"],
         ["6","Disclosures &amp; reporting","Formats, frequency"],
         ["7","Governance","Audit &amp; valuation committees, independent directors, trustees, min investors, benchmarking, systems audit, role in corporate governance"],
         ["8","Secondary market activities","Equity, debt, G-sec, derivatives"],
         ["9","NAV","Disclosure, rounding, cut-off, time stamping, sale/purchase price uniformity"],
         ["10","Valuation","Of all securities"],["11","Loads, fees, expenses","Limits; commission disclosure"],
         ["12","IDCW distribution","Procedure; distributable surplus"],["13","Investment by schemes","Restrictions and limits"],
         ["14","Advertisements","Content, statutory ads, disclaimers"],
         ["15","Investor rights &amp; obligations","Statements, payout timelines, delay penalty, <b>instant access facility</b> (liquid funds)"],
         ["16","Certification &amp; registration of intermediaries","Exam + CPE"],
         ["17","Transactions in MF units","Exchanges, record-keeping, KYC"],
         ["18","CDMDF","Corporate Debt Market Development Fund — <b>backstop facility</b> to buy investment-grade corporate debt in stress"],
         ["19","Execution Only Platforms","Scope, categories, eligibility, fees, grievance, conflicts, tech, disclosures"],
         ["20","MF Lite Framework","Light-touch regime only for passive schemes"],
         ["21","Specialized Investment Fund (SIF)","Bridge MF–PMS gap"],
         ["22","Miscellaneous","Everything else"]]) +
      K("TRI: dividends/interest notionally reinvested on ex-date + capital gains","Segregated portfolio = separate distressed/illiquid assets after a credit event"))
    sub("Other regulators' rules MFs must follow", 2,
      K("RBI: money market, overseas investment, non-resident investment, foreign remittances","Stock exchanges (SEBI-regulated): listing, trading, margining rules"))
    sub("Permitted investments — Regulation 39", 5,
      L("(a) Securities","(b) Money market instruments","(c) Privately placed debentures","(d) Securitised debt (asset-backed or mortgage-backed)","(e) Gold / gold-related","(f) Silver / silver-related","(g) Others specified by SEBI") +
      K("MF = pass-through; investors have no control over investment management → SEBI limits risk","Restrictions apply at the time of investment"))
    sub("Restrictions — Regulation 41", 5,
      L("All investments (except gold/silver ETFs) subject to <b>Sixth Schedule</b> + other SEBI restrictions",
        "Gold/silver ETFs may invest in exchange-traded commodity derivatives",
        "Settle only in <b>dematerialised</b> securities (except specified instruments)",
        "Gold/silver ETF funds only in gold/silver (related) instruments, except for redemption liquidity; pending deployment → short-term deposits of scheduled commercial banks",
        "No <b>carry forward</b> transactions (except as SEBI specifies)",
        "Derivatives only on a recognised stock exchange (SEBI framework)",
        "Short selling only on recognised exchange (short selling &amp; SLB framework)",
        "Inter-scheme transfers within same MF allowed under SEBI conditions"))
    sub("Sixth Schedule restrictions", 5,
      L("Equity, equity-related and debt only in <b>listed or to-be-listed</b> securities — except unlisted G-secs, money market instruments other than <b>CPs</b>, and unlisted NCDs as SEBI specifies",
        "Unrated debt subject to SEBI conditions",
        "Scheme may invest in another scheme (same or other MF) <b>without fees</b>, within limits (not applicable to FoFs)",
        "<b>No scheme may invest in a FoF scheme</b>",
        "A FoF may not invest in another FoF; only in MF schemes (except liquidity for redemptions)",
        "Buy/sell on <b>delivery</b> basis — take/give delivery (exceptions: short selling framework, exchange derivatives, sale of contracted G-sec per RBI)",
        "Securities held in the name of the MF on account of the scheme",
        "Pending deployment → short-term deposits of scheduled commercial banks",
        "Prudential limits as SEBI prescribes"))
    sub("SIF investment restrictions — Regulation 51", 3,
      K("SIF may invest in instruments permitted under Regulation 39","SEBI may specify manner of investment","Subject to Sixth Schedule restrictions"))
    sub("Advertisement code — Fifth Schedule", 5,
      T(["Clause","Rule"],
        [["(a)","Accurate, true, fair, clear, complete, unambiguous, concise; not misleading"],
         ["(b)","No false/biased/deceptive statements, no assumptions/projections, <b>no testimonials, no ranking</b>"],
         ["(c)","Not designed to be misunderstood or disguise significance; no misleading by implication/omission"],
         ["(d)","No exaggerated/unwarranted slogans or slogans inconsistent with risk-return"],
         ["(e)","<b>No celebrities</b> in advertisements"],
         ["(f)","Don't exploit inexperience; avoid technical/legal jargon and excessive detail"],
         ["(g)","Timely; consistent with SID, SAI, KIM"],
         ["(h)","Don't discredit other ads or make unfair comparisons"],
         ["(i)","Standard warning in legible font: 'Mutual Fund investments are subject to market risks, read all scheme related documents carefully.' — no words added/deleted"],
         ["(j)","Vernacular ads: warning in the vernacular language"],
         ["(k)","Audio-visual: visual + voice-over clear; e.g. <b>14 words for at least 5 seconds</b>"]]))
    sub("IDCW / bonus advertisement rules", 4,
      L("Disclose IDCW in ₹ per unit + face value + prevailing NAV at declaration",
        "Close-ended maturity / interval completion: 'the entire distributable surplus at the time of maturity or at the completion of the interval period shall be distributed'",
        "Immediately below payout figure: NAV will fall to the extent of payout and statutory levy (if applicable)"))
    sub("Performance advertisements", 5,
      T(["Scheme age","Rule"],
        [["&gt; 3 years","CAGR for 1, 3, 5 yrs and since inception (since date of allotment) + point-to-point value of ₹10,000"],
         ["&lt; 6 months","<b>No past performance</b>"],
         ["6 months – 1 year","Simple annualised growth for past 6 months"],
         ["Overnight, liquid, money market","Simple annualisation of yields if data for ≥ 7, 15, 30 days (not misleading)"]]) +
      L("Period computed to last day of month-end preceding the ad",
        "State regular or direct plan; footnote: plans have different expense structures",
        "Footnote if same fund manager hasn't managed for the full period",
        "Include performance of <b>all other schemes</b> of the fund manager (CAGR 1, 3, 5 yrs with benchmark); if &gt; 6 schemes → total number + top 3 and bottom 3",
        "Internet ads may give exact website link to fund manager's other schemes' data"))
    sub("Standard additional benchmarks", 4,
      T(["Scheme type","Additional benchmark"],
        [["Equity","Sensex / Nifty"],["Debt ≤ 1 yr duration/maturity, Arbitrage","1-year T-Bill"],["Other debt","10-yr dated GoI security"],
         ["Conservative Hybrid","10-yr dated GoI security"],["Balanced/Aggressive Hybrid, BAF, Multi Asset","Sensex or Nifty"],
         ["Equity Savings","10-yr dated GoI security"],["Retirement / Children's","Sensex or Nifty"],["Index funds/ETFs/FoFs","Based on underlying asset allocation"]]) +
      K("Shown in INR and CAGR","Part of SAI and all advertisements"))
    sub("Celebrity endorsement at industry level", 5,
      L("Allowed only to increase awareness of MFs as a product category",
        "Must not promote a particular MF's scheme or brand an AMC",
        "Expenses limited to industry-level pooled investor education &amp; awareness amounts",
        "<b>Prior SEBI approval</b> required"))
    sub("SIF branding & advertisement", 5,
      L("Distinct identity, separate from the MF: distinct <b>brand name and logo</b>",
        "May use sponsor's/MF's brand in SIF documents and ads for <b>5 years</b> from SEBI approval for SIF launch",
        "Use phrases like 'brought to you by', 'offered by'",
        "Sponsor/MF brand font size ≤ SIF brand font size",
        "MF advertisement guidelines apply to all SIF strategies",
        "Separate website or dedicated web page for SIF"))
    sub("Unauthenticated news guidelines", 3,
      L("Internal code of conduct; staff must not circulate rumours/unverified info",
        "Access to blogs/chat forums/messenger sites restricted, supervised or blocked",
        "Logs of such usage kept as records",
        "Market news forwarded only after Compliance Officer's approval; violations → action; Compliance Officer also liable"))
    sub("Investors' rights", 5,
      T(["Right","Detail"],
        [["Beneficial ownership","Proportionate; can ask for unit certificate; demat allotment (open &amp; close-ended); demat units freely transferable (ELSS restricted during lock-in); demat statement = SOA"],
         ["Change distributor","Written request; no NOC from existing distributor"],
         ["Inspect documents","Trust Deed, IMA, Custodial Services Agreement, RTA agreement, AMC's Memorandum &amp; Articles"],
         ["Nominees","Up to <b>3</b> nominees with % split; if not specified → equal"],
         ["Pledge","Units pledged as security to financier"],
         ["Grievance redressal","Complaint status in annual report, MF and AMFI websites; pending complaints can stop new scheme approval"],
         ["Fundamental attribute change","Exit at NAV without load for ≥ <b>30 days</b>; written communication (email/SMS), website display"],
         ["Terminate AMC / wind up","<b>75% of unitholders</b> can terminate AMC or wind up scheme"],
         ["Unclaimed amounts","Claim within 3 yrs → prevailing NAV; after 3 yrs → NAV at end of 3 yrs"],
         ["Other services","Account statements, portfolio statements, half-yearly disclosures"]]) +
      K("Trustees must get unitholders' consent: when SEBI requires; when 75% of unitholders require; when majority of trustees decide to wind up / prematurely redeem close-ended",
        "Trust is a notional entity → investors can't sue the trust, but can sue <b>trustees</b> for breach of trust",
        "Caveat emptor applies; prospective investors don't have unitholders' rights",
        "Daily disclosure of debt &amp; money market trades (incl. inter-scheme) with <b>15-day lag</b>"))
    sub("Unclaimed amounts & illiquid security proceeds", 4,
      KV([("Deployment","Money market + separate plan of a liquid scheme for unclaimed amounts"),
          ("AMC fee","Max <b>0.50% p.a.</b>; <b>no exit load</b> on this plan"),
          ("Reminders","AMC reminds investors; annual report shows unclaimed amount &amp; number of investors per scheme"),
          ("Written-off security later recovered","Substantial &amp; recovered within <b>2 years</b> → paid to old investors; else → Investor Education Fund")]))
    sub("Due diligence of distributors", 2,
      K("AMCs regulate distributor practices via due diligence","AMFI coordinates common unified due diligence","Details in Ch 6"))
    sub("Grievance redress mechanism", 5,
      F("Investor service centre → senior levels at AMC → SEBI (SCORES) → SMART ODR\nAMC must redress within 21 calendar days of receipt") +
      KV([("SCORES","SEBI's web-based centralised system (scores.sebi.gov.in): lodge, follow up, track online; physical complaints at SEBI offices are scanned &amp; uploaded"),
          ("Entities covered","Listed cos/RTAs · brokers/exchanges · DPs/depositories · MFs · portfolio managers · others (KRAs, CIS, merchant bankers, CRAs, FPIs)"),
          ("SMART ODR","Online dispute resolution: formal online conciliation and arbitration")]))
    sub("Cyber security & resilience (CSCRF)", 3,
      KV([("Framework","Cyber Security and Cyber Resilience Framework for SEBI Regulated Entities"),
          ("5 goals (from CERT-In CCMP)","Anticipate · Withstand · Contain · Recover · Evolve"),
          ("AI threats","Task force <b>cyber-suraksha.ai</b>"),
          ("Incident reporting","Email mkt_incidents@sebi.gov.in within <b>6 hours</b>; SEBI Incident Reporting Portal within <b>24 hours</b>; aligned with FSB's FIRE format")]))
    sub("AMFI Code of Ethics & AGNI", 4,
      KV([("Fourth Schedule","SEBI Code of Conduct for AMCs &amp; trustees (Appendix 1)"),
          ("ACE","AMFI Code of Ethics — higher, more explicit standards for AMCs &amp; trustees (Appendix 2)"),
          ("AGNI","AMFI Guidelines &amp; Norms for Intermediaries — agents, brokers, distribution houses, banks (Appendix 3)")]) +
      F("Breach by intermediary:\n1. AMFI writes, asks explanation within 3 weeks\n2. No/unsatisfactory reply → warning letter (next violation = cancellation)\n3. Proven second violation → registration cancelled, all AMCs informed\nIntermediary may appeal to AMFI"))
