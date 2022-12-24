taskToSenior,taskToJunior,taskToFresher=0,0,0

SHIssue,JMIssue,FLIssue=0,0,0

SHEnhmt,JMEnhmt,FLEnhmt=0,0,0 

# Tasks to Senior, Junior, Fresher
for i in range(1,327):
    if i%3==1:
        if i<=70 or i%3==1:
            SHIssue+=1
    if i%3==2:
        if 70<i<=300 or i%3==2:
            JMIssue+=1
    if i%3==0:
        if 300<i<=326 or i%3==0: 
            FLIssue+=1

for i in range(1,75):
    if i<=20:
        SHEnhmt+=1
    if 20<i<=45:
        if i<=44 or 20<i<=45:
            JMEnhmt+=1
    if 45<i<=74:
        if 44<i<=47 or 45<i<=74:
            FLEnhmt+=1
taskToSenior=SHIssue+SHEnhmt
taskToJunior=JMIssue+JMEnhmt
taskToFresher=FLIssue+FLEnhmt
print("The number of tasks assigned to Seniors, Juniors and Freshers.")
print("The number of tasks assigned to Seniors = ",taskToSenior)
print("The number of tasks assigned to Juniors = ",taskToJunior)
print("The number of tasks assigned to Freshers = ",taskToFresher)

# Task to Each
a1,a2,a3=0,0,0
for i in range(1,taskToSenior+1):
    if i%3==1:
        a1+=1
        i+=1
    elif i%3==2:
        a2+=1
        i+=1
    elif i%3==0:
        a3+=1
        i+=1
b1,b2,b3=0,0,0
for i in range(1,taskToJunior+1):
    if i%3==1:
        b1+=1
        i+=1
    elif i%3==2:
        b2+=1
        i+=1
    elif i%3==0:
        b3+=1
        i+=1
c1,c2,c3=0,0,0
for i in range(1,taskToFresher+1):
    if i%3==1:
        c1+=1
        i+=1
    elif i%3==2:
        c2+=1
        i+=1
    elif i%3==0:
        c3+=1
        i+=1
print()
print("The number of tasks assigned to each individual.")
print(" TM1-Senior  = ",a1)
print(" TM2-Senior  = ",a2)
print(" TM3-Senior  = ",a3)
print(" TM4-Junior  = ",b1)
print(" TM5-Fresher = ",b2)
print(" TM6-Junior  = ",b3)
print(" TM7-Fresher = ",c1)
print(" TM8-Fresher = ",c2)
print(" TM9-Junior  = ",c3)

# Bill of the Project
totalBillAmtS=taskToSenior*5*8*100
totalBillAmtJ=taskToJunior*3*1.5*8*50
totalBillAmtF=taskToFresher*1*2*8*15
totalBilling=totalBillAmtS+totalBillAmtJ+totalBillAmtF
print()
print("Total Billing amount = ",totalBilling)

# Total Hours
totalDays=int(taskToSenior*5+taskToJunior*3*1.5+taskToFresher*1*2)      # no of days
leavs=0
k=0
TD=totalDays
for i in range(1,totalDays+1):
    if k<=TD:
        if i%23==0:
            k+=1.5
            leavs+=1.5
totalDays=totalDays-leavs
totalHours=totalDays*8
bufferHours=(totalHours*15)/100
totalHours=totalHours+bufferHours
print()
print("Total time required to complete the project = ",totalHours,"Hrs.")