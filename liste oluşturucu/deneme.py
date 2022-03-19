from random import randint
import csv
letters=["q","w","e","r","t","y","u","ı","o","p","ğ","ü","a","s","d","f","g","h","j","k","l","ş","i","z","x","c","v","b","n","m","ö","ç",]
letters_upper=[x.upper() for x in letters]
nums_specialchars=["1","2","3","4","5","6","7","8","9","0","*","-"," ","!","'","^","+","%","&","/","(",")","=","?","_","é","<",">",":",".",",","`","£","#","$","½","{","}",";",'"',"~","¨","´@","æ","ß","€","₺","İ","[","]","","","",]
chars=letters+letters_upper+nums_specialchars
res = []
d={}
for i in chars:
    if i not in res:
        res.append(i)
def myfunc(element):
    x=randint(1000,9999)
    try:
     dnm=d[x]
     myfunc(element)
    except:
        d[x]=element
m=0
q=[]
r=[]
while m<1000:
    d={}
    m=m+1
    print(m)
    for element in res:
        myfunc(element)
    inv_map = {v: k for k, v in d.items()}
    q.append(str(d))
    r.append(str(inv_map))

with open("Data/Data.csv",'a',newline="", encoding="utf8") as file:
    writer=csv.writer(file,delimiter = "|")
    writer.writerow(q)
with open("Data/Data2.csv",'a',newline="", encoding="utf8") as file:
    writer=csv.writer(file,delimiter = "|")
    writer.writerow(r)
    
input()


    
