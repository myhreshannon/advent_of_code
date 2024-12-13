# The engineers are trying to figure out which reports are safe. 
# The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. 
# So, a report only counts as safe if both of the following are true:

# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.

# For part 2, allow for one bad reading before marking the report as unsafe.


reports = []
with open('Input', 'r') as file:
    reports = [line.rstrip('\n') for line in file]

safe_reports = 0
for line in reports:
    report = list(map(int, line.split(' ')))
    safe = True
    prev_bad = False
    previous_level = 0
    # check to see if it's increasing or decreasing
    if report[0] < report[1]:
        # Go through the levels in this report and check to make sure they're increasing by 1, 2, or 3
        for level in report:
            if previous_level == 0:
                previous_level = level
            elif level <= previous_level or (1 < (level - previous_level) > 3):
                if prev_bad:
                    safe = False
                    break
                else:
                    prev_bad = True
                    previous_level = level
            else:
                previous_level = level

    elif report[0] > report[1]:
        # Go through the levels in this report and check to make sure they're decreasing by 1, 2, or 3
        for level in report:
            if previous_level == 0:
                previous_level = level
            elif level >= previous_level or (1 < (previous_level - level) > 3):
                if prev_bad:
                    safe = False
                    break
                else:
                    prev_bad = True
                    previous_level = level
            else:
                previous_level = level

    else:
        # They're the same. Need to increase or decrease
        safe = False

    if safe:
        safe_reports += 1

print(safe_reports)
