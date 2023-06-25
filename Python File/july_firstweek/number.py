number = int(input("Enter four digit number"))

a1 = number%10;
a1 = a1*1000;

number = number//10
a2 = number%100

number = number//10
a3 = number%10
a3 = a3 * 10

a4 = number//10
reverse = a1 + a2 + a3 + a4

print(reverse)




