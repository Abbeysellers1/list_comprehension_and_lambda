def testfunc(num):
    return lambda x: x*num


result10= testfunc(10)
result100= testfunc(100)

#result10= lambda x, num: x*num

print(result100(9))

numbers_list = [2,6,8,10,11,4,12,7,13,17,0,3,21]

filtered_list= list(filter( lambda num: (num >7), numbers_list))
print(filtered_list)


mapped_list=list(map(lambda num: num %2, numbers_list))
print(mapped_list)