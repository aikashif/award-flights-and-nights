from summary_lib import *

def add(chap, sub):
    chap(11, "Mutual Fund Scheme Performance", "5", 4)
    sub("Benchmarks — requirements & choice", 5,
      L("Pre-defined comparable to judge performance",
        "Credible benchmark in sync with (a) investment objective (b) asset allocation (c) investment strategy",
        "Calculated by independent agency, transparent, published regularly (exchanges, CRAs, research houses, financial publications)",
        "Index fund: the tracked index; others: subjective — decided by <b>AMC in consultation with trustees</b>; stated in SID with benchmark performance alongside",
        "Benchmark may change (objective change, index construction change, better index) — with trustees, justified and documented; benchmark names disclosed"))
    sub("Price Return Index vs Total Return Index", 5,
      KV([("PRI","Only capital gains of constituents"),
          ("TRI","Capital gains + all dividends/interest (reinvested)"),
          ("Mandatory TRI","From <b>1 February 2018</b>"),
          ("Why","Fair comparison — scheme returns include dividends (IDCW option measured by reinvestment method); PRI gave schemes an edge"),
          ("Effect","Fewer schemes appear to beat benchmark; gap = dividend yield, historically 1.5–2.5% at index level"),
          ("No TRI for a period","Composite CAGR: PRI till TRI available, TRI thereafter (SEBI circular 4 Jan 2018)")]))
    sub("Equity scheme benchmarks", 4,
      T(["Driver","Benchmark choice"],
        [["Scheme type","Diversified: Sensex, Nifty 50, BSE 200, BSE 500, Nifty 100, Nifty 500; sectoral/thematic: Bankex, BSE FMCG, Nifty Infrastructure, Nifty Energy"],
         ["Investment universe","Large caps: Sensex (30) / Nifty 50; mid caps: Nifty Midcap 50, BSE Midcap"],
         ["Portfolio concentration","Few stocks → narrow (Sensex, Nifty 50); many → broad (100/200/500 indices)"]]))
    sub("Debt scheme benchmarks", 4,
      L("Developed by research/rating agencies recommended by AMFI: CRISIL, ICICI Securities, NSE",
        "NSE: Nifty Composite G-sec, Nifty 4–8 Year G-sec, Nifty 10-yr Benchmark G-sec; BSE: India Sovereign Bond Index, India Government Bill Index",
        "ICICI Securities <b>I-Bex</b> (sovereign): sub-indices <b>Si-Bex</b> 1–3 yrs, <b>Mi-Bex</b> 3–7 yrs, <b>Li-Bex</b> &gt; 7 yrs",
        "Liquid schemes (≤ 91 days): NSE Liquid or CRISIL Liquid Fund Index",
        "Gilt funds: G-sec indices; diversified debt: mixed-debt indices"))
    sub("Other scheme benchmarks", 3,
      T(["Scheme","Benchmark"],
        [["Hybrid","Blend: e.g. 65% Sensex + 35% I-Bex"],["Gold ETF","Gold price"],
         ["Real estate","Indices by real estate services cos — short history, limited acceptance"],
         ["International","Where it invests: Shanghai Composite (China), S&amp;P 500 (US), synthetic blend for many countries"]]))
    sub("Standard additional benchmarks", 4,
      T(["Scheme type","Benchmark"],
        [["Equity","Sensex or Nifty"],["Debt ≤ 1 yr duration/maturity, arbitrage","1-yr T-Bill"],["Other debt","10-yr dated GoI security"],
         ["Conservative Hybrid","10-yr GoI"],["Balanced/Aggressive Hybrid, BAF, Multi Asset","Sensex/Nifty"],["Equity Savings","10-yr GoI"],
         ["Retirement/Children's","Sensex/Nifty"],["Index funds/ETFs/FoFs","Per underlying allocation"]]) +
      K("Return in INR and CAGR; part of SAI and all ads"))
    sub("Two-tier benchmarks", 5,
      KV([("Circular","SEBI 27 Oct 2021, effective 1 Jan 2022; all benchmarks TRI"),
          ("Tier 1","Reflects scheme <b>category</b> (one broad market index per provider)"),
          ("Tier 2","Reflects fund manager's <b>style/strategy</b> (bespoke)"),
          ("Debt tier-1","Based on Potential Risk Class, from 1 Apr 2022")]) +
      T(["Scheme type","Tier 1","Tier 2"],
        [["Income/debt","e.g. NIFTY Ultra Short Duration Debt Index / CRISIL Ultra Short Term Debt Index","e.g. AAA Bond Index"],
         ["Growth/equity","e.g. BSE 100 / NSE 100 for large cap","e.g. Nifty 50"],
         ["Hybrid &amp; solution-oriented","Single broad market (or bespoke) benchmark",""],
         ["Thematic/sectoral","Single benchmark",""],["Index funds &amp; ETFs","Single (the replicated index)",""],
         ["FoFs","Single underlying fund → its benchmark; multiple → broad market index",""]]))
    sub("Relative returns vs risk-adjusted returns", 4,
      K("Relative return: scheme vs benchmark/peers → initial premise of out/under-performance; AMCs &amp; trustees review periodically",
        "Weakness: ignores different risk levels for same objective","Risk-adjusted: return should be commensurate with risk"))
    sub("Sharpe ratio", 5,
      F("Sharpe = (Rs − Rf) ÷ Standard deviation\nRf: risk-free (T-Bill index); Rs − Rf = risk premium\nEx: Rf 5%, Rs 7%, SD 0.5% → (7 − 5) ÷ 0.5 = 4") +
      K("Risk premium per unit of total risk","Higher = better","Compare only comparable schemes (not equity vs debt)"))
    sub("Treynor ratio", 5,
      F("Treynor = (Rs − Rf) ÷ Beta\nEx: Rf 5%, Rs 8%, β 1.2 → 3 ÷ 1.2 = 2.5") +
      K("Higher = better","Beta relevant for diversified equity → restrict comparisons to them"))
    sub("Alpha", 5,
      K("Optimal return = return in line with scheme's beta","Alpha = actual return − optimal return","Positive = out-performance; negative = under-performance","Evaluate only for diversified equity schemes",
        "Historical; calculations are arithmetic — evaluation is an art"))
    sub("Information ratio", 5,
      F("IR = (Portfolio return − Benchmark return) ÷ Standard deviation of excess return") +
      L("Measures manager's skill and consistency of excess return vs benchmark",
        "<b>Only risk-adjusted measure mandatory</b> to disclose; daily on AMC website; on AMFI website comparably",
        "Benchmark = tier-I benchmark (per SID); SD of excess returns from daily returns (SEBI circular 17 Jan 2025)"))
    sub("Tracking error", 5,
      L("Index fund β ≈ 1 → should earn market return; gap = tracking error",
        "Earlier: how closely an index fund tracks (ideally zero); now also: consistency of out-performance",
        "= <b>Standard deviation of excess returns</b>; low for a consistently out-performing fund",
        "Denominator of information ratio"))
    sub("Performance disclosure & product literature", 3,
      L("SID updated twice a year incl. performance; monthly factsheet (not statutory) fills gap; portals; product literature",
        "Suitability: product label (objective — wealth creation, regular income, liquidity; asset class; holding period) + risk-o-meter",
        "Returns: cumulative returns for periods vs benchmark; discrete annual returns show consistency",
        "Portfolio description: equity — diversification, market cap, growth/value; debt — tenor, credit quality; hybrid — allocation"))
    sub("Fund factsheets — macro metrics (Table 11.3)", 3,
      T(["Metric","Purpose"],
        [["Index levels &amp; yields","Assess scheme performance"],["Corporate results, earnings revisions, margins","Tone for equity markets"],
         ["Government spending","Positive for growth; high fiscal deficit → higher borrowing &amp; interest costs, less fiscal room"],
         ["Inflation","Demand, costs, profits; high inflation → monetary tightening"],["Interest rates","Consumption, demand, expansion capacity"],
         ["Domestic &amp; foreign portfolio flows","Expectations from Indian markets"],["GDP","Economic cycle"],
         ["Overseas economic &amp; rate data","Export demand, fund flows (low global rates → flows to emerging markets)"],
         ["Commodity &amp; input prices","Profitability; oil affects currency, exports/imports"]]) +
      K("Factsheet not mandatory but subject to SEBI ad guidelines; carries fund manager's market views","AMFI website: performance data of all schemes","Data vendors (e.g. Morningstar, Value Research) — not certified by SEBI/NISM"))
