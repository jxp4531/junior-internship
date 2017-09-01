/**
 * 
 * @authors Lewis Tian (chasetichlewis@gmail.com)
 * @date    2017-08-30 14:42:01
 * @version $Id$
 */
#include <iostream>
#include <fstream>
#include <stdlib.h> 
#include <time.h>
#include <sys/time.h>
using namespace std;

int vertex;//顶点数
int k;//初始设定的染色数
int bestF;//历史最优冲突数
unsigned long iteration;//迭代次数

void InitACT(int ** matrix, int *color, int ** &ACT){
    for (int x = 0; x < vertex; ++x){
        for (int y = x+1; y < vertex; ++y){
            if(matrix[x][y]){
                ACT[x][color[y]]++;
                ACT[y][color[x]]++;
            }
        }
    }
}

int countF(int **ACT, int *color){
    int f = 0;
    for (int i = 0; i < vertex; ++i){
        f += ACT[i][color[i]];
    }   
    return f;
}

int *OneMove(int *color, int **ACT, int **Tabu){
    int maxReduce = -1;
    int *move = new int[2];
    move[0] = 0, move[1] = 0;
    int bestCount = 2;
    int *tmp  =  new int [vertex];
    for (int i = 0; i < vertex; ++i){
        tmp[i] = color[i];
    }
    for (int i = 0; i < vertex; ++i){
        if (ACT[i][color[i]]){ //有冲突的节点
            for (int j = 0; j < k; ++j){
                if(j != color[i]){
                    int a = ACT[i][color[i]] - ACT[i][j];
                    if (a > 0){ //冲突减少>0
                        if (a > maxReduce){
                            if (Tabu[i][j] <= iteration){ //没禁忌
                                maxReduce = a;
                                move[0] = i, move[1] = j;
                                bestCount = 2;
                            }
                            else{//禁忌
                                int tmp_old = tmp[i];
                                tmp[i] = j;
                                if (countF(ACT, tmp) < bestF){
                                    maxReduce = a;
                                    move[0] = i, move[1] = j;
                                    bestCount = 2;
                                }
                                tmp[i] = tmp_old;
                            }
                        }
                        else if (a == maxReduce && Tabu[i][j] <= iteration){
                            if (rand() % bestCount == 0){
                                maxReduce = a;
                                move[0] = i, move[1] = j;
                            }
                            bestCount++;
                        }
                    }
                    //找不到减少大于0
                    else if (Tabu[i][j] <= iteration){
                        if (a > maxReduce){
                            maxReduce = a;
                            move[0] = i, move[1] = j;
                            bestCount = 2;
                        }
                        else if (a == maxReduce){
                            if (rand() % bestCount == 0){
                                maxReduce = a;
                                move[0] = i, move[1] = j;
                            }
                            bestCount += 1;
                        }
                    }
                }
            }
        }
    }
    delete tmp;
    return move; //顶点、新颜色
}

int main(int argc, char const *argv[]){
    if (argc < 3) {
       cout<<"[usage].\\a.exe .\\test\\DSJC125_5.txt 5";
       return -1;
    }
    k = atoi(argv[2]);//初始解
    iteration = 0;//迭代次数
    //读取文件
    FILE *file;
    struct timeval start, finish;

    if((file = fopen(argv[1], "r")) == NULL){
        cout<<"cannot open the file!";
        return -1;
    }

    char buf[256];
    int v1, v2;
    fgets(buf, 255, file);
    sscanf(buf, "%*s%*s%d%d", &vertex);
    int **matrix = new int* [vertex];//禁忌表
    for (int i = 0; i < vertex; ++i){
        matrix[i] = new int [vertex];
    }
    for (int i = 0; i < vertex; ++i){
        for (int j = 0; j < vertex; ++j){
            matrix[i][j] = 0;
        }
    }

    while (fgets(buf, 255, file) != NULL) {
        sscanf(buf, "%*s%d%d", &v1, &v2);
        matrix[v1-1][v2-1] = 1;
        matrix[v2-1][v1-1] = 1;
    }
    //声明所有表
    int *color = new int [vertex];//颜色表
    int **ACT = new int* [vertex];//相邻颜色表
    int **Tabu = new int* [vertex];//禁忌表
    for (int i = 0; i < vertex; ++i){
        ACT[i] = new int [k];
    }

    for (int i = 0; i < vertex; ++i){
        Tabu[i] = new int [k];
    }

    for (int i = 0; i < vertex; ++i)
        for (int j = 0; j < k; ++j){
            ACT[i][j]=0;
            Tabu[i][j]=0;
        }

    srand(time(NULL));
    //初始化节点颜色
    for (int i = 0; i < vertex; ++i){
        color[i] = (rand() % k);
    }

    gettimeofday(&start,0);
    //计算相邻颜色表
    InitACT(matrix, color, ACT);

    int f = countF(ACT, color);
    bestF = f;
    int *move;
    int oldColor;
    while(bestF > 0){
        move = OneMove(color, ACT, Tabu);
        oldColor = color[move[0]];//保存旧颜色
        color[move[0]] = move[1];//更新颜色
        //更新相邻颜色表
        for (int x = 0; x < vertex; ++x){
            if (matrix[move[0]][x]){
                ACT[x][oldColor]--;
                ACT[x][move[1]]++;
            }
        }
        //禁忌
        Tabu[move[0]][oldColor] = f + rand()%10 + iteration;
        iteration++;
        f = countF(ACT, color);
        if (f < bestF){
            bestF = f;
        }
        // delete move;
    }
    gettimeofday(&finish,0);
    double cost = 1000*(finish.tv_sec-start.tv_sec)+(finish.tv_usec-start.tv_usec)/1000;
    printf("cost: %lfms %ul\n ", cost, iteration);
    ofstream out;  
    out.open("LOG.txt", ios::app);
    if (out.is_open()){
        out<<"file: "<<argv[1]<<endl;
        out<<"best result: "<<k<<endl;
        out<<"run cost: "<<cost<<"ms, iteration: "<<iteration<<endl;
        out<<"--------------------------"<<endl;
        out.close();  
     }
    delete color;
    delete []ACT;
    delete []Tabu;
    delete []matrix;
    return 0;
}
