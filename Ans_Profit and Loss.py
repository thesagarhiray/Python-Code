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

def Data():
    cp=int(input("Enter the cost price of item : "))
    sp=int(input("Enter the selling price item: "))
    discA=int(input("Enter the Discount for Client A : "))
    discB=int(input("Enter the Discount for Client B : "))
    discC=int(input("Enter the Discount for Client C : "))
    discD=int(input("Enter the Discount for Client D : "))
    print()
    # for client A
    profit1=9*(sp-cp)
    if profit1>0:
        prt="Profit"
    else:
        prt="Loss"
    invamt=9*cp+profit1
    print("Client A :   Invoiced amount = ",invamt,",", prt," = ",profit1)
    print()
     # for client B
    profit1=3*(sp-cp)
    if profit1>0:
        prt="Profit"
    else:
        prt="Loss"
    invamt=3*cp+profit1
    print("Client B :   Invoiced amount = ",invamt,",",prt," = ",profit1)
    print()
     # for client C
    profit1=9*(sp-cp)
    if profit1>0:
        prt="Profit"
    else:
        prt="Loss"
    invamt=9*cp+profit1
    print("Client C :   Invoiced amount = ",invamt,",",prt," = ",profit1)
    print()
     # for client A
    profit1=6*(sp-cp)
    if profit1>0:
        prt="Profit"
    else:
        prt="Loss"
    invamt=6*cp+profit1
    print("Client D :   Invoiced amount = ",invamt,",",prt," = ",profit1)
    

    discA=(9*sp*discA)/100
    spA=9*sp-discA
    profitA=spA-9*cp              # profit from Client A

    discB=(3*sp*discB)/100
    spB=3*sp-discB
    profitB=spB-3*cp              # profit from Client B

    discC=(9*sp*discC)/100
    spC=9*sp-discC
    profitC=spC-9*cp              # profit from Client C

    discD=(6*sp*discD)/100
    spD=6*sp-discD
    profitD=spD-6*cp              # profit from Client D
    
    print()
    T=profitA+profitB+profitC+profitD
    if T>0:
        print("==> consolidated Profit <==")
    else:
        print("==> consolidated Loss <==")

def main():
    print("The list of items :")
    for i in range(1,28):
        print("N"+str(i),end=" ")

    print("The list of Clients :")
    for i in range(1,10):
        print("T"+str(i),end=" ")
    print()
    Print1()
    Data()
main()