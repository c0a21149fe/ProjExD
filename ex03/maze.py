import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm
import random

def key_down(event): #キーが押されたとき
    global key
    key = event.keysym

def key_up(event): #キーが上がったとき
    global key
    key = ""


def main_proc(): #メイン処理（繰り返し）
    global mx, my, jid
    if key == "Up": #keyの値によって、こうかとんの動く向きを変える
        my -= 1
        canvas.itemconfigure(image_id, image=koukaton_up) #画像の差し替え
    elif key == "Down":
        my += 1
        canvas.itemconfigure(image_id, image=koukaton_down)
    elif key == "Left":
        mx -= 1
        canvas.itemconfigure(image_id, image=koukaton)
    elif key == "Right":
        mx += 1
        canvas.itemconfigure(image_id, image=koukaton_right)

    if maze_lst[mx][my] == 1: #移動先が壁だったら、値をリセット
        if key == "Up":  
            my += 1
        elif key == "Down":
            my -= 1
        elif key == "Left":
            mx += 1
        elif key == "Right":
            mx -= 1

    canvas.coords("koukaton", mx*100+50, my*100+50)  # こうかとんの座標変更

    #ゴールの判別と処理
    if maze_lst[mx][my] == 2:
        root.after_cancel(jid)
        tkm.showinfo("ゲーム", "ゲームクリア")
    else:
        jid = root.after(100, main_proc) #100ms毎に再帰



root = tk.Tk() #ウィンドウ作成
root.title("迷えるこうかとん")
#root.geometry("1500x900")

canvas = tk.Canvas(root, width=1500, height=800, bg="black")
canvas.pack()


maze_lst = mm.make_maze(15, 9) #
mm.show_maze(canvas, maze_lst)

#ゴールの表示
goal = random.choice([(1, 7), (13, 1), (13, 7)])
goal_x, goal_y = goal
canvas.create_rectangle(goal_x*100, goal_y*100, goal_x *
                        100+100, goal_y*100+100, fill="red")
canvas.pack()
maze_lst[goal_x][goal_y] = 2 #ゴールの番号

# mm.print_maze(maze_lst)

# jumyo = 25
# label1 = tk.Label(root, text = "こうかとんの寿命", width=100, height=900)
# label1.place(x=100, y=900)
# label2 = tk.Label(root, text = jumyo, width=300, height=900)
# label2.pack()


#迷路の座標
mx, my = 1, 1
#tkインター上の座標
cx, cy = mx*100+50, my*100+50
#こうかとんの表示
#イメージを変数に代入
koukaton = tk.PhotoImage(file="fig/8.png")
koukaton_right = tk.PhotoImage(file="fig/8_right.png")
koukaton_up = tk.PhotoImage(file="fig/8_up.png")
koukaton_down = tk.PhotoImage(file="fig/8_down.png")
#イメージの作成
image_id = canvas.create_image(cx, cy, image=koukaton, tag="koukaton") #画像差し替えのためのidをimage_idに格納
canvas.pack()

key = ""
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)

jid = None #ジョブIDの初期化
main_proc()

root.mainloop()