import tkinter as tk
from tkinter import messagebox

# アプリケーションのメインウィンドウを作成
root = tk.Tk()
root.title("To-Doリストアプリ")

# タスクを保持するリスト
tasks = []

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("警告", "タスクを入力してください。")

def delete_task():
    try:
        task_index = task_listbox.curselection()[0]
        del tasks[task_index]
        update_task_list()
    except:
        messagebox.showwarning("警告", "削除するタスクを選択してください。")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# ウィジェットの作成
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="タスクを追加", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="タスクを削除", command=delete_task)
delete_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=40, height=10)
task_listbox.pack(pady=10)

root.mainloop()
