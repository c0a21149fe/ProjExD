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

    else: #=以外のボタン
        entry.insert(tk.END, num)



root = tk.Tk()
root.title("tk")
root.geometry("400x600")

entry = tk.Entry(root, justify="right", width=14, font=("", 40))
entry.grid(row=0, column=0, columnspan=4)


r, c = 1, 0
funcs = ["↶", "↷", "√", "C"]
for func in funcs:
    func_key = tk.Button(root, text = func, width=4, height=2, font=("", 30),
                         background="#dcdcdc")
    func_key.grid(row=r, column=c)
    func_key.bind("<1>", button_click)
    c += 1


r, c = 2, 0
for i in range(9, -1, -1):

    num_key = tk.Button(root, text=i, width=4, height=2, font=("", 30))
    num_key.grid(row=r, column=c)
    num_key.bind("<1>", button_click)
    if i % 3 == 1:
        r += 1
        c = 0
        if i == 1:
            c = 1
    else:
        c += 1
    print(c)

r, c = 2, 3
operators = ["*", "-", "+", "="]
for ope in operators:
    if ope != "=":
        button = tk.Button(root, text=ope, width=4, height=2,
                        font=("", 30), background="#dcdcdc")
    else:
        button = tk.Button(root, text=ope, width=4, height=2,
                           font=("", 30), background="#40e0d0")
    button.grid(row = r, column=c)
    button.bind("<1>", button_click)
    r += 1


root.mainloop()