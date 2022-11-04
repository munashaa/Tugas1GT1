item_list = []
jumlah_list = []
harga_list = []


def pilihan():
    pil=str(input("Ada barang yang ingin dimasukkan? (y/n) : "))
    if pil=="y":
        input_item()
    elif pil=="n":
        cetak_nota()
    else:
        pilihan()

def input_item():
    item=str(input("Nama Barang = "))
    harga=int(input("Harga Barang = "))
    jml=int(input("Jumlah Barang = "))
    total = harga*jml
    item_list.append(item)
    jumlah_list.append(jml)
    harga_list.append(total)
    pilihan()

nota_list = [item_list, jumlah_list, harga_list]

def cetak_nota():
    for i in range(len(nota_list)):
        for x in nota_list:
            print(x[i], end =' ')
        print(i)


print("===Kasir===\n")
pilihan()