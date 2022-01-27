from Encryption import encrypt
from Decryption import decrypt
import tkinter as tk
from tkinter import filedialog
import colorama
from colorama import Fore,Back,Style
import time
colorama.init()
root = tk.Tk()
root.withdraw()
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
print(Fore.GREEN + "--Şifreleme uygulaması--")
print("---------------------------------"+ Fore.WHITE)
while True:
 uyg_modu = giris()
 if uyg_modu == "1":
   txt = input("Şifrelenecek yazıyı yazınız:")
   ctext,key,error = encrypt(txt)
   if error != 1:
        print(Fore.GREEN+"---------------------------------"+Fore.WHITE)
        dosya_ismi = input("Dosyanın hangi isimle kaydedilmesini istersiniz? ")
        print("Dosyanın kaydedileceği konumu giriniz:")
        time.sleep(2)
        sifre_dosya_konumu = filedialog.askdirectory()
        with open(sifre_dosya_konumu + "/"+ dosya_ismi + ".sifre",'w') as sifre_dosyasi:
             sifre_dosyasi.write(str(ctext))
        print(Fore.GREEN+"---------------------------------")     
        print(Fore.RED + "Anahtarınız: " + key)
        print("Anahterınızı unutmayınız!"+ Fore.WHITE)
        print(Fore.GREEN+"---------------------------------"+Fore.WHITE) 
   elif error == 1:
        print(Fore.RED+"---------------------------------")
        print("Bir hata meydana geldi!")
        print(ctext) 
        print("---------------------------------"+Fore.WHITE)

 elif uyg_modu == "2":
     print(Fore.GREEN+"---------------------------------"+Fore.WHITE)   
     dosya_yolu = print("Şifre dosyasının konumun giriniz: ")
     time.sleep(2)
     dosya_yolu = filedialog.askopenfilename()
     
     key = input("Anahtarı giriniz:") 
     with open(dosya_yolu,'r') as sifrelenmis_dosya:
          sifrelenmis_veri = sifrelenmis_dosya.read()
          try:
              yazi = decrypt(sifrelenmis_veri,key)
              print(Fore.GREEN+"---------------------------------"+Fore.WHITE)
              print(yazi) 
              print(Fore.GREEN+"---------------------------------"+Fore.WHITE)
          except:
               print(Fore.RED+"---------------------------------"+Fore.WHITE)
               print("Bir hata meydana geldi!")
               print("Anahtarı kontrol ediniz")
               print(Fore.RED+"---------------------------------"+Fore.WHITE)


