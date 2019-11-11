def ubahvocal(kata):
    hasil = kata.replace('a', 'o').replace('i', 'o').replace('u', 'o').replace('e', 'o').replace('o', 'o')
    return hasil
print(ubahvocal(input('Ketik teks: ')))
