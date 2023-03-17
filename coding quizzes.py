# coding quiz 2
a = {'red', 'yellow', 'orange', 'green'}
b = {'red', 'orange', 'black'}
x = set(a)
y = set(b)
print(x|y)

# Coding quiz 3
user_age = input("How old are you?: ")
a = int(user_age)
if a < 18:
    print("Your ticket costs $2")
elif a >= 18:
    print("Your tcket costs $10")
elif a > 60:
    print("Your ticket costs $5")
else:
    print("Your ticket costs $10")
