def calc(fuel_sum):
    sum = 0

    while fuel_sum > 5:
        fuel_sum = fuel_sum // 3 - 2
        print(fuel_sum)
        sum += fuel_sum
    return sum 

fuel_sum = sum(map(lambda x:calc(int(x)), open('./file.txt').readlines()))
# fuel_sum = 100756

print(fuel_sum)

    

