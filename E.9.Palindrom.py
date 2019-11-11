#cara pertama
def palindrome1(kata):
    y = []
    for i in list(kata):
        y.insert(0, i)
    if ''.join(y) == kata:
        return True
    else:
        return False

#cara kedua
kata = 'kakak'
def palindrome2(kata):
    if kata[::-1] == kata:
        return True
    else:
        return False
print(palindrome2(kata))
