# Tipe Data : Angka Bulat (integer).
data_integer = 100

# Tipe Data : Angka Desimal (float), angka dengan koma.
data_float = 1.5

# Tipe Data : Kumpulan karakter (string), abcdefghi1234.
data_string = "Luca Claudia 15"

# Tipe Data : Biner (boolean) True/False , True = 1, False = 0.
data_boolean = True

print("Data Integer : ", data_integer)
print("Data Float : ", data_float)
print("Data String : ", data_string)
print("Data Boolean : ", data_boolean)

################# Tipe Data Khusus

# Bilangan kompleks
data_complex = complex(5, 6)

# Tipe Data dari bahasa C
from ctypes import c_double

data_c_double = c_double(10.5)

print("Data Complex : ", data_complex)
print("Data C Double : ", data_c_double)