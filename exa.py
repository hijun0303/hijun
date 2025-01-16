# ライブラリのインポート
import tkinter as tk

# tkオブジェクトの作成
root = tk.Tk()
root.title("packテスト")
root.geometry("300x200")

# ウィジェットの配置
btn1 = tk.Button(root, text="Button 1")
btn1.pack(side=tk.TOP, fill=tk.X)

btn2 = tk.Button(root, text="Button 2")
btn2.pack(side=tk.LEFT, fill=tk.Y)

btn3 = tk.Button(root, text="Button 3")
btn3.pack(side=tk.RIGHT, expand=True)

# メインループの実行
root.mainloop()