import tkinter as tk
from datetime import datetime
import matplotlib.pyplot as plt
import os

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

def BMIを計算():
    try:
        身長 = float(身長エントリ.get())
        体重 = float(体重エントリ.get())
        BMI = 体重 / (身長 ** 2)
        if BMI < 18.5:
            判定 = "やせ型"
        elif BMI < 25:
            判定 = "普通体重"
        elif BMI < 30:
            判定 = "肥満（1度）"
        else:
            判定 = "肥満（2度以上）"
        BMIラベル.config(text=f"BMI：{BMI:.2f}（{判定}）")
    except ValueError:
        BMIラベル.config(text="体重と身長を正しく入力してください。")

def グラフを表示():
    if not os.path.exists("体重記録.txt"):
        結果ラベル.config(text="体重記録ファイルがありません。")
        return

    日付リスト = []
    体重リスト = []

    with open("体重記録.txt", "r", encoding="utf-8") as file:
        for line in file:
            try:
                日付, 体重 = line.strip().split(",")
                日付リスト.append(日付)
                体重リスト.append(float(体重))
            except:
                continue
    if not 日付リスト:
        結果ラベル.config(text="有効な体重記録がありません。")
        return

    plt.figure(figsize=(8, 4))
    plt.plot(日付リスト, 体重リスト, marker="o", color="blue")
    plt.title("体重の推移")
    plt.xlabel("日付")
    plt.ylabel("体重 (kg)")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def 記録一覧を表示():
    記録リスト.delete(0, tk.END)
    if not os.path.exists("体重記録.txt"):
        return
    with open("体重記録.txt", "r", encoding="utf-8") as f:
        for line in f:
            記録リスト.insert(tk.END, line.strip())

def 記録を削除():
    選択 = 記録リスト.curselection()
    if not 選択:
        結果ラベル.config(text="削除する記録を選んでください。")
        return

    index = 選択[0]
    with open("体重記録.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    del lines[index]

    with open("体重記録.txt", "w", encoding="utf-8") as f:
        f.writelines(lines)

    記録一覧を表示()
    結果ラベル.config(text="記録を削除しました。")

def 記録を修正():
    選択 = 記録リスト.curselection()
    if not 選択:
        結果ラベル.config(text="修正する記録を選んでください。")
        return

    index = 選択[0]
    新体重 = 修正エントリ.get()

    try:
        新体重 = float(新体重)
    except ValueError:
        結果ラベル.config(text="正しい体重を入力してください。")
        return

    with open("体重記録.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    日付 = lines[index].split(",")[0]
    lines[index] = f"{日付},{新体重}\n"

    with open("体重記録.txt", "w", encoding="utf-8") as f:
        f.writelines(lines)

    記録一覧を表示()
    結果ラベル.config(text="記録を修正しました。")


# ウィンドウ作成
root = tk.Tk()
root.title("体重記録アプリ")
root.geometry("280x585")

# 名前・年齢・身長入力
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
表示ボタン.grid(row=3, column=0, columnspan=2, pady=5)

出力ラベル = tk.Label(root, text="")
出力ラベル.grid(row=4, column=0, columnspan=2)

# 体重入力
tk.Label(root, text="今日の体重（kg）：").grid(row=5, column=0, sticky="e")
体重エントリ = tk.Entry(root)
体重エントリ.grid(row=5, column=1)

# 記録・BMI・グラフボタン
記録ボタン = tk.Button(root, text="今日の体重を記録", command=体重を記録)
記録ボタン.grid(row=6, column=0, columnspan=2, pady=5)

BMIボタン = tk.Button(root, text="BMIを計算", command=BMIを計算)
BMIボタン.grid(row=7, column=0, columnspan=2, pady=5)

グラフボタン = tk.Button(root, text="グラフを表示", command=グラフを表示)
グラフボタン.grid(row=8, column=0, columnspan=2, pady=5)

# 出力ラベル
結果ラベル = tk.Label(root, text="")
結果ラベル.grid(row=9, column=0, columnspan=2)

BMIラベル = tk.Label(root, text="")
BMIラベル.grid(row=10, column=0, columnspan=2)

# 記録一覧と操作
tk.Label(root, text="記録一覧").grid(row=11, column=0, columnspan=2)
記録リスト = tk.Listbox(root, width=35)
記録リスト.grid(row=12, column=0, columnspan=2)

tk.Button(root, text="記録を表示", command=記録一覧を表示).grid(row=13, column=0, pady=2)
tk.Button(root, text="選択して削除", command=記録を削除).grid(row=13, column=1, pady=2)

tk.Label(root, text="新しい体重（kg）：").grid(row=14, column=0, sticky="e")
修正エントリ = tk.Entry(root)
修正エントリ.grid(row=14, column=1)

tk.Button(root, text="選択して修正", command=記録を修正).grid(row=15, column=0, columnspan=2, pady=2)

# 実行
root.mainloop()