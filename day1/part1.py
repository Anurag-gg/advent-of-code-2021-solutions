from data import a

count = 0
for i in range(1 , len(a)):
    if a[i] > a[i-1]:
        count += 1
print(count)

