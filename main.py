# Superclass
class Makanan:
    def __init__(self, nama):
        self.nama = nama

    def cara_makan(self):
        return f"{self.nama} dimakan seperti biasa."

# Subclass Nasi (Inheritance & Overriding)
class Nasi(Makanan):
    def cara_makan(self):
        return f"{self.nama} dimakan pakai sendok."

# Subclass Gorengan (Inheritance & Overriding)
class Gorengan(Makanan):
    def cara_makan(self):
        return f"{self.nama} dimakan pakai tangan."

# Uji polimorfisme
daftar_makanan = [Nasi("Nasi Goreng"), Gorengan("Bakwan"), Makanan("Roti")]

for m in daftar_makanan:
    print(m.cara_makan())