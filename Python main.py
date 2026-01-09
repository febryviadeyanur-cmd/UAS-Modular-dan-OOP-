# program utama
from Pengunjung import Pengunjung
from PengunjungProcess import PengunjungProcess
from PengunjungView import PengunjungView

daftar_pengunjung = []
process = PengunjungProcess()
view = PengunjungView()

while True:
    try:
        nama_input, umur_input, jk_input, tujuan_input = view.input_data()

        process.validasi_nama(nama_input)
        umur_valid = process.validasi_umur(umur_input)
        process.validasi_jenis_kelamin(jk_input)
        process.validasi_tujuan(tujuan_input)

        pengunjung_data = Pengunjung(nama_input, umur_valid, jk_input, tujuan_input)
        daftar_pengunjung.append(pengunjung_data)

        # tanya lanjut
        lanjut_input = input("Tambah pengunjung lagi? (l/p): ")
        if lanjut_input.lower() != "l":
            break

    except ValueError as e:
        print("Error:", e)


view.tampilkan_tabel(daftar_pengunjung)
