#class view
class PengunjungView:
    def input_data(self):
        nama = input("Masukkan nama: ")
        umur = input("Masukkan umur: ")
        jenis_kelamin = input("Masukkan jenis kelamin (L/P): ")
        tujuan = input("Masukkan tujuan: ")
        return nama, umur, jenis_kelamin, tujuan

    def tampilkan_tabel(self, daftar_pengunjung):
        print("\nData Pengunjung")
        print("-" * 70)
        print(f"{'Nama':<20}{'Umur':<10}{'Jenis Kelamin':<20}{'Tujuan':<20}")

        for p in daftar_pengunjung:
            jk_full = "Laki-laki" if p.jenis_kelamin.upper() == "L" else "Perempuan"
            print(f"{p.nama:<20}{p.umur:<10}{jk_full:<20}{p.tujuan:<20}")

        print("-" * 70)