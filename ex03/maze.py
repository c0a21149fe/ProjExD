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
    global mx, my
    if key == "Up": #keyの値によって、こうかとんの動く向きを変える
        my -= 1
    elif key == "Down":
        my += 1
    elif key == "Left":
        mx -= 1
    elif key == "Right":
        mx += 1

    if maze_lst[mx][my] == 1: #移動先が壁だったら
        if key == "Up":  # keyの値によって、こうかとんの動く向きを変える
            my += 1
        elif key == "Down":
            my -= 1
        elif key == "Left":
            mx += 1
        elif key == "Right":
            mx -= 1
    
    canvas.coords("koukaton", mx*100+50, my*100+50) #こうかとんの座標変更
    root.after(100, main_proc) #100ms毎に再帰



root = tk.Tk() #ウィンドウ作成
root.title("迷えるこうかとん")
#root.geometry("1500x900")

canvas = tk.Canvas(root, width=1500, height=800, bg="black")
canvas.pack()

maze_lst = mm.make_maze(15, 9) #
mm.show_maze(canvas, maze_lst)

#迷路の座標
mx, my = 1, 1
#tkインター上の座標
cx, cy = mx*100+50, my*100+50
#こうかとんの表示
koukaton = tk.PhotoImage(file="fig/8.png")
canvas.create_image(cx, cy, image=koukaton, tag="koukaton")
canvas.pack()

key = ""
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)

main_proc()

root.mainloop()