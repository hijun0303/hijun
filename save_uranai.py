import datetime as d
import random as r
name =input("名前を入力してください→")
kyou = d.date.today()
today = str(kyou)
uranai = ["大吉","中吉","吉","凶","大凶"]
kekka= r.choice(uranai)
txt = f"{today},{name},{kekka}\n"
print(txt)
fp = open("uranai2.txt","a",encoding="utf-8")
fp.write(txt)
fp.close()