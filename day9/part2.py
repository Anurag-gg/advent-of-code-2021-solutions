#really proud of doing this
a = []
with open("day9/data.txt" , "r") as data:
    for x in data:
        temp = list(x)
        a.append(list(map(int , temp[:-1])))


row = len(a)
col = len(temp) - 1
bin = [[0 for _ in range(col)] for _ in range(row)]

def calc(r, c ,count=0):
    if not bin[r][c] and a[r][c] != 9:
        count += 1
        bin[r][c] = 1
        #for left
        if r-1>=0:
            count += calc(r-1,c) 
        #for right
        if r+1<=row-1:
            count += calc(r+1,c) 
        #for top
        if c-1>=0:
            count += calc(r,c-1) 
        #for bottom
        if c+1<=col-1:
            count += calc(r,c+1) 
    return count

if __name__ == "__main__":
    size = []
    for i in range(row):
        for j in range(col):
            if not bin[i][j]:
                result = calc(i,j)
                size.append(result)
    size.sort(reverse=True)
    print(size[0]*size[1]*size[2])
    