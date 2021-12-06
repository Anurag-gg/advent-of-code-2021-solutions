#day    0 1 2 3 4 5 6 7 8
fish = [0,0,0,0,0,0,0,0,0]

with open("day6/data.txt","r") as data:
    for x in data:
        a = list(map(int , x.replace(",","")))

for e in a:
    fish[e] += 1

for i in range(256):
    fish = fish[1],fish[2],fish[3],fish[4],fish[5],fish[6],fish[7]+fish[0],fish[8],fish[0]

print(sum(fish))