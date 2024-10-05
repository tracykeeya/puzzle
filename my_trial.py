https://adventofcode.com/2023/day/1
# Read the input data
data = '''[YOUR INPUT HERE]'''

# Split the data by blank lines
elves = data.strip().split('\n\n')

# Initialize a list to store the sum of calories for each Elf
calorie_sums = []

# Iterate through each Elf's inventory
for elf in elves:
    # Split the Elf's inventory by line, convert to integers, and sum them
    total_calories = sum(map(int, elf.split()))
    calorie_sums.append(total_calories)

# Find the maximum calorie sum
max_calories = max(calorie_sums)

print("The Elf carrying the most calories has:", max_calories)
