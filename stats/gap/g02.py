from summary_lib import *
from helpers import P

def add(chap, sub):
    chap(2, "Research Design & Types of Research", "Module 1 · Class 2", 5)
    sub("What a research design is", 5,
      P("<b>In plain words:</b> a research design is the blueprint for the study — what data, from whom, how, when, and how it will be analysed. Your notes list designs; here are the types you are examined on.") +
      K("Parts: information needed · exploratory, descriptive or causal phase · measurement and scaling · questionnaire · sampling and sample size · data analysis plan",
        "Good design = answers the research questions with the least error at an acceptable cost"))
    sub("Types of research (classifications)", 5,
      T(["Basis","Types","Meaning"],
        [["Purpose","Basic (pure / fundamental)","Builds general knowledge and theory"],["","Applied","Solves a specific practical problem"],
         ["Method","Descriptive","Describes the state of affairs as it is (no control of variables)"],["","Analytical","Uses existing facts to critically evaluate"],
         ["Data","Quantitative","Numbers, measurement, statistics"],["","Qualitative","Words, meanings, motives"],
         ["Basis of knowledge","Conceptual","Abstract ideas and theory"],["","Empirical","Observation and experiment; tests hypotheses with data"],
         ["Time","Cross-sectional","Data at one point in time"],["","Longitudinal","Same units measured repeatedly over time"]]))
    sub("Exploratory, descriptive and causal (conclusive) research", 5,
      T(["","Exploratory","Descriptive","Causal"],
        [["Objective","Gain ideas and insights; define the problem","Describe market traits or functions","Find cause-and-effect"],
         ["Characteristics","Flexible, unstructured","Pre-planned, structured; clear hypotheses","Manipulate one or more independent variables; control others"],
         ["Sample","Small, non-representative","Large, representative","Matched groups"],
         ["Methods","Expert surveys, pilot studies, secondary data, qualitative research (focus groups, depth interviews)","Surveys, panels, observation, secondary data","Experiments"],
         ["Findings","Tentative — followed by more research","Conclusive","Conclusive"]]) +
      K("Descriptive and causal research together = <b>conclusive</b> research",
        "Saunders also uses <b>explanatory</b> research = studies a situation to explain links between variables (similar to causal)",
        "Descriptive answers the <b>6 Ws</b>: who, what, when, where, why, way") +
      TRAP("Exploratory findings are <b>not</b> used directly for decisions — they generate hypotheses."))
    sub("Descriptive designs: cross-sectional vs longitudinal", 5,
      T(["Design","How","Strength","Weakness"],
        [["Single cross-sectional","One sample, measured once","Representative snapshot","No change over time"],
         ["Multiple cross-sectional","Two or more samples, each measured once (cohort analysis)","Compare groups / generations","Different people each time"],
         ["Longitudinal (panel)","Same sample measured repeatedly","Shows change in the same units","Panel attrition, panel conditioning, costly"]]) +
      K("<b>Cohort analysis</b>: follow groups born in the same period across surveys (e.g. soft-drink use by age group over decades)"))
    sub("Causal research: experiments, variables and validity", 5,
      P("<b>In plain words:</b> to prove X causes Y, change X yourself, keep other things fixed, and see if Y changes.") +
      T(["Condition for causality","Meaning"],
        [["Concomitant variation","X and Y move together as the hypothesis predicts"],["Time order","X happens before (or at the same time as) Y"],
         ["Elimination of other causes","No other factor explains the change"]]) +
      T(["Term","Meaning"],
        [["Independent variable (treatment)","The variable you change (price, ad)"],["Dependent variable","The outcome you measure (sales)"],
         ["Extraneous variable","Other factors that can affect the outcome"],["Test units","People, stores or firms that receive treatments"],
         ["Internal validity","Did the treatment really cause the effect?"],["External validity","Can results be generalised beyond the experiment?"]]) +
      T(["Threat to internal validity","Meaning"],
        [["History","Outside events during the experiment"],["Maturation","Test units change with time (tired, older)"],
         ["Testing (main / interactive)","Earlier measurement affects later answers"],["Instrumentation","Measuring tool or observers change"],
         ["Statistical regression","Extreme scorers move toward the mean"],["Selection bias","Groups differ at the start"],
         ["Mortality","Test units drop out"]]) +
      K("Control by: <b>randomisation</b>, <b>matching</b>, statistical control (ANCOVA), design control"))
    sub("Experimental designs", 4,
      F("Notation: X = treatment, O = observation (measurement), R = random assignment, EG = experimental group, CG = control group") +
      T(["Type","Design","Symbol"],
        [["Pre-experimental (no randomisation)","One-shot case study","X O₁"],["","One-group pretest–posttest","O₁ X O₂"],["","Static group","EG: X O₁ / CG: O₂"],
         ["True experimental (randomised)","Pretest–posttest control group","EG: R O₁ X O₂ / CG: R O₃ O₄ → effect = (O₂ − O₁) − (O₄ − O₃)"],
         ["","Posttest-only control group","EG: R X O₁ / CG: R O₂ → effect = O₁ − O₂"],
         ["","Solomon four-group","Adds two posttest-only groups to measure testing effects"],
         ["Quasi-experimental","Time series","O₁ O₂ O₃ X O₄ O₅ O₆"],["","Multiple time series","Time series plus a control group"],
         ["Statistical","Randomised block","Block on one extraneous variable (e.g. store size)"],["","Latin square","Control two extraneous variables"],
         ["","Factorial","Two or more treatments and their interaction (link to two-way ANOVA)"]]) +
      K("Lab experiment: high internal validity · Field experiment (real setting): high external validity",
        "<b>Test marketing</b> = a field experiment for a new product"))
    sub("Saunders' research onion", 4,
      T(["Layer (outside → in)","Choices"],
        [["Philosophy","Positivism, critical realism, interpretivism, postmodernism, pragmatism"],
         ["Approach to theory","Deductive, inductive, abductive"],
         ["Methodological choice","Mono method (quantitative or qualitative), multi-method, mixed methods"],
         ["Strategy","Experiment, survey, archival, case study, ethnography, action research, grounded theory, narrative inquiry"],
         ["Time horizon","Cross-sectional, longitudinal"],
         ["Techniques and procedures","Data collection and analysis"]]))
