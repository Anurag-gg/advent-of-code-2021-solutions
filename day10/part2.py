score = {'(':1,'[':2,'{':3,'<':4}
match = {'}':'{',']':'[',')':'(','>':'<'}
result = []

with open("day10/data.txt", "r") as data:
    for x in data:
        stack = []
        flag = True
        for ele in x:
            temp = 0
            if ele in match.values():
                stack.append(ele)
            elif ele in match.keys():
                popped = stack.pop()
                if match[ele] != popped:
                    flag = False
                    break
        if flag:
            for _ in range(len(stack)):
                temp = temp*5 + score[stack.pop()]
            result.append(temp)

result.sort()
print(result[len(result)//2])