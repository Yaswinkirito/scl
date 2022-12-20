def main():
    n = int(input("Rows: "))
    pyramid(n)
def pyramid(i):
    k=i
    for r in range(i):
        print(" "*k,end="")
        print("* "*(r+1),end="")
        print()
        k=k-1
main()