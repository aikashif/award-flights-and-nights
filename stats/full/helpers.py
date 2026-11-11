"""Extra helpers for the statistics summary (plain-language paragraph + bell-curve figure)."""
import math
from summary_lib import PO

def P(t):
    return f'<p style="margin:2px 0 6px;line-height:1.45">{t}</p>'

def bell(title, shade="two", note="", z=1.96):
    """Standard normal curve in a 120x70 box; shade 'two', 'right', 'left' or 'none'."""
    xs = [i / 10 for i in range(-35, 36)]
    def pt(x):
        y = math.exp(-x * x / 2)
        return 60 + x * 15, 60 - y * 50
    curve = " ".join(f"{a:.1f},{b:.1f}" for a, b in map(pt, xs))
    def area(lo, hi):
        seg = [pt(lo + (hi - lo) * i / 20) for i in range(21)]
        pts = [(seg[0][0], 60)] + seg + [(seg[-1][0], 60)]
        return '<polygon points="' + " ".join(f"{a:.1f},{b:.1f}" for a, b in pts) + '" fill="#d9534f" opacity=".55"/>'
    sh = ""
    if shade in ("two", "right"): sh += area(z, 3.5)
    if shade == "two": sh += area(-3.5, -z)
    if shade == "left": sh += area(-3.5, -z)
    return (f'<figure class="po"><figcaption>{title}</figcaption><svg viewBox="0 0 120 70">'
            f'<line x1="2" y1="60" x2="118" y2="60" stroke="#8a96a3" stroke-width=".8"/>{sh}'
            f'<polyline points="{curve}" fill="none" stroke="#1f5fa8" stroke-width="2"/>'
            f'<line x1="60" y1="8" x2="60" y2="60" stroke="#8a96a3" stroke-width=".6" stroke-dasharray="2 2"/></svg><small>{note}</small></figure>')
