''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''
from numpy import minimum


numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter_numbers= list(filter(lambda num: (num), numbers))
print(filter_numbers)

filtered_evens =list(filter(lambda num: ((num%2)==0), numbers))
print(filtered_evens)

filtered_odd = list(filter(lambda num: ((num%2)!=0), numbers))
print(filtered_odd)
print()




''' 2)
find which days of the week have exactly 6 characters.
'''

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

filter_weekdays= list(filter(lambda day: (len(day)==6), weekdays))
print(filter_weekdays)
print()







''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

'''
colors =['orange', 'red', 'green', 'blue', 'white', 'black']

halloween = list(filter(lambda color: (color!= 'orange' and color != 'black'), colors))
print(halloween)
print()





''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''

list1= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2= [2, 4, 6, 8]
removed_elements = list(filter(lambda x: x not in list2, list1))
print(removed_elements)
print()





''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

'''
colorlist=['red', 'black', 'white', 'green', 'orange']
find_ack=[x for x in colorlist if 'ack' in str(x)]
print(find_ack)
find_abc=[x for x in colorlist if 'abc' in str(x)]
print(find_abc)
print()



''' 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''

str1 = "Hello8world"
check=[lambda str1: any(x.isupper() for x in str1) or 'String must have at least 1 upper case character.',
lambda str1: any(x.islower() for x in str1) or 'String must have at least 1 lower case character.',
lambda str1: any(x.isdigit() for x in str1) or 'String must have at least 1 number.',
lambda str1: len(str1) >= 8]
verify = [x for x in [v(str1) for v in check] if x != True]
if not verify:
    verify.append('This password works')
print('Problems with the password: ')
print(verify)
print()



str1 = "HELLO"
check=[lambda str1: any(x.isupper() for x in str1) or 'String must have at least 1 upper case character.',
lambda str1: any(x.islower() for x in str1) or 'String must have at least 1 lower case character.',
lambda str1: any(x.isdigit() for x in str1) or 'String must have at least 1 number.',
lambda str1: len(str1) >= 8]
verify = [x for x in [v(str1) for v in check] if x != True]
if not verify:
    verify.append('This password works')
print('Problems with the password: ')
print(verify)
print()


str1= "hello"
check=[lambda str1: any(x.isupper() for x in str1) or 'String must have at least 1 upper case character.',
lambda str1: any(x.islower() for x in str1) or 'String must have at least 1 lower case character.',
lambda str1: any(x.isdigit() for x in str1) or 'String must have at least 1 number.',
lambda str1: len(str1) >= 8]
verify = [x for x in [v(str1) for v in check] if x != True]
if not verify:
    verify.append('This password works')
print('Problems with the password: ')
print(verify)
print()






''' 7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
original_scores.sort(key = lambda x: x[1])
print(original_scores)
