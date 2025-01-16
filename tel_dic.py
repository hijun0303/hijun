tel = {"札幌":"011","東京":"03","大阪":"06","名古屋":"052","福岡":"092"}
try:
     a = input("都市名を入力:")
     print(f"{a}の市外局番は{tel[a]}です。")
except KeyError:
     print("該当都市がありません")
except KeyboardInterrupt:
     print("割り込み終了")
else:
     if a=="札幌":
          print("寒いですね")
finally:
     print('-'*20)
# elif a =="東京" or a =="大阪"or a =="名古屋" or a =="福岡":
     # print(f"{a}の市外局番は{tel[a]}")