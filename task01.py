import math

filepath = 'C:/Python/files/file.txt'
with open(filepath) as fp:
    line = fp.readline()
    sum = 0
    while line: 
        mass = int(line.strip())
        fuel_required = math.floor((mass/3)) - 2
        line = fp.readline()
        sum += fuel_required
    print(sum)

    
