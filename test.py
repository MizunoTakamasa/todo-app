import matplotlib.pyplot as plt
import os
from datetime import datetime

def 入力を取得():
    名前 = input("あなたの名前を入力してください：")
    年齢 = int(input("年齢を入力してください："))
    身長 = float(input("身長(m)を入力してください："))
    return 名前, 年齢, 身長

def BMIを計算(体重, 身長):
    return 体重 / (身長 ** 2)

def 判定を出す(BMI):
    if BMI < 18.5:
        return "やせ型"
    elif BMI < 25:
        return "普通体重"
    elif BMI < 30:
        return "肥満（1度）"
    else:
        return "肥満（2度以上）"

def 体重記録を読み込み():
    記録 = []
    if os.path.exists("体重記録.txt"):
        with open("体重記録.txt", "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    日付文字列, 体重値 = parts
                    try:
                        体重値 = float(体重値)
                        記録.append((日付文字列, 体重値))
                    except:
                        pass
    return 記録

def 体重記録を追記(日付文字列, 新体重):
    with open("体重記録.txt", "a", encoding="utf-8") as file:
        file.write(f"{日付文字列},{新体重}\n")

def 体重記録を表示(記録):
    if not 記録:
        print("記録がありません。")
        return
    print("\n過去の体重記録：")
    for i, (date, weight) in enumerate(記録, 1):
        print(f"{i}日目 {date}：{weight}kg")

def グラフを表示(記録):
    if not 記録:
        print("記録がないためグラフは表示できません。")
        return
    日付 = [d for d, _ in 記録]
    体重 = [w for _, w in 記録]
    plt.plot(日付, 体重, marker='o', color='blue')
    plt.title("体重推移")
    plt.xlabel("日付")
    plt.ylabel("体重 (kg)")
    plt.grid(True)
    plt.tight_layout()
    plt.xticks(rotation=45)
    plt.show()

def メニュー():
    print("\n===== 体重管理メニュー =====")
    print("1. 体重記録を追加")
    print("2. 過去の体重記録を表示")
    print("3. BMI計算と判定を表示")
    print("4. 体重推移グラフを表示")
    print("5. 終了")
    choice = input("番号を入力してください：")
    return choice

def main():
    名前, 年齢, 身長 = 入力を取得()
    記録 = 体重記録を読み込み()
    while True:
        choice = メニュー()
        if choice == "1":
            try:
                新体重 = float(input("今日の体重(kg)を入力してください："))
                今日の日付 = datetime.now().strftime("%Y-%m-%d")
                記録.append((今日の日付, 新体重))
                体重記録を追記(今日の日付, 新体重)
                print("体重を記録しました。")
            except ValueError:
                print("数値を正しく入力してください。")
        elif choice == "2":
            体重記録を表示(記録)
        elif choice == "3":
            if not 記録:
                print("体重記録がないためBMIは計算できません。")
            else:
                最新体重 = 記録[-1][1]
                BMI = BMIを計算(最新体重, 身長)
                判定 = 判定を出す(BMI)
                print(f"最新の体重は {最新体重}kg です。")
                print(f"BMIは {BMI:.2f} で、判定は {判定} です。")
        elif choice == "4":
            グラフを表示(記録)
        elif choice == "5":
            print("終了します。")
            break
        else:
            print("正しい番号を入力してください。")

if __name__ == "__main__":
    main()
