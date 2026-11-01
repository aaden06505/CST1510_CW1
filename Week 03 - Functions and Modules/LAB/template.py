"""
RECORD CHECK  -  my version
===========================
Name  :Asli
Lane  :  Cyber 
Date  : 19/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).
#
#    Typical and above: also write check(value, limit) that returns the
#    difference and the percentage as two values - do not print anything
#    inside it, only calculate and return.
#
#    Excellent: also write print_report(label, value, limit, difference,
#    percent, status) that does ALL of the printing below - nothing outside
#    it should contain a print() of its own.
#
#    Give each function a one-line docstring saying what it does.


def status_of(percent):
    """Return the status for a given percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Return the difference and percentage for a record."""
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print the security record report."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {label}")
    print("=" * 34)
    print(f"Failed logins : {value:>10.2f}")
    print(f"Total attempts: {limit:>10.2f}")
    print(f"Difference    : {difference:>10.2f}")
    print(f"Percentage    : {percent:>9.2f}%")
    print(f"Status        : {status:>10}")
    print("=" * 34)

# ==================================================================== INPUT
# 2. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())


over_limit_count = 0

while True:
    label = input("Enter source IP (or quit to stop): ")
    if label.lower() == "quit":
        break

    value = float(input("Enter failed logins: "))
    limit = float(input("Enter total attempts: "))

    difference, percent = check(value, limit)
    status = status_of(percent)

    print_report(label, value, limit, difference, percent, status)

    if status == "OVER LIMIT":
        over_limit_count += 1

print(f"Total OVER LIMIT records: {over_limit_count}")


# ==========================================================================
# 5. Before you finish:
#
#    [] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it