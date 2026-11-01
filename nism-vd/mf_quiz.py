"""NISM V-D mutual fund quiz (Ch1-12). Run: python3 nism-vd/mf_quiz.py

Question parts live in mf_q_*.py; each defines add(Q, inr, num).
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from quiz_lib import make_bank, inr, num, build
import mf_q_a, mf_q_b, mf_q_c

BANK, Q = make_bank()
for part in (mf_q_a, mf_q_b, mf_q_c):
    part.add(Q, inr, num)

ORDER = [9, 12, 7, 4, 5, 10, 1, 6, 11, 2, 3, 8]
NAMES = {1: "Investment Landscape", 2: "Concept & Role of a Mutual Fund", 3: "Legal Structure of MFs",
         4: "Legal & Regulatory Framework", 5: "Scheme Related Information", 6: "Fund Distribution & Channel Management",
         7: "NAV, TER & Pricing of Units", 8: "Taxation", 9: "Investor Services", 10: "Risk, Return & Performance of Funds",
         11: "Mutual Fund Scheme Performance", 12: "Mutual Fund Scheme Selection"}
MARKS = {1: "5", 2: "4", 3: "3", 4: "≈6", 5: "≈6", 6: "≈5", 7: "≈6", 8: "3", 9: "10", 10: "≈6", 11: "≈5", 12: "10"}
build(BANK, ORDER, NAMES, MARKS,
      title="NISM V-D Mutual Fund Quiz", eyebrow="NISM-Series-V-D · mutual fund module practice (Ch 1–12)",
      sub="All 12 mutual fund chapters, ordered by marks. 5 questions for every expected exam question: 3 at exam level, 2 harder. Instant answer and reason after each click. Skip any question and come back to it later. Your time is recorded.",
      storage_key="nismvd-mf-attempts-v1", out_name="mf-quiz.html")
