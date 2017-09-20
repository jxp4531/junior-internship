## 图染色优化
大三暑假实习第一个任务，开始使用[Python](https://github.com/LewisTian/GraphColoring/blob/master/GraphColoring.py)编写代码，跑出来效率低得要命，然后在进行下一个[拓扑图](https://github.com/LewisTian/Topology)的任务的时候重新用[C++](https://github.com/LewisTian/GraphColoring/blob/master/GraphColoring.cpp)写了一遍。
- Python版会从初始值跑到标准值，若是跑不出来就一直跑；
- C++版是直接跑初始值，能跑出来就跑出来，若是跑不出来就一直跑；

## 两者效率对比图
![ScreenShot](https://i.loli.net/2017/09/20/59c233b37e7c8.png "Contrast")

## Python(Python3.5 Windows10)
- usage: python GraphColoring.py [file path] [initial color number] [standard color number]
- example: `python GraphColoring.py ./test/DSJC125_1.txt 10 5`

## C++(Windows10)
- usage: 
  -  g++ GraphColoring.cpp
  - ./a.exe [file path] [initial color number]
- example: `./a.exe ./test/DSJC125_1.txt 5`
