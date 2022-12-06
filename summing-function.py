def mysum(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

print(mysum(1,12, 25, 7))
# 45
print(mysum(*[10, 32]))
# 42
print(mysum(*{8, 14, 19, 59, 101}))
# 201
