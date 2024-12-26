import matplotlib.pyplot as plt
import numpy as np

# 入力データ
data = [
    "0-0.103-103-0.103",
    "1-1.1-100-0.1",
    "2-2.086-86-0.086",
    "3-3.112-112-0.112",
    "4-4.1-100-0.1",
    "5-5.097-97-0.097",
    "6-6.109-109-0.109",
    "7-7.104-104-0.104",
    "8-8.107-107-0.107",
    "9-9.081-81-0.081",
    "10-10.105-105-0.105",
]

# 0.001秒ごとのタイムスロットを初期化
start_time = 0
end_time = 10  # データ範囲の最大値
time_slots = np.arange(start_time, end_time + 0.001, 0.001)  # 0.001秒刻み
rates = np.zeros(len(time_slots))

# データ解析と分配
for entry in data:
    start, end, size, duration = map(float, entry.split("-"))
    rate = size / duration  # 処理レート (バイト/秒)

    # 0.001秒刻みに処理サイズを分配
    start_idx = int(start * 1000)  # 0.001秒刻みのインデックス
    end_idx = int(end * 1000)
    for i in range(start_idx, end_idx):
        rates[i] += rate * 0.001  # 0.001秒ごとに分配

# グラフの描画
plt.figure(figsize=(12, 6))
plt.plot(time_slots, rates, linewidth=0.7)
plt.xlabel("Time (seconds)")
plt.ylabel("Process Rate (bytes/second)")
plt.title("Processing Rate Over Time (0.001s resolution)")
plt.grid()
plt.show()
