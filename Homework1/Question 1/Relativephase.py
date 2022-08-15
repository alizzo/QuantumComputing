import numpy as np
qubit1 = 12         #1.)    an integer variable named qubit1 and assign it a value of 12
boo = False         # 2.)    a boolean variable named boo and assign it a value of FALSE
Bell = "Collapse to 1" #this is a piece of text
BellPair = "I also collapse to 1" # 4.)  a string called BellPair and assign it a value of “I also collapse to 1”
my_list = [ Bell, qubit1, BellPair, boo ] # 5.)    Define a list called my_list containing...
print(my_list[2]) # 6.)   Print the second string from the list you just created
my_list.append(137) # 7.)   Add the number 137 to the end of the list
#print(my_list)
for i in my_list:     # 8.)  Print the final list in order
    print(i)
print(my_list[4]-np.cos(0))    #9.)  Calculate and print out the difference between the last item on the list and the cosine of zero 



a = np.array([[ 5, 1 ,3], [ 1, 1 ,1], [ 1, 2 ,1]])
b = np.array([1, 2, 3])
print a.dot(b)
