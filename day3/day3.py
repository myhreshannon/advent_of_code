# It seems like the goal of the program is just to multiply some numbers. 
# It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers.
# However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored, 
# even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

# Read input
# regex mul(#,#)
# sum all valid finds

import re

program = []
with open('Input.txt', 'r') as file:
    program = file.read()

matches = re.findall(r"mul\([0-9]?[0-9]?[0-9],[0-9]?[0-9]?[0-9]\)", program)

answer = 0
for match in matches:
    comma_index = match.find(',')
    answer += int(match[4:comma_index]) * int(match[(comma_index + 1):(len(match) - 1)])

print(answer)

# Part 2
# There are two new instructions you'll need to handle:
# The do() instruction enables future mul instructions.
# The don't() instruction disables future mul instructions.

matches = re.findall(r"mul\([0-9]?[0-9]?[0-9],[0-9]?[0-9]?[0-9]\)|do\(\)|don\'t\(\)", program)

mul_enabled = True
p2_answer = 0
for match in matches:
    if match == "do()":
        mul_enabled = True
    elif match == "don't()":
        mul_enabled = False
    elif mul_enabled:
        comma_index = match.find(',')
        p2_answer += int(match[4:comma_index]) * int(match[(comma_index + 1):(len(match) - 1)])

print(p2_answer)
