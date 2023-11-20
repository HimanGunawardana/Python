'''Write a python program to display sum of all the even numbers from 1 to 11'''

'''OutPut- 2+4+6+8+10=30'''


count=0
for x in range(1,11):
    if(x%2==0):
        count=count+x


print(count)
