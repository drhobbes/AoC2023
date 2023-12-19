def get_hash(seq):
    val = 0
    for ch in seq:
        val += ord(ch)
        val *= 17
        val %= 256
    return val

hashmap = { k:v for (k,v) in zip(range(256), [[] for i in range(256)]) }

def init_seq(step):
    idx = step.find('-') if '-' in step else step.find('=')
    label = step[:idx]
    box_num = get_hash(label)
    if '-' in step:
        for lens in hashmap[box_num]:
            if lens[0] == label:
                hashmap[box_num].remove(lens)
                return
    elif '=' in step:
        focal_length = int(step[idx+1:])
        for i in range(len(hashmap[box_num])):
            if hashmap[box_num][i][0] == label:
                hashmap[box_num][i][1] = focal_length
                return
        hashmap[box_num].append([label, focal_length])

def calc_focus_pwr(box_num, box):
    total = 0
    for i in range(len(box)):
        total += box_num*(i+1)*box[i][1]
    return total

with open('../day15_input.txt','r') as f:
    seq = f.readline().strip().split(',')

total = 0
for step in seq:
    total += get_hash(step)
    init_seq(step)
print('part 1: '+str(total))

pwr_total = 0
for key in hashmap.keys():
    pwr_total += calc_focus_pwr(key+1, hashmap[key])
print('part 2: '+str(pwr_total))
