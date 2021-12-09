answer = 0

def calc(arr):
    temp = dict()
    for e in arr:
        if len(e) == 2:
            temp[1] = set(e)
        elif len(e) == 3:
            temp[7] = set(e)
        elif len(e) == 4:
            temp[4] = set(e)
        elif len(e) == 7:
            temp[8] = set(e)
    for e in arr: 
        if len(e) == 6:
            if temp[1] - set(e):
                temp[6] = set(e)
            elif not temp[4] - set(e):
                temp[9] = set(e)
            else:
                temp[0] = set(e)
    for e in arr:
        if len(e) == 5:
            if not temp[1] - set(e):
                temp[3] = set(e)
            elif not set(e) - temp[9]:
                temp[5] = set(e)
            else:
                temp[2] = set(e)
                
    return temp

with open("day8/data.txt","r") as data:
    for x in data:
        unit = ''
        test , output = x.split("|")
        result = calc(test.split())  
        for e in output.split():
            for key , value in result.items():
                if value == set(e):
                    unit += str(key)
                    break  
        answer += int(unit)

print(answer)