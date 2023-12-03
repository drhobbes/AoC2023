'''Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?'''

def validate_pull(pull):
    max = {"red":12, "green":13, "blue":14}
    num, color = int(pull.split()[0]), pull.split()[1]
    return num <= max[color] and num >= 0

def parse_line(line):
    game_id = int(line[5:line.find(":")])
    games = line[line.find(":")+1:].split(";")
    all_valid = True
    for game in games:
        pulls = game.split(", ")
        for pull in pulls:
            if not validate_pull(pull): all_valid = False
    return game_id if all_valid else 0

with open("day2_input.txt", 'r') as f:
    total = 0
    for line in f:
        total += parse_line(line)

print(total)

''' For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?
The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together.'''

def get_counts(line):
    games = line[line.find(":")+1:].split(";")
    counts = {"red": 0, "green": 0, "blue": 0}
    for game in games:
        pulls = game.split(", ")
        for pull in pulls:
            num, color = int(pull.split()[0]), pull.split()[1]
            if counts[color] < num: counts[color] = num
    return counts

with open("day2_input.txt", 'r') as f:
    total = 0
    for line in f:
        counts = get_counts(line)
        total += counts["red"]*counts["green"]*counts["blue"]
        
print(total)