from Encryption import encrypt
from Decryption import decrypt
def giris():
     print()
     print("Hangisini yapmak istersiniz?")
     print("Şifreleme için 1")
     print("Şifre çözmek için 2")
     secim = input()
     if secim == "1":
          return secim
     if secim == "2":
          return secim
     else:     
      giris()

while True:
 uyg_modu = giris()
 if uyg_modu == "1":
   txt = input("Şifrelenecek yazıyı yazınız:")
   ctext,key,error = encrypt(txt)
   if error != 1:
        dosya_ismi = input("dosyanın hangi isimle kaydedilmesini istersiniz? ")
        with open("output/" + dosya_ismi + ".sifre",'w') as sifre_dosyasi:
             sifre_dosyasi.write(str(ctext))
        print()     
        print("Anahtarınız: " + key)
        print("Anahterınızı unutmayınız!")
   elif error == 1:
        print()
        print("Bir hata meydana geldi!")
        print(ctext) 

 elif uyg_modu == "2":
         
     dosya_yolu = input("Şifre dosyasının konumun giriniz: ")
     dosya_yolu = dosya_yolu.replace('"', '')
     key = input("Anahtarı giriniz:") 
     with open(dosya_yolu,'r') as sifrelenmis_dosya:
          sifrelenmis_veri = sifrelenmis_dosya.read()
          try:
              yazi = decrypt(sifrelenmis_veri,key)
              print()
              print(yazi) 
          except:
               print()
               print("Bir hata meydana geldi!")
               print("Anahtarı kontrol ediniz")


