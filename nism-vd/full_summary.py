"""NISM V-D complete summary (all 22 chapters + appendices) from the Sept 2026 workbook -> PDF.

Run: python3 nism-vd/full_summary.py
Content lives in nism-vd/full/chNN*.py; each module defines add(chap, sub).
"""
import sys, pathlib, importlib
here = pathlib.Path(__file__).parent
sys.path.insert(0, str(here))
sys.path.insert(0, str(here / "full"))
from summary_lib import render

CH = []
def chap(n, title, marks, stars):
    CH.append({"n": n, "title": title, "marks": marks, "stars": stars, "subs": []})
def sub(title, stars, body):
    CH[-1]["subs"].append({"t": title, "s": stars, "b": body})

mods = sorted(p.stem for p in (here / "full").glob("ch*.py"))
for m in mods:
    importlib.import_module(m).add(chap, sub)

render(CH,
  eyebrow="NISM-Series-V-D · Mutual Fund – Specialized Investment Fund Distributors · Workbook version September 2026",
  title="NISM V-D Complete Summary",
  lead="Every chapter of the September 2026 workbook (MF Ch 1–12, equity derivatives Ch 13–17, interest rate derivatives Ch 18–22, appendices) — {n} subtopics in tables, keywords and formulas. Single source: the workbook. Each subtopic rated 1–5★ for exam importance; read in any order you like.",
  foot="Source: NISM-Series-V-D MF-SIF Distributors Workbook, version September 2026 (the only source used). Chapter marks are the official weightages from the workbook. TRAP boxes flag common exam confusions and places where the workbook itself is inconsistent.",
  html_name="complete-summary.html", pdf_name="NISM-VD-Complete-Summary.pdf", footer_label="NISM V-D · Complete Summary (Sept 2026 workbook)")
