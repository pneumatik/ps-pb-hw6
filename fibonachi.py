fib1 = 1
fib2 = 1
fib_odd = 0
fib_sum = 0
i = 0

while fib_sum + fib1 <= 10000000:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1
    #print('fib2: '+str(fib2))
    if fib2%2 == 0:
        fib_odd += fib2
        print(fib_odd)

print('количество элементов в последовательности: ' +str(i + 2))
print('cумма четных элементов: ' + str(fib_odd))
print('предпоследнее число последовательности: ' + str(fib1))

