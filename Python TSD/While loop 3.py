number = int(input("Enter  any Number"))
reverseNum=0
while(number > 0):
    remain = number%10
    reverseNum = (reverseNum*10)+remain
    number //=10

print("Reverse Number: ",reverseNum)
