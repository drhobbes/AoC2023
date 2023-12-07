part1_cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def get_type(hand):
    counts = [hand.count(i) for i in hand]
    if 5 in counts: return 0 # five of a kind
    if 4 in counts: return 1 # four of a kind
    if 3 in counts and 2 in counts: return 2 # full house
    elif 3 in counts: return 3 # three of a kind
    if 2 in counts:
        if counts.count(1) == 1:
            return 4 # two pair
        else: return 5 # one pair
    return 6 # big pile of nothing

def get_type_part2(hand):
    j_count = hand.count('J')
    no_jokers = hand.replace('J','')
    if len(no_jokers) == 0: return 0 # the only actual 5-of-a-kind is all Js because of course it is
    counts = [hand.count(i) for i in no_jokers]
    if max(counts)+j_count == 5: return 0
    if max(counts)+j_count == 4: return 1
    if max(counts)+j_count == 3:
        if (min(counts)) == 1:
            return 3 # three of a kind
        return 2 # full house
    if max(counts)+j_count == 2:
        # we will never get two pair using jokers
        if counts.count(1) == 1:
            return 4
        return 5
    return 6

''' negative if hand1 < hand2, positive if hand1 > hand2, 0 if they have identical cards '''
def compare_to(hand1, hand2):
    if hand1[2] != hand2[2]:
        # different types
        return hand1[2]- hand2[2]
    # find the high card
    for i in range(len(hand1[0])):
        if cards.index(hand1[0][i]) != cards.index(hand2[0][i]):
            return cards.index(hand1[0][i])-cards.index(hand2[0][i])

# get the input
with open('../day7_input.txt','r') as f:
    hands = [[line.split()[0], int(line.split()[1])] for line in f]

for i in range(len(hands)):
    hands[i].append(get_type_part2(hands[i][0]))

def merge_sort(list):
    ''' shoot me '''
    if len(list) == 1:
        return list

    first = merge_sort(list[:len(list)//2])
    second = merge_sort(list[len(list)//2:])

    merged = []
    i, j = 0, 0
    while i < len(first) and j < len(second):
        compare = compare_to(first[i], second[j])
        if (compare < 0):
            merged.append(first[i])
            i += 1
        else:
            merged.append(second[j])
            j += 1

    if i < len(first):
        merged.extend(first[i:])
    else:
        merged.extend(second[j:])

    return merged

sorted_hands = merge_sort(hands)

rank = len(sorted_hands)
total = 0
for hand in sorted_hands:
    total += rank * hand[1]
    rank -= 1
print('total winnings: '+str(total))
