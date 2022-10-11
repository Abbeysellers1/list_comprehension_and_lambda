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

new_list=[x for x in old_list] #you don't have to have an if statement
print(new_list)

x = [i for i in range(10)]
print(x)

squares = [i**2 for i in range(10)]
print(squares)

list1=[3,4,5,]
multiplied=[item *3 for item in list1]
print(multiplied)

listOfWords = ['this', 'is', 'a', 'list', 'of', 'words']
items=[ i[0] for i in listOfWords]
print(items)


list1 = ['A','B','C']
list2=[ x.lower() for x in list1]
print(list2)
list3=[x.upper() for x in list2]
print(list3)

#adding conditions

#create a new list of the square of even nubmers from 0 to 4

new_range= [i*i for i in range(5) if i % 2 == 0]
print(new_range)

#we want to extract the numbers only from the phrase below
string= 'Hello 12345 World'
numbers = [x for x in string if x.isdigit()]
print(numbers)
letters = [x for x in string if x.isalpha()]
print(letters)

#using a file to find
myfile = open('test.txt', 'r')
result = [i.rstript('\n') for i in myfile if 'line3' in i]
print(result)


#using funtions
def double(x):
    return x*2

print(double(10))

mynumbers= [double(x) for x in range(10) if x % 2 ==0]
print(mynumbers)

#more than one list and argument

result = [x + y for x in [10,20,30] for y in [20,40,60]]
print(result)