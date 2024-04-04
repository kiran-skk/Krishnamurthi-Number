def factorial(n):
    fact = 1
    if n == 0:
        fact =1
    else:
        fact = 1
        for i in range(1,n+1):
            fact = fact*i
    return(fact)
def krish():
    n = int(input("Enter a number: "))
    string = str(n)
    krish = 0
    for i in string:
        single = int(i)
        krish = krish + factorial(single)
    if krish == n:
        print("Yippie its a Krishnamurti Number")
    else:
        print("Not a Krishnamurti Number")
    return krish
krish()
