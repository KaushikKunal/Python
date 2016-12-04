import math, time

ip = int(input("Enter a number: "))
iplen = len(list(str(ip)))
sqrtlen = math.ceil(iplen / 2)
basesqrt = 10 ** (sqrtlen - 1)
dec_places = 0.0000000001
bestsqrt = 0
while (basesqrt >= dec_places):
    bestsqr = 0
    maybesqr = 0
    maybesqrt = bestsqrt
    increment = basesqrt
    for c in range (0, 10):
        maybesqr = maybesqrt ** 2
        if ((abs(ip - maybesqr) < abs(ip - bestsqr)) and (maybesqr <= ip)):
            bestsqr = maybesqr
            bestsqrt = maybesqrt
        #print(maybesqrt)
        maybesqrt += increment
    basesqrt = basesqrt / 10
bestsqrt = round(bestsqrt, 10)
opsqrtls = list(str(bestsqrt))
print("The square root is " , end = "\r")
for loopcnt in range(0, len(opsqrtls)):
    print(opsqrtls[loopcnt] , end = "\r")
    time.sleep(0.05)
