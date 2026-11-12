
# List concept in python
l=[10,20,30,'Arfa',[1,2,3,4,5]]
print(l)

# indexing in list
print(l[2])
print(l[4])
# list type
print(type(l))

# slicing in list
print(l[1:4])
print(l[0::2])
print(l[-1:4:-1])
# for getting reverse string
print(l[-1::-1])
print(l[-1::-2])
# for getting nested string
t=len(l)
print(t) #5 because nested string also take one index
print(l[4])
print(l[4][2])
print(l[4][2])
print(l[4][0])

# REMEMBER STRING IS MUTABLE WE CAN CHANGE ITS VALUES

e=[1,20,30]
e[0]='Arfa'
print(e)
# very simple concept