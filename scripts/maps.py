#!/usr/bin/env python3
"""
Replace maps
"""
from pathlib import Path
from re import MULTILINE, findall
from sys import argv

if __name__ == "__main__":
    print(argv[1])
    text = Path(argv[1]).read_text()

    maps = findall(r'"\[.+?\]"', text, flags=MULTILINE)

    for m in maps:
        intervals = [
            i.replace("[", "(")
            .replace("]", ")")
            .replace("  ", " ")
            .replace(" ", ", ")
            .replace("{", "")
            .replace("}", "")
            for i in findall(r"\[.+?\]", m)
        ]
        m_new = f"{intervals}".replace("'", "")

        text = text.replace(m, m_new).replace("f[", "[")

        Path(argv[1]).write_text(text)
