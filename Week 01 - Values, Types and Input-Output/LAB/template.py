"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
#
#    Remember: input() always gives back text.

label = input("Hostname: ")
first = float(input("GB used: "))
second = float(input("GB total: "))


# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]
#
#    - difference : how far the first is from the second
#    - percent    : the first as a percentage of the second
#
#    Do not type the answers. Calculate them.

difference = second - first  
percent = first / second * 100 


# =================================================================== OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"  used  : {first:>10.2f}")
print(f"  total : {second:>10.2f}")
print(f"  difference  : {difference:>+10.2f}")
print(f"  percent : {percent:>10.2f}")
print(f" status       :{label} check completed")

print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ x ] Run it three times with different numbers
#    [ x ] Run it with a total of 0 and write the error in your journal
#    [ x ] Check every variable name says what it holds
#    [ x ] Show it to the person next to you
