n1 = 0
n2 = 1
sum=0
def fibonacci(num):

    for i in range(0,num):
        
        print(sum, end="")
        n1 = n2
        n2 = n1+n2
        sum = n2

fibonacci(10)