result = [2,4,3,7]
count = 0
with open("day8/data.txt","r") as data:
    for x in data:
        test , output = x.split("|")
        for e in output.split():
            if len(e) in result:
                count += 1
print(count)