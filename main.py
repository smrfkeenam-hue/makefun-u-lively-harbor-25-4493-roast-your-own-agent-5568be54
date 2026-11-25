import os

ENTRY = "My agent calls tools like a toddler pressing elevator buttons \u2014 confident, busy, and going nowhere."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

with open(OUTPUT_DIR + "/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
