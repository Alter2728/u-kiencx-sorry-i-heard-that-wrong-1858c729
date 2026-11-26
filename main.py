"""Draft flaw: the first line apologized without naming what was misheard.
Revision fix: the final line names the two confused phrases and lands on the chandelier's leg day."""

import os

TEXT = "Sorry — you said 'dim the lights,' I heard 'gym the lights,' so the chandelier is doing lunges and refuses to skip leg day."

assert TEXT == TEXT.strip()
assert "\n" not in TEXT
assert 1 <= len(TEXT) <= 140

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)
