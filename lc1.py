old_list=[10,20,30,40,50]
new_list=[]


#old way
for x in old_list:
    if x > 20:
        x += 20
        new_list.append(x)


print(new_list)

#using list comprehension
new_list= [x+20 for x in old_list if x > 20]
print(new_list)

