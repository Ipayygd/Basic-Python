# Operasi Logika (not, or, and, xor)

# Logika NOT = Kebalikan, true menjadi false
print("====== Not ======")
a = True
b = not a
print(a, "not = ", b)

# Logika OR = atau, salah satu true maka true
print("====== Or ======")
a = True
b = False
c = a or b
print(a, "or", b, "=", c)

# Logika AND = dan, kedua true maka true, jika salah satu false maka false
print("====== And ======")
a = True
b = False
c = a and b
print(a, "and", b, "=", c)

# Logika XOR = atau, salah satu true maka true, jika kedua true maka false
print("====== Xor ======")
a = True
b = False
c = a ^ b
print(a, "xor", b, "=", c)