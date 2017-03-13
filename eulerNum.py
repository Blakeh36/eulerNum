# e is approximated using sum(1/n!)
def factorial(x):   # this function carries out the factorial
    i = x
    while i <= x and i > 1: #i needs to match x so that it can count down and be multiplied each time
        x = x * (i-1)
        i -= 1
    return x
j = 1 #j is how many times the series will be run. In the future I would like to instead ask the user how accurate they want it to be
e  = 1.0
while j < 1000:
    e = e + 1.0/factorial(float(j))
    j += 1
print(e) #prints Euler's number
