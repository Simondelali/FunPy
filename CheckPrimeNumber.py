num = int(input('Enter a number: '))
#prime umbers are greater than 1
if num > 1:
    for i in range(2,num):
        if(num % i) == 0:
            print(num, 'is not a prime number')
            print(i,'times', num//i, 'is', num )
            break
 
    else:
        print(num, "is a prime number") 
#if number is less than or equal to 1,
#it is not a prime number
else:
    print(num, 'is not a prime number')