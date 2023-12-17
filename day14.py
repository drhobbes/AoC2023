with open('../day14_input.txt','r') as f:
    grid = [line.strip() for line in f]

def get_load(row_num, grid):
    weight = len(grid)-row_num
    row_total = 0
    for col in range(len(grid[row_num])):
        # in each column, find the north edge OR the lowest-index # above i
        top_index = 0
        for j in range(row_num+1)[::-1]:
            if grid[j][col] == '#':
                top_index = j+1
                break

        # in each column, find the south edge OR the next-lowest-index # after i
        bottom_index = len(grid)
        for j in range(row_num, len(grid)):
            if grid[j][col] == '#':
               bottom_index = j
               break

        if top_index < bottom_index:
            # in each column, count the number of Os between the top and bottom limits
            o_count = 0
            for j in range(top_index, bottom_index):
                if grid[j][col] == 'O': o_count += 1

            # subtract out any that rolled above
            num_above = row_num-top_index
            if o_count - num_above > 0:
                row_total += weight
    return row_total

total = 0
for i in range(len(grid)):
    total += get_load(i, grid)
print('part 1: '+str(total))
