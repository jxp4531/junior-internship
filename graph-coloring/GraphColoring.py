#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-03 16:04:28
# @Author  : Lewis Tian (chasetichlewis@gmail.com)
# @Link    : https://github.com/LewisTian
# @Version : Python3.5

from random import randint
import time
import sys
# from threading import Thread

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

#计算相邻颜色表 ACT = n * k
def CountACT(ACT, matrix, color):
    n = len(matrix)
    for x in range(n):
        for y in range(x+1, n):
            if matrix[x][y]:
                ACT[x][color[y]] = ACT[x][color[y]] + 1
                ACT[y][color[x]] = ACT[y][color[x]] + 1
    return ACT

#计算评估函数f
def CountF(ACT, color):
    f = 0
    n = len(color)
    for x in range(n):
        f = f + ACT[x][color[x]]
    return f

#选择一个邻域动作
def OneMove(color, ACT, Tabu, iteration, f):
    move = [-1, 0, 0] #冲突减少量、顶点、新颜色
    n = len(ACT) #顶点数
    m = len(ACT[1]) #颜色数
    bestCount = 2
    for x in range(n):
        i = ACT[x][color[x]] #当前节点的冲突数
        if i:
            for y in range(m):
                if y != color[x]:
                    a = i - ACT[x][y]
                    if a > 0: #冲突减少>0
                        if a > move[0]:  #找出最优的一步
                            if Tabu[x][y] <= iteration: #没禁忌
                                move = a, x, y
                                bestCount = 2
                            else: #禁忌
                                tmp_color = color[:]
                                tmp_color[x] = y
                                if  CountF(ACT, tmp_color) < f:
                                    move = a, x, y
                                    bestCount = 2
                        elif a == move[0] and Tabu[x][y] <= iteration: #若有多个最优则随机选择一个
                            if randint(1, n) % bestCount == 0:
                                move = a, x, y
                            bestCount += 1
                    elif Tabu[x][y] <= iteration: #找不到能减少冲突的
                        if a > move[0]:
                            move = a, x, y
                            bestCount = 2
                        elif a == move[0]:
                            if randint(1, n) % bestCount == 0:  
                                move = a, x, y
                            bestCount += 1
    return move[1:] #顶点、新颜色

def main(file, opt):
    k = K
    t1 = time.time()
    matrix = ReadData(file) #邻接矩阵
    n = len(matrix) #顶点数
    color = [0 for i in range(n)]
    iteration = 0
    #初始化各顶点颜色(0 ~ k-1)
    for i in range(n):
        color[i] = randint(0, k-1)
    while k >= opt:
        print("-------------------\n", k)
        Tabu = [([0] * k) for i in range(n)] #禁忌表
        ACT = [([0] * k) for i in range(n)] 
        ACT = CountACT(ACT, matrix, color) #相邻颜色表
        f = CountF(ACT, color) #计算评估函数
        bestF = f
        while f:
            test = 0
            move = OneMove(color, ACT, Tabu, iteration, bestF) #顶点，新颜色
            oldColor = color[move[0]] #旧颜色
            color[move[0]] = move[1] #新颜色
            #更新相邻颜色表
            for x in range(n):
                if matrix[move[0]][x]:
                    ACT[x][oldColor] = ACT[x][oldColor] - 1
                    ACT[x][move[1]] = ACT[x][move[1]] + 1
            #禁忌
            Tabu[move[0]][oldColor] = f + randint(1, 10) + iteration
            iteration = iteration + 1
            f = CountF(ACT, color)
            if f < bestF:
                bestF = f
                print(bestF,iteration)
            # print(f)
        k = k - 1
        for x in range(n):
            if color[x] == k:
                color[x] = randint(0, k-1)
    t2 = time.time()
    print("耗时: ", t2-t1)
    print(k, f, iteration)
    for x in range(n):
        for y in range(x+1, n):
            if matrix[x][y] and color[x] == color[y]:
                print(x, y, color[x], color[y])
    
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("文件名 初始颜色数 参考值")
    else:
        file = sys.argv[1]
        K = int(sys.argv[2])
        val = int(sys.argv[3])
        main(file, val)
