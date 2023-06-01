memmbuat kelas mahasiswa yang memiliki tiga atribut: nama, nim, dan jurusan
class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def tampilkan_info(self):
        print("Nama    : ", self.nama)
        print("NIM     : ", self.nim)
        print("Jurusan : ", self.jurusan.NamaJurusan)

membuat kelas jurusan yang memiliki atribut : self, nama_jurusan
class Jurusan:
    def __init__(self, nama_jurusan):
        self.NamaJurusan = nama_jurusan
        self.DaftarMahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.DaftarMahasiswa.append(mahasiswa)

    def tampilkan_daftar_mahasiswa(self):
        print("=====Daftar Mahasiswa di Jurusan", self.NamaJurusan + "=====")
        for mahasiswa in self.DaftarMahasiswa:
            mahasiswa.tampilkan_info()


# Membuat kelas universitas untuk menampilkan nama universitas dan jurusan
class Universitas:
    def __init__(self, nama_universitas):
        self.NamaUniversitas = nama_universitas
        self.DaftarJurusan = []

    def tambah_jurusan(self, jurusan):
        self.DaftarJurusan.append(jurusan)

    def tampilkan_daftar_jurusan(self):
        print("Daftar Jurusan di Universitas ", self.NamaUniversitas)
        for jurusan in self.DaftarJurusan:
            print(jurusan.NamaJurusan)
            

untuk mendapatkan luaran yang diinginkan
# Poin 2 bjek Universitas dengan nama "XYZ University"
universitas_xyz = Universitas("XYZ University")

# Poin 3 objek Jurusan dengan nama dan tambahkan objek tersebut ke dalam Universitas XYZ
jurusan_informatika = Jurusan("Teknik Informatika")
universitas_xyz.tambah_jurusan(jurusan_informatika)

# Poin 4 objek Mahasiswa 
mahasiswa = Mahasiswa("Resyaliana Esa Putri", "G1A022038", jurusan_informatika)
jurusan_informatika.tambah_mahasiswa(mahasiswa)

# Poin 5 Tampilkan daftar jurusan
universitas_xyz.tampilkan_daftar_jurusan()

# Poin 6 Tampilkan daftar mahasiswa
jurusan_informatika.tampilkan_daftar_mahasiswa()
