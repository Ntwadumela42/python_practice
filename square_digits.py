def square_digits(num):
    
    num = str(num)
    res = ''
    
    for i in range(len(num)):
        res += str(int(num[i])**2)

    num = int(res)   
    return num
