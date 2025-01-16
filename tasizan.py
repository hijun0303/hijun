import random as r
total = 0
num = 0
while num != 9:
     num = r.randint(0,9)
     print(num)
     if num == 8:
          print("8は足しません")
     elif num == 9:
          print("9がでました")
     else:
          total+=num
          print(f"足し算合計：{total}")
print("終了します")