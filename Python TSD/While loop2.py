count=0
number = int(input("Enter  any Number"))

while(number != 0):
    number //= 10
    count+=1

print("The number of digits: ",count)
