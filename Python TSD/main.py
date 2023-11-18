
workHours = int(input("Enter the number of working hours: "))
normalHors = 9
normalPay = 1000
extraPay = 200

if(workHours>normalHors):
    extraHours = workHours - normalHors
    otPay = extraHours*extraPay
else:
    otPay = 0

finalPay = normalPay + otPay

print(finalPay)
