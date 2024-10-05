with open('calories.txt', 'r') as file:
    data = file.read().splitlines()

calories = []
current_total = 0

for line in data:
    if line.strip():
        current_total += int(line.strip())
    else:
        calories.append(current_total)
        current_total = 0

# Add the last Elf's calories if there's no newline at the end
if current_total > 0:
    calories.append(current_total)

# Sort the list to get the top 3 Elves
calories.sort(reverse=True)

# Get the sum of the top 3
top_three_sum = sum(calories[:3])
print(f"Sum of top 3 Elves' calories: {top_three_sum}")
