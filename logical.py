
# LOGICAL OPERATORS
#  AND (all cases true then true)  OR (if any case is true then true)
#  NOT (reverse result)

a=20
b=30
print(a==20 and b!=20) #true
print(a!=20 or b!=20) #true
print( not a==20 and b!=20) #false
print(not a==20) #false

if(a==20 or b!=30):
    print('this is false condition')
else:
        print('this is true condition')
