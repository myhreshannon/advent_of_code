# If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
# If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. 
#   The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. 
#   (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
# If none of the other rules apply, the stone is replaced by a new stone; 
# the old stone's number multiplied by 2024 is engraved on the new stone.

# Initial arrangement:
# 125 17

# After 1 blink:
# 253000 1 7

# After 2 blinks:
# 253 0 2024 14168


from collections import defaultdict

def blink(input):
    output = []
    for i in range(len(input)):
        if input[i] == 0:
            output.append(1)
        elif len(str(input[i])) % 2 == 0:
            stone = str(input[i])
            length = int(len(stone) / 2)
            output.append(int(stone[:length]))
            output.append(int(stone[length:]))
        else:
            new_stone = input[i] * 2024
            output.append(new_stone)
    return output

# Prompt says order matters, but it doesn't actually matter to get the answer
# Use dictionary to keep track of the count of each stone, instead of keeping a list with the correct order
# Use defaultdict so I don't have to worry about adding new keys for new stones
def blink_opt(input_dict):
    output_dict = defaultdict(int)
    for key,value in input_dict.items():
        if key == 0:
            output_dict[1] += value
        elif len(str(key)) % 2 == 0:
            stone = str(key)
            length = int(len(stone) / 2)
            output_dict[(int(stone[:length]))] += value
            output_dict[(int(stone[length:]))] += value
        else:
            output_dict[key * 2024] += value
    return output_dict

input = "0 5601550 3914 852 50706 68 6 645371"
input = input.split(" ")
# I got the wrong answer without explicitly converting in the input list to ints,
# probably due to leading zeros giving me an "even" number of numbers on some splits after multiple blinks
input = list(map(int,input))
input_dict = {n: 1 for n in input}

count = 0
for loop in range(25):
    input = blink(input)

print(f"Total stones part 1: {len(input)}")

for loop in range(75):
    input_dict = blink_opt(input_dict)

print(f"Total stones part 2: {sum(input_dict.values())}")
