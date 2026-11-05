
# 5-11-2026 work
# DATATYPES    1-MUTABLE 2- IMMUTABLE
# MUTABLE -- LIST , ARRAY, DICTIONARY
# IMMUTABLE --STRING, NUMBER, TUPLE, SET
# 1- NUMBER(INTEGER,FLOAT,COMPLEX NO.)
# 2- STRING
# 3- LIST , TUPLE , DICTIONARY , SET

# -------- numbers
a=10
print(a,type(a))
b=10.23
print(b,type(b))
c=1+3j
print(c,type(c))

# ----------- string
name='Arfa Munam'
print(name,'is type of', type(name))

multi=""" Hey there
    M just checking multi
    line strings which 
    need triple quotes"""
print(multi)

# list  (mutable ----can change)
l=[1,3,'world',1+3j]
l[0]=33
l[2]='arfa'
print(l,type(l))

# tuple --- like list but immutable and fase and use parenthesis and should contain more than one items
t=(1,2,'arfa')
print(t,type(t))
t=(2) # single item cannot be a tuple
print(type(t))

# ------- dictionary  (key and values) mutable
d={
    'name':'arfa munam',
   'age':20,
    'semester':'5th'
}
print(d['name'])
d['name']='iram mughal'
print(d,type(d))

# ---------- set  (should contain unique values) remove repeating values by itself
my_set={1,2,3,3} # 3 will be shown one time only
print(my_set,type(my_set))
# () parenthesis   {} braces  [] square brackets