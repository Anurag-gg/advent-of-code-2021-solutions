a = []
with open("day11/data.txt","r") as data:
    for x in data:
        temp = list(map(int , list(x)[:-1]))
        a.append(temp)

col = len(temp)
row = len(a)

def calc(r, c, bin):
    if a[r][c] != 9:
        if bin[r][c]:
            a[r][c] += 1
    else:
        a[r][c] = 0
        bin[r][c] = 0
        #left
        if c-1 >= 0:
            calc(r,c-1,bin)
        #right
        if c+1<=col-1:
            calc(r,c+1,bin)
        #down
        if r+1<= row-1:
            calc(r+1,c,bin)
        #up
        if r-1>= 0:
            calc(r-1,c,bin)
        #nw
        if r-1>=0 and c-1>=0:
            calc(r-1,c-1,bin)
        #ne
        if r-1>=0 and c+1<=col-1:
            calc(r-1,c+1,bin)
        #sw
        if r+1<=row-1 and c-1>=0:
            calc(r+1,c-1,bin)
        #se
        if r+1<=row-1 and c+1<=col-1:
            calc(r+1,c+1,bin)

if __name__ == '__main__':
    result = 0
    step = 0
    while True:
        if bin == [[0 for _ in range(col)] for _ in range(row)]:
            print(step)
            exit()
        bin = [[1 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                calc(i,j, bin)
        step += 1