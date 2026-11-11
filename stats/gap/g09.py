from summary_lib import *
from helpers import P

def add(chap, sub):
    chap(9, "Coverage Map: Session Plan vs Your Notes", "—", 4)
    sub("Where to study each session-plan topic", 4,
      T(["Session-plan topic","Class","Where"],
        [["Introduction to research, problem formulation","1","This PDF, Ch 1"],["Research design, types of research","2","This PDF, Ch 2 (+ Statistics Summary Ch 1)"],
         ["Primary and secondary data","3–4","This PDF, Ch 3"],["Sampling techniques","3–4","Statistics Summary Ch 2 (+ this PDF Ch 3)"],
         ["Measurement scaling techniques","5–6","This PDF, Ch 4 (+ Statistics Summary Ch 1 scales)"],["Questionnaire designing","5–6","This PDF, Ch 5"],
         ["Hypotheses, LOS, Type I/II, power, df","7–8","Statistics Summary Ch 6 + this PDF Ch 7"],["Point and interval estimates; differences","9–10","This PDF, Ch 6"],
         ["One-sample, two-sample, paired t","11–13","Statistics Summary Ch 7 + this PDF Ch 7"],["z tests for means and proportions, F-test, ANOVA","14–18","Statistics Summary Ch 7, 8, 10"],
         ["Chi-square goodness of fit and contingency table","19–21","Statistics Summary Ch 9"],["Report structure and components","22–23","This PDF, Ch 8"]]))
