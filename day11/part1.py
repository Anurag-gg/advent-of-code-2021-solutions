a = []
with open("day11/data.txt","r") as data:
    for x in data:
        temp = list(map(int , list(x)[:-1]))
        a.append(temp)

col = len(temp)
row = len(a)

def calc(r, c, bin,flash = 0):
    if a[r][c] != 9:
        if bin[r][c]:
            a[r][c] += 1
    else:
        flash  += 1
        a[r][c] = 0
        bin[r][c] = 0
        #left
        if c-1 >= 0:
            flash += calc(r,c-1,bin)
        #right
        if c+1<=col-1:
            flash += calc(r,c+1,bin)
        #down
        if r+1<= row-1:
            flash += calc(r+1,c,bin)
        #up
        if r-1>= 0:
            flash += calc(r-1,c,bin)
        #nw
        if r-1>=0 and c-1>=0:
            flash += calc(r-1,c-1,bin)
        #ne
        if r-1>=0 and c+1<=col-1:
            flash += calc(r-1,c+1,bin)
        #sw
        if r+1<=row-1 and c-1>=0:
            flash += calc(r+1,c-1,bin)
        #se
        if r+1<=row-1 and c+1<=col-1:
            flash += calc(r+1,c+1,bin)
    return flash

if __name__ == '__main__':
    result = 0
    for _ in range(100):
        bin = [[1 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                result += calc(i,j, bin)
    print(result) 