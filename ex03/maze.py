import tkinter as tk
import tkinter.messagebox as tkm


root = tk.Tk()
root.title("迷えるこうかとん")
#root.geometry("1500x900")

canvas = tk.Canvas(root, width=1500, height=800, bg="black")
canvas.pack()

koukaton = tk.PhotoImage(file="fig/8.png")
cx, cy = 300, 400
canvas.create_image(cx, cy, image=koukaton, tag="koukaton")
canvas.pack()

root.mainloop()