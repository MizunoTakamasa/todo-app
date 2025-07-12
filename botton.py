import tkinter as tk

def ボタンを押した():
    ラベル["text"] = "こんにちは！"

root = tk.Tk()
root.title("テストアプリ")

ボタン = tk.Button(root, text="クリックしてね", command=ボタンを押した)
ボタン.pack()

ラベル = tk.Label(root, text="")
ラベル.pack()

root.mainloop()