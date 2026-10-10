"""
Addition quiz

Step 1: Generate two single-digit integers for number1 (e.g., 4) and number 2 (e.g., 5)
Step 2: Prompt the student to answer, "What is 4 + 5?" (user input)
Step 3: Check whether the student's answer is correct.
"""

import random

while True:
    num_1 = random.randint(1, 9)
    num_2 = random.randint(1, 9)

    answer = int(input(f"What is {num_1} + {num_2}? "))

    if answer == num_1 + num_2:
        print("Correct!")
        break
    else:
        print(f"Incorrect. The correct answer is {num_1 + num_2}.")
