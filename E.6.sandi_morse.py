source = {
    'a': '.-', 'b' : '-...', 'c' : '-.-.', 'd' : '-..', 'e' : '.',
    'f' : '..-.', 'g' : '--.', 'h' : '....', 'i' : '..', 'j': '.---',
    'k' : '-.-', 'l' : '.-..', 'm' : '--', 'n' : '-.', 'o' : '---', 
    'p' : '.--.','q' : '--.-', 'r' : '.-.', 's' : '...', 't' : '-',
    'u' : '..-', 'v' : '...-', 'w' : '.--', 'x' : '-..-', 'y' : '-.--', 'z' : '--..',
    '0' : '-----', '1' : '.----', '2' : '..---', '3' : '...--', '4' : '....-',
    '5' : '.....', '6' : '-....', '7' : '--...', '8' : '---..', '9' : '----.', ' ' : '|',
}

def morse(teks):
    if teks.upper() == teks.lower():
        kalimat = teks.split('/')
        hasil = ''
        for i in kalimat:
            hasil += list(source.keys())[list(source.values()).index(i)]
        print(hasil)
    else:
        kalimat = teks.lower().replace(' ', '')
        hasil = ''
        for i in kalimat:
            hasil += source[i] + ' / '
        print(hasil)

morse(input('Ketik teks: '))
