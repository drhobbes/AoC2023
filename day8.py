with open('day8_input.txt','r') as f:
    dirs = [0 if x == 'L' else 1 for x in f.readline().strip()]
    f.readline() # blank
    nodes = {}
    for line in f:
        key = line.split()[0]
        left = line.split('(')[1].split(',')[0]
        right = line.split(',')[1][1:-2]
        nodes[key] = [left,right]

# part 1
curr, goal = 'AAA', 'ZZZ'
num_steps = 0
while curr != goal:
    for d in dirs:
        curr = nodes[curr][d]
        num_steps += 1
print('part1: '+str(num_steps)+' steps')

def part2_find(start):
    num_steps = 0
    while start[-1] != 'Z':
        for d in dirs:
            start = nodes[start][d]
            num_steps += 1
    return num_steps

def prime_factors(N):
    factors = []
    if N % 2 == 0: factors.append(2)
    while N % 2 == 0:
        N = N // 2
        if N % 2 == 0: factors.append(2)
        if N == 1:
            return factors # this was a power of 2
    for f in range(3, N+1, 2):
        if N % f == 0:
            factors.append(f)
            while N % f == 0:
                N = N // f
                if N % f == 0: factors.append(f)
                if N == 1:
                    return factors
    
# part 2
curr_part2 = [x for x in nodes.keys() if x[-1] == 'A']
steps_part2 = [part2_find(start) for start in curr_part2]
factors_part2 = [prime_factors(steps) for steps in steps_part2]
num_steps = len(dirs)
for f in factors_part2:
    num_steps *= f[0]
print('part2: '+str(num_steps)+' steps')
