def kalkulator():
    angka1 = float(input('Masukkan angka 1: '))
    operator = input('Masukkan operator aritmatika (+-*/): ')
    angka2 = float(input('Masukkan angka 2: '))
    if operator == '+':
        print(f'Hasil penghitungannya yaitu {angka1 + angka2}')
    elif operator == '-':
        print(f'Hasil penghitungannya yaitu {angka1 - angka2}')
    elif operator == '*':
        print(f'Hasil penghitungannya yaitu {angka1 * angka2}')
    elif operator == '/':
        print(f'Hasil penghitungannya yaitu {angka1 / angka2}')
    else:
        print(f'Maaf operator {operator} tidak dikenali')

kalkulator()
