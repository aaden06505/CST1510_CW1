"""
RECORD CHECK  -  my version
===========================

Name  :  Asli
Lane  :  Cyber 
Date  :  15/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
over_limit_count = 0
while True:
    label = input("Enter source IP: ")  
    if label.lower() == "quit":
        break
    failed_logins = float(input("Enter failed login attempts: "))
    total_attempts = float(input("Enter total login attempts: "))
    if total_attempts <= 0:
        print("Total attempts must be greater than 0. Please try again.")
        continue
    # ================================================================== PROCESS
    # 2. Work out the difference and the percentage.       [Typical and above]
    successful_logins = total_attempts - failed_logins
    percent_failed = (failed_logins / total_attempts) * 100
    percent_success = (successful_logins / total_attempts) * 100
    # 3. Decide a status and store it in a variable called status.
    #
    #    Threshold : if / else        -> "OVER LIMIT" or "OK"
    #    Typical   : if / elif / else -> "OVER LIMIT" (100% or more),
    #                                     "WARNING" (90% or more), otherwise "OK"

    if percent_failed >= 100:
        status = "OVER LIMIT"
    elif percent_failed >= 90:
        status = "WARNING"
    else:
        status = "OK"


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

   
    print(f"Failed logins     : {failed_logins:>10.2f}")
    print(f"Total attempts    : {total_attempts:>10.2f}")
    print(f"Successful logins : {successful_logins:>10.2f}")
    print(f"Failed %          : {percent_failed:>10.2f}%")
    print(f"Success %         : {percent_success:>10.2f}%")
    print(f"Status            : {status}")
            

    print("=" * 34)
    if status == "OVER LIMIT":
        over_limit_count += 1
print(f"OVER LIMIT records: {over_limit_count}")
# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
