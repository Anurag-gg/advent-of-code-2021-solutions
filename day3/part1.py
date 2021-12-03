from data import a

gamma ,epsilon = '',''
for i in range(11,-1,-1):
    ones , zeroes = 0,0
    for element in a:
        if int(element[i]):
            ones+= 1
        else:
            zeroes+=1
    if ones>zeroes:
        gamma = "1" + gamma
        epsilon = "0" + epsilon
    else:
        gamma = "0" + gamma
        epsilon = "1" + epsilon
print(int(gamma , 2)* int(epsilon,2))
