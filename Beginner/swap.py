a = 10
b = 20
print("a = ", a)
print("b = ", b)
# By using a temporary variable
temp = a
a = b
b = temp
print("Swap 1, using temp")
print("a = ", a)
print("b = ", b)

# By adding and subtracting
print("Swap 2, using + and -")
a = a + b
b = a - b
a = a - b
print("a = ", a)
print("b = ", b)

# By using bitwise XOR operator
print("Swap 3, using ^")
a = a ^ b
b = a ^ b
a = a ^ b

print("a = ", a)
print("b = ", b)

# By multiplying and dividing
print("Swap , using * and /")

a = a * b
b = int(a / b)
a = int(a / b)
print("a = ", a)
print("b = ", b)

