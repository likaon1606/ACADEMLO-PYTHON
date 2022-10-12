# Dado el siguiente string valida si estan balanceados o no "[[[[][]]]]" [][]][

a ="[[[[][]]]]"
b ="[][]]["
c = "]["

bracket = c
check = 0

for i in bracket:
    if i == "[":
        check += 1
    elif i == "]":
        check -= 1
    
    if check < 0:
        break
print(check==0)