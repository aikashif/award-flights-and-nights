from summary_lib import *
from helpers import P

def add(chap, sub):
    chap(12, "Cheat Sheet: Which Test Do I Use?", "—", 5)
    sub("Choosing the right test", 5,
      T(["Your question","Data","Test","Statistic"],
        [["Is one mean equal to a value? (n ≥ 30 or σ known)","Numbers","One-sample z","z = (x̄ − μ)/(σ/√n)"],
         ["Same, but n &lt; 30 and σ unknown","Numbers","One-sample t","t = (x̄ − μ)/(s/√n), df n − 1"],
         ["Do two group means differ? (large)","Numbers","Two-sample z","(x̄₁ − x̄₂)/√(σ₁²/n₁ + σ₂²/n₂)"],
         ["Same people measured twice?","Numbers","Paired t","D̄/(s_D/√n)"],
         ["Is a share equal to a claimed value?","Yes/no","One-sample proportion z","(p̂ − P)/√(PQ/n)"],
         ["Do two variances differ?","Numbers","F-test","larger s² / smaller s²"],
         ["Do 3+ group means differ?","Numbers","ANOVA","F = MSB/MSW"],
         ["Do counts fit an expected pattern?","Categories","χ² goodness of fit","Σ(O − E)²/E, df k − 1"],
         ["Are two categorical variables linked?","Categories","χ² independence","Σ(O − E)²/E, df (r−1)(c−1)"]]))
    sub("Ten things beginners get wrong", 5,
      L("Reject H₀ when p is <b>small</b> (≤ α), not large",
        "'Do not reject' ≠ 'H₀ proved true'",
        "Type I = rejecting a true H₀ (α); Type II = keeping a false H₀ (β)",
        "Sample SD divides by <b>n − 1</b>; population SD by N",
        "Standard error = σ/√n — it shrinks as n grows",
        "Stratified samples every stratum; cluster takes all members of some clusters",
        "χ² needs counts (nominal data), not means; it is non-parametric",
        "ANOVA tells you <b>that</b> means differ; post hoc tests tell you <b>which</b>",
        "Two-tailed 5% uses 1.96; one-tailed 5% uses 1.645",
        "CLT: sample means are roughly normal when n ≥ 30, even from a skewed population"))
