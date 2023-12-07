def get_lines(f):
    lines = []
    line = f.readline()
    while not line[0].isdigit():
        line = f.readline()
    while line and line[0].isdigit():
        lines.append([int(x) for x in line.split()])
        line = f.readline()
    return lines

def complete_map(input_array, map_lines): # part 1, just map one number at a time
    output_map = [0]*len(input_array)
    for dest_start, source_start, range_len in map_lines:
        for i in range(len(input_array)):
            if input_array[i] >= source_start and input_array[i] < source_start + range_len:
                output_map[i] = dest_start + (input_array[i]-source_start)
    for i in range(len(output_map)):
        if output_map[i] == 0:
            output_map[i] = input_array[i]
    return output_map

def update_map(pairs, lines): # part 2, map ranges
    new_pairs = []
    for start, length in pairs:
        while length > 0:
            check_start = start # to see if we found anything to map the front to
            for dest_start, src_start, range_len in lines:
                if src_start <= start < src_start+range_len:
                    new_pairs.append([start+(dest_start-src_start),
                                      min(length, src_start+range_len-start)])
                    start += new_pairs[-1][1]
                    length -= new_pairs[-1][1]
            if check_start == start:
                # we didn't find a mapping for this front value, it's the same
                check_len = length
                for dest_start, src_start, range_len in lines:
                    if start <= src_start <= start+length:
                        new_pairs.append([start, src_start-start])
                        length -= new_pairs[-1][1]
                        new_pairs.append([src_start, min(length, range_len)])
                        start = src_start+new_pairs[-1][1]
                        length -= new_pairs[-1][1]
                if check_len == length:
                    new_pairs.append([start, length])
                    length = 0
    return new_pairs

# part 1: map each seed number to a location
with open('day5_input.txt', 'r') as f:
    # get the seed numbers
    seeds = f.readline()
    seeds = seeds[seeds.find(': ')+1:].split()
    for i in range(len(seeds)):
        seeds[i] = int(seeds[i])

    # find the end of the file
    curpos = f.tell()
    f.seek(0,2)
    eof = f.tell()
    f.seek(curpos)

    # until we hit the end of the file, keep updating the map
    while f.tell() != eof:
        lines = get_lines(f)
        seeds = complete_map(seeds, lines)
    print('part 1: '+str(min(seeds)))

# part 2: pairs of values
with open('../day5_input.txt','r') as f:
    seeds_line = f.readline()
    seeds = [int(x) for x in seeds_line[seeds_line.find(': ')+1:].split()]
    pairs = []
    for i in range(len(seeds))[::2]:
        pairs.append([seeds[i], seeds[i+1]])

    curpos = f.tell()
    f.seek(0,2)
    eof = f.tell()
    f.seek(curpos)

    # get the next mapping
    while f.tell() != eof:
        lines = get_lines(f)
        pairs = update_map(pairs, lines)

    starts = [x[0] for x in pairs]
    print(min(starts))
