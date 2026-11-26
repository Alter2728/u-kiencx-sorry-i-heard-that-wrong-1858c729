"""Draft was a generic misheard song title with no consequence.
Revision makes the mishearing act on the owner's life and ends on the reply."""

import os

TEXT = "Sorry, I heard 'set a timer for the pasta' as 'text your ex about the pasta'. He replied."

assert TEXT == TEXT.strip()
assert "\n" not in TEXT and "\r" not in TEXT
assert 1 <= len(TEXT) <= 140

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)
