import os

FILENAME = "todo.txt"

def タスクを読む():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]

def タスクを書き出す(タスクリスト):
    with open(FILENAME, "w", encoding="utf-8") as f:
        for task in タスクリスト:
            f.write(task + "\n")

def タスクを追加():
    task = input("追加するタスクを入力してください: ")
    tasks = タスクを読む()
    tasks.append(task)
    タスクを書き出す(tasks)
    print("タスクを追加しました。")

def タスクを表示():
    tasks = タスクを読む()
    if not tasks:
        print("タスクはありません。")
    else:
        print("\nTODOリスト：")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def タスクを削除():
    タスクを表示()
    try:
        index = int(input("削除するタスクの番号を入力してください: ")) - 1
        tasks = タスクを読む()
        if 0 <= index < len(tasks):
            削除タスク = tasks.pop(index)
            タスクを書き出す(tasks)
            print(f"「{削除タスク}」を削除しました。")
        else:
            print("番号が無効です。")
    except ValueError:
        print("番号を正しく入力してください。")

def メニュー():
    while True:
        print("\n=== TODOリストメニュー ===")
        print("1. タスク追加2")
        print("2. タスク表示2")
        print("3. タスク削除2")
        print("4. 終了2")
        choice = input("番号を選んでください: ")

        if choice == "1":
            タスクを追加()
        elif choice == "2":
            タスクを表示()
        elif choice == "3":
            タスクを削除()
        elif choice == "4":
            print("終了します。")
            break
        else:
            print("正しい番号を入力してください。")

if __name__ == "__main__":
    メニュー()
