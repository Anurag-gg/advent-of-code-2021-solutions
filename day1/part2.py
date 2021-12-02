from data import a

count = 0
prev = a[0] + a[1] + a[2]
for i in range(1, len(a) - 2):
    number = prev - a[i-1] + a[i+2]
    if number > prev:
        count += 1
    prev = number
    
print(count)
    
