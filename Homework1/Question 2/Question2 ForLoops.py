
''' 1)	Print a list of all j values from 1 to 64.
Note that you’ll have to modify the given code,
which starts at j=0 by default.
This result is an example of a linear progression of values. '''
#j = 1
#for anumber in range(0,64,1):      # linear progression  # range(start, stop, step) function
#    print(j)
#    j += 1
    

''' 2)	Print a list of 64 values,
starting with j=1 and doubling the value of j for each successive iteration '''

#for j in range(1,64+1,1):     # double     
#    print(j*2)



'''3)	Print a list of 64 values, starting with j=1 and squaring the value of j for each successive iteration.
This result is an example of a quadratic progression of values. '''
    
#for j in range(1,64+1,1):         # quadratic progression
#    print(j*j)


''' 4)	Print a list of 64 values, starting with j=1 and raising 2 to the power j for each successive iteration.
Note that the Python code for A raised to the N power is A**N.  This result is an example of an exponential progression of values. '''
#i = 1
#for j in range(1,64+1,1):      # exponential progression
#    i = 2 ** j
#    print(i)

'''5)	Compare the last value on each of the above four lists. 
How many times larger is the 64th value of the exponential progression than the quadratic progression? 
How many times large is the 64th value of the exponential progression than the linear progression?     '''


LastExponentialProgression = 18446744073709551616
LastQuadraticProgression = 4096
LastDoublingProgression = 128
LastLinearProgression = 64

ExponentialMultipleofQuadratic = LastExponentialProgression / LastQuadraticProgression
ExponentialMultipleofLinear = (LastExponentialProgression / LastLinearProgression)

print("The 64th value of the exponential progression is " + str(ExponentialMultipleofQuadratic) + " times greater than the quadratic progression" )
print("The 64th value of the exponential progression is " + str(ExponentialMultipleofLinear) + " times greater than the linear progression" )
