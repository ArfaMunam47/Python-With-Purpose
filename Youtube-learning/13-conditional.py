
# 10-11-2026 WORK
# CONDITIONAL STATEMENTS
#  --IF   ---ELIF ---ELSE
# PYTHON DON'T ACCEPT IRRELEVANT SPACE
# ------------------ IF
a=100
if a%2==0:
    print('A is even number')

# ----------------- ELSE
a=int(input('Enter a number : '))
if a%2==0:
    print('A is even number')
else:
    print('A is prime number')

    # ------------- ELIF
marks=int(input('Enter your marks : '))
if marks >=80:
    print('You got 1st division')
elif marks >=50:
    print('You got 2nd division')
elif marks >=30:
    print('You got passed')
else:
    print('You got failed')