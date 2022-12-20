def main():
    r=int(input("No of rows: "))
    flyod(r)
def flyod(r):
    i=1
    for j in range(r):
        for j in range(0,j+1):
            print(i,end=" ")
            i=i+1
        print()
main()