kanji1 = input("問１、啄木鳥：読み方をひらがなで入力してください→")
kanji2 = input("問２、郭公：読み方をひらがなで入力してください→")
kanji3 = input("問３、海豹：読み方をひらがなで入力してください→")
kanji4 = input("問４、鬼灯：読み方をひらがなで入力してください→")
kanji5 = input("問５、大熊猫：読み方をひらがなで入力してください→")
kanji = [kanji1,kanji2,kanji3,kanji4,kanji5]
yomi = ["きつつき","かっこう","あざらし","ほおずき","ぱんだ"]
ans = 0
for i in range(len(kanji)):
     if kanji[i] == yomi[i]:
          print(f"問{i+1}、正解")
          ans+=1
     else:
          print(f"問{i+1}、不正解")
print(f"合計{ans}問正解")