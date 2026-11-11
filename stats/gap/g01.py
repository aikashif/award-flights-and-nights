from summary_lib import *
from helpers import P

def add(chap, sub):
    chap(1, "Introduction to Research & Problem Formulation", "Module 1 · Class 1", 4)
    sub("What research is", 4,
      P("<b>In plain words:</b> research is a careful, organised search for an answer to a question. Business research collects and analyses information so that managers can make better decisions.") +
      T(["Feature of good research","Meaning"],
        [["Systematic","Follows clear, planned steps"],["Logical","Reasoning (induction/deduction) links evidence to conclusions"],
         ["Empirical","Based on real data you observe or measure"],["Replicable","Others can repeat it and check the result"],
         ["Objective","Free from the researcher's personal bias"],["Purpose-driven","Clear objective; limits stated honestly"]]) +
      T(["Kind of reasoning","How it works","Example"],
        [["Deductive","Theory → hypothesis → data → accept/reject","Theory says price cuts raise sales → test in stores"],
         ["Inductive","Data → patterns → theory","Interviews show customers value delivery speed → new theory"],
         ["Abductive","Move back and forth between data and theory","Surprising result → best explanation → test again"]]))
    sub("The research process (step by step)", 5,
      P("<b>In plain words:</b> every study follows the same order — define the problem, plan, collect data, analyse, report. A mistake early (wrong problem) spoils everything later.") +
      T(["Kothari (11 steps)","Malhotra (6 steps)"],
        [["1. Formulate the research problem","1. Define the problem"],
         ["2. Extensive literature survey","2. Develop an approach (theory, models, research questions, hypotheses)"],
         ["3. Develop working hypotheses",""],
         ["4. Prepare the research design","3. Formulate the research design"],
         ["5. Determine the sample design",""],
         ["6. Collect the data","4. Fieldwork / data collection"],
         ["7. Execute the project",""],
         ["8. Analyse the data","5. Data preparation and analysis"],
         ["9. Test hypotheses",""],
         ["10. Generalise and interpret",""],
         ["11. Prepare the report","6. Report preparation and presentation"]]) +
      K("The process is not strictly linear — results can send you back to an earlier step",
        "Literature review: find what is already known, the gaps, and theories and measures you can reuse"))
    sub("Problem formulation: management problem vs research problem", 5,
      P("<b>In plain words:</b> the manager asks 'what should I <b>do</b>?' The researcher turns it into 'what do I need to <b>know</b>?' Getting this translation right is the most important step.") +
      T(["Management decision problem","Research problem"],
        [["Asks what the decision maker must do","Asks what information is needed and how to get it"],
         ["Action-oriented","Information-oriented"],["Focus on symptoms","Focus on underlying causes"],
         ["Should a new product be launched?","Find consumer preferences and purchase intention for the new product"],
         ["Should the advertising campaign be changed?","Measure how effective the current campaign is"],
         ["Should the price be raised?","Estimate price elasticity of demand and the effect of price changes on sales and profit"]]) +
      K("Symptom vs problem: falling sales is a <b>symptom</b>; the problem may be a new competitor, poor service or wrong price"))
    sub("How to define the problem", 5,
      T(["Task","Purpose"],
        [["Discussion with decision makers","Learn the objectives, history, alternatives and what decision the research must support (problem audit)"],
         ["Interviews with industry experts","Expert knowledge, quick and cheap"],
         ["Secondary data analysis","Facts already published — check before collecting new data"],
         ["Qualitative research","Small exploratory studies (focus groups, depth interviews) to understand the issue"]]) +
      T(["Environmental context to study","Examples"],
        [["Past information and forecasts","Sales, market share, industry trends"],["Resources and constraints","Budget, time, skills"],
         ["Objectives","Of the organisation and the decision maker"],["Buyer behaviour","Who buys, why, how"],
         ["Legal, economic environment","Regulation, income, interest rates"],["Marketing and technology skills","What the firm can actually do"]]) +
      F("Problem statement = broad statement (general problem) + specific components (exact questions)\nBroad: 'Improve the store's image'\nComponents: 1. What criteria do shoppers use to choose a store?\n2. How do shoppers rate our store and competitors on these criteria?\n3. Which customer groups visit us?") +
      TRAP("Common errors: problem too <b>broad</b> (no clear guide) or too <b>narrow</b> (misses options). Use a broad statement plus specific components."))
    sub("Developing the approach: research questions & hypotheses", 5,
      T(["Component","Meaning"],
        [["Objective / theoretical framework","Theory from the literature that guides what to measure"],
         ["Analytical model","Variables and their links: verbal, graphical (diagram) or mathematical (equation)"],
         ["Research questions (RQs)","Refined questions about the specific components"],
         ["Hypotheses (H)","Testable, unproven statements that answer an RQ"],
         ["Information needed","Exact list of data required"]]) +
      F("RQ: Do loyal customers of the store differ in income from non-loyal customers?\nH₁: Loyal customers have higher average income than non-loyal customers\nH₀: There is no difference in average income") +
      T(["A good research problem / hypothesis is…","…because"],
        [["Clear and specific","Everyone understands it the same way"],["Testable / researchable","Data can answer it"],
         ["Relevant and significant","Supports a real decision"],["Feasible","Time, money, data and skills exist"],
         ["Ethical","No harm to participants"]]))
