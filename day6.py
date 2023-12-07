def num_ways_to_win(time, dist):
    # find the LONGEST we can hold the button
    i = 1
    while dist/(time-i) > i: i+= 1
    longest = time-i
    # find the SHORTEST we can hold the button
    i = 1
    while dist/i > time-i: i+= 1
    return longest-i+1

# get input
races = []
with open('day6_input.txt','r') as f:
    times = [int(x) for x in f.readline().split(':')[1].split()]
    dists = [int(x) for x in f.readline().split(':')[1].split()]
    for i in range(len(times)):
        races.append([times[i], dists[i]])

# part 1: how many different ways to break the current distance record
prod = 1
for time, dist in races:
    prod *= num_ways_to_win(time, dist)
print('part 1: '+str(prod))

# part 2: oops those spaces weren't supposed to be there
with open('day6_input.txt','r') as f:
    time = int(f.readline().split(':')[1].replace(" ",""))
    dist = int(f.readline().split(':')[1].replace(" ",""))
    print('part 2: '+str(num_ways_to_win(time,dist)))
