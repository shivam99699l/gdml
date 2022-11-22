def check_Prime(num):
    if num < 2:
        print(0)
    else:
        for i in range (2,num):
            if num % i == 0:
                print(0)
                break
        else:
            print(1)

check_Prime(4)
