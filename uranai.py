import random
color = ["赤","青","黄","緑","オレンジ"]
data = ['大吉','中吉','吉','凶','大凶']
data_choice = random.choice(data)
data_color =random.choice(color)
print("今日の運勢は",data_choice,"です。",sep="")
print("ラッキーカラーは",data_color,"です。",sep ="")
