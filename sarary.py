import csv
with open("month.csv","r") as f:
     kekka = {i[0]:[int(i[1]),int(i[2]),int(i[3])] for i in csv.reader(f)}
import func_sarary as f
for k,v in kekka.items():
     print(f"{k}さんの給与は{f.sarary(v[0],v[1],v[2])}円です。")