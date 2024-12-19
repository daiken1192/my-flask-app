import matplotlib.pyplot as plt

# データの準備
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# グラフの作成
plt.plot(x, y, label="y = x^2", color="blue", marker="o")

# グラフの装飾
plt.title("My First Graph")  # グラフのタイトル
plt.xlabel("X-axis")        # X軸のラベル
plt.ylabel("Y-axis")        # Y軸のラベル
plt.legend()                # 凡例を追加

# グラフの表示
plt.show()
