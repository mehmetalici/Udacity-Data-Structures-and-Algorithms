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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def get_column(record, col_idx):
    return [row[col_idx] for row in record]  


def get_unique_multi(records, col_incides):
    all_numbers = set()
    for record in records:
        for col_idx in col_incides:
            all_numbers.update(get_column(record, col_idx))
    return all_numbers


records = (texts, calls)
cols_with_nr = (0, 1)
print(f"There are {len(get_unique_multi(records, cols_with_nr))} different telephone numbers in the records.")