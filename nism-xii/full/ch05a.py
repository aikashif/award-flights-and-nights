from summary_lib import *

def add(chap, sub):
    chap(5, "Mutual Funds", "20", 5)
    sub("Direct investing vs mutual funds", 4,
      K("Direct investing burdens: <b>selection · price · timing · weighting · evaluation · exit · operations</b>",
        "Mutual fund = someone else selects and manages the portfolio for a fee"))
    sub("Basic features of a mutual fund", 5,
      L("Pool of investors' money managed by specialist firms; scheme objectives stated upfront",
        "Investors get <b>units</b> = proportional share; are <b>unit holders</b>; bear all risk, no guarantee",
        "Portfolio disclosed periodically; buy/sell from fund or on exchange if listed",
        "MFs <b>may not borrow to invest</b> — only for temporary liquidity (redemptions, interest/dividend payment)",
        "Unit holders are sole owners of the assets; all activity under SEBI regulations") +
      K("Products differ by: asset allocation · investment objective · costs &amp; fees · operational details"))
    sub("Mutual fund, scheme, categories", 5,
      L("Assets held in a <b>trust</b>; investors = joint beneficial owners; trustees oversee the investment manager",
        "'Mutual fund' also means the fund house",
        "SEBI's 5 groups: <b>Equity · Debt · Hybrid · Life Cycle Funds · Others</b>",
        "<b>One scheme per category</b>, except: index funds/ETFs on different indices · FoFs with different underlyings · sectoral/thematic funds on different sectors/themes",
        "'Type of scheme' must appear in offer documents and ads"))
    sub("Pooling, units, unit capital (worked)", 5,
      F("3 investors: ₹10,000, ₹20,000, ₹30,000 → pool ₹60,000, ratio 1:2:3\nPortfolio grows to ₹72,000 → holdings ₹12,000 / ₹24,000 / ₹36,000\nAt FV ₹10: 1,000 / 2,000 / 3,000 units → unit capital = 6,000 × ₹10 = ₹60,000") +
      K("Face value (typically ₹10) matters for accounting","<b>MTM</b> = value securities at current market price daily (₹60,000 cost → ₹72,000 MTM)"))
    sub("NAV (worked)", 5,
      F("Net assets = MTM value + income − expenses\n72,000 + 3,000 dividend − 600 expenses = 74,400\nNAV = 74,400 ÷ 6,000 units = <b>₹12.40</b>") +
      K("Computed every business day; investors buy and sell at NAV-based prices"))
    sub("Why transactions are priced at NAV (worked)", 5,
      T(["Case","Assets ÷ units","New NAV","Effect"],
        [["A. Buy 1,000 at FV ₹10","84,400 ÷ 7,000","12.05","Existing holders lose"],["B. Buy 1,000 at NAV ₹12.40","86,800 ÷ 7,000","12.40","No change"],
         ["C. Redeem 1,000 at FV ₹10","64,400 ÷ 5,000","12.88","Remaining holders gain"],["D. Redeem 1,000 at NAV","62,000 ÷ 5,000","12.40","No change"]]) +
      K("Open-ended: no maturity; buy/redeem any business day","NAV pricing keeps parity between entering, staying and exiting investors"))
    sub("Expenses, loads, performance, diversification", 5,
      L("Expenses as % of <b>daily average net assets</b>; deducted daily, already in NAV; quoted as <b>TER</b> (% of AUM); limits set by regulation, differ by fund type",
        "<b>Exit load</b>: % of NAV by holding period; <b>entry load prohibited</b>",
        "No assured return; equity funds move with equity markets; aim to match or beat an index",
        "Diversified portfolio even with ~₹5,000; spreads sector and stock risk") +
      F("Exit load 1% within 1 year; NAV ₹12 → load 0.12 → redemption price ₹11.88"))
    sub("Pass-through status", 5,
      L("Income of a SEBI-registered MF is <b>fully exempt</b> from tax — earned for investors and passed through",
        "Avoids taxing the same income twice (fund + investor); taxed only in investors' hands",
        "Unit capital is capital, not a loan"))
    sub("Open-ended, closed-end, interval funds", 5,
      T(["","Open-ended","Closed-end","Interval"],
        [["Maturity","None","Fixed — fund buys back and winds up","—"],["Buying after launch","Any time at NAV","No — only in <b>NFO</b>","In set windows (e.g. 3 days a quarter)"],
         ["Selling","Back to fund at NAV","On exchange only (fund not involved)","To fund in windows, or on exchange"],
         ["Listing","Optional","<b>Mandatory</b>","Listed"]]))
    sub("Growth vs IDCW options", 5,
      T(["Option","How returns come"],
        [["Growth","Gains retained; NAV rises; realise by selling units"],
         ["IDCW payout","Dividend from <b>realised</b> profits paid out"],["IDCW reinvestment","Dividend reinvested in additional units"]]) +
      K("SEBI 5 Oct 2020 renamed dividend options '<b>Income Distribution cum Capital Withdrawal</b>' — part of capital can be paid out"))
    sub("How a mutual fund works", 5,
      L("<b>AMC</b> = investment manager; fund manager and staff are AMC employees; launches schemes, collects and manages money, charges a fee; supervised by AMC board and trustees",
        "<b>Trustees</b> approve major decisions; meet at least <b>6 times a year</b>",
        "NFO = primary issue; scheme related documents: <b>SID, SAI, KIM</b>",
        "Distributors (banks, brokers, individuals) empanelled; earn <b>trail commission</b> as % of assets while money stays; investors may go <b>direct</b>",
        "NFO price usually FV ₹10; ongoing at NAV; minimum ₹500 / ₹5,000 (most) / ₹10,000",
        "Holdings tracked in unique <b>folio</b> numbers; R&amp;T agents service investors",
        "Money held by <b>custodian</b>, not AMC's bank account",
        "Daily valuation, NAV published by end of day; full portfolio and accounts disclosed periodically") +
      T(["Constituent (SEBI-registered, trustee-approved)","Role"],
        [["Custodian","Holds and settles funds and securities"],["R&amp;T agent","Keeps and services investor records"],["Banks","Collections and payments"],
         ["Auditor","Audits scheme accounts"],["Distributors","Sell products"],["Brokers","Execute securities trades"]]))
    sub("Equity scheme categories", 5,
      T(["Category","Rule (min % of total assets)"],
        [["Multi cap","Equity ≥ <b>75%</b>; ≥ 25% each in large, mid, small"],["Large cap","Large-cap equity ≥ <b>80%</b>"],
         ["Large &amp; mid cap","≥ <b>35%</b> large + ≥ <b>35%</b> mid"],["Mid cap","Mid-cap ≥ <b>65%</b>"],["Small cap","Small-cap ≥ <b>65%</b>"],
         ["Flexi cap","Equity ≥ <b>65%</b>, dynamic across caps"],["Dividend yield","Equity ≥ <b>80%</b>, mainly dividend-yielding stocks"],
         ["Value / Contra","Equity ≥ <b>80%</b>; value strategy / contrarian strategy"],
         ["Focused","Max <b>30 stocks</b>; equity ≥ 80%; state focus (multi/large/mid/small)"],
         ["Sectoral / Thematic","≥ <b>80%</b> in sector/theme; ≤ <b>50%</b> overlap with other equity schemes (except large cap)"],
         ["ELSS (Tax Saver)","Equity ≥ <b>80%</b>; <b>3-year lock-in</b>; ELSS 2005; Sec 80C up to <b>₹1.5 lakh</b> — <b>old tax regime only</b>"],
         ["ESG (thematic sub-category, 20 Jul 2023)","Strategies: exclusion · integration · best-in-class &amp; positive screening · impact · sustainable objectives · transition"]]) +
      T(["Cap","Rank by full market cap"],[["Large","1st – 100th"],["Mid","101st – 250th"],["Small","251st onwards"]]) +
      TRAP("The XII workbook says an AMC may offer a value fund <b>or</b> a contra fund, not both. The V-D (Sept 2026) workbook allows both with at most 50% portfolio overlap. For the XII exam, answer 'either value or contra'."))
