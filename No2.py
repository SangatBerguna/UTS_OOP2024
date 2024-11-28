class Mahasiswa:
    def __init__(self, nama, nim, program_studi):
        self.nama = nama
        self.nim = nim
        self.program_studi = program_studi

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Program Studi: {self.program_studi}")

# Membuat objek Mahasiswa
mahasiswa = Mahasiswa("Giezka Prasetyo Wibowo", "202311004", "Informatika")
mahasiswa.tampilkan_info()
