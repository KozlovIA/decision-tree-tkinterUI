import tkinter as tk

root = tk.Tk()
frame1 = tk.Frame(root, width=100, height=100, background="bisque")
frame2 = tk.Frame(root, width=50, height = 50, background="#b22222")

frame1.pack(fill=None, expand=False)
frame2.place(relx=.5, rely=.5, anchor="c")

root.mainloop()