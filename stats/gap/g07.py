from summary_lib import *
from helpers import P, bell

def add(chap, sub):
    chap(7, "t-Tests in Full, Power of a Test & Degrees of Freedom", "Module 3 · Classes 7–13", 5)
    sub("Two independent samples t-test (pooled variance)", 5,
      P("<b>In plain words:</b> compare the means of two separate small groups (n &lt; 30) when population SDs are unknown. If we can assume equal population variances, we <b>pool</b> the two sample variances into one estimate.") +
      F("H₀: μ₁ = μ₂   Hₐ: μ₁ ≠ μ₂ (or &gt; / &lt;)\ns_p² = [(n₁ − 1)s₁² + (n₂ − 1)s₂²] / (n₁ + n₂ − 2)\nt = (x̄₁ − x̄₂) / [s_p √(1/n₁ + 1/n₂)]      df = n₁ + n₂ − 2") +
      F("Worked: method A n₁ = 10, x̄₁ = 20, s₁ = 4 ; method B n₂ = 12, x̄₂ = 17, s₂ = 5 ; α = 5% two-tailed\ns_p² = (9 × 16 + 11 × 25) / 20 = 419 / 20 = 20.95 → s_p = 4.577\nSE = 4.577 × √(1/10 + 1/12) = 4.577 × 0.428 = 1.960\nt = (20 − 17) / 1.960 = <b>1.53</b> ; df = 20 → t crit = 2.086\n|1.53| &lt; 2.086 → <b>do not reject H₀</b>: no significant difference\n95% CI = 3 ± 2.086 × 1.960 = (−1.09, 7.09) → includes 0 (same conclusion)") +
      K("Check equal variances first with the <b>F-test</b> (larger s² / smaller s²)",
        "Unequal variances → <b>Welch's t</b>: t = (x̄₁ − x̄₂)/√(s₁²/n₁ + s₂²/n₂) with adjusted (smaller) df",
        "Assumptions: independent random samples, roughly normal populations") +
      TRAP("Two independent groups ≠ paired data. Same people measured twice → use the <b>paired</b> t-test."))
    sub("Paired (dependent) t-test: worked", 5,
      P("<b>In plain words:</b> when each value in one group is linked to one in the other (same person before/after, matched pairs), test the <b>differences</b>. This removes person-to-person variation and is more powerful.") +
      F("D = after − before ; D̄ = ΣD/n ; s_D = √[Σ(D − D̄)²/(n − 1)]\nt = D̄ / (s_D/√n)     df = n − 1\nTraining: 6 employees, scores after − before: 3, 5, −1, 4, 2, 5\nD̄ = 18/6 = 3 ; deviations 0, 2, −4, 1, −1, 2 → squares sum = 26\ns_D = √(26/5) = 2.280 ; SE = 2.280/√6 = 0.931\nt = 3 / 0.931 = <b>3.22</b> ; df 5, two-tailed 5% crit = 2.571\n3.22 &gt; 2.571 → <b>reject H₀</b>: training changed scores\n(one-tailed 'improved?' crit 2.015 → also reject)"))
    sub("Which mean test? (summary)", 5,
      T(["Situation","Test","Statistic","df"],
        [["One mean, σ known or n ≥ 30","z","(x̄ − μ)/(σ/√n)","—"],["One mean, σ unknown, n &lt; 30","t","(x̄ − μ)/(s/√n)","n − 1"],
         ["Two independent means, large","z","(x̄₁ − x̄₂)/√(s₁²/n₁ + s₂²/n₂)","—"],["Two independent means, small, equal σ²","Pooled t","(x̄₁ − x̄₂)/[s_p√(1/n₁ + 1/n₂)]","n₁ + n₂ − 2"],
         ["Two means, same subjects","Paired t","D̄/(s_D/√n)","n − 1"],["One proportion","z","(p̂ − p₀)/√(p₀q₀/n)","—"],
         ["Two proportions","z","(p̂₁ − p̂₂)/√[p̄q̄(1/n₁ + 1/n₂)], p̄ = (x₁ + x₂)/(n₁ + n₂)","—"],
         ["Two variances","F","s₁²/s₂² (larger on top)","n₁ − 1, n₂ − 1"],["3+ means","ANOVA F","MSB/MSW","k − 1, N − k"]]))
    sub("Power of a test", 5,
      P("<b>In plain words:</b> power = the chance the test <b>catches</b> a real effect = P(reject H₀ when H₀ is false) = 1 − β. Low power means real differences are missed (Type II errors).") +
      F("Worked: H₀: μ = 100 vs Hₐ: μ &gt; 100 ; σ = 15, n = 36 → SE = 2.5 ; α = 5% (z = 1.645)\nReject H₀ if x̄ &gt; 100 + 1.645 × 2.5 = <b>104.11</b>\nIf true μ = 106: β = P(x̄ ≤ 104.11 | μ = 106) = P(z ≤ (104.11 − 106)/2.5) = P(z ≤ −0.755) = <b>0.225</b>\nPower = 1 − 0.225 = <b>0.775</b>") +
      T(["Change","Effect on power"],
        [["Larger sample n","Up"],["Larger true difference (effect size)","Up"],["Higher α (e.g. 10% vs 5%)","Up (but more Type I errors)"],
         ["Smaller σ (less noise)","Up"],["One-tailed instead of two-tailed (right direction)","Up"]]) +
      K("Power curve: plot power against possible true μ values; operating characteristic (OC) curve plots β",
        "Common target: power ≥ 0.80 when planning sample size") +
      TRAP("α and β move in opposite directions for a fixed n — only a bigger sample cuts both."))
    sub("Degrees of freedom", 5,
      P("<b>In plain words:</b> degrees of freedom (df) = number of values free to vary after you use the data to estimate something. Knowing the mean of 5 numbers, only 4 can be chosen freely — the last is fixed. df picks the right row in t, χ² and F tables.") +
      T(["Test","df"],
        [["Sample variance / one-sample t","n − 1"],["Paired t","n − 1 (pairs)"],["Pooled two-sample t","n₁ + n₂ − 2"],
         ["Chi-square goodness of fit","k − 1 − (parameters estimated)"],["Chi-square independence","(r − 1)(c − 1)"],
         ["F-test for two variances","(n₁ − 1, n₂ − 1)"],["One-way ANOVA","between k − 1 ; within N − k ; total N − 1"],
         ["Two-way ANOVA (interaction)","(r − 1)(c − 1) for interaction"]]))
