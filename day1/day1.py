# Part 1
# Pair up the smallest number in the left list with the smallest number in the right list, 
# then the second-smallest left number with the second-smallest right number, and so on.

# Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. 
# For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; 
# if you pair up a 9 with a 3, the distance apart is 6.

import csv

#ingest lists
left_lst, right_lst = [],[]
with open('Input', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        left_lst.append(row[0])
        right_lst.append(row[1])      
 
#sort
left_lst.sort()
right_lst.sort()

#loop lists and compare
#add the distance between them to total difference variable
total_diff = 0
for item in range(len(left_lst)):
    diff = int(left_lst[item]) - int(right_lst[item])
    total_diff += abs(diff)

print(f"Total distance between lists: {total_diff}")


# Part 2
# This time, you'll need to figure out exactly how often each number from the left list appears in the right list. 
# Calculate a total similarity score by adding up each number in the left list after multiplying it by 
# the number of times that number appears in the right list.

similarity_score = 0
# Get the numbers in both lists by casting the left list to a set and checking intersections with the right list
both_list_nums = (set(left_lst).intersection(right_lst))
#print(both_list_nums)

# For each number we know is in both lists, find the count of how many times it's in the right list
for num in both_list_nums:
    count = 0
    for i in right_lst:
        if i == num:
            count += 1
        # right_list is sorted so when we get to something over the number, no use searching anymore
        elif i > num:
            break

    #print(f"There are {count} occurrences of {num} in right_lst")
    # Get the similarity score of this number by multiplying it by the number of times it's seen in the right list
    # Add this value to the total similarity score
    similarity_score += int(num) * int(count)

print(f"Similarity score between lists: {similarity_score}")
