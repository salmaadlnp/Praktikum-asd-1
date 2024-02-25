class Skincare:
    def __init__(self, id, nama, jenis, harga, stok):
        self.id = id
        self.nama = nama
        self.jenis = jenis
        self.harga = harga
        self.stok = stok

class TokoSkincare:
    def __init__(self):
        self.skincare_list = []

    def tambah_skincare(self, skincare):
        self.skincare_list.append(skincare)
        print("Skincare '{}' telah ditambahkan.".format(skincare.nama))

    def tampilkan_skincare(self):
        if self.skincare_list:
            print("Daftar Skincare:")
            for skincare in self.skincare_list:
                print("ID:", skincare.id)
                print("Nama:", skincare.nama)
                print("Jenis:", skincare.jenis)
                print("Harga:", skincare.harga)
                print("Stok:", skincare.stok)
                print("-----------------------")
        else:
            print("Tidak ada skincare tersedia.")

    def update_skincare(self, id, field, value):
        for skincare in self.skincare_list:
            if skincare.id == id:
                if hasattr(skincare, field):
                    setattr(skincare, field, value)
                    print("Skincare dengan ID {} berhasil diperbarui.".format(id))
                    return
                else:
                    print("Field tidak valid.")
                    return
        print("Skincare dengan ID {} tidak ditemukan.".format(id))

    def hapus_skincare(self, id):
        for skincare in self.skincare_list:
            if skincare.id == id:
                self.skincare_list.remove(skincare)
                print("Skincare dengan ID {} telah dihapus.".format(id))
                return
        print("Skincare dengan ID {} tidak ditemukan.".format(id))

if __name__ == "__main__":
    toko = TokoSkincare()

    # Menambahkan beberapa skincare
    skincare1 = Skincare(1, "Cleanser", "Cleanser", 50000, 10)
    skincare2 = Skincare(2, "Moisturizer", "Moisturizer", 155000, 15)
    skincare3 = Skincare(3, "Serum", "Serum", 200000, 8)
    skincare4 = Skincare(4, "Sunscreen", "Sunscreen", 100000, 20)
    skincare5 = Skincare(5, "Lip balm", "Lip balm", 20000, 5)
    skincare6 = Skincare(6, " Eye Serum", " Eye Serum", 200000, 5)
    

    toko.tambah_skincare(skincare1)
    toko.tambah_skincare(skincare2)
    toko.tambah_skincare(skincare3)
    toko.tambah_skincare(skincare4)
    toko.tambah_skincare(skincare5)
    toko.tambah_skincare(skincare6)




    # Menampilkan daftar skincare
    toko.tampilkan_skincare()

    # Mengupdate harga skincare dengan ID 1
    toko.update_skincare(1, "harga", 120000)

    # Menampilkan daftar skincare setelah pembaharuan
    toko.tampilkan_skincare()

    # Menghapus skincare dengan ID 2
    toko.hapus_skincare(2)

    # Menampilkan daftar skincare setelah penghapusan
    toko.tampilkan_skincare()
