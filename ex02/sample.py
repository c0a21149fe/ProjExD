import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    tkm.showinfo("aaa", "bbb")

root = tk.Tk()
root.title("おためし")
root.geometry("500x200")

button = tk.Button(root, text="押すな", bg="red", activebackground="blue")
button.bind("<1>", button_click)
button.pack()

entry = tk.Entry(root, width=30, fg="purple")
entry.insert(tk.END, "fugapiyo")
entry.pack()

tkm.showerror("たいとる", "めっせーじ")


root.mainloop()