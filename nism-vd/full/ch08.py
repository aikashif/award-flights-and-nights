from summary_lib import *

def add(chap, sub):
    chap(8, "Taxation", "3", 4)
    sub("Two levels: fund vs investor", 5,
      KV([("Principle","Not what you earn but what you keep after tax; MF is pass-through → tax at fund level and investor level"),
          ("Fund's income","Interest, dividend, capital gains"),
          ("Fund taxation","<b>Exempt</b> — MFs are trusts for unitholders: <b>Section 10(23D)</b> of Income Tax Act"),
          ("Investor","Growth option → only capital gains on sale; IDCW option → IDCW + capital gains")]))
    sub("What decides the tax rate", 5,
      T(["Factor","Point"],
        [["Type of income","Capital gains taxed differently from IDCW"],
         ["Holding period","Short-term vs long-term"],
         ["Type of scheme","Equity-oriented: <b>&gt; 65%</b> of AUM in equity shares listed on recognised Indian exchanges; all others non-equity. FoF investing in equity MFs = <b>non-equity</b>"],
         ["Type of investor","Resident, NRI, non-individual; joint holding → income of <b>first holder</b>"],
         ["Date of purchase","Budget 2023 changes from 1 Apr 2023; earlier investments keep old structure"],
         ["Date of redemption","Budget July 2024: new rates for redemptions on/after <b>23 July 2024</b>; before → old rates"]]))
    sub("Capital gains: holding periods", 5,
      K("Gain = sale price − purchase price (loss if lower)","Only two holding periods: 12 months and 24 months","12 months: all listed securities + units of equity-oriented funds","24 months: all other assets"))
    sub("Grandfathering (Budget 2018)", 5,
      KV([("Why","Equity LTCG was exempt till Budget 2018; taxing past gains = retrospective tax"),
          ("Rule","Gains up to <b>31 Jan 2018</b> not taxed; cost = higher of purchase price or NAV on 31 Jan 2018")]) +
      F("Invested ₹1,00,000 in 2017; value on 31 Jan 2018 = ₹2,00,000\nScenario 1: sold for ₹1,80,000 → taxable LTCG = 0\nScenario 2: sold for ₹2,20,000 → taxable LTCG = ₹20,000"))
    sub("₹1.25 lakh LTCG exemption", 5,
      F("Equity shares + equity-oriented MFs: first ₹1.25 lakh of LTCG per year exempt\nLTCG ₹90,000 → all exempt ; LTCG ₹1,35,000 → ₹10,000 taxable"))
    sub("Tax table for unitholders", 5,
      T(["Investment","STCG","LTCG","Long-term after"],
        [["Equity-oriented funds (incl. hybrids &gt; 65% equity)","20%","12.5% (₹1.25 lakh exempt per FY)","12 months"],
         ["Debt-oriented funds (incl. hybrids &gt; 65% debt)","Marginal slab rate (MSR)","MSR","—"],
         ["Hybrid 35%–65% domestic equity","MSR","12.5%","24 months"],
         ["Other MFs (FoFs, international funds/FoFs)","MSR","12.5%","24 months"],
         ["Equity ETFs","MSR","12.5%","12 months"],
         ["Gold ETFs","MSR","12.5%","12 months"],
         ["Debt ETFs","MSR","MSR","—"]]))
    sub("IDCW taxation", 5,
      KV([("Till 2019-20","IDCW tax-free for investor; Dividend Distribution Tax (DDT) deducted by scheme"),
          ("Budget Feb 2020","DDT abolished; from <b>April 2020</b> IDCW added to income, taxed at slab"),
          ("Effect","High-income investors pay more than before; tax-exempt investors (charitable trusts, exempt-slab individuals) now pay nothing"),
          ("DDT vs new","DDT wasn't investor's tax, no set-off; new tax can use exemptions/adjustments"),
          ("Common","NAV falls more than net-of-tax amount investor receives")]) +
      F("Old: Drop in NAV = Dividend paid + DDT\nNew: Post-tax IDCW = IDCW paid − tax at investor's slab (except tax-exempt)") +
      K("Growth option more tax-efficient — tax deferral, compounding pre-tax","From 1 Apr 2021: MF must show how much IDCW is income distribution (appreciation) vs capital distribution; tax on segregated basis"))
    sub("Stamp duty", 5,
      T(["Transaction","Stamp duty"],
        [["Issue of units (purchase, additional purchase, IDCW reinvestment, SIP, STP, IDCW Transfer Plan incl. triggers from past registrations, switch-ins)","<b>0.005%</b> of amount (SoA &amp; demat)"],
         ["Transfer of units (e.g. between demat accounts)","<b>0.015%</b>"]]) +
      K("From 1 July 2020 (Indian Stamp Act amended Feb 2019)","Units allotted on amount after deducting stamp duty"))
    sub("Set-off & carry forward", 5,
      L("Capital loss can't be set off against any other head (e.g. salary)",
        "Short-term capital loss → against STCG or LTCG","Long-term capital loss → only LTCG","Unabsorbed capital loss carried forward up to <b>8 years</b>") +
      K("Heads of income: salaries, house property, business/profession, capital gains, other sources"))
    sub("Bonus stripping", 4,
      F("Buy at ₹30 → 1:1 bonus → NAV ₹15 → sell original at ₹15 = loss ₹15\nLoss NOT allowed if bought within 3 months BEFORE record date and sold within 9 months AFTER\n→ loss becomes cost of acquisition of the bonus units") +
      K("Even if allowed, practice is discouraged — invest for fundamentals"))
    sub("Securities Transaction Tax (STT)", 5,
      T(["Transaction","Rate","Payable by"],
        [["Purchase of equity-oriented fund units","Nil","Purchaser"],
         ["Sale of equity-oriented fund units (delivery, on exchange)","0.001%","Seller"],
         ["Sale of equity shares / business trust units / equity fund units (non-delivery)","0.025%","Seller"],
         ["Sale of equity-oriented fund units to the mutual fund","0.001%","Seller"]]) +
      K("Applies on redemption/switch/sale of equity-oriented funds only","Not on purchase; not on debt securities or debt funds"))
    sub("Section 80C — ELSS Tax Saver", 5,
      L("Deduction up to <b>₹1.50 lakh</b> per year for individuals &amp; HUFs, <b>Old Tax Regime</b> only",
        "Lock-in <b>3 years</b> from date of investment",
        "Limit shared with other 80C avenues — if exhausted, ELSS still locked in without extra benefit",
        "SIP: each instalment locked in for 3 years from its own date",
        "IDCW reinvestment: each reinvestment gets fresh 3-yr lock-in (most AMCs offer only growth/IDCW payout)",
        "Joint holding: benefit to first holder",
        "New tax regime (Budget 2020): more slabs, lower rates, no 80C → ELSS = equity fund with lock-in",
        "Some older retirement funds also have 80C benefit, <b>5-yr lock-in</b> — check scheme") +
      K("MFs = tax-sheltered vehicles → tax deferral → pre-tax compounding in growth option"))
    sub("Tax Deducted at Source (TDS)", 5,
      KV([("Resident — redemption","No TDS"),
          ("Resident — IDCW","10% if IDCW &gt; <b>₹10,000</b>"),
          ("Non-resident","TDS at rates by investor type, investment type and income type"),
          ("DTAA","Lower of Income Tax rate or DTAA rate; investor must provide documents")]))
    sub("GST in MF schemes", 4,
      T(["GST on","Treatment"],
        [["Investment management &amp; advisory fees","Charged to scheme <b>over and above</b> TER limits"],
         ["All other fees","Within TER limit"],
         ["Exit load","Deducted from exit load; net credited to scheme"],
         ["Brokerage &amp; transaction cost","Within TER limit"],
         ["Distributor commission","May attract GST for ARN holder; cannot be charged to scheme"]]) +
      KV([("From 1 Apr 2026","Cost = base expense ratio + execution brokerage (within limits) + statutory levies (e.g. GST)"),
          ("Base expense ratio","Investment &amp; advisory fees + out-of-pocket expenses + brokerage commission, excluding statutory levies and transaction cost")]))
