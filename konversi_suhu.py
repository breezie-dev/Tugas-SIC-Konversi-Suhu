from fungsi_konvers import (C_from_F, K_from_F, F_from_C, K_from_C, C_from_K, F_from_K)

garis = "-"*4
print(f"{garis} KONVERSI SUHU {garis}")
print()

nilai = float(input("Masukkan nilai suhu yang akan dikonversi: "))
satuan_awal = input("Masukkan satuan suhu (C/F/K): ").upper()
satuan_tujuan = input("Masukkan satuan tujuan (C/F/K): ").upper()
print()

if satuan_awal == "C" and satuan_tujuan == "F":
    hasil = F_from_C(nilai)
    print(f"{nilai}°C = {hasil:.2f}°F")
elif satuan_awal == "C" and satuan_tujuan == "K":
    hasil = K_from_C(nilai)
    print(f"{nilai}°C = {hasil:.2f}K")
elif satuan_awal == "F" and satuan_tujuan == "C":
    hasil = C_from_F(nilai)
    print(f"{nilai}°F = {hasil:.2f}°C")
elif satuan_awal == "F" and satuan_tujuan == "K":
    hasil = K_from_F(nilai)
    print(f"{nilai}°F = {hasil:.2f}K")
elif satuan_awal == "K" and satuan_tujuan == "C":
    hasil = C_from_K(nilai)
    print(f"{nilai}K = {hasil:.2f}°C")
elif satuan_awal == "K" and satuan_tujuan == "F":
    hasil = F_from_K(nilai)
    print(f"{nilai}K = {hasil:.2f}°F")
else:
    print("Satuan tidak valid. Silakan masukkan C, F, atau K.")
