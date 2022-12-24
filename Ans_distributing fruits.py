def seatingArrangement():
    for i in range(2):
        for j in range(i+1,21,2):
            print("G"+str(j),end=" ")
        print()
        if i==1:
            i=2
        for k in range(1+i,3+i):
            for p in range(k,41,4):
                print("B"+str(p),end=" ")
            print()
       
def allocatedToGirls():
    AforG=0
    MforG=0
    OforG=0
    A=0
    M=0
    O=0
    for i in range(30):
        if A<100:
            AforG+=2
            A+=2
        if M<95:
            MforG+=2
            M+=2
        if O<90: 
            OforG+=2
            O+=2
        for j in range(2):
            if A<100:
                A+=2
            if M<95:
                M+=2
            if O<90:
                O+=2
    print()   
    print("Quantity of apples, mangoes and oranges are allocated to girls.")
    print("Apple = ",AforG)
    print("Mangoes = ",MforG)
    print("Oranges = ",OforG)
    print("Total fruits = ",AforG+MforG+OforG)

def damagedFruits():
    total=100+95+90
    damagedPerc=14.3
    damagedFruits=(total*14.3)/100
    if isinstance(damagedFruits,float):
        damagedFruits=int(damagedFruits)+1
    avrg=damagedFruits/3
    if isinstance((avrg),float):
        damagedB=int(avrg*2)+1
        damagedG=int(avrg)
    else:
        damagedB=avrg*2
        damagedG=avrg
    print()
    print("Quantity of damaged fruits allocated to total boys and total girls, respectively.")
    print("Damaged fruits allocated to total boys = ",damagedB)
    print("Damaged fruits allocated to total girls = ",damagedG)

def main():
    seatingArrangement()
    allocatedToGirls()
    damagedFruits()

main()