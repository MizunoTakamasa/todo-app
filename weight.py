import tkinter as tk
from datetime import datetime

def 入力を表示():
    名前 = 名前エントリ.get()
    年齢 = 年齢エントリ.get()
    身長 = 身長エントリ.get()
    出力ラベル.config(text=f"名前：{名前}\n年齢：{年齢}歳\n身長：{身長}m")

def 体重を記録():
    try:
        体重 = float(体重エントリ.get())
        今日の日付 = datetime.now().strftime("%Y-%m-%d")
        with open("体重記録.txt", "a", encoding="utf-8") as file:
            file.write(f"{今日の日付},{体重}\n")
        結果ラベル.config(text=f"{今日の日付} の体重 {体重}kg を記録しました。")
    except ValueError:
        結果ラベル.config(text="正しい体重を数字で入力してください。")

# ウィンドウの作成
root = tk.Tk()
root.title("体重記録アプリ")
root.geometry("350x300")

# 名前・年齢・身長
tk.Label(root, text="名前：").grid(row=0, column=0, sticky="e")
名前エントリ = tk.Entry(root)
名前エントリ.grid(row=0, column=1)

tk.Label(root, text="年齢：").grid(row=1, column=0, sticky="e")
年齢エントリ = tk.Entry(root)
年齢エントリ.grid(row=1, column=1)

tk.Label(root, text="身長（m）：").grid(row=2, column=0, sticky="e")
身長エントリ = tk.Entry(root)
身長エントリ.grid(row=2, column=1)

# 表示ボタン
表示ボタン = tk.Button(root, text="情報を表示", command=入力を表示)
表示ボタン.grid(row=3, column=0, columnspan=2, pady=10)

出力ラベル = tk.Label(root, text="")
出力ラベル.grid(row=4, column=0, columnspan=2)

# 体重入力
tk.Label(root, text="今日の体重（kg）：").grid(row=5, column=0, sticky="e")
体重エントリ = tk.Entry(root)
体重エントリ.grid(row=5, column=1)

# 体重記録ボタン
記録ボタン = tk.Button(root, text="今日の体重を記録", command=体重を記録)
記録ボタン.grid(row=6, column=0, columnspan=2, pady=10)

結果ラベル = tk.Label(root, text="")
結果ラベル.grid(row=7, column=0, columnspan=2)

# メインループ
root.mainloop()
