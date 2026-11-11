from summary_lib import *
from helpers import P

def add(chap, sub):
    chap(1, "Research Basics: Quantitative vs Qualitative, Designs, Scales", "—", 4)
    sub("What 'quantitative' and 'qualitative' research mean", 4,
      P("<b>In plain words:</b> research is a careful way of answering a question with evidence. "
        "<b>Quantitative</b> research collects <b>numbers</b> (marks, income, ratings out of 5) and analyses them with statistics. "
        "<b>Qualitative</b> research collects <b>words and meanings</b> (interviews, quotations, observations) and looks for themes.") +
      T(["Point (from your notes)","Quantitative","Qualitative"],
        [["Data form","Numbers","Quotations, text"],["Time needed","More","Less"],
         ["Expertise needed","More (statistics)","Less"],["Typical sample size","At least <b>200</b>","Small — about <b>15 to 20</b> people"],
         ["Software mentioned","Statistical software (e.g. SPSS — Added)","<b>Atlas.ti</b>"],
         ["Engagement with respondent","Less (fixed questions)","More (open conversation)"],
         ["Scope for triangulation","Less","More"]]) +
      K("Triangulation = checking a finding from two or more sources or methods so that it is more believable"))
    sub("Research designs", 4,
      P("<b>In plain words:</b> a research design is the overall plan of a study — who you study, how, and what you compare.") +
      T(["Approach","Designs listed in your notes","One-line meaning (Added)"],
        [["Qualitative","Grounded theory","Build a new theory from the data itself"],["","Ethnography","Live with a group and observe its culture"],
         ["","Narrative research","Study people's life stories"],["","Case study","Deep study of one person, firm or event"],
         ["Quantitative","Experimental","Change one thing (treatment) and measure the effect"],["","Action research","Researcher solves a real problem while studying it"],
         ["","Survey","Ask many people fixed questions"],["","Correlational","Measure whether two variables move together"]]))
    sub("Population, sample, sampling frame, sampling error", 5,
      P("<b>In plain words:</b> the <b>population</b> is everyone you want to know about (all students in India). "
        "You usually cannot ask all of them, so you pick a smaller group — the <b>sample</b>. "
        "The <b>sampling frame</b> is the list or source from which you can actually reach the population (a college register, a phone directory).") +
      T(["Term","Meaning"],
        [["Population","Whole group of interest"],["Sample","Part of the population actually studied"],
         ["Sampling frame","Where you can access the population data from"],
         ["Sampling error","Difference between a sample result and the true population value that happens just because you studied a part, not the whole"],
         ["Non-sampling error","Mistakes not caused by sampling: wrong recording, biased questions, non-response"]]) +
      TRAP("Your notes say sampling error is 'any bias attributed to mistake'. Strictly, <b>sampling error</b> comes from studying only a sample (chance), while mistakes and bias are <b>non-sampling errors</b>."))
    sub("Scales of measurement", 5,
      P("<b>In plain words:</b> the scale tells you what kind of numbers you have, and so which statistics you may use.") +
      T(["Scale","Meaning","Example","Allowed maths"],
        [["Nominal","Names/labels only; number has no relation to the object","Gender, brand, colour (1 = red, 2 = blue)","Counts, mode, <b>chi-square</b>"],
         ["Ordinal","Order or rank matters, gaps not equal","1st/2nd/3rd, low/medium/high","Median, ranks"],
         ["Interval (Added — blank in notes)","Equal gaps, but no true zero","Temperature in °C","Mean, SD, t, z, ANOVA"],
         ["Ratio (Added)","Equal gaps <b>and</b> a true zero","Income, weight, marks","All of the above + ratios"]]) +
      K("Nominal data are also called <b>categorical</b> or <b>attribute</b> data (Krishan's chi-square notes)"))
