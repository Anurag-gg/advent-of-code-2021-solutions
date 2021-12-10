score = {')':3,']':57,'}':1197,'>':25137}
match = {'}':'{',']':'[',')':'(','>':'<'}
result = 0

with open("day10/data.txt", "r") as data:
    for x in data:
        stack = []
        for ele in x:
            if ele in match.values():
                stack.append(ele)
            elif ele in match.keys():
                popped = stack.pop()
                if match[ele] != popped:
                    result += score[ele]

print(result)