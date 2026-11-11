
# NEW STRING FUNCTIONS
# FIND() INDEX() ISALPHA() ISDIGIT() ISALNUM()

# IN FIND() WE CAN GIVE STARTING AND ENDING VALUE BUT IT DOESN'T RESET INDEX AND IF NOT FOUND ANY LETER IT RETURN -1
w='HELLO WORLD HOW ARE YOU GUYS!'
print(w.find('O',11))

# index() when letter not found it give us error otherwise it work similarly like find()
print(w.index('O',11))

# isalpha()
# gave us true or false and gave true when all letters are alphabets
q='amndfnadjkgbnkjag'
print(q.isalpha())

# isdigit()
# gave us true or false and gave true when all letters are numbers
q='123423587249856'
print(q.isdigit())

# isalpha()
# gave us true or false and gave true when letter or alphabets but should not contain special character
# and it should  not contain space too because space is also special character
q='amndfnadjkgbn jag'
print(q.isalnum())
