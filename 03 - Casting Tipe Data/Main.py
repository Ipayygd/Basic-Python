# Casting : Merubah tipe data dari satu tipe ke tipe lain.
# Contoh : int, float, str, bool

# Integer
print("=============== Integer ==================")
data_integer = 9
print(data_integer, " adalah tipe : ", type(data_integer))

data_float = float(data_integer)
data_string = str(data_integer)
data_boolean = bool(data_integer) # akan false jika data_integer = 0

print(data_float, " adalah tipe : ", type(data_float))
print(data_string, " adalah tipe : ", type(data_string))
print(data_boolean, " adalah tipe : ", type(data_boolean))

# Float
print("=============== Float ==================")
data_float = 9.8
print(data_float, " adalah tipe : ", type(data_float))

data_integer = int(data_float) # akan dibulatkan ke bawah
data_string = str(data_float)
data_boolean = bool(data_float) # akan false jika data_float = 0

print(data_integer, " adalah tipe : ", type(data_integer))
print(data_string, " adalah tipe : ", type(data_string))
print(data_boolean, " adalah tipe : ", type(data_boolean))

# String
print("=============== String ==================")
data_string = "9"
print(data_string, " adalah tipe : ", type(data_string))

data_integer = int(data_string) # string harus berupa angka
data_float = float(data_string) # string harus berupa angka
data_boolean = bool(data_string) # akan false jika data_string = ""

print(data_integer, " adalah tipe : ", type(data_integer))
print(data_float, " adalah tipe : ", type(data_float))
print(data_boolean, " adalah tipe : ", type(data_boolean))

# Boolean
print("=============== Boolean ==================")
data_boolean = True
print(data_boolean, " adalah tipe : ", type(data_boolean))

data_integer = int(data_boolean) # akan false jika data_boolean = False
data_float = float(data_boolean) # akan false jika data_boolean = False
data_string = str(data_boolean) # akan false jika data_boolean = False

print(data_integer, " adalah tipe : ", type(data_integer))
print(data_float, " adalah tipe : ", type(data_float))
print(data_string, " adalah tipe : ", type(data_string)) 