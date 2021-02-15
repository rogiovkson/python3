def fact(n):
    step = 1
    for i in range(1, n + 1):
        step *= i
        yield step
n = int(input("Укажите факториал какого числа необходимо найти\n"))
for i in fact(n):
    print(i)