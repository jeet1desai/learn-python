# Condition: ==, !=, >, <, <=, >=
val = 10

print(type(val))

try:
    if val > 0:
        print("Greater then 0")
    elif val < 0:
        print("Less then 0")
    else:
        print("It is 0")
except ValueError:
    print("Something went wrong")






