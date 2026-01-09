#class process
class PengunjungProcess:
    def validasi_nama(self, nama):
        if nama.strip() == "":
            raise ValueError("Nama tidak boleh kosong")

    def validasi_umur(self, umur):
        if not umur.isdigit():
            raise ValueError("Umur harus berupa angka")
        umur = int(umur)
        if umur <= 0:
            raise ValueError("Umur tidak valid")
        return umur

    def validasi_jenis_kelamin(self, jk):
        if jk.lower() not in ["laki-laki", "perempuan"]:
            raise ValueError("Jenis kelamin harus Laki-laki atau Perempuan")

    def validasi_tujuan(self, tujuan):
        if tujuan.strip() == "":
            raise ValueError("Tujuan tidak boleh kosong")
