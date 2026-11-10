"""NISM Series XII quiz (Ch1-6). Run: python3 nism-xii/quiz.py

Question parts live in q_*.py; each defines add(Q, inr, num).
Uses the shared builder in nism-vd/quiz_lib.py.
"""
import sys, pathlib
here = pathlib.Path(__file__).parent
sys.path.insert(0, str(here.parent / "nism-vd")); sys.path.insert(0, str(here))
from quiz_lib import make_bank, inr, num, build
import q_a, q_a2, q_b, q_c, q_d, q_e

BANK, Q = make_bank()
for part in (q_a, q_a2, q_b, q_c, q_d, q_e):
    part.add(Q, inr, num)

ORDER = [2, 3, 4, 5, 1, 6]
NAMES = {1: "Understanding Securities Markets", 2: "Securities, Asset Allocation & Investing", 3: "Primary Markets",
         4: "Secondary Markets", 5: "Mutual Funds", 6: "Derivatives Markets"}
MARKS = {1: "10", 2: "20", 3: "20", 4: "20", 5: "20", 6: "10"}
build(BANK, ORDER, NAMES, MARKS,
      title="NISM XII Quiz", eyebrow="NISM-Series-XII · Securities Markets Foundation practice (Sept 2026 workbook)",
      sub="All 6 chapters, highest marks first. 5 questions for every expected exam question: 3 at exam level, 2 harder. Instant answer and reason after each click. Skip any question and come back to it later. Your time is recorded.",
      storage_key="nismxii-attempts-v1", out_name="../nism-xii/quiz.html")
