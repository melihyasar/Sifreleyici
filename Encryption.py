from random import randint
def encrypt(text):
    x = randint(1, 2)
    i1 = randint(1, 9)
    i2 = randint(1, 9)
    vtextenable = 1
    vtext = ""
    stext = ""
    error = 0
    if x == 1:
        for element in list(text):
            if element == "a":
                stext = stext + "17"
            elif element == "b":
                stext = stext + "47"
            elif element == "c":
                stext = stext + "12"
            elif element == "ç":
               stext = stext + "24"
            elif element == "d":
               stext = stext + "36"
            elif element == "e":
               stext = stext + "34" 
            elif element == "f":
                stext = stext + "44"
            elif element == "g":
               stext = stext + "52"
            elif element == "ğ":
               stext = stext + "33"
            elif element == "h":
               stext = stext + "15"
            elif element == "ı":
               stext = stext + "46"
            elif element == "i":
               stext = stext + "22"
            elif element == "j":
               stext = stext + "35"
            elif element == "k":
               stext = stext + "11" 
            elif element == "l":
               stext = stext + "27"
            elif element == "m":
               stext = stext + "51" 
            elif element == "n":
               stext = stext + "16" 
            elif element == "o":
                stext = stext + "43"
            elif element == "ö":
               stext = stext + "26"
            elif element == "p":
               stext = stext + "31"
            elif element == "r":
               stext = stext + "37"
            elif element == "s":
               stext = stext + "45"
            elif element == "ş":
               stext = stext + "14"
            elif element == "t":
               stext = stext + "25"
            elif element == "u":
               stext = stext + "41" 
            elif element == "ü":
               stext = stext + "23"
            elif element == "v":
               stext = stext + "13"  
            elif element == "y":
               stext = stext + "42"
            elif element == "z":
               stext = stext + "21" 
            elif element == " ":
                stext = stext + "32"
            elif element == "x":
                stext = stext + "53"
            elif element == "w":
                stext = stext + "39"
            elif element == "q":
                stext = stext + "28"
            elif element == ".":
                stext = stext + "69"     
            else:
                stext = "Hata! Desteklenmeyen karakter: " + str(element)
                vtextenable = 0
                break
        if vtextenable == 1:
            vtext = int(stext) * i1
            vtext = vtext + i2
        else:
            vtext = stext
            error = 1
        return vtext, "1" + str(i1) + str(i2), error
    elif x == 2:
         for element in list(text):
            if element == "a":
                stext = stext + "11"
            elif element == "b":
                stext = stext + "12"
            elif element == "c":
                stext = stext + "13"
            elif element == "ç":
               stext = stext + "14"
            elif element == "d":
               stext = stext + "15"
            elif element == "e":
               stext = stext + "16" 
            elif element == "f":
                stext = stext + "17"
            elif element == "g":
               stext = stext + "21"
            elif element == "ğ":
               stext = stext + "22"
            elif element == "h":
               stext = stext + "23"
            elif element == "ı":
               stext = stext + "24"
            elif element == "i":
               stext = stext + "25"
            elif element == "j":
               stext = stext + "26"
            elif element == "k":
               stext = stext + "27" 
            elif element == "l":
               stext = stext + "31"
            elif element == "m":
               stext = stext + "32" 
            elif element == "n":
               stext = stext + "33" 
            elif element == "o":
                stext = stext + "34"
            elif element == "ö":
               stext = stext + "35"
            elif element == "p":
               stext = stext + "36"
            elif element == "r":
               stext = stext + "37"
            elif element == "s":
               stext = stext + "41"
            elif element == "ş":
               stext = stext + "42"
            elif element == "t":
               stext = stext + "43"
            elif element == "u":
               stext = stext + "28" 
            elif element == "ü":
               stext = stext + "54"
            elif element == "v":
               stext = stext + "46"  
            elif element == "y":
               stext = stext + "47"
            elif element == "z":
               stext = stext + "51" 
            elif element == " ":
                stext = stext + "52"
            elif element == "x":
                stext = stext + "45"
            elif element == "w":
                stext = stext + "44"
            elif element == "q":
                stext = stext + "69"
            elif element == ".":
                stext = stext + "39"
            else:
                stext = "Hata! Desteklenmeyen karakter: " + str(element)
                vtextenable = 0
                break
         if vtextenable == 1:
            vtext = int(stext) * i1
            vtext = vtext + i2
         else:
            vtext = stext
            error = 1
         return vtext, "2" + str(i1) + str(i2), error
     #Yazan :Mustafa Melih Yaşar
     #deneme123

        
   

