# ============================================================
# STUDI KASUS OOP PYTHON
# Minimal 5 objek pada setiap tugas
# ============================================================


# ============================================================
# KASUS 1 - CLASS & OBJECT
# Sistem Pendataan Mahasiswa
# ============================================================

class Mahasiswa:
    def __init__(self, nama, nim, jurusan, nilai):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.nilai = nilai

    def cek_kelulusan(self):
        if self.nilai >= 75:
            return "LULUS"
        return "TIDAK LULUS"

    def tampilkan_data(self):
        print(f"Nama     : {self.nama}")
        print(f"NIM      : {self.nim}")
        print(f"Jurusan  : {self.jurusan}")
        print(f"Nilai    : {self.nilai}")
        print(f"Status   : {self.cek_kelulusan()}")
        print("-" * 40)


print("=" * 50)
print("KASUS 1 - SISTEM PENDATAAN MAHASISWA")
print("=" * 50)

# 5 objek Mahasiswa
mhs1 = Mahasiswa("Muhammad Irsyad Ibrahim", "2595114020", "Informatika", 85)
mhs2 = Mahasiswa("Budi", "2301002", "Sistem Informasi", 72)
mhs3 = Mahasiswa("Citra", "2301003", "Teknik Komputer", 90)
mhs4 = Mahasiswa("Dinda", "2301004", "Informatika", 76)
mhs5 = Mahasiswa("Eko", "2301005", "Sistem Informasi", 68)

daftar_mahasiswa = [mhs1, mhs2, mhs3, mhs4, mhs5]

for mahasiswa in daftar_mahasiswa:
    mahasiswa.tampilkan_data()





