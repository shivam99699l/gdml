def factorial(num):
    fact =1
    while num > 0:
        fact *=num
        num -=1
    print("factorial of this numbe is ->",fact)

factorial(5)