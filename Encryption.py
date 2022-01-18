from random import randint
def encrypt(text):
    x = randint(1, 2)
    i1 = randint(1, 9)
    i2 = randint(1, 9)
    ctext = ""
    c2text = ""
    error = 0
    key = ""
    txkarakter = ""
    if x == 1:            
         d1 = {'a':'26','b':'41','c':'64','ç':'42','d':'40','e':'82','f':'57','g':'27','ğ':'65','h':'34','ı':'85','i':'56','j':'28','k':'63','l':'55','m':'10','n':'83','o':'43','ö':'11','p':'68','r':'84','s':'12','ş':'44','t':'58','u':'35','ü':'13','v':'14','y':'81','z':'45','x':'54','w':'86','q':'29','A':'53','B':'15','C':'67','Ç':'59','D':'16','E':'66','F':'17','G':'62','Ğ':'30','H':'46','I':'39','İ':'61','J':'69','K':'60','L':'18','M':'75','N':'70','O':'72','Ö':'36','P':'74','R':'71','S':'37','Ş':'38','T':'47','U':'31','Ü':'32','V':'87','Y':'33','Z':'19','W':'88','Q':'49','X':'48','1':'23','2':'24','3':'25','4':'76','5':'73','6':'78','7':'51','8':'52','9':'20','0':'79',' ':'89','.':'50',',':'80','!':'21','?':'77',}
         for element in list(text):
           try: 
              ctext = ctext + d1[element]
           except KeyError: 
              txkarakter = txkarakter + " " + element
              c2text = 'Tanımlanmamış karakterler: ' + txkarakter
              error = 1
              
         if error != 1:
          ctext = int(ctext) * i1
          ctext = int(ctext) + i2
          key = str(x) + str(i1) + str(i2)
         elif error == 1:
             return c2text, key, error  
         return ctext, key, error  
    elif x == 2:            
         d2 = {'a':'24','b':'14','c':'40','ç':'25','d':'19','e':'39','f':'59','g':'30','ğ':'68','h':'16','ı':'29','i':'52','j':'69','k':'72','l':'43','m':'64','n':'23','o':'75','ö':'44','p':'41','r':'73','s':'31','ş':'10','t':'46','u':'26','ü':'67','v':'53','y':'17','z':'42','x':'74','w':'15','q':'66','A':'65','B':'22','C':'71','Ç':'87','D':'45','E':'70','F':'32','G':'18','Ğ':'47','H':'60','I':'27','İ':'11','J':'33','K':'58','L':'54','M':'63','N':'61','O':'50','Ö':'62','P':'51','R':'37','S':'76','Ş':'82','T':'35','U':'80','Ü':'48','V':'36','Y':'12','Z':'57','W':'21','Q':'85','X':'34','0':'28','1':'49','2':'38','3':'79','4':'86','5':'20','6':'83','7':'81','8':'84','9':'77',' ':'78','.':'55',',':'56','!':'13','?':'89',}
         for element in list(text):
           try: 
              ctext = ctext + d2[element]
           except KeyError: 
              txkarakter = txkarakter + " " + element
              c2text = 'Tanımlanmamış karakterler: ' + txkarakter
              error = 1
         if error != 1:
          ctext = int(ctext) * i1
          ctext = int(ctext) + i2
          key = str(x) + str(i1) + str(i2)
         elif error == 1:
            return c2text, key, error
         return ctext, key, error


