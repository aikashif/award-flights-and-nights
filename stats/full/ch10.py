from summary_lib import *
from helpers import P

def add(chap, sub):
    chap(10, "Analysis of Variance (ANOVA) — Dr Krishan Pandey", "—", 5)
    sub("What ANOVA does", 5,
      P("<b>In plain words:</b> a t-test compares two means. ANOVA compares <b>three or more</b> means at once. "
        "It splits the total spread of the scores into two parts: spread <b>between</b> the groups (are the group means far apart?) and spread <b>within</b> the groups (how much people in the same group differ). "
        "If between-group spread is large compared to within-group spread, the groups really differ.") +
      F("F = MSB / MSW\nMSB = SSB / df_B      df_B = K − 1        (K = number of groups)\nMSW = SSW / df_W      df_W = N_T − K      (N_T = total subjects)\nSST = SSB + SSW       df_T = N_T − 1") +
      F("SSB = (ΣX₁)²/n₁ + (ΣX₂)²/n₂ + (ΣX₃)²/n₃ − (ΣX_T)²/N_T\nSSW = [ΣX₁² − (ΣX₁)²/n₁] + [ΣX₂² − (ΣX₂)²/n₂] + [ΣX₃² − (ΣX₃)²/n₃]\nSST = ΣX_T² − (ΣX_T)²/N_T") +
      K("One independent variable → <b>one-way</b> ANOVA; two → <b>two-way</b> ANOVA","H₀: all means equal; Hₐ: 'not H₀' — some or all means differ"))
    sub("One-way ANOVA (worked: test anxiety)", 5,
      T(["","Group 1 (5 h therapy)","Group 2 (10 h)","Group 3 (15 h)"],
        [["Scores","48, 50, 53, 52, 50","55, 52, 53, 55, 53","51, 52, 50, 53, 50"],["ΣX","253","268","256"],["ΣX²","12,817","14,372","13,114"],["Mean","50.6","53.6","51.2"]]) +
      F("ΣX_T = 777, N_T = 15, ΣX_T² = 40,303 → (ΣX_T)²/N_T = 40,248.6\nSSB = 253²/5 + 268²/5 + 256²/5 − 40,248.6 = <b>25.2</b>\nSST = 40,303 − 40,248.6 = <b>54.4</b> ;  SSW = 54.4 − 25.2 = <b>29.2</b>\nMSB = 25.2/2 = 12.6 ; MSW = 29.2/12 = 2.43 ; F = <b>5.178</b>\nF.05(2,12) = 3.88 → 5.178 ≥ 3.88 → <b>reject H₀</b>") +
      T(["Source","SS","df","MS","F","p"],[["Between","25.20","2","12.60","5.178","&lt; .05"],["Within","29.20","12","2.43","",""],["Total","54.40","14","","",""]]) +
      K("Result: amount of therapy significantly affects test anxiety scores",
        "Next: <b>post hoc</b> (after-the-fact) comparisons to see <b>which</b> pairs differ — only when F is significant"))
    sub("Practice problems (answers from the notes)", 5,
      T(["Problem","F (df)","F crit","Decision","Meaning"],
        [["1. Antidepressant: placebo vs low vs moderate dose (Beck scores)","11.26 (2,12)","6.93 at 1%","Significant, p &lt; .01","Placebo differs from both doses; low vs moderate no difference → low dose recommended"],
         ["2. US history scores by major (4 groups, 32 students)","0.04 (3,28)","—","Not significant","All majors equal (equally poor); if wrong, it's a Type II error"],
         ["3. Rat environment and maze learning (4 groups)","12.71 (3,16)","5.29 at 1%","Significant, p &lt; .01","Differences appear only between groups at least two levels apart"]]) +
      K("Problem 1: α = .01 chosen because a false 'drug works' claim (Type I) would be costly","Problem 2: α = .05 because little risk either way") +
      TRAP("In Problem 3 the notes say enriched vs super enriched is 'no significant difference' but print 'p &lt; .05' beside it. Treat it as <b>not significant</b>."))
    sub("Two-way ANOVA: main effects & interaction", 5,
      P("<b>In plain words:</b> two factors at once (e.g. protein level and gender). A <b>main effect</b> is the effect of one factor on its own. An <b>interaction</b> means the effect of one factor changes depending on the other.") +
      T(["Protein breakfast study","SS","df","MS","F","Result"],
        [["Protein level","20","1","20.00","8.89","Significant, p &lt; .01"],["Gender","45","1","45.00","20.00","Significant, p &lt; .01"],
         ["Protein × Gender","5","1","5.00","2.22","Not significant"],["Within","36","16","2.25","",""],["Total","106","19","","",""]]) +
      K("Means: males high 8, low 5; females high 4, low 3","High protein → better fitness; males score higher") +
      T(["Life satisfaction study","SS","df","MS","F","Result"],
        [["Age","180","2","90.00","49.09","Significant, p &lt; .01"],["Gender","30","1","30.00","16.36","Significant, p &lt; .01"],
         ["Age × Gender","0","2","0.00","0.00","No interaction"],["Within","44","24","1.83","",""],["Total","254","29","","",""]]) +
      K("Older adults most satisfied, young least; women more satisfied than men","Without post hoc tests you can't say exactly which age groups differ"))
