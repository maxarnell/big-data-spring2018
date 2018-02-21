# here goes nothing.

x = "Curling is the sport of royalty"

# A.1
l_one =["The Winter Olympics are arguably more bizarre than the Summer edition", "However, one thing is clear to all:", x, "Decathalon is cool too."]
# A.2 print the 3rd item
print(l_one[2])
# A.3 print the 1st and 2nd items using index slicing
print(l_one[0:2])

#A.4 add a new string with the text "last" and print the list
l_one.append("last")
print(l_one)
#A.5
l_onel = len(l_one)
print(l_onel)

#A.6 list replacement
l_one[4] = "new"

print(l_one)

# Strings
#B.1
sentence_words = ['I', 'am', 'learning', 'Python', 'to', 'munge', 'large', 'datasets', 'and', 'visualize', 'them']
spa_sentence_words = ' '.join(sentence_words)
print(spa_sentence_words)
#B.2
sentence_words.reverse()
sentence_words
#B.3
list.sort(sentence_words)
sentence_words
#B.4
sorted(sentence_words)
"""
The biggest difference between the sorted() function and the .sort function
is that sorted() returns a new list whereas .sort modifies the original list.
Another major difference is that sorted() will work on many data types, including floats and ints.
.sort only works on lists.
"""
#B.5
# taken from Matthais Eisen

sort_sentence_words = sorted(sentence_words, key=lambda x: x.lower())
print(sort_sentence_words)
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

from random import randint
#this returns a random integer between 100 and 1000
num = randint(100, 1000)
#C
#Assistance from Saritha
def userints(up, low):
    up = int(input("Enter the upper bound"))
    type(up)
    low = int(input("Enter the lower bound. No entry means a lower bound of 0"))
    if low == []:
        low = 0
    num_gen = randint(low, up)
    print(num_gen)

#assert tests the function by checking to see if it is true

assert(0 <= userints(100) <= 100)
assert(50 <= userints(100, low = 50) <=100)

userints(up, low)



#D String Formatting function

def books(book_title, n):
    book_title = str(input("Enter the title of the book."))
    n = int(input("Enter the position on the bestseller list."))
    tbook_title = book_title.title()
    print(f"{tbook_title} is currently number {n} on the bestsellers list.")

books(tbook_title, n)

# E Password Validation function
#Assistance from Kavya

def password(pw):
    pw = str(input("Please enter a secure password."))
    err_mess = "That password does not match our security criteria. Please try again."
    s = 1
    #length Checks
    if len(pw) >= 15 or len(pw) <= 7:
        s = s*0
    #digit checks
    pw_count = ( pw.count("0") + pw.count("1") + pw.count("2") + pw.count("3") + pw.count("4") + pw.count("5") + pw.count("6") + pw.count("7") + pw.count("8") + pw.count('9'))
    if pw_count <= 1:
        s = s*0
    #special character checks
    char_count = ( pw.count("!") + pw.count("?") + pw.count("@") + pw.count("#") + pw.count("$") + pw.count("%") + pw.count("^") + pw.count("&") + pw.count("*") + pw.count("(") + pw.count(")") + pw.count("-") + pw.count("_") + pw.count("+") + pw.count('='))
    if char_count < 1:
        s = s*0
    #capital check
    low_bool = pw.islower()
    if low_bool == True:
        s = s*0
    if s == 0:
        print(err_mess)
    else:
        print(f"{pw} is a secure password.")

password(pw)



#F Exponentiation Function
def exp(v, w):
    z = v
    for x in range(0, w-1):
        z = z*v
    print(z)

exp(2, 4)

exp(3, 2)

exp(5, 4)
