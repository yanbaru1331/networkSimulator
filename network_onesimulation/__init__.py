import queue
import time
import random

throughput = 1000


class timeTable:
    reqSize: int = 0
    clientNum: int = 0
    serverNum: int = 0
    clientTime: time = 0
    serverTime: time = 0


class req:
    reqSize: int = 0
    clientNum: int = 0
    clientTime: time = 0


# タスクを挿入するキューの作成
task_queue = queue.Queue()


# データセットの作成
# 引数で入力した時間分のデータを作成
def createTestSet(time):

    for i in range(0, time + 1):
        tmp = req()
        tmp.reqSize = int(random.gauss(1000, 10))
        tmp.clientNum = i
        tmp.clientTime = i
        # tmp.clientTime = i+random.poisson(1, 1)
        print(tmp)
        task_queue.put(tmp)
    return


def server():
    serverThroughput = throughput
    serverTime = 0
    while not task_queue.empty():
        # データの取得
        item = task_queue.get()
        # 　もし処理可能なサイズ以上だったとき(1s以上かかるとき)の待機処理
        if serverThroughput < item.reqSize:
            serverThroughput += throughput
        # サーバ時間と処理可能なサイズの引き算
        serverTime += item.reqSize / throughput
        serverThroughput -= item.reqSize

    return


def main():
    createTestSet(100)
    server()
    return


if __name__ == "__main__":
    main()
