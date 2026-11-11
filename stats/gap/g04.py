from summary_lib import *
from helpers import P

def add(chap, sub):
    chap(4, "Measurement & Scaling Techniques", "Module 2 · Classes 5–6", 5)
    sub("Measurement and scaling: basic ideas", 5,
      P("<b>In plain words:</b> <b>measurement</b> = giving numbers to characteristics by a rule (1 = male, 2 = female). <b>Scaling</b> = placing objects on a continuum (very unhappy … very happy). Your notes cover the four scale levels (nominal, ordinal, interval, ratio); this chapter covers the scaling <b>techniques</b>.") +
      T(["Scale level (recap)","What you can say","Allowed statistics"],
        [["Nominal","Categories only","Count, mode, chi-square"],["Ordinal","Order","Median, percentiles, rank correlation"],
         ["Interval","Equal gaps, no true zero","Mean, SD, correlation, t, ANOVA"],["Ratio","True zero","All statistics, incl. ratios"]]))
    sub("Comparative scaling techniques", 5,
      P("<b>In plain words:</b> respondents compare objects <b>directly</b> with each other. Results are ordinal (relative), not absolute.") +
      T(["Technique","How","Example / note"],
        [["Paired comparison","Choose one of two objects, for every pair","n brands → n(n − 1)/2 pairs: 5 brands = 10 pairs; transitivity check"],
         ["Rank order","Rank all objects together","Rank 5 shampoos 1–5; quick, realistic; n − 1 decisions"],
         ["Constant sum","Share a fixed total (e.g. 100 points) across items","Brand attributes: price 40, quality 35, design 25; gives ratio-like data"],
         ["Q-sort","Sort many statements into piles by criteria","Used for large numbers of items (60–140)"]]) +
      K("Pros: easy to understand, small differences show up · Cons: ordinal only; results can't be generalised beyond the objects compared"))
    sub("Non-comparative scaling: continuous and itemised rating scales", 5,
      P("<b>In plain words:</b> each object is rated <b>on its own</b>, not against others.") +
      T(["Scale","How","Example"],
        [["Continuous (graphic) rating","Mark a point on a line","Worst ———|——— Best (score 0–100)"],
         ["<b>Likert</b> (summated)","Agree/disagree with statements, usually 5 points","1 Strongly disagree … 5 Strongly agree; sum or average items"],
         ["<b>Semantic differential</b>","7-point scale between two opposite adjectives","Cold 1 2 3 4 5 6 7 Warm; shows a profile of a brand"],
         ["<b>Stapel</b>","Unipolar −5 to +5 with one adjective in the middle, no zero","+5 … +1 [High quality] −1 … −5; good for phone surveys"]]) +
      T(["Scale decision","Options"],
        [["Number of categories","5–9 usual; more = finer but harder"],["Balanced vs unbalanced","Equal favourable/unfavourable categories or not"],
         ["Odd vs even","Odd has a neutral midpoint"],["Forced vs non-forced","Non-forced adds 'no opinion'"],
         ["Verbal description","Label all, some or only end points"],["Physical form","Horizontal/vertical, numbers, faces"]]) +
      TRAP("Likert data are strictly ordinal, but are usually <b>treated as interval</b> (means, t-tests) in practice."))
    sub("Multi-item scales and measurement error", 4,
      K("A construct (e.g. customer satisfaction) is measured with several items, then summed: develop theory → generate items → reduce items (expert judgement, pretest) → check reliability and validity → final scale") +
      F("Observed score X_O = X_T (true score) + X_S (systematic error) + X_R (random error)\nReliability: low X_R ; Validity: low X_S and X_R  (X_O = X_T)"))
    sub("Reliability and validity", 5,
      P("<b>In plain words:</b> <b>reliable</b> = gives the same result each time. <b>Valid</b> = measures what it should. A bathroom scale that always shows 2 kg too much is reliable but not valid.") +
      T(["Reliability type","How it is checked"],
        [["Test–retest","Same scale, same people, two times; correlate"],["Alternative forms","Two equivalent versions; correlate"],
         ["Internal consistency: split-half","Split items in two halves; correlate"],["Internal consistency: <b>Cronbach's alpha</b>","Average of all split-half coefficients; 0–1; <b>≥ 0.6</b> acceptable (≥ 0.7 often required)"]]) +
      T(["Validity type","Meaning"],
        [["Content (face) validity","Experts judge whether items cover the construct"],["Criterion validity","Agrees with a criterion: <b>concurrent</b> (same time) or <b>predictive</b> (future)"],
         ["Construct validity","Measures the theoretical construct: <b>convergent</b> (correlates with related measures), <b>discriminant</b> (not with unrelated), <b>nomological</b> (fits theory)"]]) +
      K("Valid ⇒ reliable · Reliable does <b>not</b> ⇒ valid · Unreliable ⇒ not valid",
        "Also: <b>generalisability</b> — can results extend beyond this sample and setting?"))
