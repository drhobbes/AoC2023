def get_num_rows_above(pattern):
    for i in range(len(pattern)-1):
        num_reflect = min(i+1, len(pattern)-i-1)
        reflect_i = i
        for j in range(i+1, i+num_reflect+1):
            if pattern[reflect_i] == pattern[j]:
                reflect_i -= 1
        if reflect_i == i-num_reflect:
            return i+1
    return -1

def rotate(pattern):
    return [[pattern[j][i] for j in range(len(pattern))] for i in range(len(pattern[0]))]

# read in the patterns from the file
patterns = []
with open('../day13_input.txt', 'r') as f:
    pattern = []
    for line in f:
        if not line.isspace():
            pattern.append(line.strip())
        else:
            patterns.append(pattern)
            pattern = []
    patterns.append(pattern)

row_total, col_total = 0, 0
for pattern in patterns:
    temp = get_num_rows_above(pattern)
    if temp > -1: row_total += temp
    temp = get_num_rows_above(rotate(pattern))
    if temp > -1: col_total += temp

print('part 1: '+str(100*row_total + col_total))

def off_by_one(line1, line2):
    mismatch_count = 0
    for i in range(len(line1)):
        if line1[i] != line2[i]: mismatch_count += 1
    return mismatch_count == 1

def get_num_rows_smudge(pattern):
    for i in range(len(pattern)-1):
        num_reflect = min(i+1, len(pattern)-i-1)
        reflect_i = i
        smudge_remains = True
        for j in range(i+1, i+num_reflect+1):
            if pattern[reflect_i] == pattern[j]:
                reflect_i -= 1
            elif smudge_remains and off_by_one(pattern[reflect_i], pattern[j]):
                reflect_i -= 1
                smudge_remains = False
        if reflect_i == i-num_reflect and not smudge_remains:
            # EVERY mirror has a smudge, ignore the smudgeless results
            return [i+1, smudge_remains]
    return [-1, True]

row_total, col_total = 0, 0
for pattern in patterns:
    row = get_num_rows_smudge(pattern)
    col = get_num_rows_smudge(rotate(pattern))
    if not row[1]: row_total += row[0]
    elif not col[1]: col_total += col[0] 

print('part 2: '+str(100*row_total + col_total))
