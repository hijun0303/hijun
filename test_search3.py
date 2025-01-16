import csv
kekka = {}
with open("kekka2.csv","r") as f:
     for i in csv.reader(f):
          kekka[i[0]] = [int(i[1]),int(i[2]),int(i[3])]
ja = 0
ma = 0
en = 0
count = 0
for k,v in kekka.items():
     print(f"{k}さんの合計点は{sum(v)}点です。")
     ja+=v[0]
     ma+=v[1]
     en+=v[2]
     count+=1

print(f"平均点は国語{ja/count}点,数学{ma/count}点,英語{en/count}点")



     