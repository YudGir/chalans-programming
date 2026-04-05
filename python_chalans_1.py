banyak_input_user = int(input("Berapa angka Anda ingin masukkan? "))

angka_user = []
jumlah_angka_genap = 0
jumlah_angka_ganjil = 0
total_angka_genap = 0
total_angka_ganjil = 0
i = 0

for i in range (banyak_input_user):
    angka = int(input("Masukkan angka: "))
    angka_user.append(angka)

for angka in angka_user:
    if angka % 2 == 0:
        total_angka_genap += 1
        jumlah_angka_genap += angka
    else:
        total_angka_ganjil += 1
        jumlah_angka_ganjil += angka

print("Jumlah angka genap Anda adalah:", jumlah_angka_genap)
print("Banyak angka genap Anda adalah:", total_angka_genap)
print("Jumlah angka ganjil Anda adalah:",jumlah_angka_ganjil)
print("Banyak angka ganjil Anda adalah:", total_angka_ganjil)


angka_user = []
angka = 1
while True:
    if angka != -1:
        angka = int(input("Masukkan angka: "))
        angka_user.append(angka)
        i += 1
    else:
        angka_user.remove(angka) #ini ada biar angka -1 yg terakhir tidak dimasukkan ke list (atau di c++: array) angka_user
        break

banyak_muncul = 0
modus = 0

for angka in angka_user:
    jumlah = angka_user.count(angka)
    
    if jumlah > banyak_muncul:
        banyak_muncul = jumlah
        modus = angka
print(f"Angka yang paling banyak muncul (modus): {modus}")

print(f"Banyak angka: {angka_user.count(angka)}")
print(f"Banyak angka Anda adalah: {len(angka_user)}")
print(f"Angka terbesar (max)-nya adalah: {max(angka_user)}")
print(f"Angka terkecil (min)-nya adalah: {min(angka_user)}")
print(f"Angka rata-rata (average)-nya adalah: {int(sum(angka_user)/len(angka_user))}")
# aku buat nilai averagenya jadi int, bukan float biar enak

