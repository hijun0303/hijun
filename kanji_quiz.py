dic = {"啄木鳥":"きつつき",
       "郭公":"かっこう",
       "海豹":"あざらし",
       "鬼灯":"ほおずき",
       "大熊猫":"ぱんだ"}
count = 0
for k,v in dic.items():
    ans = input(f"{k}は何と読む？→")
    if ans == v:
        print("正解")
        count+=1
    else:
        print("不正解")

print(f"{count}問正解しました。")