def get_next(sequence):
    new_seq = [sequence[i+1]-sequence[i] for i in range(len(sequence)-1)]
    if new_seq == [0]*len(new_seq): return 0
    
    calc_num = get_next(new_seq)
    return new_seq[-1]+calc_num

def get_prev(sequence):
    new_seq = [sequence[i+1]-sequence[i] for i in range(len(sequence)-1)]
    if new_seq == [0]*len(new_seq): return 0

    calc_num = get_prev(new_seq)
    return new_seq[0]-calc_num

seq = []
with open('../day9_input.txt','r') as f:
    for line in f:
        seq.append([int(x) for x in line.split()])

total = 0
for s in seq:
    total += get_next(s)+s[-1]
print('part1: '+str(total))

total = 0
for s in seq:
    total += s[0]-get_prev(s)
print('part2: '+str(total))
