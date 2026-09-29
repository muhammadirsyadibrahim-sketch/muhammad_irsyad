# ============================================================
# KASUS 2 - INHERITANCE
# Sistem Rental Kendaraan
# ============================================================

class Kendaraan:
    def __init__(self, nama, merk, tahun, kecepatan):
        self.nama = nama
        self.merk = merk
        self.tahun = tahun
        self.kecepatan = kecepatan

    def informasi(self):
        return (
            f"Nama: {self.nama}, Merk: {self.merk}, "
            f"Tahun: {self.tahun}, Kecepatan: {self.kecepatan} km/jam"
        )


class Mobil(Kendaraan):
    def __init__(self, nama, merk, tahun, kecepatan, jumlah_kursi):
        super().__init__(nama, merk, tahun, kecepatan)
        self.jumlah_kursi = jumlah_kursi

    # Method overriding
    def informasi(self):
        return (
            f"[MOBIL] {self.nama} | Merk: {self.merk} | "
            f"Tahun: {self.tahun} | Kecepatan: {self.kecepatan} km/jam | "
            f"Kursi: {self.jumlah_kursi}"
        )


class Motor(Kendaraan):
    def __init__(self, nama, merk, tahun, kecepatan, tipe_motor):
        super().__init__(nama, merk, tahun, kecepatan)
        self.tipe_motor = tipe_motor

    # Method overriding
    def informasi(self):
        return (
            f"[MOTOR] {self.nama} | Merk: {self.merk} | "
            f"Tahun: {self.tahun} | Kecepatan: {self.kecepatan} km/jam | "
            f"Tipe: {self.tipe_motor}"
        )


print("=" * 50)
print("KASUS 2 - SISTEM RENTAL KENDARAAN")
print("=" * 50)

# Minimal 5 objek kendaraan
kendaraan1 = Mobil("Avanza", "Toyota", 2022, 180, 7)
kendaraan2 = Mobil("Xpander", "Mitsubishi", 2023, 190, 7)
kendaraan3 = Mobil("Civic", "Honda", 2021, 220, 5)
kendaraan4 = Motor("NMAX", "Yamaha", 2023, 150, "Matic")
kendaraan5 = Motor("CBR 150R", "Honda", 2022, 170, "Sport")

daftar_kendaraan = [
    kendaraan1,
    kendaraan2,
    kendaraan3,
    kendaraan4,
    kendaraan5
]

for kendaraan in daftar_kendaraan:
    print(kendaraan.informasi())

print()