#Class Notes
# how to write an iterator
# Python thinks in objects

fun_list = ['are','we','having','fun','yet']
fun_list.sort()
print(fun_list)
#in-place method takes object and changes it

#branching - accomplished with if/else statements

flag = True
if flag:
        x = 1
        print('Flag is true.')
else:
        x = 2
        print('Flag is false')
print(x)

#iteration

x = range(10)
x = [0,1,2,3,4,5,6,7,8,9]

for i in x:
    print(i*3)

turtle = range(10)
print(turtle)

tutle_list = ['This','is','python']
for i in tutle_list:
    print(i)
    print(tutle_list.index(i))


#how to iterate over a list containing values

x = 0
for i in range(100):
    x = x + i
print(x)

def for_sum(x, y):
    for i in range(y):
        x += i
    return x

 for_sum(0, 200)

 #vectorization
 #lets you add together lists more easily

import numpy as np
