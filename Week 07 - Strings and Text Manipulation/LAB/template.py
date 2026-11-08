"""
RECORD CHECK  -  my version
===========================

Name  :Asli
Lane  : Cyber 
Date  :26/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

def parse_line(raw_line):
    """Clean a record and convert attempts to an integer."""
    fields = raw_line.strip().lower().split(",")
    record = {}

    for field in fields:
        key, value = field.split("=", 1)
        record[key.strip()] = value.strip()

    record["attempts"] = int(record["attempts"])
    return record


def status_of(record):
    """Flag failed results with at least 10 attempts."""
    if record["result"] == "failed" and record["attempts"] >= 10:
        return "FLAGGED"
    return "OK"


# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

from pathlib import Path

with open(Path(__file__).with_name("records.txt"), encoding="utf-8") as file:
    raw_records = [line for line in file if line.strip()]

# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.

flagged_count = 0

for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record)
    print(record, "-", status)

    if status == "FLAGGED":
        flagged_count += 1

print(f"Summary: {len(raw_records)} records, {flagged_count} flagged.")


# ==========================================================================
# 4. Before you finish:
#
#   [ X ] Run it against at least 5 genuinely messy raw records
#    [ X ] Run it with a value that will not convert to a number - write the
#        error down
#    [X ] Check every function does one job, with a docstring
# Error test: changed ATTEMPTS=12 to ATTEMPTS=twelve.
# ValueError: invalid literal for int() with base 10: 'twelve'
# int() cannot convert the word "twelve" into an integer.
# Changed it back to 12 and ran successfully.