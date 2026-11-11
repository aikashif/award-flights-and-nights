from summary_lib import *
from helpers import P

def add(chap, sub):
    chap(9, "Chi-Square (χ²) Tests — Dr Krishan Pandey", "—", 5)
    sub("What chi-square is for", 5,
      P("<b>In plain words:</b> chi-square works with <b>counts</b> in categories (how many chose red, blue…). "
        "It asks: are the counts we <b>observed</b> close to the counts we would <b>expect</b> if nothing special were going on?") +
      T(["Question","Test"],
        [["Are all package designs / brands equally preferred? (one variable)","<b>Goodness of fit</b>"],
         ["Is income linked to brand chosen? Family size to washing-machine size? Education to job type? (two variables)","<b>Test of independence</b> (contingency table)"]]) +
      K("Variables are <b>nominal</b> (categorical / attribute data)",
        "χ² is <b>non-parametric</b> (distribution-free): no assumption about the population's shape — unlike parametric tests (z, t, F) that assume e.g. normality",
        "χ² distribution is skewed for small df and approaches normal as df grows",
        "Notes: χ² is a sum of squared standard normal (z) values"))
    sub("Formula & degrees of freedom", 5,
      F("χ² = Σ (O − E)² / E        O = observed frequency, E = expected frequency\nGoodness of fit: df = number of categories − 1\nIndependence: df = (rows − 1) × (columns − 1)\nExpected cell (independence) = (Row total × Column total) / Grand total\nReject H₀ if χ² calculated &gt; χ² critical") +
      TRAP("Keep expected frequencies with decimals — do not round them (Krishan's notes)."))
    sub("Goodness of fit (worked: package colours)", 5,
      T(["Colour","O","E","(O − E)²","(O − E)²/E"],
        [["Red","70","80","100","1.250"],["Blue","106","80","676","8.450"],["Green","80","80","0","0.000"],["Pink","70","80","100","1.250"],["Orange","74","80","36","0.450"],["<b>Total</b>","400","400","","<b>11.400</b>"]]) +
      F("H₀: all colours equally preferred → E = 400/5 = 80 each\nχ² = 11.40 ; df = 5 − 1 = 4 ; critical at 5% = 9.488\n11.40 &gt; 9.488 → <b>reject H₀</b>: colours not equally preferred; Blue is most preferred → launch blue packaging"))
    sub("Test of independence (worked: income vs detergent brand)", 5,
      T(["Income","Brand 1","Brand 2","Brand 3","Brand 4","Total"],
        [["Lower","25","15","55","65","160"],["Middle","30","25","35","30","120"],["Upper middle","50","55","20","22","147"],["Upper","60","80","15","18","173"],["<b>Total</b>","165","175","125","135","600"]]) +
      F("Brands 1, 2 = premium; 3, 4 = economy; stratified random sample of 600\nH₀: income and brand preference are independent (no association); α = 5%\nExpected (Lower, Brand 1) = 160 × 165 / 600 = 44.0 ; (Upper, Brand 2) = 173 × 175 / 600 = 50.458\nSum of 16 cells of (O − E)²/E = <b>131.76</b>\ndf = (4 − 1)(4 − 1) = 9 ; critical at 5% = 16.92\n131.76 &gt; 16.92 → <b>reject H₀</b>: brand choice depends on income") +
      T(["Biggest contributions (O − E)²/E","Value"],[["Lower × Brand 4","23.36"],["Lower × Brand 2","21.49"],["Upper × Brand 2","17.30"],["Lower × Brand 3","14.08"]]) +
      K("Conclusion: upper-middle and upper incomes prefer premium brands; lower and middle prefer economy brands → position each accordingly"))
