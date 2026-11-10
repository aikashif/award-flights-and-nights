"""NISM Series XII complete summary from the September 2026 workbook -> PDF.

Run: python3 nism-xii/summary.py
Content lives in nism-xii/full/chNN*.py; each module defines add(chap, sub).
Reuses the shared renderer in nism-vd/summary_lib.py.
"""
import sys, pathlib, importlib
here = pathlib.Path(__file__).parent
sys.path.insert(0, str(here.parent / "nism-vd"))
sys.path.insert(0, str(here / "full"))
from summary_lib import render

CH = []
def chap(n, title, marks, stars):
    CH.append({"n": n, "title": title, "marks": marks, "stars": stars, "subs": []})
def sub(title, stars, body):
    CH[-1]["subs"].append({"t": title, "s": stars, "b": body})

for m in sorted(p.stem for p in (here / "full").glob("ch*.py")):
    importlib.import_module(m).add(chap, sub)

render(CH,
  eyebrow="NISM-Series-XII · Securities Markets Foundation · Workbook version September 2026",
  title="NISM XII Complete Summary",
  lead="Every chapter of the September 2026 workbook (securities markets, securities and investing, primary markets, secondary markets, mutual funds, derivatives) — {n} subtopics in tables, keywords and formulas. Exam: 100 questions × 1 mark, 2 hours, pass 60%, no negative marking. Single source: the workbook. Each subtopic rated 1–5★ for exam importance.",
  foot="Source: NISM-Series-XII Securities Markets Foundation Workbook, version September 2026 (the only source used). Marks are the official weightages (100 questions). TRAP boxes flag common exam confusions and places where the workbook itself is inconsistent.",
  html_name="../nism-xii/complete-summary.html", pdf_name="../nism-xii/NISM-XII-Complete-Summary.pdf", footer_label="NISM XII · Complete Summary (Sept 2026 workbook)")
