user_file = open('user_list.csv', 'r',encoding='utf-8')
total = 0
for line in user_file:
     lines = line.strip().split(",")
     if lines[4]=="ゴールド":
          print(f"{lines[1]}{lines[2]}")
          total+=int(lines[3])
print(f"合計金額は{total}円です。")
user_file.close()