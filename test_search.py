import csv

with open("kekka.csv","r") as f:
     kekka = {i[0]:int(i[1]) for i in csv.reader(f)}

while True:
     try:
          name = input("名前を入力してください/0を入力で終了→")
          if name=="0":
               print("終了します。")
               break
          print(f"{name}さんは{kekka[name]}点です。")
     except KeyError:
          print("該当データがありません。")
     except KeyboardInterrupt:
          print("割り込み終了")
     finally:
          print("-"*20)