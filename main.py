from Encryption import encrypt
from Decryption import decrypt
txt = input("Birşey yaz: ")
f = open("Deneme.txt", 'w')
x, y, z= encrypt(txt)
print(x)
f.write(str(x))
f.close()
if z != 1:
     print("Anahtarınız: " + str(y))
     print()
     input()
     yazi1 = decrypt(str(x), str(y))
     print(yazi1)
     input()

     






    #Yazan: Mustafa Melih Yaşar
    #deneme123