from summary_lib import *
from helpers import P, bell

def add(chap, sub):
    chap(6, "Hypothesis Testing: The Logic", "—", 5)
    sub("Null and alternative hypotheses", 5,
      P("<b>In plain words:</b> a hypothesis test is like a court case. The <b>null hypothesis (H₀)</b> is 'nothing special is happening' — the accused is innocent. "
        "The <b>alternative (Hₐ or H₁)</b> is what the researcher suspects. We keep H₀ unless the sample gives strong evidence against it.") +
      T(["","H₀ — statistical hypothesis","Hₐ / H₁ — research hypothesis"],
        [["Example","μ_girls = μ_boys (no difference in average marks)","μ_girls &gt; μ_boys, or &lt;, or ≠"],
         ["Always contains","'=' sign","'&gt;', '&lt;' or '≠'"]]) +
      T(["Hₐ","Test type","Rejection area"],[["μ ≠ value","Two-tailed","Both tails"],["μ &gt; value","One-tailed (right)","Right tail"],["μ &lt; value","One-tailed (left)","Left tail"]]) +
      PO(bell("Two-tailed, 5%", "two", "2.5% in each tail, z = ±1.96"), bell("Right-tailed, 5%", "right", "z = 1.645", 1.645)))
    sub("Type I and Type II errors", 5,
      T(["Decision","H₀ actually true","H₀ actually false"],
        [["Reject H₀","<b>Type I error</b> (probability α)","Correct (power = 1 − β)"],
         ["Do not reject H₀","Correct","<b>Type II error</b> (probability β)"]]) +
      F("α = P(reject H₀ | H₀ true) = level of significance (LOS)\nβ = P(do not reject H₀ | H₀ false)\nPower of test = 1 − β   → approaches 1 as β → 0\nCommon α: 1%, 2%, 5%, 10%") +
      K("Neyman–Pearson lemma: fix α, then choose the test with the highest power","ANOVA problem: α = 1% chosen when a false 'drug works' claim would be costly") +
      TRAP("Your notes say 'α = consumer risk, β = producer risk'. The standard terms are the other way: <b>α = producer's risk</b> (a good lot is rejected), <b>β = consumer's risk</b> (a bad lot is accepted).") +
      TRAP("'α = 1%' does not mean 'H₀ is true'. It means you accept a 1% chance of rejecting a true H₀ — i.e. 99% confidence."))
    sub("Decision rules: critical value and p-value", 5,
      T(["Compare","Decision"],
        [["|calculated| &gt; |tabulated| (critical)","<b>Reject H₀</b>"],["|calculated| &lt; |tabulated|","Do not reject H₀"],
         ["p-value ≤ 0.05","<b>Reject H₀</b> at 5%"],["p-value &gt; 0.05","Do not reject H₀ at 5%"]]) +
      P("<b>Reject H₀</b> is a strong decision: the sample evidence is statistically significant enough. <b>Do not reject</b> is weaker: we only lack evidence; we never 'prove' H₀.") +
      TRAP("One line in your notes says 'if p-value &gt; 0.05, reject H₀'. That is wrong. Reject when <b>p ≤ 0.05</b>. A small p-value means the data are unlikely if H₀ were true."))
    sub("Critical values you must remember", 5,
      T(["Test","Critical value"],
        [["z, 5%, two-tailed","<b>1.96</b>"],["z, 5%, one-tailed","<b>1.645</b>"],["z, 1%, two-tailed","2.58"],["z, 1%, one-tailed","2.33 (notes: 2.32)"],
         ["z, 10%, two-tailed","1.645 (notes round to 1.6)"],["t, 9 df, 5% two-tailed","2.262"],["χ², 4 df, 5%","9.488"],["χ², 9 df, 5%","16.92"],
         ["F(2,12), 5%","3.88"],["F(2,12), 1%","6.93"],["F(3,16), 1%","5.29"]]))
    sub("The step-by-step procedure", 5,
      F("1. State H₀ and Hₐ (decide one- or two-tailed)\n2. Set α (usually 5%)\n3. Compute the test statistic (z, t, χ², F) and its degrees of freedom\n4. Write the decision rule: reject H₀ if statistic ≥ critical value\n5. Decide: reject or do not reject\n6. State the result in plain English"))
