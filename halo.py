import datetime

# 1. Sapaan Nama
nama = input("Masukkan nama Anda: ")
print(f"Halo, {nama}! Selamat datang di praktikum Python.")

# 2. Tugas Mandiri (Tahun Lahir & Penanganan Error)
try:
    tahun_lahir_input = input("Masukkan tahun lahir Anda: ")
    tahun_lahir = int(tahun_lahir_input)
    tahun_sekarang = datetime.datetime.now().year

    if tahun_lahir > tahun_sekarang or tahun_lahir < 1900:
        print("Tahun lahir tidak valid!")
    else:
        usia = tahun_sekarang - tahun_lahir
        print(f"Perkiraan usia Anda adalah {usia} tahun.")
except ValueError:
    print("Error: Harap masukkan angka yang valid untuk tahun lahir!")