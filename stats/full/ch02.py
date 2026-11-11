from summary_lib import *
from helpers import P

def add(chap, sub):
    chap(2, "Sampling Methods", "—", 5)
    sub("Why the way you choose a sample matters", 4,
      P("<b>In plain words:</b> a sample is useful only if it looks like the population. If you ask only your friends, you learn about your friends, not about everyone. "
        "So statisticians use <b>random</b> methods, where chance — not you — decides who is in the sample.") +
      L("Parameters (μ, σ, p) describe the population and are usually <b>unknown</b>",
        "Pollster: knows answers are agree/disagree (binomial) but not p, the true share who agree",
        "Agronomist: knows wheat yield is roughly normal but not μ or σ",
        "The <b>sampling plan</b> (experimental design) decides how much information you get and how reliable it is"))
    sub("Simple random sampling", 5,
      P("<b>In plain words:</b> every possible group of n people has the <b>same chance</b> of being picked — like drawing names from a hat.") +
      F("89 students, need a group of 5:\n1. Number students 01 to 89\n2. Read 5 pairs of digits from a random number table\n3. If 90–99 or 00 comes up, skip it and read another\n4. The 5 students with those numbers form the group") +
      K("Use a computer or random number table","Problems: <b>non-response</b>, <b>undercoverage</b>, <b>wording bias</b>"))
    sub("Observational studies vs experiments", 4,
      T(["Type","Meaning","Watch out for"],
        [["Observational study","Data already existed before you studied it","<b>Non-response</b> (only opinionated people reply) · <b>Undercoverage</b> (some groups left out) · <b>Wording bias</b> (confusing questions)"],
         ["Experiment","You create data by applying a treatment to units","Population may be hypothetical; sample must be representative and <b>behave like a random sample</b>"]]))
    sub("Other random (probability) sampling plans", 5,
      T(["Plan","How","Example from the deck"],
        [["Stratified random","Split population into groups (<b>strata</b>), take a simple random sample from <b>each</b>","Random sample within every county of California"],
         ["Cluster","Split into groups (<b>clusters</b>, made of neighbouring elements), randomly pick some clusters, study <b>everyone</b> in them","Pick 10 random city blocks and interview all residents; pick 10 random counties"],
         ["1-in-k systematic","Pick a random start among the first k, then every k-th one","Random entry in phone book, then every 50th (1-in-50)"]]) +
      TRAP("Stratified = sample <b>from every</b> group. Cluster = sample <b>some</b> groups and take <b>all</b> inside them. Exams swap these."))
    sub("Non-random (non-probability) sampling", 5,
      P("<b>In plain words:</b> here a person, not chance, decides who is included. These are cheap and quick but should <b>not</b> be used for statistical inference.") +
      T(["Plan","Meaning"],
        [["Convenience","Whoever is easy to reach (people walking by)"],["Judgment (judgement)","Researcher decides who is in"],
         ["Quota","Sample must match the population on chosen traits (gender, race…)"],["Purposive (notes)","Chosen for a specific purpose"],
         ["Snowball (notes)","'Referring' sampling — each respondent refers the next"]]) +
      K("Notes: probability sampling = simple random, systematic, stratified, cluster","Non-probability = judgment, quota, convenience, purposive, snowball"))
