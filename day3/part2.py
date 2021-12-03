from data import a

o2 = a.copy()
co2 = a.copy()

for i in range(12):
    if len(o2)>1:
        zeroes , ones = 0,0
        for element in o2:
            if int(element[i]):
                ones+= 1
            else:
                zeroes += 1
        temp_o2 = []
        for element in o2:
            if ones >= zeroes and  int(element[i]):
                temp_o2.append(element)
            elif zeroes > ones and not int(element[i]):
                temp_o2.append(element)
        o2 = [*temp_o2]

    if len(co2)>1:
        zeroes , ones = 0,0
        for element in co2:
            if int(element[i]):
                ones+= 1
            else:
                zeroes += 1
        temp_co2 = []
        for element in co2:
            if zeroes > ones and  int(element[i]):
                temp_co2.append(element)
            elif ones >= zeroes and not int(element[i]):
                temp_co2.append(element)
        co2 = [*temp_co2]

print(int(*o2 , 2)* int(*co2,2))