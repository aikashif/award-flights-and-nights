"""Research methods: topics missing from the class notes (session plan gaps) -> PDF.

Run: python3 stats/gap_summary.py
Content lives in stats/gap/gNN*.py; each module defines add(chap, sub).
"""
import sys, pathlib, importlib
here = pathlib.Path(__file__).parent
sys.path.insert(0, str(here.parent / "nism-vd"))
sys.path.insert(0, str(here / "gap"))
from summary_lib import render

CH = []
def chap(n, title, marks, stars):
    CH.append({"n": n, "title": title, "marks": marks, "stars": stars, "subs": []})
def sub(title, stars, body):
    CH[-1]["subs"].append({"t": title, "s": stars, "b": body})

for m in sorted(p.stem for p in (here / "gap").glob("g*.py")):
    importlib.import_module(m).add(chap, sub)

render(CH,
  eyebrow="Quantitative Research Methods · Fall 2026 · topics missing from your notes",
  title="Research Methods: Missing Topics",
  lead="The session-plan topics that your four class files do not cover, or cover only in part — explained from zero. {n} subtopics. Each starts with 'In plain words', then tables, formulas and fully worked examples. Read it together with your Research Statistics Summary.",
  foot="Sources: the standard texts on your session plan — Malhotra (Marketing Research), Zikmund (Business Research Methods), Saunders, Lewis &amp; Thornhill (Research Methods for Business Students), Kothari (Research Methodology), Levin &amp; Rubin (Statistics for Management), Chawla &amp; Sondhi (Research Methodology). Worked examples are written for this summary; check the numbers your professor uses in class.",
  html_name="../stats/missing-topics.html", pdf_name="../stats/Research-Methods-Missing-Topics.pdf", footer_label="Research Methods · Missing Topics")
