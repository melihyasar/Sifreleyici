
def decrypt(text1, key):
    keyr = list(key)[::-1]
    t = int(keyr[0])
    c = int(keyr[1])
    a = int(keyr[2])
    global text2
    global text3
    global text4
    text2 = int(text1) - t
    text3 = int(text2) // c
    text4 = str(text3)
    gtext = ""
    a_string = text4
    split_strings = []
    n  = 2
    
    for index in range(0, len(a_string), n):
        split_strings.append(a_string[index : index + n])
    
    if a == 2:
        for p in split_strings:
            if p == "11":
                gtext= gtext + "a"
            elif p == "12":
                gtext= gtext + "b"
            elif p == "13":
                gtext= gtext + "c"
            elif p == "14":
                gtext= gtext + "ç"
            elif p == "15":
                gtext= gtext + "d"
            elif p == "16":
                gtext= gtext + "e"
            if p == "17":
                gtext= gtext + "f"
            elif p == "21":
                gtext= gtext + "g"
            elif p == "22":
                gtext= gtext + "ğ"
            elif p == "23":
                gtext= gtext + "h"
            elif p == "24":
                gtext= gtext + "ı"
            elif p == "25":
                gtext= gtext + "i"
            elif p == "26":
                gtext= gtext + "j"
            elif p == "27":
                gtext= gtext + "k"
            elif p == "31":
                gtext= gtext + "l"
            elif p == "32":
                gtext= gtext + "m"
            elif p == "33":
                gtext= gtext + "n"
            elif p == "34":
                gtext= gtext + "o"
            elif p == "35":
                gtext= gtext + "ö"
            elif p == "36":
                gtext= gtext + "p"
            elif p == "37":
                gtext= gtext + "r"
            elif p == "41":
                gtext= gtext + "s"
            elif p == "42":
                gtext= gtext + "ş"
            elif p == "43":
                gtext= gtext + "t"
            elif p == "28":
                gtext= gtext + "u"
            elif p == "54":
                gtext= gtext + "ü"
            elif p == "46":
                gtext= gtext + "v"
            elif p == "47":
                gtext= gtext + "y"
            elif p == "51":
                gtext= gtext + "z"
            elif p == "52":
                gtext= gtext + " "
            elif p == "45":
                gtext= gtext + "x"
            elif p == "44":
                gtext= gtext + "w"
            elif p == "69":
                gtext= gtext + "q"
            elif p == "39":
                gtext= gtext + "."
        return gtext
    elif a == 1:
        for p in split_strings:
            if p == "17":
                gtext= gtext + "a"
            elif p == "47":
                gtext= gtext + "b"
            elif p == "12":
                gtext= gtext + "c"
            elif p == "24":
                gtext= gtext + "ç"
            elif p == "36":
                gtext= gtext + "d"
            elif p == "34":
                gtext= gtext + "e"
            elif p == "44":
                gtext= gtext + "f"
            elif p == "52":
                gtext= gtext + "g"
            elif p == "33":
                gtext= gtext + "ğ"
            elif p == "15":
                gtext= gtext + "h"
            elif p == "46":
                gtext= gtext + "ı"
            elif p == "22":
                gtext= gtext + "i"
            elif p == "35":
                gtext= gtext + "j"
            elif p == "11":
                gtext= gtext + "k"
            elif p == "27":
                gtext= gtext + "l"
            elif p == "51":
                gtext= gtext + "m"
            elif p == "16":
                gtext= gtext + "n"
            elif p == "43":
                gtext= gtext + "o"
            elif p == "26":
                gtext= gtext + "ö"
            elif p == "31":
                gtext= gtext + "p"
            elif p == "37":
                gtext= gtext + "r"
            elif p == "45":
                gtext= gtext + "s"
            elif p == "14":
                gtext= gtext + "ş"
            elif p == "25":
                gtext= gtext + "t"
            elif p == "41":
                gtext= gtext + "u"
            elif p == "23":
                gtext= gtext + "ü"
            elif p == "13":
                gtext= gtext + "v"
            elif p == "42":
                gtext= gtext + "y"
            elif p == "21":
                gtext= gtext + "z"
            elif p == "32":
                gtext= gtext + " "
            elif p == "53":
                gtext= gtext + "x"
            elif p == "39":
                gtext= gtext + "w"
            elif p == "28":
                gtext= gtext + "q"
            elif p == "69":
                gtext= gtext + "."
        return gtext

    
  


     


  
