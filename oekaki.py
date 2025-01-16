import tkinter as tk
gamen = tk.Tk()
gamen.title("お絵描きアプリ")
gamen.geometry("600x450")
cv = tk.Canvas(gamen,width=600,height=400,bg="white")
cv.pack()

def draw(event):
     x1=event.x-5
     y1=event.y-5
     x2=event.x+5
     y2=event.y+5
     cv.create_oval(x1,y1,x2,y2,fill=color,outline=color)
def color_red():
     global color
     color = "red"
def color_yellow():
     global color
     color = "yellow"
def color_green():
     global color
     color = "green"
def color_blue():
     global color
     color = "blue"
def color_white():
     global color
     color = "white"

button_red = tk.Button(gamen,text="赤",bg="red",command=color_red)
button_yellow = tk.Button(gamen, text="黄", bg="yellow",command=color_yellow)
button_green = tk.Button(gamen, text="緑", bg="green",command=color_green)
button_blue = tk.Button(gamen, text="青", bg="blue",command=color_blue)
button_white = tk.Button(gamen, text="消しゴム", bg="white",command=color_white)
button_red.place(x=30,y=410,width=50)
button_yellow.place(x=90, y=410, width=50)
button_green.place(x=150, y=410, width=50)
button_blue.place(x=210, y=410, width=50)
button_white.place(x=270, y=410, width=50)
color = "blue"
cv.bind("<B1-Motion>",draw)
gamen.mainloop()