"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from os import O_APPEND

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
A telephone company wants to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def get_possible_telemarketers(calls: list, texts: list):
    callers = set()
    other_numbers = set()
    for call in calls:
        callers.add(call[0])
        other_numbers.add(call[1])

    for text in texts:
        other_numbers.add(text[0])
        other_numbers.add(text[1])

    tele = callers - other_numbers

    return tele


print("These are the possible telemarketers:")
print("\n".join(sorted(get_possible_telemarketers(calls, texts))))