
# 12-11-2026 WORK
# STRING FORMATTING()
# MEANS INJECTING VARIABLES IN STRING
name='Saira'
age=20
print("My name is {:2} and my age is {}".format(name,age))
print("My name is {} and my age is {}".format('Jaziba',22))
print("My name is {0} and my age is {1}".format(name,age)) #can also give index number
print("My name is {1} and my age is {0}".format(name,age)) #can also change order

# no. or integer default space from left
# alphabets or string default space from right
# :^ -------------- center
# :> -------------- right
# :< -------------- left
print("Lets check it {a} out last time {b} because its weirdly interesting {c}".format(a=10, b='Farooq',c=9))
print("Lets check it {a:10} out last time {b:10} because its weirdly interesting {c:10}".format(a=10, b='Farooq',c=9)) #a space from left --b space from right and c space from left
print("Lets check it {a:^10} out last time {b:^10} because its weirdly interesting {c:^10}".format(a=10, b='Farooq',c=9)) #all space from center because of :^
print("Lets check it {a:<10} out last time {b:>10} because its weirdly interesting {c:<10}".format(a=10, b='Farooq',c=9))