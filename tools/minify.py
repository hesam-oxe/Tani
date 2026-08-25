#!/usr/bin/env python3
"""Dependency-free CSS minifier for Tani.

String-aware and deliberately conservative:
  * strips /* */ comments and collapses whitespace outside strings
  * removes spaces around { } ; , > ~  (safe in any CSS)
  * does NOT touch '+' or ':' regions  -> calc(100% + 6px) and :hover stay intact
Usage: python3 tools/minify.py <in.css> <out.css>
"""
import sys

def minify(css: str) -> str:
    out = []
    i, n = 0, len(css)
    in_str = None              # '"' or "'" while inside a string
    # pass 1: strip comments, keep strings verbatim
    src = []
    while i < n:
        c = css[i]
        if in_str:
            src.append(c)
            if c == "\\" and i + 1 < n:          # escaped char inside string
                src.append(css[i + 1]); i += 2; continue
            if c == in_str:
                in_str = None
            i += 1; continue
        if c in "\"'":
            in_str = c; src.append(c); i += 1; continue
        if c == "/" and i + 1 < n and css[i + 1] == "*":
            j = css.find("*/", i + 2)
            i = n if j == -1 else j + 2
            src.append(" ")                      # comment becomes a separator
            continue
        src.append(c); i += 1
    data = "".join(src)

    # pass 2: collapse whitespace, then drop safe-adjacent spaces
    res = []
    in_str = None
    k = 0
    m = len(data)
    def prev_sig(buf):
        return buf[-1] if buf else ""
    while k < m:
        c = data[k]
        if in_str:
            res.append(c)
            if c == "\\" and k + 1 < m:
                res.append(data[k + 1]); k += 2; continue
            if c == in_str:
                in_str = None
            k += 1; continue
        if c in "\"'":
            in_str = c; res.append(c); k += 1; continue
        if c.isspace():
            # find next significant char
            nxt = ""
            p = k + 1
            while p < m and data[p].isspace():
                p += 1
            if p < m:
                nxt = data[p]
            last = prev_sig(res)
            SAFE = "{};,>~"
            if last in SAFE or nxt in SAFE or nxt == "":
                pass                              # drop the space entirely
            else:
                res.append(" ")
            k = p
            continue
        res.append(c); k += 1

    out_css = "".join(res)
    # final tidy-ups (safe globally: no strings involved in these pairs)
    out_css = out_css.replace(";}", "}").replace("{ ", "{").replace(" }", "}")
    return out_css.strip() + "\n"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__); sys.exit(2)
    css = open(sys.argv[1], encoding="utf-8").read()
    mini = minify(css)
    open(sys.argv[2], "w", encoding="utf-8").write(mini)
    print(f"{sys.argv[1]}: {len(css)} -> {len(mini)} bytes")
