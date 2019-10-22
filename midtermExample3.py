n =int(input('What is the value of n'))
for num in range(n):
    #the placement of the str() function determines whether
    #it will be a square or repition
    fun = lambda num: print(str(num)*num+('\n'))
    fun(num)

