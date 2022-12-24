def fun(no,k):
    for j in range(no,27+k,9):
        if j>27:
            j=j-27
            yield j
        else:
            yield j


def Print1():
    item=input("Enter the starting Item to distribute :")
    no=int(item[1:])
    k=no
    no-=1
    for i in range(1,10):
        no+=1
        P=fun(no,k)
        print("T"+str(i),end=" ")
        for j in P:
            print("N"+str(j),end=" ")
        print()


def main():
    print("The list of items :")
    for i in range(1,28):
        print("N"+str(i),end=" ")

    print("The list of Clients :")
    for i in range(1,10):
        print("T"+str(i),end=" ")
    print()
    Print1()
main()