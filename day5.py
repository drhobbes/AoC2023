def get_lines(f):
    lines = []
    line = f.readline()
    while not line[0].isdigit():
        line = f.readline()
    while line and line[0].isdigit():
        lines.append([int(x) for x in line.split()])
        line = f.readline()
    return lines

def update_map(pairs, lines):
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
