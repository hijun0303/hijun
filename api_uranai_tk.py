import tkinter as tk
import json
import requests
import datetime as dt
def clear_btn(event,num):
     global b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12
     for i in bl:
          i.destroy()
     get_uranai(num)

def get_uranai(num):
     global result12
     today = dt.date.today()
     today = str(today)
     today = today.replace("-","/")
     res = requests.get(f"http://api.jugemkey.jp/api/horoscope/free/{today}")
     result = json.loads(res.text)
     result12 = result["horoscope"][today][num]
     view_uranai(result12)

def view_uranai(dic):
     global se,kekka,item,color,name1,name2,job,name3,money,name4,total,name5,rank,name6
     se = tk.Label(text = result12["sign"])
     se.pack()
     kekka = tk.Entry(width=95)
     kekka.pack()
     kekka.insert(tk.END,result12["content"])
     item = tk.Entry()
     item.place(x=240,y=70)
     item.insert(tk.END,result12["item"])
     name1 = tk.Label(text="ラッキーアイテム")
     name1.place(x=160,y=70)
     color = tk.Entry()
     color.place(x=240,y=100)
     color.insert(tk.END,result12["color"])
     name2 = tk.Label(text="ラッキーカラー")
     name2.place(x=160,y=100)
     job = tk.Entry()
     job.place(x=240,y=130)
     job.insert(tk.END,result12["job"])
     name3 = tk.Label(text="仕事運")
     name3.place(x=160,y=130)
     money = tk.Entry()
     money.place(x=240,y=160)
     money.insert(tk.END,result12["money"])
     name4 = tk.Label(text="金運")
     name4.place(x=160,y=160)
     total = tk.Entry()
     total.place(x=240,y=190)
     total.insert(tk.END,result12["total"])
     name5 = tk.Label(text="総合運")
     name5.place(x=160,y=190)
     rank = tk.Entry()
     rank.place(x=240,y=190)
     rank.insert(tk.END,f"{result12["rank"]}位")
     name6 = tk.Label(text="ランキング")
     name6.place(x=160,y=190)
     make_return()
     
def make_return():
     global rb
     rb = tk.Button(text = "戻る")
     rb.bind("<1>",back_main)
     rb.place(x=280,y=270)

def make_btn():
     global b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,bl
     b1 = tk.Button(text = "牡羊座")
     b1.bind("<1>",lambda event:clear_btn(event,0))
     b1.place(x=150,y=30)
     b2 = tk.Button(text = "牡牛座")
     b2.bind("<1>",lambda event:clear_btn(event,1))
     b2.place(x=150,y=60)
     b3 = tk.Button(text = "双子座")
     b3.bind("<1>",lambda event:clear_btn(event,2))
     b3.place(x=150,y=90)
     b4 = tk.Button(text = "蟹座")
     b4.bind("<1>",lambda event:clear_btn(event,3))
     b4.place(x=150,y=120)
     b5 = tk.Button(text = "獅子座")
     b5.bind("<1>",lambda event:clear_btn(event,4))
     b5.place(x=150,y=150)
     b6 = tk.Button(text = "乙女座")
     b6.bind("<1>",lambda event:clear_btn(event,5))
     b6.place(x=150,y=180)
     b7 = tk.Button(text = "天秤座")
     b7.bind("<1>",lambda event:clear_btn(event,6))
     b7.place(x=400,y=30)
     b8 = tk.Button(text = "蠍座")
     b8.bind("<1>",lambda event:clear_btn(event,7))
     b8.place(x=400,y=60)
     b9 = tk.Button(text = "射手座")
     b9.bind("<1>",lambda event:clear_btn(event,8))
     b9.place(x=400,y=90)
     b10 = tk.Button(text = "山羊座")
     b10.bind("<1>",lambda event:clear_btn(event,9))
     b10.place(x=400,y=120)
     b11 = tk.Button(text = "水瓶座")
     b11.bind("<1>",lambda event:clear_btn(event,10))
     b11.place(x=400,y=150)
     b12 = tk.Button(text = "魚座")
     b12.bind("<1>",lambda event:clear_btn(event,11))
     b12.place(x=400,y=180)
     bl = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12]

def back_main(event):
     global rb,se,kekka,item,color,name1,name2,job,name3,money,name4,total,name5,rank,name6,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12
     rb.destroy()
     se.destroy()
     kekka.destroy()
     item.destroy()
     color.destroy()
     name1.destroy()
     name2.destroy()
     job.destroy()
     name3.destroy()
     money.destroy()
     name4.destroy()
     total.destroy()
     name5.destroy()
     rank.destroy()
     name6.destroy()
     make_btn()
     

root = tk.Tk()
root.title("今日の星座占い")
root.geometry("600x300")
title = tk.Label(text = "今日の星座占い")
title.pack()
make_btn()

root.mainloop()