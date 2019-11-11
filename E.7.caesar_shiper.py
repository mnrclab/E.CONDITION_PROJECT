#cara pertama
huruf = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

input = (input('Masukkan teks: ')).upper()
hasil = ''
for i in input:
    hasil += huruf[(huruf.index(i)+2)% len(huruf)]
print((hasil).lower())

#cara kedua
teks = input('Masukkan teks Anda: ')
jarak = int(input('Majukan berapa angka: '))
def CS(teks):
    kata = ''
    for x in teks.upper():
        if x in huruf:
            kata += huruf[(huruf.index(x)+jarak) % len(huruf)]
        else:
            kata += x
    return kata
print(CS(teks))
