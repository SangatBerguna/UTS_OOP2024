class AkunBank:
    def __init__(self, nomor_rekening, saldo):
        self.nomor_rekening = nomor_rekening
        self.__saldo = saldo

    def set_saldo(self, saldo_baru):
        self.__saldo = saldo_baru

    def get_saldo(self):
        return self.__saldo

    def tambah_saldo(self, jumlah):
        self.__saldo += jumlah

    def tarik_saldo(self, jumlah):
        if jumlah <= self.__saldo:
            self.__saldo -= jumlah
        else:
            print("Saldo tidak mencukupi.")

# Membuat objek AkunBank
akun = AkunBank("1234567890", 1000000)
akun.tambah_saldo(500000)
print("Saldo saat ini:", akun.get_saldo())
akun.tarik_saldo(300000)
print("Saldo setelah penarikan:", akun.get_saldo())
