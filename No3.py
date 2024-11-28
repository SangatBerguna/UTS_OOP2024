class Laptop:
    def __init__(self, merk, ram, processor):
        self.merk = merk
        self.ram = ram
        self.processor = processor

    def __del__(self):
        print(f"Laptop {self.merk} telah dihapus dari memori.")

# Membuat objek Laptop
laptop = Laptop("ASUS", 16, "Intel i7")
print(f"Laptop: {laptop.merk}, RAM: {laptop.ram}GB, Processor: {laptop.processor}")
del laptop
