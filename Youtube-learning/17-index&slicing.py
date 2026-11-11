
# 11-11-2026 WORK
# INDEXING AND SLICING CONCEPTS IN PYTHON
# STRING IS SPECIAL SEQUENCE OF CHARACTERS

# Indexing start from 0 in order left to right and space is also considered
# Indexing start from -1 in order right to left and space is also considered

#  STRING INDEXING
n="Welcome to Arfa's learning channel"
print(n)
print(type(n))
print(n[0])
print(n[8])
print(n[-2])
print(n[-5])

# STRING SLICING
# WHEN WE WANNA TAKE MULTIPLE CHARACTERS THEN WE DO SLICING
# IN SLICING WE USE COLONS AND WE GAVE STARTING POINT, RANGE AND INCREMENT AND IN REVERSE ORDER WE HAVE TO GIVE DECREMENT VALUE
print(n[0:6])
print(n[0:9])
print(n[0::3])
print(n[0:12:2]) # MEANS INCREMENT BY 2
# PYTHON ADD 1 BY DEFAULT OKAY

print(n[-1:-4:-1])
print(n[-1:-14:-3])
print(n[-1::-3])
