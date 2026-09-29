# ============================================================
# KASUS 3 - MULTIPLE INHERITANCE
# Sistem Manajemen Pegawai
# ============================================================

class Pegawai:
    def __init__(self, id_pegawai, nama, gaji):
        self.id_pegawai = id_pegawai
        self.nama = nama
        self.gaji = gaji

    def informasi_pegawai(self):
        return f"ID: {self.id_pegawai}, Nama: {self.nama}, Gaji: Rp{self.gaji:,.0f}"


class PegawaiProyek:
    def __init__(self, nama_proyek):
        self.nama_proyek = nama_proyek

    def informasi_proyek(self):
        return f"Proyek: {self.nama_proyek}"


class ProjectManager(Pegawai, PegawaiProyek):
    def __init__(self, id_pegawai, nama, gaji, nama_proyek, jumlah_anggota):
        # Inisialisasi class Pegawai
        Pegawai.__init__(self, id_pegawai, nama, gaji)

        # Inisialisasi class PegawaiProyek
        PegawaiProyek.__init__(self, nama_proyek)

        self.jumlah_anggota = jumlah_anggota

    def tampilkan_data(self):
        print(f"ID Pegawai       : {self.id_pegawai}")
        print(f"Nama              : {self.nama}")
        print(f"Gaji              : Rp{self.gaji:,.0f}")
        print(f"Nama Proyek       : {self.nama_proyek}")
        print(f"Jumlah Anggota    : {self.jumlah_anggota}")
        print("-" * 40)


print("=" * 50)
print("KASUS 3 - SISTEM MANAJEMEN PEGAWAI")
print("=" * 50)

# 5 objek ProjectManager
pm1 = ProjectManager("PM001", "Fajar", 10000000, "Website Kampus", 8)
pm2 = ProjectManager("PM002", "Gina", 12000000, "Aplikasi Mobile", 6)
pm3 = ProjectManager("PM003", "Hendra", 11000000, "Sistem Akademik", 10)
pm4 = ProjectManager("PM004", "Intan", 13000000, "Digital Marketing", 7)
pm5 = ProjectManager("PM005", "Joko", 12500000, "E-Commerce", 9)

daftar_project_manager = [pm1, pm2, pm3, pm4, pm5]

for project_manager in daftar_project_manager:
    project_manager.tampilkan_data()


print("=" * 50)
print("SEMUA STUDI KASUS SELESAI")
print("=" * 50)
