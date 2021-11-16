from Encryption import encrypt
txt = input("Birşey yaz: ")
f = open("Deneme.txt", 'w')

x, y, z= encrypt(txt)
print(x)
f.write(str(x))
f.close()
if z != 1:
     print("Anahtarınız: " + str(y))
     input()
    #Yazan: Mustafa Melih Yaşar
    #deneme123