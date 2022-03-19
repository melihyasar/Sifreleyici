from random import randint
import csv
import ast
def encrypt(text):
   x = randint(0, 999)
   i1 = randint(1, 9)
   i2 = randint(1, 9)
   ctext = ""
   c2text = ""
   error = 0
   key = ""
   txkarakter = ""
   with open('data\data2.csv','r',encoding="utf8") as file:
            data=csv.reader(file,delimiter = "|")
            rows=[r for r in data]     
   d1=ast.literal_eval(rows[0][x])
   for element in list(text):
      try: 
         ctext = ctext + str(d1[element])
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
    


