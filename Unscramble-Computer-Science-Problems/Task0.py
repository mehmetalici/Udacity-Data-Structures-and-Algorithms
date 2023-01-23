"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

def get_text_repr(entry):
    assert len(entry) == 3
    return f"{entry[0]} texts {entry[1]} at time {entry[2]}"

def get_call_repr(entry):
    assert len(entry) == 4
    return f"{entry[0]} calls {entry[1]} at time {entry[2]}, lasting {entry[3]} seconds"

print(f"First record of texts, {get_text_repr(texts[0])}")
print(f"Last record of calls, {get_call_repr(calls[-1])}")

