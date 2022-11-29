import tkinter as tk
import tkinter.messagebox as tkm


rireki = [""]
f_rireki = []

def num_click(event):
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo("", f"{num}ボタンがクリックされました")
    entry.insert(tk.END, num)


def ope_fun_click(event):
    global rireki, f_rireki
    operators = {"×":"*", "-":"-", "+":"+", "÷":"/"}
    btn = event.widget
    ipt = btn["text"]
    

    if ipt in operators.keys():
        if entry.get()[-1] in operators.values():
            pass
        else:
            entry.insert(tk.END, operators[ipt])

    if ipt == "=":
        siki = entry.get()
        rireki.append(siki)
        # for k, v in operators.items():
        #     siki.replace(k, v)
        
        ans = eval(siki)
        entry.delete(0, tk.END)
        entry.insert(tk.END, ans)

    elif ipt == "C":
        rireki.append(entry.get())
        entry.delete(0, tk.END)

    elif ipt == "↶":
        p_siki = rireki.pop(-1)
        f_rireki.append(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, p_siki)

    elif ipt == "↷":
        p_siki = entry.get()
        try:
            rireki.append(p_siki)
            entry.delete(0, tk.END)
            entry.insert(tk.END, f_rireki.pop(-1))
        except IndexError:
            pass
        
    print(rireki)


root = tk.Tk()
root.title("tk")
root.geometry("400x600")

entry = tk.Entry(root, justify="right", width=14, font=("", 40))
entry.grid(row=0, column=0, columnspan=4)


r, c = 1, 0
funcs = ["↶", "↷", "÷", "C"]
for func in funcs:
    func_key = tk.Button(root, text = func, width=4, height=2, font=("", 30),
                         background="#dcdcdc")
    func_key.grid(row=r, column=c)
    func_key.bind("<1>", ope_fun_click)
    c += 1


r, c = 2, 0
for i in range(9, -1, -1):

    num_key = tk.Button(root, text=i, width=4, height=2, font=("", 30))
    num_key.grid(row=r, column=c)
    num_key.bind("<1>", num_click)
    if i % 3 == 1:
        r += 1
        c = 0
        if i == 1:
            c = 1
    else:
        c += 1
    print(c)

r, c = 2, 3
operators = ["×", "-", "+", "="]
for ope in operators:
    if ope != "=":
        button = tk.Button(root, text=ope, width=4, height=2,
                        font=("", 30), background="#dcdcdc")
    else:
        button = tk.Button(root, text=ope, width=4, height=2,
                           font=("", 30), background="#40e0d0")
    button.grid(row = r, column=c)
    button.bind("<1>", ope_fun_click)
    r += 1


root.mainloop()