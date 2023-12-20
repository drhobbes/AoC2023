with open('../day16_input.txt','r') as f:
    tiles = [line.strip() for line in f]
energized = [[False for c in line] for line in tiles]

def is_energized(loc, d):
    if loc[0]+d[0] < 0 or loc[1]+d[1] < 0 or loc[0]+d[0] >= len(tiles) or loc[1]+d[1] >= len(tiles[0]):
        return False
    return energized[loc[0]+d[0]][loc[1]+d[1]]

def nav_maze_iter(beams):
    while len(beams) != 0:
        # move each beam one step
        for beam in beams:
            # if i moved off the map, remove this beam from the beams
            if beam['loc'][0] < 0 or beam['loc'][1] < 0:
                beams.remove(beam)
                continue
            if beam['loc'][0] >= len(tiles) or beam['loc'][1] >= len(tiles[0]):
                beams.remove(beam)
                continue

            # otherwise, energize this location and continue
            if energized[beam['loc'][0]][beam['loc'][1]]:
                beam['loop'] += 1
                if beam['loop'] > 20:
                    beams.remove(beam)
                    continue
            else:
                beam['loop'] = 0
            energized[beam['loc'][0]][beam['loc'][1]] = True

            # handle mirror: swap [row, col]
            if tiles[beam['loc'][0]][beam['loc'][1]] == '/':
                temp = beam['dir'][0]
                beam['dir'][0] = -1*beam['dir'][1]
                beam['dir'][1] = -1*temp
                beam['loc'][0]+=beam['dir'][0]
                beam['loc'][1]+=beam['dir'][1]
            elif tiles[beam['loc'][0]][beam['loc'][1]] == '\\':
                temp = beam['dir'][0]
                beam['dir'][0] = beam['dir'][1]
                beam['dir'][1] = temp
                beam['loc'][0]+=beam['dir'][0]
                beam['loc'][1]+=beam['dir'][1]

            # handle splitter: [row, col]
            elif tiles[beam['loc'][0]][beam['loc'][1]] == '-' and beam['dir'][1] == 0:
                beam['loc'][1]+=1
                beam['dir']=[0,1]
                beams.append({'loc':[beam['loc'][0],beam['loc'][1]-1], 'dir':[0,-1], 'loop':0})
            elif tiles[beam['loc'][0]][beam['loc'][1]] == '|' and beam['dir'][0] == 0:
                beam['loc'][0]+=1
                beam['dir']=[1,0]
                beams.append({'loc':[beam['loc'][0]-1,beam['loc'][1]], 'dir':[-1,0], 'loop':0})

            else:
                beam['loc'][0]+=beam['dir'][0]
                beam['loc'][1]+=beam['dir'][1]

# each beam is a baby object with a location and a direction
beams = [ {'loc':[0,0], 'dir':[0,1], 'loop':0} ]

nav_maze_iter(beams)

total = 0
for row in energized:
    total += row.count(True)
print('part 1: '+str(total))

high_beam = {'loc':[0,0], 'dir':[0,1]}
high_score = total

for i in range(len(tiles)):
    # try each row from the left
    energized = [[False for c in line] for line in tiles]
    beams = [ {'loc':[i,0], 'dir':[0,1], 'loop':0} ]
    nav_maze_iter(beams)
    total = 0
    for row in energized:
        total += row.count(True)
    if total > high_score:
        high_score = total
        high_beam = {'loc':[i,0], 'dir':[0,1]}

    # try each row from the right
    energized = [[False for c in line] for line in tiles]
    beams = [ {'loc':[i,len(tiles[0])-1], 'dir':[0,-1], 'loop':0} ]
    nav_maze_iter(beams)
    total = 0
    for row in energized:
        total += row.count(True)
    if total > high_score:
        high_score = total
        high_beam = {'loc':[i,len(tiles[0])-1], 'dir':[0,-1]}

print('new high left/right: '+str(high_score)+' from '+str(high_beam))

for i in range(len(tiles[0])):
    # try each col from the top
    energized = [[False for c in line] for line in tiles]
    beams = [ {'loc':[0,i], 'dir':[1,0], 'loop':0} ]
    nav_maze_iter(beams)
    total = 0
    for row in energized:
        total += row.count(True)
    if total > high_score:
        high_score = total
        high_beam = {'loc':[0,i], 'dir':[1,0]}

    # try each col from the bottom
    energized = [[False for c in line] for line in tiles]
    beams = [ {'loc':[len(tiles)-1,i], 'dir':[-1,0], 'loop':0} ]
    nav_maze_iter(beams)
    total = 0
    for row in energized:
        total += row.count(True)
    if total > high_score:
        high_score = total
        high_beam = {'loc':[len(tiles)-1,i], 'dir':[-1,0]}

print('new high left/right: '+str(high_score)+' from '+str(high_beam))
