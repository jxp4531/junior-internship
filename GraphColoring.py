# -*- coding:utf-8 -*

from random import randint
import time
global K

#FileName为读取文件名
def ReadData(FileName):
    data = open(FileName, 'r')   
    line = data.readline()
    vertex = int(line.split(' ')[2])
    edge = int(line.split(' ')[3])
    print(vertex, int(edge))

    matrix = [([0] * vertex) for i in range(vertex)]
    while edge > 0:
        line = data.readline()
        a = line.split(' ')
        matrix[int(a[1]) - 1][int(a[2]) - 1] = 1
        matrix[int(a[2]) - 1][int(a[1]) - 1] = 1
        edge = edge - 1 
    data.close()
    return matrix

def Degree(matrix):
    a = [0, 0]
    n = len(matrix)
    for x in range(n):
        i = 0
        for y in range(n):
            if matrix[x][y]:
                i = i + 1
        if i > a[1]:
            a[0] = x
            a[1] = i
    return a 

#初始化各顶点颜色(0 ~ k-1)
def InitialColor(color, k):
    for i in range(len(color)):
        color[i] = randint(0, k-1)
    return color

#计算相邻颜色表 ACT = n * k
def CountACT(ACT, matrix, color):
    n = len(matrix)
    for x in range(n):
        for y in range(n):
            if matrix[x][y]:
                ACT[x][color[y]] = ACT[x][color[y]] + 1
    return ACT

#更新相邻颜色表
def updateACT(ACT, vertex, oldColor, newColor, matrix, color):
    length = len(matrix)
    for x in range(length):
        if matrix[vertex][x]:
            if ACT[x][oldColor] > 0:
                ACT[x][oldColor] = ACT[x][oldColor] - 1
            ACT[x][newColor] = ACT[x][newColor] + 1
    return ACT

#计算评估函数f
def CountF(ACT, color):
    f = 0
    n = len(color)
    for x in range(n):
        f = f + ACT[x][color[x]]
    return f

#新加一个禁忌
#禁忌表、相邻颜色表、顶点、旧颜色
def TabuTable(Tabu, ACT, vertex, color, myliter):
    Tabu[vertex][color] = ACT[vertex][color] + randint(1, 10) + myliter
    return Tabu

#选择一个邻域动作
def OneMove(color, ACT, Tabu, myliter):
    move = [0, 0] #冲突减少量、顶点、新颜色
    # if flag:
    #     j = randint(1, len(ACT))
    #     for x in range(n):
    #         i = ACT[x][color[x]] #当前染色的冲突数
    #         for y in range(K):
    #             if i - ACT[x][y] >= move[0] and Tabu[x][y] == 0:
    #                 j = j - 1
    #                 if j == 0 :
    #                     move[1] = x
    #                     move[2] = y
    #                     return move[1:]
    n = len(ACT)
    m = len(ACT[1])
    j = randint(2, n)
    for x in range(n):
        i = ACT[x][color[x]] #当前染色的冲突数
        for y in range(m):
            if Tabu[x][y] <= myliter:
                a = i - ACT[x][y] 
                if a >= move[0]:
                    if a == move[0]:
                        j = j - 1
                    move = a, x, y
                    if j == 0:
                        return move[1:]
    return move[1:] #顶点、新颜色

def main(file):
    k = K
    matrix = ReadData(file) #无向图邻接矩阵
    n = len(matrix) #顶点数
    a = Degree(matrix)
    color = [0 for i in range(len(matrix))]
    color = InitialColor(color, k)
    print(a, color)
    myliter = 0
    while k != 12:
        print("-------------------\n", k)
        Tabu = [([0] * k) for i in range(n)] #禁忌表
        ACT = [([0] * k) for i in range(n)] 
        ACT = CountACT(ACT, matrix, color) #相邻颜色表
        f = CountF(ACT, color) #计算评估函数
        while f:
            print(k, f, myliter)
            move = OneMove(color, ACT, Tabu, myliter) #顶点，新颜色
            # sleep(0.1)
            # print(move)
            # print(ACT)
            oldColor = color[move[0]] #旧颜色
            color[move[0]] = move[1] #新颜色
            ACT = updateACT(ACT,  move[0], oldColor, move[1], matrix, color)
            Tabu = TabuTable(Tabu, ACT, move[0], oldColor, myliter)
            # if f == CountF(ACT, color):
                # print("当前颜色数%s, 邻域动作(%s), 算不下去了..."%(k, move))
                # print("禁忌(%s, %s) ： "%(move[0], oldColor), Tabu[move[0]][oldColor])
            myliter = myliter + 1
            f = CountF(ACT, color)
        k = k - 1
        color = InitialColor(color, k)
    Tabu = [([0] * k) for i in range(len(matrix))]
    ACT = [([0] * k) for i in range(len(matrix))]
    ACT = CountACT(ACT, matrix, color)
    f = CountF(ACT, color)
    while f:
        move = OneMove(color, ACT, Tabu, myliter) #顶点，新颜色
        print(k, f, myliter)
        # print(move)
        oldColor = color[move[0]] #旧颜色
        color[move[0]] = move[1]
        ACT = updateACT(ACT,  move[0], oldColor, move[1], matrix, color)
        Tabu = TabuTable(Tabu, ACT, move[0], oldColor, myliter)
        # if f < 8:
            # print("当前颜色数%s, 邻域动作(%s), 算不下去了..."%(k, move))
            # print("禁忌(%s, %s)： %s"%(move[0], oldColor, Tabu[move[0]][oldColor]))
            # print(color, ACT)
        myliter = myliter + 1
        f = CountF(ACT, color)
    # print(k, f, color)

if __name__ == '__main__':
    file = 'DSJC500_1.txt'
    K = 12
    t1 = time.time()
    main(file)
    t2 = time.time()
    print("耗时: ", t2-t1)
