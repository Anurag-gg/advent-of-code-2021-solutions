paths = 0
a = []
with open("day12/data.txt", "r") as data:
    for x in data:
        e1 , e2 = x.split('-')
        a.append((e1,e2[:-1]))

def calc(current, visited):
    if 'end' in current:
        global paths
        paths += 1
        return
    for ele in a:
        if ele[0] == current[-1] or ele[1] == current[-1]:
            temp = list(ele)
            temp.remove(current[-1])
            if ((len(set(visited)) == len(visited) or len(set(visited))+ 1 == len(visited)) and temp[0]!="start" and 'end' not in visited) or temp[0].isupper():
                if temp[0].islower():
                    calc([*current ,temp[0]] , [*visited , temp[0]])
                else:
                    calc([*current ,temp[0]] , visited)

calc(['start'] , ['start'])
print(paths)



