def factorial(x):
    i = x
    while i <= x and i > 1:
        x = x * (i-1)
        i -= 1
    return x
j = 1
e  = 1
while j < 1000:
    e = e + 1.0/factorial(float(j))
    j += 1
print(e)
