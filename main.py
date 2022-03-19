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
     print("Hangisini yapmak istersiniz?")
     print("Şifreleme için 1")
     print("Şifre çözmek için 2") 
     secim = input()
     if secim == "1":
          return secim
     elif secim == "2":
          return secim
     elif secim !="1" or secim !="2":        
      giris()
print("".join([Fore.GREEN ,"--Şifreleme uygulaması--"]))
print("---------------------------------"+ Fore.WHITE)
while 1:
 uyg_modu = giris()
 if uyg_modu == "1":
   txt = input("Şifrelenecek yazıyı yazınız:")
   ctext,key,error = encrypt(txt)
   if error != 1:
        print(Fore.GREEN+"---------------------------------"+Fore.WHITE)
        dosya_ismi = input("Dosyanın hangi isimle kaydedilmesini istersiniz? ")
        print("Dosyanın kaydedileceği konumu giriniz:")
        time.sleep(1)
        sifre_dosya_konumu = filedialog.askdirectory()
        if sifre_dosya_konumu != "":
          try:   
               with open("".join([sifre_dosya_konumu, "/",dosya_ismi ,".sifre"]),'w') as sifre_dosyasi:
                    sifre_dosyasi.write(str(ctext))
               print(Fore.GREEN+"---------------------------------")     
               print("".join([Fore.RED , "Anahtarınız: " ,key]))
               print("Anahterınızı unutmayınız!"+ Fore.WHITE)
               print(Fore.GREEN+"---------------------------------"+Fore.WHITE)
          except Exception as e:
               print(Fore.RED+"---------------------------------")
               print("Bir hata meydana geldi!")
               print(e)
               print("---------------------------------"+Fore.WHITE)
        elif sifre_dosya_konumu == "":
               print(Fore.RED+"---------------------------------")
               print("Dosya konumu seçilmedi!")
               print("---------------------------------"+Fore.WHITE)
   elif error == 1:
        print(Fore.RED+"---------------------------------")
        print("Bir hata meydana geldi!")
        print(ctext) 
        print("---------------------------------"+Fore.WHITE)

 elif uyg_modu == "2":
     print(Fore.GREEN+"---------------------------------"+Fore.WHITE)   
     dosya_yolu = print("Şifre dosyasının konumun giriniz: ")
     time.sleep(1)
     dosya_yolu = filedialog.askopenfilename()
     if dosya_yolu != "":
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
     elif dosya_yolu == "":
          print(Fore.RED+"---------------------------------")
          print("Dosya konumu seçilmedi!")
          print("---------------------------------"+Fore.WHITE)               


