import math


#Mode calculator
def Mode_calculator(ipls):
    Mode = 0
    totalls = []
    loopcnt = 0
    while (loopcnt < len(ipls)):
        element = int(ipls[loopcnt])
        if (element in totalls):
            totalls[(totalls.index(element) + 1)] += 1
        else:
            totalls.append(element)
            ecount = 1
            totalls.append(ecount)
        #print(totalls)
        loopcnt += 1
    #Find highest
    loopcnt = 1
    High_ecount = 0
    while (loopcnt < len(totalls)):
        check_dig = totalls[loopcnt]
        if (check_dig > High_ecount):
            High_ecount = check_dig
        loopcnt += 2
    #print("High_ecount: " , High_ecount)
    Mode = totalls[(totalls.index(High_ecount) - 1)]
    print("The mode is " , Mode)

#Median calculator
def Median_calculator(ipls):
    Median = 0
    if (len(ipls) % 2 == 1):
        Median = ipls[math.floor(len(ipls) / 2)]
    else:
        Median = ((int(ipls[int(len(ipls) / 2)])) + ((int(ipls[int(len(ipls) / 2)]) - 1))) / 2
    print("The median is " , Median)

#Mean calculator
def Mean_calculator(ipls):
    Mean = 0
    loopcnt = 0
    total = 0
    while(loopcnt < len(ipls)):
        total += int(ipls[loopcnt]) 
        loopcnt += 1
    Mean = total / (len(ipls))
    print("The mean is " , Mean)


ipls = []
print("Enter the numbers in the set. Enter '' when complete")
ip = str(input("1 . "))
ipls.append(ip)
loopcnt = 2
while (ip != ""):
    print(loopcnt , "." , end = "\r")
    ip = str(input(""))
    ipls.append(ip)
    loopcnt += 1
ipls.remove ("")
Mean_calculator(ipls)
Median_calculator(ipls)
Mode_calculator(ipls)


















