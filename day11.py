def expand(grid):
    galaxy_col = [False]*len(grid[0])
    galaxy_row = [False]*len(grid)
    for i in range(len(grid)):
        if '#' in grid[i]:
            galaxy_row[i] = True
            for idx, value in enumerate(grid[i]):
                if value == '#':
                    galaxy_col[idx] = True
    return [galaxy_row, galaxy_col]

def find_galaxies(grid, gal_map, expn_fctr):
    galaxy_dir = {}
    for i in range(len(grid)):
        for idx, value in enumerate(grid[i]):
            if value == '#':
                empty_rows = sum([1 for row in gal_map[0][:i] if not row])
                empty_cols = sum([1 for col in gal_map[1][:idx] if not col])
                galaxy_dir[len(galaxy_dir)] = [i+empty_rows*(expn_fctr-1), idx+empty_cols*(expn_fctr-1)]
    return galaxy_dir

with open('../day11_input.txt', 'r') as f:
    grid = [list(line.strip()) for line in f]
gal_map = expand(grid)

gal_dir = find_galaxies(grid, gal_map, 2)
total_dist = 0
for i in range(len(gal_dir)-1):
    for j in range(i+1, len(gal_dir)):
        total_dist += abs(gal_dir[i][0]-gal_dir[j][0])+abs(gal_dir[i][1]-gal_dir[j][1])
print('part 1: '+str(total_dist))

gal_dir = find_galaxies(grid, gal_map, 1000000)
total_dist = 0
for i in range(len(gal_dir)-1):
    for j in range(i+1, len(gal_dir)):
        total_dist += abs(gal_dir[i][0]-gal_dir[j][0])+abs(gal_dir[i][1]-gal_dir[j][1])
print('part 2: '+str(total_dist))
