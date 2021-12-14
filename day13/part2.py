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
                grid[(e1,e2)] = True
 
for fold in folds:
    temp_grid = defaultdict(bool)
    if fold[0] == 'x':
        for ele in grid.keys():
            x , y =  ele
            if int(x) < int(fold[1]):
                temp_grid[(int(x),int(y))] = True
            else:
                temp_grid[(2*int(fold[1])-int(x), int(y))] = True
    else:
        for ele in grid.keys():
            x , y =  ele
            if int(y) < int(fold[1]):
                temp_grid[(int(x),int(y))] = True
            else:
                temp_grid[(int(x) , 2*int(fold[1])-int(y))] = True
    grid = temp_grid.copy()


row = max([int(y) for x,y in grid.keys() if grid.values()])
col = max([int(x) for x,y in grid.keys() if grid.values()])

for i in range(row+1):
    for j in range(col+1):
        if grid[(j,i)]:
            print('xx', end = '')
        else:
            print('  ', end= '')
    print()
    