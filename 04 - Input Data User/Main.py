# Mengambil Input Data dari User

# Input data akan dalam bentuk string
nama = input("Masukan Nama : ") 
print("Nama : ", nama, ", tipe data : ", type(nama))

# Input data akan dalam bentuk integer (Casting)
umur = int(input("Masukan umur : "))
print("Umur : ", umur, ", tipe data : ", type(umur))

# Input data akan dalam bentuk float (Casting)
tinggi = float(input("Masukan tinggi : "))
print("Tinggi : ", tinggi, ", tipe data : ", type(tinggi))

# Input data akan dalam bentuk boolean (Casting)
menikah = bool(int(input("Menikah (0/1): ")))
print("Menikah : ", menikah, ", tipe data : ", type(menikah))