import random

def main():
    print("★ おみくじプログラム ★")
    input("引く準備ができたらEnterキーを押してください...\n")

    fortunes = ["大吉", "中吉", "小吉", "吉", "末吉", "凶", "大凶"]
    result = random.choice(fortunes)

    print(f"今日の運勢は...『{result}』です！")
    if result == "大吉":
        print("素晴らしい一日が待っています！")
    elif result == "大凶":
        print("少し慎重に行動しましょう。でも、明日は良いことがあるかも！")
    else:
        print("平穏な一日を楽しんでください！")

if __name__ == "__main__":
    main()
    