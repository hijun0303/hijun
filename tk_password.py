import tkinter as tk
import tkinter.messagebox as tkme
def mes0():
     button1["state"]=tk.DISABLED
     word = en1.get()
     if word == word_ans:
          mes1 = tkme.showinfo(title="パスワード確認",message="解除しました")
     else:
          mes2 =tkme.showwarning(title="パスワード確認",message="パスワードが間違っています")
          en1.delete(0,tk.END)
          button1["state"]=tk.NORMAL
root = tk.Tk()
root.title("パスワード")
root.geometry("300x250")
word_ans = "123aaa"
st1 = tk.Label(text = "パスワードを入力してください")
st1.place(x=80,y=50)
en1 = tk.Entry(show="*")
en1.place(x=80,y=100)
def click(event):
     root.after(1,mes0)
button1 = tk.Button(text="決定")
button1.place(x=130,y=150)
button1.bind("<Button-1>",click)
root.mainloop()