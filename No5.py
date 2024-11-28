class Hewan:
    def suara(self):
        print("Hewan membuat suara.")

class Kucing(Hewan):
    def suara(self):
        print("Meow")

class Anjing(Hewan):
    def suara(self):
        print("Woof")

# Membuat objek dan memanggil metode suara
hewan = Hewan()
kucing = Kucing()
anjing = Anjing()

hewan.suara()
kucing.suara()
anjing.suara()
