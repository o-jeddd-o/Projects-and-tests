user_age = input("How old are you?: ")
a = user_age
b = int(a)
if b < 18:
    print("Your ticket costs $2")
elif b >= 18:
    print("Your tcket costs $10")
elif b > 60:
    print("Your ticket costs $5")
else:
    print("Your ticket costs $10")
