from summary_lib import *
from helpers import P

def add(chap, sub):
    chap(5, "Questionnaire Design", "Module 2 · Classes 5–6", 5)
    sub("Why questionnaire design matters", 4,
      P("<b>In plain words:</b> a questionnaire is a fixed set of questions to get information from respondents. A badly worded question gives wrong data no matter how good the sample or analysis.") +
      K("Objectives: turn information needs into questions people <b>can</b> and <b>will</b> answer · motivate respondents to finish · minimise response error"))
    sub("The 10 steps of questionnaire design (Malhotra)", 5,
      F("1. Specify the information needed\n2. Specify the type of interviewing method\n3. Decide the content of individual questions\n4. Design questions to overcome inability and unwillingness to answer\n5. Decide the question structure\n6. Decide the question wording\n7. Arrange the questions in proper order\n8. Identify the form and layout\n9. Reproduce the questionnaire\n10. Pretest") +
      K("Step 3: is the question necessary? Do you need several questions instead of one? (avoid <b>double-barrelled</b> questions)",
        "Step 4 inability: is the respondent informed? can they remember? can they say it? — use filter questions, aided recall",
        "Step 4 unwillingness: reduce effort, explain purpose, make the context fit; sensitive topics last, use third-person or counter-biasing statements, ranges (income bands)"))
    sub("Question structure", 5,
      T(["Type","Description","Pros / cons"],
        [["Unstructured (open-ended)","Respondent answers in own words","Rich insight; hard to code, interviewer bias"],
         ["Multiple choice","Choose from given answers","Easy to analyse; need full, exclusive options; order bias → rotate"],
         ["Dichotomous","Two answers (yes/no), maybe a neutral","Simple; forces a choice; wording strongly affects result"],
         ["Scales","Likert, semantic differential, etc.","Measure attitudes (see Chapter 4)"]]))
    sub("Question wording rules", 5,
      T(["Rule","Bad","Better"],
        [["Define the issue (who, what, when, where, why, way)","Which brand of shampoo do you use?","Which brand(s) of shampoo have you personally used at home in the last month?"],
         ["Use ordinary words","Is distribution adequate?","Can you find the product easily in shops?"],
         ["Use unambiguous words","Do you shop often?","How many times did you shop in the last 4 weeks?"],
         ["Avoid leading questions","Do you agree that patriotic Indians should buy Indian cars?","Which car brand would you buy?"],
         ["Avoid implicit alternatives","Do you like to fly when travelling short distances?","Do you like to fly or drive on short trips?"],
         ["Avoid implicit assumptions","Are you for a balanced budget?","…if it means higher taxes?"],
         ["Avoid generalisations and estimates","What is your annual household spending on groceries?","How much do you spend on groceries in a week?"],
         ["No double-barrelled questions","Is the food tasty and cheap?","Two separate questions"],
         ["Use positive and negative statements","All items worded positively","Mix to reduce acquiescence bias"]]))
    sub("Order, layout and pretesting", 5,
      T(["Order rule","Reason"],
        [["Opening questions simple and interesting","Build trust and interest"],["Qualifying (screening) questions first","Check the respondent belongs to the target"],
         ["Basic information → classification → identification","Most important data first; personal details (income, name) last"],
         ["Difficult or sensitive questions later","Rapport first"],["<b>Funnel approach</b>: general → specific","Avoids earlier questions biasing later ones"],
         ["Logical order; branching (skip) questions","Clear flow; route people correctly"]]) +
      K("Layout: divide into parts, number questions, pre-code answers, keep it uncluttered; booklet form, clear instructions",
        "<b>Pretest</b> on 15–30 people like the target respondents, with the same interview method; revise and pretest again",
        "Checklist of errors: leading, double-barrelled, ambiguous, too long, missing options, sensitive questions too early"))
