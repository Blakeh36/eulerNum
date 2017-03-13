# e is approximated using sum(1/n!)
def factorial(x):   # this function carries out the factorial
    i = x - 1
    while i > 0: #i needs to match x so that it can count down and be multiplied each time
        x = x * i
        i -= 1
    return x
j = 1.0 #j is how many times the series will be run. In the future I would like to instead ask the user how accurate they want it to be
e  = 1.0

limit = int(input("Please enter upper limit(eg. 1000)"))
print("calculating. . .")
while j < limit: # reminder that it's still calculating
    e = e + 1.0/factorial(j)
    if j % 2000 == 0:
        print("still calculating. . .")
    j += 1
print(e) #prints Euler's number
eReal = 2.7182818284590452
print("e actually equals %s" %eReal)
percError = 100 * (eReal - e)/e
if percError < 0: # for some reason at higher upper limits the error will be less than one. to counter this I multiplied it by -1
    percError *= -1
print("the percent error is %s" %percError)
