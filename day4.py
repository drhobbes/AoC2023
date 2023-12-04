# part 1
with open('day4_input.txt', 'r') as f:
    total = 0
    for line in f:
        winning = line[line.find(':')+2:].split('|')[0].split()
        yours = line.split('|')[1].split()
        subtotal = 0
        for num in winning:
            if num in yours:
                subtotal = 1 if subtotal == 0 else subtotal * 2
        total += subtotal
    print('points: '+str(total))

# part 2
wins = []
with open('day4_input.txt', 'r') as f:
    for line in f:
        winning = line[line.find(':')+2:].split('|')[0].split()
        yours = line.split('|')[1].split()
        subtotal = 0
        for num in winning:
            if num in yours: 
                subtotal += 1
        wins.append([1,subtotal]) # copies of card at index 0

# propogate the cards forward
for i in range(len(wins)):
    for j in range(i+1, i+wins[i][1]+1):
        # add the number of copies of THIS card to the total number of copies of THAT card
        wins[j][0] += wins[i][0]

# calculate the total
total, count = 0, 0
for card in wins:
    total += card[0]
    count += 1
print('number of cards: '+str(total))