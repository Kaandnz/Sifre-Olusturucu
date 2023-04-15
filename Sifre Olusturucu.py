import random
import string

def sifre_olustur(length):

    karakterler = string.ascii_letters + string.digits + string.punctuation
    sifre = ''.join(random.choice(karakterler) for i in range(length))
    return sifre

length = int(input("Şifrenin uzunluğunu girin: "))
sifre1 = sifre_olustur(length)
print("Oluşturulan şifre: " + sifre1)