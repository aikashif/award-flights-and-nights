from summary_lib import *
from helpers import P

def add(chap, sub):
    chap(8, "Tests for Proportions & Variances (F-test)", "—", 4)
    sub("One-sample proportion test", 5,
      P("<b>In plain words:</b> use it for <b>attributes</b> — something present or absent (male/female, defective/good). You compare the sample share with a claimed population share.") +
      F("z = (p̂ − P) / √(PQ/n)        Q = 1 − P\nBirths: n = 3232, boys 1705 → p̂ = 0.5275; claim P = 1/2\nz = (0.5275 − 0.5) / √(0.5 × 0.5 / 3232) = <b>3.13</b> &gt; 1.96 → <b>reject H₀</b>: the data do not support a 50:50 ratio") +
      F("First class passengers: n = 400, 70 hold first class → p̂ = 0.175; H₀: P = 0.20, Hₐ: P ≠ 0.20\nz = (0.175 − 0.20) / √(0.2 × 0.8 / 400) = −0.025 / 0.02 = <b>−1.25</b>\nAt 10%: z tab = 1.645 → |1.25| &lt; 1.645 → <b>do not reject H₀</b>") +
      F("Defectives: n = 400, 34 defective → p̂ = 0.085; H₀: P = 10%, Hₐ: P &lt; 10%\nz = (0.085 − 0.10) / √(0.10 × 0.90 / 400) = −0.015 / 0.015 = <b>−1.0</b>\nAt 1% one-tailed: z tab = 2.33 → <b>do not reject H₀</b>"))
    sub("Two-sample proportion test", 4,
      F("z = (p₁ − p₂) / √(P₁Q₁/n₁ + P₂Q₂/n₂)") +
      TRAP("Your notes write the two-sample proportion test with x̄ and σ² terms. That is the formula for two <b>means</b>. For proportions use p and pq, as above."))
    sub("F-test for equality of variances", 5,
      P("<b>In plain words:</b> it checks whether two samples are equally spread out ('homogeneous'). Homogeneous variance means one group is not more variable than the other.") +
      F("H₀: σ₁² = σ₂²   vs   Hₐ: σ₁² ≠ σ₂²\nF = larger sample variance / smaller sample variance\nSample variance = Σ(x − x̄)² / df\nNumerator df = df of the larger variance (n₁ − 1); denominator df = n₂ − 1") +
      K("Also called the <b>variance ratio test</b>","Always put the higher variance on top, so F ≥ 1"))
