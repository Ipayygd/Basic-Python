# Latihan Konversi Satuan Temperatur (Celcius, Fahrenheit, Reamur, Kelvin)

# ================= Konversi Celcius =================
print("======= Konversi Celcius ========")
celcius = float(input("Masukan Nilai Celcius : "))
fahrenheit = (celcius * 1.8) + 32
reamur = celcius * 0.8
kelvin = celcius + 273.15

print("Suhu = ", celcius, "Celcius")
print("Suhu dalam Fahrenheit = ", fahrenheit)
print("Suhu dalam Reamur = ", reamur)
print("Suhu dalam Kelvin = ", kelvin)

# ================= Konversi Fahrenheit =================
print("======= Konversi Fahrenheit ========")
fahrenheit = float(input("Masukan Nilai Fahrenheit : "))
celcius = (fahrenheit - 32) / 1.8
reamur = (fahrenheit - 32) / 2.0
kelvin = (fahrenheit - 32) / 1.8 + 273.15

print("Suhu = ", fahrenheit, "Fahrenheit")
print("Suhu dalam Celcius = ", celcius)
print("Suhu dalam Reamur = ", reamur)
print("Suhu dalam Kelvin = ", kelvin)

# ================= Konversi Reamur =================
print("======= Konversi Reamur ========")       
reamur = float(input("Masukan Nilai Reamur : "))
celcius = reamur * 0.8
fahrenheit = reamur * 2.0 + 32
kelvin = reamur + 273.15

print("Suhu = ", reamur, "Reamur")
print("Suhu dalam Celcius = ", celcius)
print("Suhu dalam Fahrenheit = ", fahrenheit)
print("Suhu dalam Kelvin = ", kelvin)

# ================= Konversi Kelvin =================
print("======= Konversi Kelvin ========")
kelvin = float(input("Masukan Nilai Kelvin : "))
celcius = kelvin - 273.15
fahrenheit = (kelvin - 273.15) * 1.8 + 32
reamur = kelvin - 273.15

print("Suhu = ", kelvin, "Kelvin")
print("Suhu dalam Celcius = ", celcius)
print("Suhu dalam Fahrenheit = ", fahrenheit)
print("Suhu dalam Reamur = ", reamur)