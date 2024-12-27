# Operasi Biner

a = 9 
b = 5

# Bitwise OR
print("====== Bitwise OR ======")
c = a | b
print("Nilai a:", a, "binary :", format(a, "08b"))
print("Nilai b:", b, "binary :", format(b, "08b"))
print("------------------------------- (|)")
print("Nilai c:", c, "binary :", format(c, "08b"))

# Bitwise AND
print("====== Bitwise AND ======")
c = a & b
print("Nilai a:", a, "binary :", format(a, "08b"))
print("Nilai b:", b, "binary :", format(b, "08b"))
print("------------------------------- (&)")
print("Nilai c:", c, "binary :", format(c, "08b"))

# Bitwise XOR
print("====== Bitwise XOR ======")    
c = a ^ b
print("Nilai a:", a, "binary :", format(a, "08b"))
print("Nilai b:", b, "binary :", format(b, "08b"))
print("------------------------------- (^)")
print("Nilai c:", c, "binary :", format(c, "08b"))

# Bitwise NOT
print("====== Bitwise NOT ======")    
c = ~a
print("Nilai a:", a, "binary :", format(a, "08b"))
print("------------------------------- (~)")
print("Nilai c:", c, "binary :", format(c, "08b"))

# Bitwise Left Shift
print("====== << ======")    
c = a << 2
print("Nilai a:", a, "binary :", format(a, "08b"))
print("------------------------------- (<<)")
print("Nilai c:", c, "binary :", format(c, "08b"))

# Bitwise Right Shift
print("====== >> ======")    
c = a >> 2
print("Nilai a:", a, "binary :", format(a, "08b"))
print("------------------------------- (>>)")
print("Nilai c:", c, "binary :", format(c, "08b"))