def fizz_Buzz(num):
    for i in range (0,num+1):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizz_Buzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)   

fizz_Buzz(20)