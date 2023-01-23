"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from enum import Enum


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

TELEMARKET_PREFIX = "140"


class AreaCodes:
  BANGALORE = "080"
  UNKNOWN = "XXX"

  @classmethod
  def get_as_list(cls):
    return [cls.BANGALORE]


class PrefixTypes:
  MOBILE = 0
  FIXED = 1
  TELEMARKET = 2



class UndefinedPrefixException(Exception):
  def __init__(self, *args: object) -> None:
      super().__init__(*args)


def get_unique(arr: list):
  return set(arr)


def get_column(record: list, col_idx: int):
  return [row[col_idx] for row in record]


def get_prefix_type(number: str):
  if number[0] == '(' and ')' in number[1:]:
    return PrefixTypes.FIXED

  if ' ' in number and int(number[0]) in [7, 8, 9]:  
    return PrefixTypes.MOBILE

  if number[:3] == TELEMARKET_PREFIX:  
    return PrefixTypes.TELEMARKET

  raise UndefinedPrefixException


def get_mobile_prefix(number: str):
  try:
    type = get_prefix_type(number)  
  except UndefinedPrefixException:
    #print(f"Warning: {number} contains unknown prefix. Skipping...")
    return

  if type == PrefixTypes.FIXED:
    start_idx = 1
    try:
      end_idx = number.index(')')  
    except ValueError:
      #print(f"Warning: {number} contains unended paranthesis. Skipping...")
      return
    return number[start_idx:end_idx]
  
  if type == PrefixTypes.MOBILE:  
    return number[0:4]  

  if type == PrefixTypes.TELEMARKET:
    return TELEMARKET_PREFIX  


def get_indices_of_same_area(col: list, indices: list, area_code: AreaCodes):
  return [idx for idx in indices if get_mobile_prefix(col[idx]) == area_code]


def calc_same_area_percentage(record: list, area_code: AreaCodes):
  xer_col, xee_col = [get_column(record, col_idx=i) for i in range(2)]
  xer_col_indices = [idx for idx, number in enumerate(xer_col) if get_mobile_prefix(number) == area_code]
  xee_col_indices = get_indices_of_same_area(xee_col, xer_col_indices, area_code)
  percentage = len(xee_col_indices) / len(xer_col_indices) * 100
  return percentage

def get_numbers_called_from_area(area_code: AreaCodes, callers: list, callees: list):
  return [callees[i] for i in range(len(callees)) if get_mobile_prefix(callers[i]) == area_code]


# Part A
callers, callees = [get_column(calls, col_idx=i) for i in range(2)]
numbers = get_numbers_called_from_area(area_code=AreaCodes.BANGALORE,
                                       callers=callers,
                                       callees=callees)
unique_prefixes = get_unique([get_mobile_prefix(number) for number in numbers])
print("\n".join(sorted(unique_prefixes)))

# Part B
fixed_type_percentage = calc_same_area_percentage(record=calls, area_code=AreaCodes.BANGALORE)
print(f"{fixed_type_percentage:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")










