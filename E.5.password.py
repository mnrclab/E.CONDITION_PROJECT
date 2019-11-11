password = '12345'
inputuser = ''
jumlahInput = 0
batasInput = 5
lebih = False

while inputuser != password and not lebih:
    if jumlahInput < batasInput:
        inputuser = input(f'Tebakan ke-{jumlahInput+1} Ketik Password: ')
        jumlahInput += 1
    else:
        lebih = True
if lebih:
    print('Kesempatan habis, tunggu 24 jam')
else:
    print('Password benar')
