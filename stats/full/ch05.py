from summary_lib import *
from helpers import P, bell

def add(chap, sub):
    chap(5, "Sampling Distributions & the Central Limit Theorem", "—", 5)
    sub("What a sampling distribution is", 5,
      P("<b>In plain words:</b> a <b>statistic</b> (like the sample mean) changes from sample to sample, so it is a random variable. "
        "If you list every value it can take and how often, you get its <b>sampling distribution</b>.") +
      F("Population: 3, 5, 2, 1   → all samples of n = 3, without replacement\n3,5,2 → x̄ = 3.33 ; 3,5,1 → 3 ; 3,2,1 → 2 ; 5,2,1 → 2.67\nEach x̄ has probability 1/4") +
      K("Found by maths, by simulation, or by theorems like the Central Limit Theorem"))
    sub("Central Limit Theorem (CLT)", 5,
      P("<b>In plain words:</b> even if the population is not bell-shaped, the <b>average</b> of a large random sample behaves like a bell curve. "
        "This is why the normal curve appears everywhere in statistics.") +
      F("If the population has mean μ and SD σ, then for large n:\nx̄ ~ approximately Normal(mean = μ, SD = σ/√n)\nSum of n values ~ approximately Normal(mean = nμ, SD = σ√n)") +
      T(["Population shape","How large must n be?"],
        [["Normal","Any n — x̄ is always normal"],["Roughly symmetric","Fairly small n"],["Skewed","n ≥ <b>30</b>"]]) +
      T(["Die example (fair die, faces 1–6)","Mean","SD of x̄"],
        [["n = 1 (flat/uniform)","3.5","1.71"],["n = 2 (mound-shaped)","3.5","1.71/√2 = 1.21"],["n = 3 (≈ normal)","3.5","1.71/√3 = 0.987"]]) +
      TRAP("The deck says 'toss a fair coin', but the values 1–6 show it is a <b>die</b>."))
    sub("Sampling distribution of the sample mean", 5,
      F("Mean of x̄ = μ        SD of x̄ (standard error) = σ/√n\nz = (x̄ − μ) / (σ/√n)\nn = 16 from Normal(μ 10, σ 8): P(x̄ &gt; 12) = P(z &gt; (12−10)/(8/4)) = P(z &gt; 1) = 1 − .8413 = <b>.1587</b>\nSoda fills: μ 12.1 oz, σ 0.2, 6-pack: P(x̄ &lt; 12) = P(z &lt; (12 − 12.1)/(0.2/√6)) = P(z &lt; −1.22) = <b>.1112</b>"))
    sub("Sampling distribution of the sample proportion", 5,
      P("<b>In plain words:</b> p̂ = x/n is the share of 'successes' in your sample (e.g. share of defective cans). For large n it is also roughly normal.") +
      F("Mean of p̂ = p        SE = √(pq/n)        z = (p̂ − p) / √(pq/n)\nCondition: np &gt; 5 and nq &gt; 5\nn = 100, p = .4: P(p̂ &gt; .5) = P(z &gt; (.5 − .4)/√(.4×.6/100)) = P(z &gt; 2.04) = 1 − .9793 = <b>.0207</b>\nSoda: claim p = .05 underfilled, n = 200 (np = 10, nq = 190 → OK)\nP(p̂ &gt; .10) = P(z &gt; (.10 − .05)/√(.05×.95/200)) = P(z &gt; 3.24) = 1 − .9994 = <b>.0006</b> → very unusual if p really is .05"))
