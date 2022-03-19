import csv
import ast
def decrypt(text1, key):
    n  = 4
    with open('data\data.csv','r',encoding="utf8") as file:
            data=csv.reader(file,delimiter = "|")
            rows=[r for r in data]         
    keyr = list(key)[::-1]
    t = int(keyr[0])
    c = int(keyr[1])
    a = ""
    for i in keyr[2:]:
        a=a+i
    a=a[::-1]
    a=int(a)
    text1 = int(text1) - t
    text1 = int(text1) // c
    text1 = str(text1)
    gtext = ""
    split_strings = []
    g=ast.literal_eval(rows[0][a])
    
    for index in range(0, len(text1), n):
        split_strings.append(text1[index : index + n])
    for p in split_strings:
        gtext=gtext+g[int(p)]
    return gtext