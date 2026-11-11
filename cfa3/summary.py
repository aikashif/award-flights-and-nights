"""CFA Level III Portfolio Management pathway summary (Schweser 2025, readings P1-P8) -> PDF.

Run: python3 cfa3/summary.py
Content lives in cfa3/full/chNN*.py; each module defines add(chap, sub).
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
  eyebrow="CFA® Level III · Portfolio Management Pathway · for the February 2027 exam",
  title="CFA L3 Portfolio Management Pathway Summary",
  lead="Every reading (P1–P8) of the Schweser 2025 Portfolio Management pathway notes, explained from zero — {n} subtopics. The pathway is 30–35% of the Level III exam (about 7 of the 20 scored question sets). Each subtopic opens with 'In plain words', then tables, formulas, worked examples and exam traps. Stars combine exam weight, essay likelihood and depth in the curriculum.",
  foot="Source: Kaplan Schweser 2025 CFA Level III Portfolio Management SchweserNotes (readings P1–P8 and formula sheet). Weight estimates: CFA Institute's 30–35% pathway share, split by curriculum depth. The core readings (asset allocation, portfolio construction, performance, derivatives & risk, ethics) are not in this file. CFA® is a trademark of CFA Institute.",
  html_name="../cfa3/pm-pathway-summary.html", pdf_name="../cfa3/CFA-L3-PM-Pathway-Summary.pdf", footer_label="CFA L3 · PM Pathway Summary")
