"""Draft mishears a shopping item but the ending has no consequence.
Revision keeps the list mix-up and ends on the recipe he sent back."""

import os

TEXT = "Sorry, I heard 'add pasta to the list' as 'ask your ex about the pasta'. He sent a recipe."

assert TEXT == TEXT.strip()
assert "\n" not in TEXT and "\r" not in TEXT
assert 1 <= len(TEXT) <= 140

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)
