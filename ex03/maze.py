import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm


def key_down(event): #キーが押されたとき
    global key
    key = event.keysym

def key_up(event): #キーが上がったとき
    global key
    key = ""

def main_proc(): #メイン処理（繰り返し）
    global cx, cy
    if key == "Up": #keyの値によって、こうかとんの動く向きを変える
        cy -= 20
    elif key == "Down":
        cy += 20
    elif key == "Left":
        cx -= 20
    elif key == "Right":
        cx += 20
    
    canvas.coords("koukaton", cx, cy) #こうかとんの座標変更
    root.after(100, main_proc) #100ms毎に再帰



root = tk.Tk() #ウィンドウ作成
root.title("迷えるこうかとん")
#root.geometry("1500x900")

canvas = tk.Canvas(root, width=1500, height=800, bg="black")
canvas.pack()

maze_lst = mm.make_maze(15, 9) #迷路の生成

koukaton = tk.PhotoImage(file="fig/8.png")
cx, cy = 300, 400
canvas.create_image(cx, cy, image=koukaton, tag="koukaton")
canvas.pack()

key = ""
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)

main_proc()

root.mainloop()