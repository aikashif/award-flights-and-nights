"""Shared quiz builder: question helpers + HTML assembly for NISM V-D quizzes."""
import json, random, pathlib

def make_bank():
    bank = []
    def Q(ch, lvl, q, right, why, *wrongs):
        """lvl: 'S' = exam level, 'H' = harder. wrongs: 3 × (text, why-this-is-wrong)."""
        assert len(wrongs) == 3, q
        bank.append({"ch": ch, "lvl": lvl, "q": q, "right": right, "why": why, "wrongs": list(wrongs)})
    return bank, Q

def inr(x, d=0):
    neg = x < 0; x = abs(x)
    whole, _, frac = f"{x:.{d}f}".partition(".")
    if len(whole) > 3:
        head, tail = whole[:-3], whole[-3:]; parts = []
        while len(head) > 2: parts.insert(0, head[-2:]); head = head[:-2]
        if head: parts.insert(0, head)
        whole = ",".join(parts + [tail])
    return ("−" if neg else "") + "₹" + whole + ("." + frac if frac else "")

def num(x, d=2):
    return f"{x:,.{d}f}"

def build(bank, order, names, marks, *, title, eyebrow, sub, storage_key, out_name, seed=42):
    rng = random.Random(seed)
    out = {"storageKey": storage_key, "chapters": [], "questions": []}
    for ch in order:
        s = [q for q in bank if q["ch"] == ch and q["lvl"] == "S"]
        h = [q for q in bank if q["ch"] == ch and q["lvl"] == "H"]
        rng.shuffle(s); rng.shuffle(h)
        seq = []
        while s or h:
            seq += [s.pop() for _ in range(min(3, len(s)))]
            seq += [h.pop() for _ in range(min(2, len(h)))]
        for i, q in enumerate(seq, 1):
            opts = [(q["right"], None)] + q["wrongs"]
            texts = [o[0] for o in opts]
            assert len(set(texts)) == 4, (q["q"], texts)
            idx = list(range(4)); rng.shuffle(idx)
            out["questions"].append({"id": f"c{ch}-{i:03d}", "ch": ch, "lvl": q["lvl"], "q": q["q"],
                "o": [opts[j][0] for j in idx], "a": idx.index(0), "why": q["why"], "x": [opts[j][1] for j in idx]})
        out["chapters"].append({"ch": ch, "name": names[ch], "marks": marks[ch], "n": len(seq),
            "s": sum(1 for q in seq if q["lvl"] == "S"), "h": sum(1 for q in seq if q["lvl"] == "H")})
    here = pathlib.Path(__file__).parent
    tpl = (here / "quiz.template.html").read_text()
    html = (tpl.replace("__TITLE__", title).replace("__EYEBROW__", eyebrow).replace("__SUB__", sub)
               .replace("/*__BANK__*/null", json.dumps(out, ensure_ascii=False, separators=(",", ":"))))
    (here / out_name).write_text(html)
    for c in out["chapters"]: print(c)
    print("total", len(out["questions"]))
    return out
