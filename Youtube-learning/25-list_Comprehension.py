
# STRING COMPREHENSION
# ELEGANT AND FAST WAY FOR CREATING LIST
l=[]
l.append('Arfa')
l.append(33)
l.append('Tayba')
print(l)
# we use APPEND FOR adding elements in list

l=[]
for a in range(1,101,2):
    l.append(a)
print(l)

# another efficient and one line code for this
l=[]
a=[m for m in range(1,30,2)]
print(a)

l=[]
t=[m for m in range(0,40) if m%2==0 ]
print(t)