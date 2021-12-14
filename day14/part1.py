from typing import Counter

actions = []
with open("day14/data.txt", 'r') as data:
    for x in data:
        x = x.strip()
        if x:
            if "->" in x:
                actions.append(list(map(lambda e: e.strip(),x.split("->"))))
            else:
                poly  = x

for i in range(10):
    temp_poly = ''
    for ptr in range(len(poly)-1):
        for action in actions:
            if poly[ptr:ptr+2] == action[0]:
                temp_poly += poly[ptr] + action[1] 
                break
        else:
            temp_poly += poly[ptr]
    poly = temp_poly + poly[-1]


freq = Counter(poly)
high = max([x for x in freq.values()])
low = min([x for x in freq.values()])
print(high - low)