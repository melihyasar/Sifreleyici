
def decrypt(text1, key):
    gtext = ""
    a_string = text1

    split_strings = []
    n  = 2
    for index in range(0, len(a_string), n):
        split_strings.append(a_string[index : index + n])

    if key == 2:
        for p in split_strings:
            if p == "11":
                gtext= gtext + "a"
            if p == "12":
                gtext= gtext + "b"
            if p == "13":
                gtext= gtext + "c"
            if p == "14":
                gtext= gtext + "ç"
            if p == "15":
                gtext= gtext + "d"
            if p == "16":
                gtext= gtext + "e"
            if p == "17":
                gtext= gtext + "f"
            if p == "21":
                gtext= gtext + "g"
            if p == "22":
                gtext= gtext + "ğ"
            if p == "23":
                gtext= gtext + "h"
            if p == "24":
                gtext= gtext + "ı"
            if p == "25":
                gtext= gtext + "i"
            if p == "26":
                gtext= gtext + "j"
            if p == "27":
                gtext= gtext + "k"
            if p == "31":
                gtext= gtext + "l"
            if p == "32":
                gtext= gtext + "m"
            if p == "33":
                gtext= gtext + "n"
            if p == "34":
                gtext= gtext + "o"
            if p == "35":
                gtext= gtext + "ö"
            if p == "36":
                gtext= gtext + "p"
            if p == "37":
                gtext= gtext + "r"
            if p == "41":
                gtext= gtext + "s"
            if p == "42":
                gtext= gtext + "ş"
            if p == "43":
                gtext= gtext + "t"
            if p == "28":
                gtext= gtext + "u"
            if p == "54":
                gtext= gtext + "ü"
            if p == "46":
                gtext= gtext + "v"
            if p == "47":
                gtext= gtext + "y"
            if p == "51":
                gtext= gtext + "z"
            if p == "52":
                gtext= gtext + " "
            if p == "45":
                gtext= gtext + "x"
            if p == "44":
                gtext= gtext + "w"
            if p == "69":
                gtext= gtext + "q"
            if p == "39":
                gtext= gtext + "."
        return gtext
    if key == 1:
        for p in split_strings:
            if p == "17":
                gtext= gtext + "a"
            if p == "47":
                gtext= gtext + "b"
            if p == "12":
                gtext= gtext + "c"
            if p == "24":
                gtext= gtext + "ç"
            if p == "36":
                gtext= gtext + "d"
            if p == "34":
                gtext= gtext + "e"
            if p == "44":
                gtext= gtext + "f"
            if p == "52":
                gtext= gtext + "g"
            if p == "33":
                gtext= gtext + "ğ"
            if p == "15":
                gtext= gtext + "h"
            if p == "46":
                gtext= gtext + "ı"
            if p == "22":
                gtext= gtext + "i"
            if p == "35":
                gtext= gtext + "j"
            if p == "11":
                gtext= gtext + "k"
            if p == "27":
                gtext= gtext + "l"
            if p == "51":
                gtext= gtext + "m"
            if p == "16":
                gtext= gtext + "n"
            if p == "43":
                gtext= gtext + "o"
            if p == "26":
                gtext= gtext + "ö"
            if p == "31":
                gtext= gtext + "p"
            if p == "37":
                gtext= gtext + "r"
            if p == "45":
                gtext= gtext + "s"
            if p == "14":
                gtext= gtext + "ş"
            if p == "25":
                gtext= gtext + "t"
            if p == "41":
                gtext= gtext + "u"
            if p == "23":
                gtext= gtext + "ü"
            if p == "13":
                gtext= gtext + "v"
            if p == "42":
                gtext= gtext + "y"
            if p == "21":
                gtext= gtext + "z"
            if p == "32":
                gtext= gtext + " "
            if p == "53":
                gtext= gtext + "x"
            if p == "39":
                gtext= gtext + "w"
            if p == "28":
                gtext= gtext + "q"
            if p == "69":
                gtext= gtext + "."
        return gtext
yazi = decrypt("5134272215", 1)
print(yazi)
input()


    
  


     


  
