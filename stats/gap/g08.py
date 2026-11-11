from summary_lib import *
from helpers import P

def add(chap, sub):
    chap(8, "Report Writing Mechanics", "Module 4 · Classes 22–23", 5)
    sub("Purpose and types of research reports", 4,
      P("<b>In plain words:</b> the report is the only thing most managers see. A good study with a poor report is often ignored. Write for the reader: clear, short, focused on the decision.") +
      T(["Type","Use"],
        [["Technical report","Full method, data, analysis — for specialists"],["Popular / management report","Findings and recommendations in plain language — for decision makers"],
         ["Short report (memo, letter)","Small studies, progress updates"],["Long (formal) report","Major projects"],["Oral presentation","Explain and discuss findings with the client"]]))
    sub("Structure and components of a research report", 5,
      T(["Part","Contents"],
        [["<b>Prefatory (front) part</b>",""],["Title page","Title, client, researcher, date"],["Letter of transmittal","Hands the report to the client; summarises the project"],
         ["Letter of authorisation","Client's approval to do the research"],["Table of contents","Sections, list of tables, figures, appendices"],
         ["<b>Executive summary</b>","1–2 pages: problem, approach, design, key findings, conclusions, recommendations — often the only part read"],
         ["<b>Main body</b>",""],["Introduction / problem definition","Background, decision problem, research problem, objectives"],
         ["Approach to the problem","Theory, models, research questions, hypotheses"],
         ["Research design","Type of design, information needed, data collection, scaling, questionnaire, sampling"],
         ["Data analysis","Methods used and why"],["Results / findings","Organised by objective; tables and charts"],
         ["Limitations and caveats","Time, budget, sample, non-response, measurement problems"],
         ["Conclusions and recommendations","Answer the problem; actions for management"],
         ["<b>End (appended) part</b>",""],["Appendices","Questionnaire, detailed tables, technical details"],["Bibliography / references","All sources in one citation style (APA, Harvard)"]]) +
      K("Some formats also add: abstract, acknowledgements, glossary, index"))
    sub("Guidelines for writing", 5,
      T(["Guideline","Meaning"],
        [["Know the readers","Technical depth to suit them; use their language"],["Easy to follow","Logical structure, headings, short paragraphs"],
         ["Presentable","Professional layout, page numbers, consistent format"],["Objective","Report results honestly, including findings against expectations"],
         ["Reinforce text with visuals","Tables and graphs for key points"],["Concise","No unnecessary words; but complete"],
         ["Findings vs conclusions vs recommendations","Findings = facts from data; conclusions = what they mean; recommendations = what to do"]]) +
      TRAP("Do not put raw computer output in the main body — put it in the appendix."))
    sub("Tables and graphs", 4,
      T(["Table element","Rule"],
        [["Title and number","Short, descriptive; Table 1, 2…"],["Arrangement","Order rows by size or logic"],["Basis of measurement","Units and base (n, %) shown"],
         ["Leaders, rulings, spaces","Guide the eye"],["Headings and stubs","Label columns and rows"],["Footnotes and sources","Explain and credit"]]) +
      T(["Graph","Best for"],
        [["Pie chart","Parts of a whole (few categories)"],["Bar / column chart","Comparing categories"],["Line chart","Trends over time"],
         ["Histogram","Distribution of a continuous variable"],["Pictograph, map","Simple visual messages, regions"],["Flow chart","Processes and steps"]]))
    sub("Oral presentation and follow-up", 4,
      K("Know the audience; rehearse; use visuals; tell → show → tell; keep eye contact; leave time for questions (KISS: keep it simple and straightforward)",
        "Help the client understand and act on the report; answer questions after delivery",
        "Evaluate the project afterwards: what to do better next time",
        "Ethics: report honestly, no selective reporting or misuse of statistics, protect respondent confidentiality"))
