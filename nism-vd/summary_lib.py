"""Shared helpers + renderer for the NISM V-D summary PDFs."""
import pathlib, subprocess

def T(head, rows, cls=""):
    h = "".join(f"<th>{c}</th>" for c in head)
    b = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="{cls}"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>'
def KV(rows):
    return '<table class="kv"><tbody>' + "".join(f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in rows) + "</tbody></table>"
def K(*w):
    return '<div class="kw">' + "".join(f"<span>{x}</span>" for x in w) + "</div>"
def F(t):
    return f'<pre class="f">{t}</pre>'
def TRAP(t):
    return f'<div class="trap"><b>Trap</b> {t}</div>'
def L(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
V = '<span class="v">‡</span>'


def payoff(title, pts, note=""):
    """Small payoff SVG. pts: 'x,y x,y' in a 120x70 box; y=35 is zero P&L."""
    return (f'<figure class="po"><figcaption>{title}</figcaption><svg viewBox="0 0 120 70">'
            f'<line x1="2" y1="35" x2="118" y2="35" stroke="#8a96a3" stroke-width=".8" stroke-dasharray="2 2"/>'
            f'<polyline points="{pts}" fill="none" stroke="#b86e00" stroke-width="2.4"/>'
            f'<text x="98" y="44" font-size="7" fill="#8a96a3">spot</text></svg><small>{note}</small></figure>')
def PO(*figs):
    return '<div class="pos">' + "".join(figs) + "</div>"

def render(CH, eyebrow, title, lead, foot, html_name, pdf_name, footer_label):
    def stars(n):
        return f'<span class="st s{n}">' + "★"*n + '<i>' + "★"*(5-n) + '</i></span>'

    total_subs = sum(len(c["subs"]) for c in CH)
    five = [(c["n"], s["t"]) for c in CH for s in c["subs"] if s["s"] == 5]
    four = [(c["n"], s["t"]) for c in CH for s in c["subs"] if s["s"] == 4]

    idx_rows = "".join(
        f'<tr><td>{c["n"]}</td><td>{c["title"]}</td><td class="n">{c["marks"]}</td><td>{stars(c["stars"])}</td>'
        f'<td class="n">{len(c["subs"])}</td><td class="n">{sum(1 for s in c["subs"] if s["s"]==5)}</td></tr>' for c in CH)

    def fivelist(items):
        out = {}
        for n, t in items: out.setdefault(n, []).append(t)
        return "".join(f'<p><b>Ch {n}</b> · ' + " · ".join(v) + "</p>" for n, v in out.items())

    body = []
    for c in CH:
        subs = "".join(
            f'<div class="sub-t"><div class="sh"><h3>{s["t"]}</h3>{stars(s["s"])}</div>{s["b"]}</div>' for s in c["subs"])
        body.append(f'''<section class="ch"><div class="chh"><span class="cn">{(format(c["n"], "02d") if isinstance(c["n"], int) else c["n"])}</span><div><h2>{c["title"]}</h2>
          <p class="meta">≈{c["marks"]} marks · {len(c["subs"])} subtopics · chapter priority {stars(c["stars"])}</p></div></div><div class="body2">{subs}</div></section>''')

    HTML = f'''<!doctype html><html><head><meta charset="utf-8"><title>{title}</title>
    <style>
    @page {{ size: A4; margin: 11mm 10mm 12mm 10mm; }}
    :root {{ --ink:#14202b; --muted:#56636f; --line:#cfd7df; --teal:#0d6a73; --teal-soft:#e2f1f2; --amber:#b86e00; --amber-soft:#fbefd9; --red:#b3261e; --red-soft:#fbe7e5; }}
    * {{ box-sizing:border-box; }}
    body {{ font-family: Carlito, "Liberation Sans", "DejaVu Sans", sans-serif; color:var(--ink); font-size:8.6pt; line-height:1.28; margin:0; background:#fff; }}
    h1,h2,h3 {{ font-family: "Inter Display", Inter, Carlito, sans-serif; margin:0; line-height:1.12; }}
    h1 {{ font-size:22pt; letter-spacing:-.01em; }}
    h2 {{ font-size:13.5pt; }}
    h3 {{ font-size:9.3pt; font-weight:700; }}
    .cover {{ border-bottom:2.5pt solid var(--ink); padding-bottom:6pt; margin-bottom:8pt; }}
    .cover .eyebrow {{ font:600 7.4pt Inter, sans-serif; letter-spacing:.08em; text-transform:uppercase; color:var(--muted); }}
    .lead {{ color:var(--muted); margin:4pt 0 0; font-size:9pt; }}
    .legend {{ display:flex; gap:14pt; flex-wrap:wrap; margin:6pt 0; font-size:8.2pt; }}
    .st {{ font-family:"DejaVu Sans", sans-serif; color:var(--amber); letter-spacing:.5pt; font-size:8pt; white-space:nowrap; }}
    .st i {{ color:#d9dde1; font-style:normal; }}
    .st.s5 {{ color:var(--red); }}
    table {{ border-collapse:collapse; width:100%; margin:3pt 0; page-break-inside:auto; }}
    tr {{ page-break-inside:avoid; }}
    th,td {{ border:.5pt solid var(--line); padding:2pt 4pt; vertical-align:top; text-align:left; }}
    thead th {{ background:var(--teal-soft); font-weight:700; }}
    .kv th {{ width:28%; background:#f4f6f8; font-weight:700; }}
    td.n {{ text-align:right; font-variant-numeric:tabular-nums; white-space:nowrap; }}
    .kw {{ display:flex; flex-wrap:wrap; gap:2.5pt; margin:3pt 0; }}
    .kw span {{ border:.5pt solid var(--line); border-radius:6pt; padding:0 5pt; background:#fafbfc; font-size:8pt; }}
    pre.f {{ font-family:"JetBrains Mono", "DejaVu Sans Mono", monospace; font-size:7.3pt; background:#f4f6f8; border-left:2pt solid var(--teal); padding:4pt 6pt; margin:3pt 0; white-space:pre-wrap; }}
    .trap {{ background:var(--red-soft); border-left:2pt solid var(--red); padding:2.5pt 6pt; margin:3pt 0; font-size:8.2pt; }}
    .trap b {{ color:var(--red); margin-right:4pt; text-transform:uppercase; font-size:7.2pt; letter-spacing:.05em; }}
    .v {{ color:var(--red); font-weight:700; }}
    ul {{ margin:2pt 0; padding-left:12pt; }} li {{ margin:0; }}
    p {{ margin:2pt 0; }} .sub {{ color:var(--muted); }}
    .ch {{ margin-top:8pt; }}
    .body2 {{ columns:2; column-gap:9pt; column-fill:balance; }}
    .chh {{ break-after:avoid; break-inside:avoid; display:flex; gap:8pt; align-items:center; border-bottom:1.5pt solid var(--ink); padding-bottom:4pt; margin-bottom:5pt; }}
    .cn {{ font:800 22pt "Inter Display", Inter, sans-serif; color:var(--teal); line-height:1; }}
    .meta {{ color:var(--muted); font-size:8pt; margin:1pt 0 0; }}
    .sub-t {{ margin:0 0 5pt; break-inside:avoid; }}
    .sh {{ display:flex; justify-content:space-between; align-items:baseline; gap:6pt; border-bottom:.5pt dotted var(--line); margin-bottom:2pt; padding-bottom:1pt; }}
    .prio {{ background:var(--amber-soft); padding:5pt 7pt; margin:5pt 0; }}
    .prio p {{ margin:1.5pt 0; }}
    .cols {{ columns:2; column-gap:10pt; }}
    .pos {{ display:grid; grid-template-columns:repeat(3,1fr); gap:3pt; margin:3pt 0; }}
.po {{ margin:0; border:.5pt solid var(--line); padding:2pt 3pt; break-inside:avoid; }}
.po figcaption {{ font-weight:700; font-size:7.6pt; }}
.po small {{ display:block; font-size:7pt; color:var(--muted); }}
.foot {{ color:var(--muted); font-size:7.4pt; margin-top:6pt; }}
    </style></head><body>
    <div class="cover">
      <p class="eyebrow">{eyebrow}</p>
      <h1>{title}</h1>
      <p class="lead">{lead.format(n=total_subs)}</p>
      <div class="legend"><span>{stars(5)} must know, asked often</span><span>{stars(4)} high</span><span>{stars(3)} medium</span><span>{stars(2)} low</span><span>{stars(1)} skim</span><span><span class="v">‡</span> rule or number that changes often; check workbook edition</span></div>
    </div>
    <table><thead><tr><th>Ch</th><th>Chapter</th><th>Marks</th><th>Priority</th><th>Subtopics</th><th>5★</th></tr></thead><tbody>{idx_rows}</tbody></table>
    <div class="prio"><h3>5★ list ({len(five)}) — read these first</h3>{fivelist(five)}</div>
    <div class="prio" style="background:#f4f6f8"><h3>4★ list ({len(four)})</h3>{fivelist(four)}</div>
    <p class="foot">{foot}</p>
    {"".join(body)}
    </body></html>'''

    here = pathlib.Path(__file__).parent
    (here / html_name).write_text(HTML)
    js = f'''const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage();
    await p.goto('file://{(here / html_name).resolve()}');await p.pdf({{path:'{(here / pdf_name).resolve()}',format:'A4',printBackground:true,
    displayHeaderFooter:true,headerTemplate:'<span></span>',footerTemplate:'<div style="font-size:7px;width:100%;text-align:center;color:#777;font-family:Carlito">{footer_label} · <span class="pageNumber"></span>/<span class="totalPages"></span></div>',
    margin:{{top:'11mm',bottom:'13mm',left:'10mm',right:'10mm'}}}});await b.close();}})();'''
    subprocess.run(["node", "-e", js], check=True)
    print("subtopics", total_subs, "5-star", len(five), "4-star", len(four))
