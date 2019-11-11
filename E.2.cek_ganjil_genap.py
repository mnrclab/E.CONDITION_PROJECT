def gangen(angka):
    if angka % 2 == 0:
        print(angka, 'tergolong GENAP')
    else:
        print(angka, 'tergolong GANJIL')

angka = float(input('Masukkan angka: '))
gangen(angka)
