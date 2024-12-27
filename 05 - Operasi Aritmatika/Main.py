# Operasi Aritmatika
a = 10
b = 3

# Penjumlahan (+)
hasil = a + b
print(a, "+", b, "=", hasil)

# Pengurangan (-)
hasil = a - b
print(a, "-", b, "=", hasil)

# Perkalian (*) 
hasil = a * b
print(a, "*", b, "=", hasil)

# Pembagian (/), akan memiliki hasil float
hasil = a / b
print(a, "/", b, "=", hasil)

# Eksponen (**), Perpangkatan
hasil = a ** b
print(a, "^", b, "=", hasil)

# Modulus (%), Sisa bagi
hasil = a % b
print(a, "%", b, "=", hasil)

# Floor Division (//), Kebalikan dari modulus atau pembulatan ke bawah
hasil = a // b
print(a, "//", b, "=", hasil)

# Prioritas Operasi
# 1. ()
# 2. **
# 3. * , / , // , %
# 4. + , -
x = 3
y= 2
z = 4

hasil = x ** y * (z + x) / y - y % z // x
print(x, "**", y, "*", z, "+", x, "/", y, "-", y, "%", z, "//", x, "=", hasil)