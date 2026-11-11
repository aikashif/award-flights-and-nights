from summary_lib import *
from helpers import P

def add(chap, sub):
    chap(3, "Describing Data: Spread, Parameters, Statistics, Estimation", "—", 5)
    sub("Measures of spread: range, mean deviation, variance, SD", 5,
      P("<b>In plain words:</b> the mean tells you the centre. Spread tells you how far the values sit from that centre. "
        "If spread (variance) is high, the mean is a poor summary of the data — your notes say 'variance high, mean not good'.") +
      F("Range = largest − smallest        (a crude measure)\nMean deviation = (1/N) Σ |xᵢ − x̄|\nVariance σ² = (1/N) Σ (xᵢ − x̄)²     = average squared distance from the mean\nStandard deviation σ = √variance") +
      F("Worked: values 1, 2, 3 → mean 2\nVariance = [(1−2)² + (2−2)² + (3−2)²] ÷ 3 = (1 + 0 + 1) ÷ 3 = 2/3\nSD = √(2/3) ≈ 0.816"))
    sub("Parameter vs statistic", 5,
      P("<b>In plain words:</b> a <b>parameter</b> is a number about the whole population (usually unknown). A <b>statistic</b> is the same kind of number worked out from your sample (known).") +
      T(["","Population parameter","Sample statistic"],
        [["Mean","μ","x̄"],["SD","σₚ (σ)","σₛ (s)"],["Variance","σₚ²","σₛ²"],["Proportion","p (P)","p̂ (p)"]]) +
      K("Going from the known sample to a guess about the unknown population = <b>estimation</b>","Hypotheses are tested with sample statistics"))
    sub("Sample SD: why divide by n − 1", 5,
      P("<b>In plain words:</b> if you divide by n when working out a <b>sample</b> variance, the answer is on average a bit too small. Dividing by <b>n − 1</b> fixes this, so it is 'unbiased'.") +
      F("Population SD:  σₚ = √[ (1/N) Σ(xᵢ − x̄)² ]\nSample SD:      σₛ = √[ (1/(n−1)) Σ(xᵢ − x̄)² ]\nWith divisor n: E(σₛ²) = ((n−1)/n) σₚ²   → biased (too small)\nMultiply by n/(n−1):  (n/(n−1)) × (1/n) Σ(xᵢ − x̄)² = (1/(n−1)) Σ(xᵢ − x̄)²  → unbiased") +
      T(["Sample (n = 2, with replacement) from {1,2,3}","x̄"],
        [["(1,1)","1"],["(1,2) (2,1)","1.5"],["(1,3) (2,2) (3,1)","2"],["(2,3) (3,2)","2.5"],["(3,3)","3"]]) +
      K("Average of all 9 sample means = 2 = μ → <b>E(x̄) = μ</b>: the sample mean is an <b>unbiased estimator</b>",
        "If σₚ is not given, use σₛ as its estimate") +
      TRAP("Your notes use capital N for the sample size in this proof. Read it as small n (sample size)."))
    sub("Standard error", 5,
      P("<b>In plain words:</b> if you took many samples, their means would differ a little. The <b>standard error</b> is the SD of those sample means. Bigger samples → smaller standard error → more precise.") +
      F("SE of mean = σ / √n\nSE of proportion = √(pq / n)") +
      K("σ = SD, σ² = variance, σ/√n = standard error"))
