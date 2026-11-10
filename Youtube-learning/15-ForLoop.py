
# Range and FOR-LOOP CONCEPT
# LOOP USED FOR REPEATITION

# range(5) #5 parameter passed
# # start from 0
# # condition less than 5 means 4
# # increment by 1
#
# range(1,5) #5 parameter passed
# # start from 1
# # condition less than 5 means 4
# # increment by 1
#
# range(1,10,2) #5 parameter passed
# # start from 1
# # condition less than 10 means 9
# # increment by 2
#
# # Reverse
# range(10,0,-1)
# range(20,0,-2)
# # we always have to decrement value at the last parameter in reverse order

# EXAMPLE-1
for n in range(5):
    print(n)
# EXAMPLE-2
for n in range(1,20,2):
    print(n)
    # EXAMPLE-3
for n in range(1,11):
    print(4,'*',n,'=',n*4)
    # EXAMPLE-4
for n in range(11,0,-1):
    print(3,'*',n,'=',n*3)
    # EXAMPLE-5
for n in range(21,0,-3):
    print(n)