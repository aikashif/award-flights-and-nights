from summary_lib import *
from helpers import P

def add(chap, sub):
    chap(11, "Statistical Process Control (control charts)", "—", 3)
    sub("In control vs out of control", 4,
      P("<b>In plain words:</b> a factory process always varies a little by chance (<b>random variation</b>). If something specific goes wrong (a machine slips), that is an <b>assignable cause</b> — it can be found and fixed. "
        "A process with only random variation is <b>in control</b>.") +
      K("Out of control → reduce variation and bring the measurements back within limits"))
    sub("x̄ chart (for process means)", 4,
      F("Take k samples of size n; x̿ = grand mean of all nk values; s = SD of all nk values\nCentreline = x̿\nLCL = x̿ − 3s/√n        UCL = x̿ + 3s/√n\nA sample mean outside the limits → process may be out of control") +
      K("Based on the CLT: almost all x̄ fall within μ ± 3σ/√n"))
    sub("p chart (for proportion defective)", 4,
      F("p̄ = Σp̂ᵢ / k   (average of the k sample proportions)\nCentreline = p̄\nLCL = p̄ − 3√(p̄(1 − p̄)/n)        UCL = p̄ + 3√(p̄(1 − p̄)/n)\nA sample proportion outside the limits → process may be out of control"))
