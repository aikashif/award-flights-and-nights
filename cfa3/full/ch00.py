from summary_lib import *
from helpers import P

def add(chap, sub):
    chap(0, "Exam Trend & How to Use This Summary", "—", 5)
    sub("Level III exam structure (Feb 2027)", 5,
      T(["Item","Detail"],
        [["Question sets","11 item sets + 11 essay (constructed response) sets, 12 points each; 20 scored, 2 trial"],
         ["Item set","Short vignette + 4 multiple-choice questions"],
         ["Essay set","Vignette + questions you answer in writing: justify, calculate, 'determine and justify'"],
         ["Core share","≈ 65–70% (asset allocation, portfolio construction, performance, derivatives &amp; risk, ethics)"],
         ["PM pathway share","≈ <b>30–35%</b> ≈ 7 scored sets"]]) +
      TRAP("Topic weights here are from CFA Institute's 2025 pathway structure and prep providers. Check the official Level III page for any 2027 change."))
    sub("Where the pathway marks come from", 5,
      T(["Reading","Share of pathway (est.)","Exam style","Priority"],
        [["P6 Credit strategies","≈ 19%","Calculations (spread measures, CDS), strategy choice","★★★★★"],
         ["P8 Institutional case study","≈ 15%","Essay: liquidity, asset allocation changes, ESG, risk","★★★★★"],
         ["P4 LDI &amp; index-based fixed income","≈ 14%","Calculations: immunisation, BPV hedge, contingent immunisation","★★★★★"],
         ["P5 Yield curve strategies","≈ 13%","'Which trade?' + return estimates + currency","★★★★★"],
         ["P2 Active equity: strategies","≈ 12%","Identify strategy / style / IC","★★★★"],
         ["P7 Trade strategy &amp; execution","≈ 12%","Benchmarks, implementation shortfall, algo choice","★★★★"],
         ["P3 Active equity: portfolio construction","≈ 11%","Active share vs active risk, risk budget, long/short","★★★★"],
         ["P1 Index-based equity","≈ 4%","Short explain questions","★★★"]]) +
      K("Fixed income (P4 + P5 + P6) ≈ <b>46%</b> of the pathway — prep providers call it the heaviest technical content",
        "Essays favour 'determine the most appropriate strategy and justify'","Numbers to master: BPV hedge ratio, immunisation, rolldown return, spread duration, CDS price, implementation shortfall"))
    sub("How to read this summary", 3,
      L("Each subtopic starts with <b>In plain words</b> — read that first",
        "Formula boxes show the formula, then a worked example from the notes",
        "Red TRAP boxes are the mistakes that cost marks",
        "Page 1 lists every 5★ subtopic — the minimum to study"))
