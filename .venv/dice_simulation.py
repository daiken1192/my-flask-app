import numpy as np
import matplotlib.pyplot as plt

# サイコロを振る回数を設定
num_rolls = 100000

# サイコロの出目をランダムに生成 (1～6)
dice_rolls = np.random.randint(1, 7, size=num_rolls)

# 出目の平均を計算
average = np.mean(dice_rolls)
print(f"サイコロを{num_rolls}回振った平均の出目: {average:.2f}")

# 出目の分布を可視化
plt.hist(dice_rolls, bins=6, range=(0.5, 6.5), edgecolor="black", color="skyblue", rwidth=0.8)
plt.title("サイコロの出目の分布")
plt.xlabel("出目")
plt.ylabel("回数")
plt.xticks(range(1, 7))  # x軸の目盛りを1～6に設定
plt.grid(axis="y", linestyle="--", alpha=0.7)

# グラフを表示
plt.show()
