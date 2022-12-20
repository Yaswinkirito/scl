def main():
    a = input("Do want to use recursive function or not:(y/n) ")
    i = int(input("N: "))
    if (a.lower()) == "y":
        print(myfunction(i))
    else:
        print(not_function(i))


def myfunction(i):  # With recursive function
    if i == 1:
        return 1
    elif i == 0:
        return 0
    else:
        return i * (myfunction(i - 1))


def not_function(i):  # without recursive function
    f = 1
    if i == 0:
        return 0
    for a in range(1, i + 1):
        f = f * a
    return f


main()
