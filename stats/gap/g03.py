from summary_lib import *
from helpers import P

def add(chap, sub):
    chap(3, "Methods of Data Collection: Primary & Secondary Data", "Module 2 · Classes 3–4", 5)
    sub("Primary vs secondary data", 5,
      P("<b>In plain words:</b> <b>primary</b> data you collect yourself for this study. <b>Secondary</b> data someone already collected for another purpose. Always check secondary data first — it is quicker and cheaper.") +
      T(["","Primary data","Secondary data"],
        [["Collected for","The problem at hand","Other purposes"],["Process","Very involved","Rapid and easy"],
         ["Cost","High","Relatively low"],["Time","Long","Short"],["Fit to problem","Exact","May not fit (units, dates, definitions)"],
         ["Control over quality","Full","None"]]))
    sub("Sources and evaluation of secondary data", 5,
      T(["Source","Examples"],
        [["Internal","Sales records, invoices, customer databases, accounting data, CRM, loyalty cards"],
         ["External: published","Government (Census, RBI, NSSO/MoSPI), industry reports, journals, books, newspapers"],
         ["External: computerised databases","Online, offline, bibliographic, numeric, full-text, directory"],
         ["External: syndicated services","Paid data sold to many clients: consumer panels, retail audits (Nielsen), media audience data"]]) +
      T(["Criterion to judge secondary data","Question to ask"],
        [["Specifications / methodology","How was it collected — sample, response rate, fieldwork?"],["Error / accuracy","Is it accurate? Compare sources"],
         ["Currency","When was it collected? Is it out of date?"],["Objective","Why was it collected? (bias risk)"],
         ["Nature","Definitions, units, categories — do they fit?"],["Dependability","Is the source expert, credible, reputable?"]]) +
      TRAP("Secondary data is a starting point, rarely a complete answer — definitions and dates often do not match your problem."))
    sub("Qualitative primary methods", 4,
      T(["Method","How","Use / limits"],
        [["Focus group","8–12 people, a moderator, 1–2 hours","Ideas, reactions, new concepts; not representative"],
         ["Depth interview","One-to-one, unstructured, 30 min–1 hr+","Sensitive topics, experts; costly, depends on interviewer"],
         ["Projective techniques","Indirect tasks that reveal hidden motives","Word association, sentence completion, picture response (TAT), cartoon tests, role playing, third-person technique"]]) +
      K("Direct approach (purpose clear: focus groups, depth interviews) vs indirect (purpose disguised: projective techniques)"))
    sub("Survey methods", 5,
      P("<b>In plain words:</b> a survey asks many respondents structured questions. The mode (how you ask) affects cost, speed, response rate and quality.") +
      T(["Mode","Strengths","Weaknesses"],
        [["Personal (in-home, mall intercept, CAPI)","Complex questions, visual aids, high response","Costly, interviewer bias"],
         ["Telephone (CATI)","Fast, wide reach, supervision","Short only, no visuals, low response now"],
         ["Mail","Cheap, no interviewer bias, anonymous","Low response, slow, no control over who answers"],
         ["Electronic (email, web, mobile)","Very cheap, fast, multimedia, automatic data entry","Sample may not represent population; low response; security"]]) +
      T(["Kothari: questionnaire vs schedule","Questionnaire","Schedule"],
        [["Who fills it","Respondent (by post/online)","Enumerator, face to face"],["Cost","Cheap","Costly (field staff)"],
         ["Non-response","High","Low"],["Respondent identity","Not always known","Known"],["Needs literate respondents","Yes","No"]]))
    sub("Observation and experiments", 4,
      T(["Observation type","Meaning"],
        [["Structured vs unstructured","Pre-set checklist vs record everything relevant"],["Disguised vs undisguised","Respondents unaware vs aware"],
         ["Natural vs contrived","Real setting vs artificial setting"],["Personal","Human observer"],["Mechanical","Cameras, scanners, eye-tracking, people meters, web analytics"],
         ["Audit","Count stock / pantry items"],["Content analysis","Analyse communication content (ads, posts)"],["Trace analysis","Physical traces (waste, browser history)"]]) +
      K("Observation: records actual behaviour, no recall bias — but cannot see motives or attitudes",
        "Experiments: the only method that shows cause and effect (see Chapter 2)"))
    sub("Sampling: steps and sample size (supplement)", 4,
      P("Your notes cover sampling methods. These are the design steps around them.") +
      F("1. Define the target population (elements, units, extent, time)\n2. Determine the sampling frame (list of the population)\n3. Select the sampling technique (probability or non-probability)\n4. Determine the sample size\n5. Execute the sampling process") +
      K("Sample size depends on: importance of the decision, nature of research, number of variables, analysis planned, incidence and completion rates, resources",
        "Formulas for sample size are in Chapter 6 (estimation)",
        "Errors: <b>sampling error</b> (sample ≠ population) vs <b>non-sampling error</b> (wrong frame, non-response, measurement, data entry) — non-sampling errors are often larger"))
