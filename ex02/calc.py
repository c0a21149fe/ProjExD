import tkinter as tk
import tkinter.messagebox as tkm



root = tk.Tk()
root.title("tk")
root.geometry("300x500")

r, c = 0, 0
for i in range(9, -1, -1):

    num_key = tk.Button(root, text=i, width=4, height=2, font=("", 30))
    num_key.grid(row=r, column=c)
    
    if i % 3 == 1:
        r += 1
        c = 0
    else:
        c += 1

root.mainloop()