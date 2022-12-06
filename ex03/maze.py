import tkinter as tk
import tkinter.messagebox as tkm


def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

root = tk.Tk()
root.title("迷えるこうかとん")
#root.geometry("1500x900")

canvas = tk.Canvas(root, width=1500, height=800, bg="black")
canvas.pack()

koukaton = tk.PhotoImage(file="fig/8.png")
cx, cy = 300, 400
canvas.create_image(cx, cy, image=koukaton, tag="koukaton")
canvas.pack()

key = ""
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)

root.mainloop()