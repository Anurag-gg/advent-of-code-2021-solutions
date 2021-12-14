from collections import defaultdict

actions = []
with open("day14/data.txt", 'r') as data:
    for x in data:
        x = x.strip()
        if x:
            if "->" in x:
                actions.append(list(map(lambda e: e.strip(),x.split("->"))))
            else:
                poly  = x

comb =  defaultdict(int)
for i in range(len(poly)-1):
    comb[poly[i:i+2]] += 1

word_count = defaultdict(int)
for x in poly:
    word_count[x] +=1

for i in range(40):
    temp_comb = defaultdict(int)
    for key, value in  comb.items():
        for action in actions:
            if key == action[0]:
                word_count[action[1]] += value
                temp_comb[action[0][0]+ action[1]] += comb[key]
                temp_comb[action[1]+ action[0][1]] += comb[key]
                break  
    comb = temp_comb.copy()

high = max([x for x in word_count.values()])
low = min([x for x in word_count.values()])
print(high - low)