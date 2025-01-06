import math
import queue
import time
import random
from dataclasses import dataclass

# import copy

throughput = 1000
testTime = 10
response = []
serverNum = 3
timeRate = 50
timeOutRate = 2


# class timeTable:
#     reqSize: int = 0
#     clientNum: int = 0
#     serverNum: int = 0
#     clientTime: time = 0
#     serverTime: time = 0


@dataclass
class Server:
    serverId: int = 0
    serverTime: time = 0


@dataclass
class Req:
    reqSize: int = 0
    clientNum: int = 0
    clientTime: time = 0


class Graph:
    reqSize: int = 0
    # processingTime: time = 0
    startServerTime: time = 0
    finishServerTime: time = 0
    startClietTime: time = 0


# タスクを挿入するキューの作成
RR_queue = queue.Queue()
# RR_graph_queue = queue.Queue()


# データセットの作成
# 引数で入力した時間分のデータを作成
def createTestSet(time):

    # タイムレートの分だけリクエストのテンプレを作成
    # RR_DataSet = [
    #     Req(reqSize=0, clientNum=0, clientTime=0)
    #     for i in range(0, (time + 1) * timeRate)
    # ]
    clientTime = 0
    for _ in range((time + 1)):
        for _ in range(timeRate):
            # for _ in range(serverNum):
            # ここtmpで値取る必要なくない？
            tmp = Req()
            tmp.reqSize = int(random.gauss(500, 10))
            tmp.clientNum = 1
            tmp.clientTime = clientTime
            # tmp.clientTime = i+random.poisson(1, 1)
            # print(tmp)
            RR_queue.put(tmp)
            # RR_DataSet[i] = tmp
        clientTime += 1
    # 時間軸で整列するようなフィルタ処理をする
    # もう一つの方法_queue = copy.deepcopy(task_queue)
    return


# # 　サーバの処理
# def server():
#     # serverThroughput = throughput
#     serverTime = 0
#     while not task_queue.empty():
#         # ロードバランサの処理はここに書く
#         # データの取得
#         item = task_queue.get()
#         tmp = graph()
#         serverTime = round(max(serverTime, item.clientTime), 4)
#         # サーバ時間と処理可能なサイズの引き算
#         tmp.startServerTime = serverTime
#         serverTime += round(item.reqSize / throughput, 4)
#         # serverThroughput -= item.reqSize

#         # tmp.processingTime = round(item.reqSize / throughput, 4)
#         tmp.reqSize = item.reqSize
#         # tmp.finishServerTime = round(serverTime, 4)
#         graph_queue.put(tmp)

#     return


# 　ラウンドロビンサーバの処理
def RR_server():
    # serverThroughput = throughput
    servers = [Server(serverId=i, serverTime=0) for i in range(serverNum)]
    RR_graph = [Graph() for i in range(RR_queue.qsize())]
    i: int = 0
    while not RR_queue.empty():
        # ラウンドロビンロードバランサ
        # 1->2->3で順番に処理する
        for s in servers:
            if RR_queue.empty():
                break
            # print(s)
            # ロードバランサの処理はここに書く
            # データの取得
            item = RR_queue.get()
            # タイムアウトの処理
            # 2秒以上遅延して受け取ったリクエストの場合は処理せずパスする
            if s.serverTime - item.clientTime > timeOutRate:
                continue
            tmp = Graph()
            tmp.reqSize = item.reqSize
            # クライアント時間の記録
            tmp.startClietTime = item.clientTime
            s.serverTime = round(max(s.serverTime, item.clientTime), 4)
            # サーバ時間と処理可能なサイズの引き算
            tmp.startServerTime = s.serverTime
            s.serverTime += round(item.reqSize / throughput, 4)
            tmp.finishServerTime = s.serverTime

            RR_graph[i] = tmp
            i += 1
            # RR_graph_queue.put(tmp)
    return RR_graph


def viewGraph(res):
    prosessRate = [0] * (testTime + timeOutRate)
    # プロセスレートの計算
    # 時間を切り上げてn.1~n+1秒の間に発生したリクエストをカウント
    # 配列は0からスタートなので、n秒のリクエストはn-1番目の要素にカウント
    # は切り捨てと等しい(-1)処理
    # print("RR_graph_queue.length=", RR_graph_queue.qsize())
    # while not RR_graph_queue.empty():
    #     a = RR_graph_queue.get()
    #     prosessRate[math.floor(a.startServerTime)] += 1
    for data in res:
        # print("data=", data.finishServerTime)
        if data.finishServerTime == 0:
            continue
        prosessRate[math.floor(data.startServerTime)] += 1
    print(prosessRate)
    # このあとにグラフを各処理
    return


if __name__ == "__main__":
    # RR_DataSet = createTestSet(testTime)
    # res = RR_server(RR_DataSet)
    createTestSet(testTime)
    res = RR_server()
    # for data in res:å
    # print(data.startServerTime)
    viewGraph(res)
