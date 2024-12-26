import math
import queue
import time
import random

throughput = 1000
testTime = 100
response = []


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


class graph:
    reqSize: int = 0
    # processingTime: time = 0
    startServerTime: time = 0
    # finishServerTime: time = 0


# タスクを挿入するキューの作成
task_queue = queue.Queue()
graph_queue = queue.Queue()


# データセットの作成
# 引数で入力した時間分のデータを作成
def createTestSet(time):

    for i in range(0, time + 1):
        tmp = req()
        tmp.reqSize = int(random.gauss(1000, 10))
        tmp.clientNum = i
        tmp.clientTime = i
        # tmp.clientTime = i+random.poisson(1, 1)
        # print(tmp)
        task_queue.put(tmp)
    return


# 　サーバの処理
def server():
    # serverThroughput = throughput
    serverTime = 0
    while not task_queue.empty():
        # データの取得
        item = task_queue.get()
        tmp = graph()
        serverTime = round(max(serverTime, item.clientTime), 4)
        # サーバ時間と処理可能なサイズの引き算
        tmp.startServerTime = serverTime
        serverTime += round(item.reqSize / throughput, 4)
        # serverThroughput -= item.reqSize

        # tmp.processingTime = round(item.reqSize / throughput, 4)
        tmp.reqSize = item.reqSize
        # tmp.finishServerTime = round(serverTime, 4)
        graph_queue.put(tmp)

    return


def viewGraph():
    prosessRate = [0] * (testTime + 1)
    # プロセスレートの計算
    # 時間を切り上げてn.2~n+1秒の間に発生したリクエストをカウント
    # 配列は0からスタートなので、n秒のリクエストはn-1番目の要素にカウント
    # は切り捨てと等しい(-1)処理
    while not graph_queue.empty():
        a = graph_queue.get()
        prosessRate[math.floor(a.startServerTime)] += 1
    print(prosessRate)
    return


if __name__ == "__main__":
    createTestSet(testTime)
    server()
    viewGraph()
