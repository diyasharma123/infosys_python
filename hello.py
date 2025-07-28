import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()
root.geometry("400x400")
root.title("Combined Layout Example")

icon = PhotoImage(file='logo.png')
root.iconphoto(True, icon)
label1 = tk.Label(root, text="Hello World", bg="red")
#label1.grid(row=0, column=0)
label1.place(x=100, y=100)

label2 = tk.Label(root, text="Hello World", bg="green")
#label2.grid(row1, column=1)
label2.place(x=100, y=150)


frame_top = tk.Frame(root)
frame_bottom = tk.Frame(root)

frame_top.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
frame_bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

label1 = tk.Label(frame_top, text="top frame - Label 1")
label2 = tk.Label(frame_top, text="top frame - Label 2")
label3 = tk.Label(frame_bottom, text="bottom frame - Label 1")
label4 = tk.Label(frame_bottom, text="bottom frame - Label 2")

label1.pack(side=tk.LEFT)
label2.pack(side=tk.RIGHT)
label3.grid(row=0, column=0)
label4.grid(row=1, column=1)

root.mainloop()