import datetime
today = datetime.date.today()
md = input("生年月日を入力(例)2024/12/3：")
md2 = md.split("/")
birth = datetime.date(int(md2[0]),int(md2[1]),int(md2[2]))
life = today - birth
print(life.days)