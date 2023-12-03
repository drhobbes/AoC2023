'''We have a 140x140 grid, and I think the most efficient way to do this will be to map out the symbols' locations first.'''

def get_symbol_index(line):
    symbols = []
    index = 0
    for c in line:
    	# part1: just find the locations of any symbols
        #if not c.isdigit() and not c == '.' and not c .isspace(): symbols.append(index)
        # part2: where are the stars, how many numbers adjacent to them, what's their product:
        if c == '*': symbols.append([index,0,1])
        index += 1
    return symbols

def make_digit_dict(line, linenum):
    i = 0
    numbers = []
    while i < len(line):
        while i < len(line) and not line[i].isdigit(): # find the next number
            i += 1
        if i < len(line):
            # we found a number
            number = {"start": i}
            while i < len(line) and line[i].isdigit():
                i += 1
            number["end"] = i
            number["value"] = int(line[number["start"]:number["end"]])
            number["row"] = linenum
            numbers.append(number)
    return numbers

def adj_to_symbol(number, symbol_map):
    row_range = []
    if number["row"] > 0: row_range.append(number["row"]-1)
    row_range.append(number["row"])
    if number["row"] < len(symbol_map)-2: row_range.append(number["row"]+1)
    col_range = []
    if number["start"] > 0: col_range.append(number["start"]-1)
    for i in range(number["start"],number["end"]): col_range.append(i)
    col_range.append(number["end"])
    for x in row_range:
    	# part1: was there a symbol in the range of this number?
    	# part2: which numbers are adjacent to each symbol
        if len(symbol_map[x]) > 0:
            for symbol in symbol_map[x]:
                if symbol[0] in col_range:
                    symbol[1] += 1
                    symbol[2] *= number["value"]
            #for y in col_range:
                #if y in symbol_map[x]: return True
    #return False

symbol_map = []
numbers = []
with open("day3_input.txt","r") as f:
    linenum = 0
    for line in f:
        symbol_map.append(get_symbol_index(line))
        numbers.extend(make_digit_dict(line, linenum))
        linenum += 1

total = 0
for num in numbers:
	# part1: if this is true, add num to total
    adj_to_symbol(num, symbol_map)

# part2: if there were exactly two numbers adjacent to this one, add product to total
for symbol_row in symbol_map:
    if len(symbol_row) > 0:
        for symbol in symbol_row:
            if symbol[1] == 2:
                total += symbol[2]

print(total)