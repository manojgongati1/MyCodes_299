for n in range(1,101):
    c=""
    if n%3==0:
        c +="Fizz"
    if n%5==0:
        c +="Buzz"
    print(c or n)
