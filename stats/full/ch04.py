from summary_lib import *
from helpers import P, bell

def add(chap, sub):
    chap(4, "Probability Distributions: Binomial, Poisson, Geometric, Normal", "—", 4)
    sub("Binomial distribution", 5,
      P("<b>In plain words:</b> you repeat a yes/no trial n times (toss a coin 10 times). Each trial has success chance p and failure chance q = 1 − p. The binomial gives the chance of exactly x successes.") +
      F("P(x) = ⁿCₓ pˣ qⁿ⁻ˣ ,   x = 0, 1, 2 … n\nMean = np      SD = √(npq)") +
      K("n is finite","Pollster's agree/disagree answers follow a binomial"))
    sub("Poisson distribution", 4,
      P("<b>In plain words:</b> when trials are extremely many (n → ∞) and success is very rare (p → 0) but np stays a fixed number λ, the binomial turns into the <b>Poisson</b> — used for counts of rare events (accidents per day).") +
      F("P(X = x) = e^(−λ) λˣ / x! ,   x = 0, 1, 2 … ∞      λ = np"))
    sub("Geometric distribution", 3,
      P("<b>In plain words:</b> you keep tossing a coin and stop the moment you get the first head. The number of tosses needed follows the <b>geometric</b> distribution.") +
      F("P(first success on trial x) = q^(x−1) p   (Added)"))
    sub("Normal distribution & z-score", 5,
      P("<b>In plain words:</b> the normal curve is the symmetric bell shape. Most values sit near the mean; few are far away. "
        "A <b>z-score</b> says how many SDs a value is from the mean. Converting to z lets one table (Table 3) give every normal probability.") +
      F("z = (x − mean) / SD        → standard normal variate (mean 0, SD 1)\nRuns from −∞ to +∞, centred at 0") +
      T(["Area rule (Added)","Share of values"],[["Within ±1 SD","≈ 68%"],["Within ±2 SD","≈ 95%"],["Within ±3 SD","≈ 99.7%"]]) +
      PO(bell("Standard normal curve", "none", "Centre 0, symmetric")))
