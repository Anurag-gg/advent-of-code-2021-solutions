import math
with open("day7/data.txt","r") as data:
    for x in data:
        a = list(map(int ,str(x).split(",")))


def helper(num):
    return sum([i for i in range(num+1)])


avg = sum(a)//len(a)
print(sum([helper(abs(e-avg)) for e in a]))


