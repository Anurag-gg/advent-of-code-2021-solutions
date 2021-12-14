from collections import defaultdict
grid = defaultdict(bool)
folds , pos = [] , []
with open('day13/data.txt','r') as data:
    for x in data:
        x = x.strip()
        if x and x.startswith('fold'):
            temp = x.split()[-1].split('=')
            folds.append(temp)
        else:
            if x:
                e1 , e2 = x.split(',')
                pos.append((e1,e2))


if folds[0][0] == 'x':
    for ele in pos:
        x , y =  ele
        if int(x) < int(folds[0][1]):
            grid[(int(x),int(y))] = True
        else:
            grid[(2*int(folds[0][1])-int(x), int(y))] = True


print(len(grid.keys()))