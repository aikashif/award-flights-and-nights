from summary_lib import *
from helpers import P, bell

def add(chap, sub):
    chap(6, "Point & Interval Estimates (Confidence Intervals)", "Module 3 · Classes 9–10", 5)
    sub("Point vs interval estimates", 5,
      P("<b>In plain words:</b> a <b>point estimate</b> is one number used as a best guess for a population value (sample mean 50 → guess μ = 50). An <b>interval estimate</b> gives a range that probably contains the true value, with a stated <b>confidence level</b> (e.g. 95%).") +
      T(["Population parameter","Point estimator","Standard error (SE)"],
        [["Mean μ","Sample mean x̄","σ/√n (or s/√n)"],["Proportion p","Sample proportion p̂ = x/n","√(p̂q̂/n), q̂ = 1 − p̂"],
         ["Difference μ₁ − μ₂","x̄₁ − x̄₂","√(s₁²/n₁ + s₂²/n₂)"],["Difference p₁ − p₂","p̂₁ − p̂₂","√(p̂₁q̂₁/n₁ + p̂₂q̂₂/n₂)"],
         ["Variance σ²","s² (divide by n − 1)","—"]]) +
      T(["Quality of a good estimator","Meaning"],
        [["Unbiased","Its average over all samples equals the parameter (E(x̄) = μ)"],["Efficient","Smallest standard error among unbiased estimators"],
         ["Consistent","Gets closer to the parameter as n grows"],["Sufficient","Uses all the information in the sample"]]))
    sub("General form of a confidence interval", 5,
      F("CI = point estimate ± (critical value × standard error)\nMargin of error E = critical value × SE\nz values: 90% → 1.645 ; 95% → 1.96 ; 99% → 2.576") +
      bell("95% CI: 2.5% in each tail", "two", "±1.96 SE around the estimate") +
      K("Meaning of 95%: if we took many samples and built a CI from each, about 95% of them would contain the true μ",
        "Wider interval when: higher confidence, smaller n, bigger σ",
        "Link to tests: if a two-tailed 5% test value lies <b>outside</b> the 95% CI → reject H₀") +
      TRAP("Do not say 'there is a 95% probability that μ is in this interval' — μ is fixed; the interval is what varies."))
    sub("CI for a mean: σ known or large sample (z)", 5,
      F("x̄ ± z × σ/√n   (n ≥ 30: use s for σ)\nn = 36, x̄ = 50, σ = 12, 95%\nSE = 12/√36 = 2 ; E = 1.96 × 2 = 3.92\nCI = 50 ± 3.92 = <b>(46.08, 53.92)</b>\nFinite population (n/N &gt; 5%): multiply SE by √[(N − n)/(N − 1)]"))
    sub("CI for a mean: σ unknown, small sample (t)", 5,
      F("x̄ ± t(α/2, n − 1) × s/√n\nn = 16, x̄ = 72, s = 8, 95% → df 15, t = 2.131\nSE = 8/4 = 2 ; E = 2.131 × 2 = 4.262\nCI = 72 ± 4.26 = <b>(67.74, 76.26)</b>") +
      T(["df","t one-tail 5% (two-tail 10%)","t two-tail 5%"],
        [["5","2.015","2.571"],["10","1.812","2.228"],["15","1.753","2.131"],["20","1.725","2.086"],["30","1.697","2.042"],["∞ (= z)","1.645","1.960"]]) +
      K("t has fatter tails than z → wider interval; t → z as n grows",
        "Assumes the population is roughly normal"))
    sub("CI for a proportion", 5,
      F("p̂ ± z × √(p̂q̂/n)   (need np̂ and nq̂ ≥ 5)\n120 of 400 customers prefer brand A → p̂ = 0.30\nSE = √(0.30 × 0.70 / 400) = 0.0229 ; E = 1.96 × 0.0229 = 0.0449\nCI = 0.30 ± 0.045 = <b>(0.255, 0.345)</b> → 25.5% to 34.5%"))
    sub("CIs for differences (analysis of differences)", 5,
      P("<b>In plain words:</b> to compare two groups, build a CI for the <b>difference</b>. If the interval does not include 0, the groups really differ.") +
      F("Means, large samples: (x̄₁ − x̄₂) ± z √(s₁²/n₁ + s₂²/n₂)\nx̄₁ 85, s₁ 10, n₁ 50 ; x̄₂ 80, s₂ 12, n₂ 60\nSE = √(100/50 + 144/60) = √4.4 = 2.098 ; E = 1.96 × 2.098 = 4.11\nCI = 5 ± 4.11 = <b>(0.89, 9.11)</b> → excludes 0 → significant difference") +
      F("Means, small samples (pooled): (x̄₁ − x̄₂) ± t(n₁ + n₂ − 2) × s_p √(1/n₁ + 1/n₂)\nProportions: (p̂₁ − p̂₂) ± z √(p̂₁q̂₁/n₁ + p̂₂q̂₂/n₂)\nCity A 80/200 = 0.40, city B 60/200 = 0.30\nSE = √(0.24/200 + 0.21/200) = 0.0474 ; E = 0.093\nCI = 0.10 ± 0.093 = <b>(0.007, 0.193)</b> → excludes 0 → A higher") +
      K("Paired data: CI = D̄ ± t(n − 1) × s_D/√n"))
    sub("Sample size for estimation", 5,
      F("Mean: n = (z σ / E)²\nσ = 12, E = 2, 95% → (1.96 × 12 / 2)² = 138.3 → <b>139</b> (always round <b>up</b>)\nProportion: n = z² p q / E²\nNo prior p → use p = 0.5 (largest n)\nE = 0.03, 95% → 1.96² × 0.25 / 0.0009 = 1,067.1 → <b>1,068</b>") +
      K("Halving E needs four times the sample","Higher confidence or larger σ → larger n"))
