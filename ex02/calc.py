import tkinter as tk
import tkinter.messagebox as tkm


def button_click(event):
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo("", f"{num}ボタンがクリックされました")
    if num == "=":
        siki = entry.get()
        ans = eval(siki)
        entry.delete(0, tk.END)
        entry.insert(tk.END, ans)
#
    else: #=以外のボタン
        entry.insert(tk.END, num)

root = tk.Tk()
root.title("tk")
root.geometry("300x500")

entry = tk.Entry(root, justify="right", width=10, font=("", 40))
entry.grid(row=0, column=0, columnspan=3)


r, c = 1, 0
for i in range(9, -1, -1):

    num_key = tk.Button(root, text=i, width=4, height=2, font=("", 30))
    num_key.grid(row=r, column=c)
    num_key.bind("<1>", button_click)
    if i % 3 == 1:
        r += 1
        c = 0
    else:
        c += 1

operators = ["+", "="]
for ope in operators:
    button = tk.Button(root, text=ope, width=4, height=2, font=("", 30))
    button.grid(row = r, column=c)
    button.bind("<1>", button_click)
    if i % 3 == 1:
        r += 1
        c = 0
    else:
        c += 1

root.mainloop()