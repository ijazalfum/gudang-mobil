class Node:
    def __init__(self, mobil):
        self.mobil = mobil
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def tambah_mobil(self, mobil):
        new_node = Node(mobil)
        new_node.next = self.head
        self.head = new_node

    def hapus_mobil(self, nama_mobil):
        elemen_saat_ini = self.head
        elemen_sebelumnya = None
        while elemen_saat_ini:
            if elemen_saat_ini.mobil.nama_mobil.lower() == nama_mobil.lower():
                if elemen_sebelumnya:
                    elemen_sebelumnya.next = elemen_saat_ini.next
                else:
                    self.head = elemen_saat_ini.next
                return elemen_saat_ini.mobil
            elemen_sebelumnya = elemen_saat_ini
            elemen_saat_ini = elemen_saat_ini.next
        return None

    def tampilkan_mobil(self):
        sekarang = self.head
        if not sekarang:
            print("Tidak ada data mobil.")
        while sekarang:
            print(f"Nama mobil  : {sekarang.mobil.nama_mobil}")
            print(f"Merek       : {sekarang.mobil.merek}")
            print(f"Tipe        : {sekarang.mobil.tipe}")
            print(f"Tahun       : {sekarang.mobil.tahun}")
            print(f"Harga       : {sekarang.mobil.harga}")
            print()
            sekarang = sekarang.next

class Stack:
    def __init__(self):
        self.top = None

    def tambah_transaksi(self, mobil):
        new_node = Node(mobil)
        new_node.next = self.top
        self.top = new_node

    def hapus_transaksi(self):
        if self.top is None:
            return None
        transaksi = self.top
        self.top = self.top.next
        return transaksi.mobil

    def is_kosong(self):
        return self.top is None

    def lihat_transaksi(self):
        sekarang = self.top
        if not sekarang:
            print("Tidak ada transaksi.")
        while sekarang:
            print(sekarang.mobil) 
            sekarang = sekarang.next

class Mobil:
    def __init__(self, nama_mobil, merek, tipe, tahun, harga):
        self.nama_mobil = nama_mobil
        self.merek = merek
        self.tipe = tipe
        self.tahun = tahun
        self.harga = harga

    def __str__(self):
        return f"Mobil {self.nama_mobil}, Merek: {self.merek}, Harga: {self.harga}"

class TreeNode:
    def __init__(self, name, data=None):
        self.name = name
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children = self.children + [child]  

    def display(self, level=0):
        print("  " * level + f"- {self.name}")
        for child in self.children:
            child.display(level + 1)


def build_tree(mobil):
    root = TreeNode("daftar merek mobil")

    categories = {"Toyota": TreeNode("Toyota"),
                  "Honda": TreeNode("Honda"),
                  "Suzuki": TreeNode("Suzuki")}

    for car in mobil:
        if car.merek in categories:
            categories[car.merek].add_child(TreeNode(car.nama_mobil, car))

    for category_node in categories.values():
        root.add_child(category_node)

    return root

def display_tree():
    tree = build_tree(daftar_mobil)
    print("\nStruktur tree mobil:")
    tree.display()

daftar_mobil = [
    Mobil("Agya", "Toyota", "Hatchback", 2022, 170000000),
    Mobil("Yaris", "Toyota", "Hatchback", 2022, 250000000),
    Mobil("Fortuner", "Toyota", "SUV", 2023, 700000000),
    Mobil("Civic", "Honda", "Sedan", 2021, 800000000),
    Mobil("Ertiga", "Suzuki", "MPV", 2019, 255000000),
    Mobil("Jimny", "Suzuki", "SUV", 2023, 400000000),
]

linked_list_mobil = SingleLinkedList()
for mobil in daftar_mobil:
    linked_list_mobil.tambah_mobil(mobil)

stack_transaksi = Stack()

def sort_mobil(arr):
    for n in range(len(arr) - 1, 0, -1):
        swapped = False
        for i in range(n):
            if arr[i].harga > arr[i + 1].harga:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break

def urutkan_mobil_berdasarkan_harga():
    sort_mobil(daftar_mobil)
    linked_list_mobil.head = None
    for mobil in daftar_mobil:
        linked_list_mobil.tambah_mobil(mobil)    
    print("\nDaftar mobil telah diurutkan berdasarkan harga (termurah ke termahal).")
    linked_list_mobil.tampilkan_mobil()

def tampilkan_semua_data_mobil():
    print("Data Mobil dari Linked List:")
    linked_list_mobil.tampilkan_mobil()

def cari_mobil(nama_mobil):
    sekarang = linked_list_mobil.head
    while sekarang:
        if sekarang.mobil.nama_mobil.lower() == nama_mobil.lower():
            return sekarang.mobil
        sekarang = sekarang.next
    return None

def tambah_mobil():
    nama_mobil = input("Masukkan nama mobil baru: ")
    merek = input("Masukkan merek mobil: ")
    tipe = input("Masukkan tipe mobil: ")
    tahun = int(input("Masukkan tahun mobil: "))
    harga = int(input("Masukkan harga mobil: "))
    mobil_baru = Mobil(nama_mobil, merek, tipe, tahun, harga)
    linked_list_mobil.tambah_mobil(mobil_baru)
    stack_transaksi.tambah_transaksi(f"Mobil {nama_mobil} ditambahkan.")
    print(f"Mobil {nama_mobil} berhasil ditambahkan.")

def hapus_mobil():
    nama_mobil = input("Masukkan nama mobil yang ingin dihapus: ")
    mobil = linked_list_mobil.hapus_mobil(nama_mobil)
    if mobil:
        stack_transaksi.tambah_transaksi(f"Mobil {nama_mobil} dihapus.")
        print(f"Mobil {nama_mobil} berhasil dihapus.")
    else:
        print("Mobil tidak ditemukan.")

def tampilkan_histori():
    print("Histori Transaksi:")
    stack_transaksi.lihat_transaksi()

def main():
    while True:
        print("\nMANAJEMEN GUDANG MOBIL")
        print("1. Tampilkan semua data mobil")
        print("2. Cari mobil")
        print("3. Urutkan mobil berdasarkan harga termurah")
        print("4. Tambah mobil")
        print("5. Hapus mobil")
        print("6. Tampilkan histori")
        print("7. Tampilkan merek mobil ")
        print("8. Keluar")

        pilihan = input("Pilih menu (1-8): ")

        if pilihan == '1':
            tampilkan_semua_data_mobil()
        elif pilihan == '2':
            nama_mobil = input("Masukkan nama mobil yang dicari: ")
            mobil = cari_mobil(nama_mobil)
            if mobil:
                print(f"Nama mobil  : {mobil.nama_mobil}")
                print(f"Merek       : {mobil.merek}")
                print(f"Tipe        : {mobil.tipe}")
                print(f"Tahun       : {mobil.tahun}")
                print(f"Harga       : {mobil.harga}")
            else:
                print("Mobil tidak ditemukan.")
        elif pilihan == '3':
            urutkan_mobil_berdasarkan_harga()
        elif pilihan == '4':
            tambah_mobil()
        elif pilihan == '5':
            hapus_mobil()
        elif pilihan == '6':
            tampilkan_histori()
        elif pilihan == '7':
            display_tree()
        elif pilihan == '8':
            print("Program ditutup.")
            break
        else:
            print("Pilihan tidak valid, coba kembali")

if __name__ == "__main__":
    main()
