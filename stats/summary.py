"""Research methods & statistics summary (4 class files) -> PDF.

Run: python3 stats/summary.py
Content lives in stats/full/chNN*.py; each module defines add(chap, sub).
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
  eyebrow="Quantitative Research · Sampling & Sampling Distributions · Hypothesis Tests · Chi-Square · ANOVA",
  title="Research Statistics Summary",
  lead="Everything in your four files — class notes on quantitative research, the Brooks/Cole sampling-distribution deck, and Dr Krishan Pandey's Chi-Square and ANOVA notes — explained from zero. {n} subtopics. Each starts with 'In plain words', then tables, formulas and fully worked examples. Stars show how important a subtopic is for an exam.",
  foot="Sources: your handwritten Quantitative Research notes; 'Sampling Distributions' (Introduction to Probability and Statistics, Brooks/Cole 2006); Dr Krishan K. Pandey, 'Chi Square Test' and 'Analysis of Variance' (OP Jindal Global University). TRAP boxes mark common confusions and places where a source has an error. Lines marked 'Added' fill gaps your notes left blank.",
  html_name="../stats/statistics-summary.html", pdf_name="../stats/Research-Statistics-Summary.pdf", footer_label="Research Statistics · Complete Summary")
