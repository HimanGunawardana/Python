#using list slicing method
value = [1,4,5,6,2,9]
print(value[::-1])
print(value)

#using reverse() function
value = [1,4,5,6,2,9]
value.reverse()
print(value)
print("==========Append,Extend,Insert==========================")

#adding items using append() function
value = [1,4,5,6,2,9]
value.append([17,45])
print(value)   #only one element adding [17,45] =>1


#adding items using extend() function
value = [1,4,5,6,2,9]
value.extend([17,45])
print(value)   #two elements adding 17,45  => 2 elements



#adding items using insert() function
value = [1,4,5,6,2,9]
value.insert(2,50)
print(value)  #by adding 2nd index,add to 50

print("===========Del,Pop=========================")

#deleting
value = [1,4,5,6,2,9]
del value[2]
print(value)

#pop
value = [1,4,5,6,2,9]
value.pop()
print(value)

value = [1,4,5,6,2,9]
poppeditem = value.pop(2)
print(poppeditem)
