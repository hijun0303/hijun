import csv

with open("kekka.csv","r") as f:
     kekka = {int(i[1]):i[0] for i in csv.reader(f)}

while True:
     try:
          goukaku = int(input("合格点を入力/0を入力で終了→"))
     except ValueError:
          print("数値を入力してください。")
     except KeyboardInterrupt:
          print("割り込み終了")
     else:
          if goukaku==0:
               print("終了します。")
               break
          for k,v in kekka.items():
               if k>=goukaku:
                    print(f"{v}は{k}点で合格です。")
     finally:
          print("-"*20)