def find_start(lines):
    for i in range(len(lines)):
        if 'S' in lines[i]:
            return [i, lines[i].find('S')]

pipes = {'S':{'|':'S', 'L':'E', 'J':'W'},
         'N':{'|':'N', '7':'W', 'F':'E'},
         'W':{'-':'W', 'L':'N', 'F':'S'},
         'E':{'-':'E', 'J':'N', '7':'S'}}

# x moves N to S, y moves W to E
dir_map = {'N':[-1,0], 'S':[1,0], 'E':[0,1], 'W':[0,-1]}

def trace_path(grid, start, direction):
    counter = 1
    x, y = start
    while grid[x][y] != 'S':
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]):
            return -1
        if grid[x][y] in pipes[direction]:
            counter += 1
            direction = pipes[direction][grid[x][y]]
            x += dir_map[direction][0]
            y += dir_map[direction][1]
        else:
            return -1
    return counter

dirs = {'N':[0,1], 'E':[1,0], 'W':[-1,0], 'S':[0,-1]}              

with open('../day10_input.txt', 'r') as f:
    grid = [line.strip() for line in f]

start_x, start_y = find_start(grid)
max_path = -1
use = []
for d in dir_map:
    path = trace_path(grid, [start_x+dir_map[d][0], start_y+dir_map[d][1]], d)
    if path > -1 and path >= max_path:
        max_path = path
        use.append(d)

print('part 1: '+str(max_path//2))

def map_start():
    if 'S' in use:
        if 'N' in use: return '|'
        if 'E' in use: return 'F'
        else: return '7'
    if 'N' in use:
        if 'E' in use: return 'L'
        else: return 'J'
    else: return '-'

def draw_path(grid, start, direction):
    x, y = start
    while x >= 0 and x < len(grid) and y >= 0 and y < len(grid[x]) and grid[x][y] != 'S':
        if grid[x][y] in pipes[direction]:
            direction = pipes[direction][grid[x][y]]
            grid[x][y] = 'P'
            x += dir_map[direction][0]
            y += dir_map[direction][1]
    grid[x][y] = map_start()

draw_grid = [list(line) for line in grid]
draw_path(draw_grid, [start_x+dir_map[use[0]][0], start_y+dir_map[use[0]][1]], use[0])

def inner_pass(grid, draw_grid):
    # turns out just translating how my brain does this task to code is in fact the right way, who knew
    inside_count = 0
    for i in range(len(draw_grid)):
        inside = False
        for j in range(len(draw_grid[i])):
            if draw_grid[i][j] == 'P' or grid[i][j] == 'S':
                char = grid[i][j] if grid[i][j] != 'S' else draw_grid[i][j]
                if char == '|':
                    inside = not inside
                elif char == 'F' or char == 'L':
                    waiting = char
                elif (char == 'J' and waiting == 'F') or (char == '7' and waiting == 'L'):
                    inside = not inside
            elif inside:
                inside_count += 1
    return inside_count

print('part 2: '+str(inner_pass(grid, draw_grid)))

