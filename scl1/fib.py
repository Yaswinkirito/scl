def main():
    a = int(input("N: "))
    if a <= 0:
        print("Input a valid number")
        main()
    for i in range(0, a, 1):
        print(fib(i))


def fib(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fib(i - 1) + fib(i - 2)


main()
