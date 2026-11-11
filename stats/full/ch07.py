from summary_lib import *
from helpers import P

def add(chap, sub):
    chap(7, "Tests for Means: z-test and t-test (worked)", "—", 5)
    sub("Which test: z or t?", 5,
      P("<b>In plain words:</b> both compare a sample mean with a value (or with another mean). Use <b>z</b> when the sample is large (n ≥ 30) or the population SD is known. Use <b>t</b> when the sample is small (n &lt; 30) and you must estimate SD from the sample.") +
      T(["Small sample test (n &lt; 30)","Large sample test (n ≥ 30)"],
        [["<b>t-test</b>","<b>z-test</b> (normal test)"],["1. One sample (single mean)","1. One sample (single mean)"],
         ["2. Two independent samples","2. Two samples"],["3. Paired (dependent) t-test","3. Proportion test"]]) +
      F("One-sample t:  t = (x̄ − μ) / (σₛ/√n)       df = n − 1\nOne-sample z:  z = (x̄ − μ) / (σₚ/√n)\nσ/√n is the standard error (SE)"))
    sub("One-sample z-test (worked: heights)", 5,
      F("n = 400, x̄ = 67.47\", μ = 67.39\", σₚ = 1.30\", α = 5%\nI.   H₀: μ = 67.39   vs   Hₐ: μ ≠ 67.39 (two-tailed)\nII.  z = (x̄ − μ) / (σₚ/√n)\nIII. z = (67.47 − 67.39) / (1.30/20) = 0.08 / 0.065 = <b>1.23</b>\nIV.  z tab (5%, two-tailed) = 1.96 → |1.23| &lt; 1.96\nV.   <b>Do not reject H₀</b>: the sample is consistent with a population mean of 67.39\"") +
      K("If population size is unknown, treat it as infinite") +
      TRAP("Your notes say the sample 'belongs to the population whose mean was 67.47'. The population mean is <b>67.39</b>; 67.47 is the sample mean."))
    sub("Finite population correction (worked)", 4,
      P("<b>In plain words:</b> when the population is small and known (N), and you sample a big part of it, the SE shrinks. Multiply SE by √((N − n)/(N − 1)).") +
      F("z = (x̄ − μ) / [ (σₚ/√n) × √((N − n)/(N − 1)) ]\nN = 20, μ = 320, σₚ = 75, n = 5, x̄ = 300\nH₀: μ = 320  vs  Hₐ: μ ≠ 320\nz = (300 − 320) / [ (75/√5) × √(15/19) ] = −20 / 29.8 = <b>−0.67</b>\n|0.67| &lt; 1.96 → <b>do not reject H₀</b>: sample mean consistent with population mean at 95% confidence") +
      TRAP("One line in your notes writes the correction as (N − n)/(n − 1). The correct factor is <b>√((N − n)/(N − 1))</b>, as used in the working."))
    sub("One-tailed z-test (worked: production process)", 5,
      F("μ = 50, σₚ = 2.5, n = 12, x̄ = 48.5, α = 5%\nH₀: μ = 50 (process unchanged)   Hₐ: μ &lt; 50 (manager guards against a fall)\nz = (48.5 − 50) / (2.5/√12) = −1.5 / 0.722 = <b>−2.08</b>\nz tab (5%, one-tailed) = 1.645 → |2.08| &gt; 1.645\n<b>Reject H₀</b>: the process mean has fallen") +
      TRAP("The notes write σ/√5 in one line and label Hₐ as 'H₀: μ &lt; 50'. Use √12 (n = 12) and call μ &lt; 50 the <b>alternative</b>."))
    sub("One-sample t-test (worked: bag weights)", 5,
      F("Values: 578, 572, 570, 568, 572, 578, 570, 572, 596, 544   (n = 10)\nH₀: μ = 578   Hₐ: μ ≠ 578\nx̄ = 5720/10 = 572\nΣ(x − x̄)² = 36+0+4+16+0+36+4+0+576+784 = 1456\nσₛ = √(1456/9) = <b>12.72</b>\nt = (572 − 578) / (12.72/√10) = <b>−1.49</b>\nt tab (9 df, 5%, two-tailed) = 2.262 → |1.49| &lt; 2.262 → <b>do not reject H₀</b>") +
      F("Second example: n = 12, x̄ = 6576/12 = 548, H₀: μ = 500, Hₐ: μ &gt; 500\nσₛ = √(23979/11) = 46.68\nt = (548 − 500) / (46.68/√12) = <b>3.56</b>\nt tab (11 df, 5%, one-tailed) = 1.796 (Added) → <b>reject H₀</b>: mean exceeds 500"))
    sub("Two-sample z-test (worked)", 5,
      F("z = [(x̄₁ − x̄₂) − (μ₁ − μ₂)] / √(σ₁²/n₁ + σ₂²/n₂)\nUnder H₀: μ₁ − μ₂ = 0 → z = (x̄₁ − x̄₂) / √(σ₁²/n₁ + σ₂²/n₂)\nσ's unknown → use sample σₛ₁², σₛ₂²\nSame σ for both → z = (x̄₁ − x̄₂) / [σ √(1/n₁ + 1/n₂)]  (σ unknown → combined σ)") +
      F("n₁ = 100, x̄₁ = 200, n₂ = 150, x̄₂ = 220, population σ = 11, α = 5%\nH₀: μ₁ = μ₂ (same population)   Hₐ: μ₁ ≠ μ₂\nz = (200 − 220) / [11 √(1/100 + 1/150)] = −20 / 1.42 = <b>−14.08</b>\n|14.08| &gt; 1.96 → <b>reject H₀</b>: the two samples come from different populations"))
    sub("Paired (dependent) t-test", 4,
      P("<b>In plain words:</b> use it when the same people are measured twice (before and after a course). Work with the differences D.") +
      F("t = D̄ / (σ_D/√n)       σ_D = √[ (1/(n−1)) Σ(Dᵢ − D̄)² ]       df = n − 1"))
