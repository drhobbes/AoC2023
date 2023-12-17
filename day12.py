with open('../day12_input.txt','r') as f:
    lines = [line.split() for line in f]

def get_possibilities(poss_list, group, min_after):
    target_str = '#'*group
    if min_after != 0: target_str += '.'

    new_possibilities = []

    for seq, min_before in poss_list: # [possible alignment, next min start position]
        #print(' '+seq)

        if min_after == 0 and target_str in seq[min_before:len(seq)-min_after]:
            new_possibilities.append([seq, seq.find(target_str, min_before)+len(target_str)])
            continue
        
        for i in range(min_before, len(seq)-len(target_str)-min_after+1):
            # take a target-sized slice of the feasible sequence and see if this works
                search_substr = seq[i:i+len(target_str)]
                exact, inexact = True, True
                for j in range(len(target_str)):
                    if target_str[j] == search_substr[j]:
                        # exact match
                        pass
                    elif search_substr[j] == '?':
                        # inexact match
                        if target_str[j] == '#':
                            exact = False
                    else:
                        # not a match
                        exact, inexact = False, False
                        
                # add this into our list of possibilities
                if (exact or inexact) and (i == 0 or seq[i-1] != '#'):
                    if target_str[-1] != '.' and seq[i+len(target_str):].find('#') != -1:
                        continue # not the droids you're looking for
                    if seq[min_before:i].find('#') != -1:
                        continue # also not the droids you're looking for
                    mutable_str = list(seq)
                    for idx1, idx2 in zip(range(i, i+len(target_str)), range(len(target_str))):
                        mutable_str[idx1] = target_str[idx2]
                    if (i != 0): mutable_str[i-1] = '.'
                    new_possibilities.append([''.join(mutable_str),i+len(target_str)])
                    if exact:
                        break

    return new_possibilities

def get_num_solutions(line, exp_factor):
    conditions = ((line[0]+'?')*exp_factor)[:-1]
    groups = [int(x) for x in line[1].split(',')]*exp_factor

    # most basic: every group already separated by one .
    min_len = sum(groups)+len(groups)-1
    if len(conditions) == min_len:
        return 1

    # let's try storing each possible fit? this could probably be optimized
    possibilities = [[conditions, 0]] # [possible alignment, next min start position]
    for i in range(len(groups)):
        min_after = sum(groups[i+1:])+len(groups[i+1:])-1 if i < len(groups)-1 else 0
        possibilities = get_possibilities(possibilities, groups[i], min_after)

    # and only keep the ones that actually have the right number of # characters
    count = 0
    for poss in possibilities:
        if poss[0].count('#') == sum(groups):
            count += 1

    return count

total = 0
for line in lines:
    total += get_num_solutions(line, 1)
print('part 1: '+str(total))

# theoretically this should work but the brute force of it is taking too long
progress = 0
total = 0
for line in lines:
    total += get_num_solutions(line, 5)
    progress += 1
    if progress % 5 == 0:
        print(str(progress)+'/'+str(len(lines))+' ('+str(total)+')')
print('part 2: '+str(total))
