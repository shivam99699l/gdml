def armstrong(num):
    order=len(str(num))
    copy_num = num 
    sum =0
    while num >0:
        digit=num %10
        sum += digit ** order
        num = num //10
    if copy_num == sum:
        print(1)
    else:
        print(0)
armstrong(370)