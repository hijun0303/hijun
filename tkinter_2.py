import tkinter as tk
root = tk.Tk()
root.title("テキストボックスを作ろう")
root.geometry("400x300")
static1 = tk.Label(text="テキストボックスを作る")
static1.pack()
entry1 = tk.Entry()
entry1.pack()
root.mainloop()