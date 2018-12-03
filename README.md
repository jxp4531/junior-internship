## 图染色优化
大三暑假实习(2017/6/28-7/31)第一个任务，开始使用 `Python` 编写代码，跑出来效率低得要命，然后在进行下一个 [拓扑图](https://github.com/LewisTian/Topology) 的任务的时候重新用 `C++` 写了一遍。
- Python 版会从初始值跑到标准值(或者跑不出来)
- C++ 版是直接跑初始值，并未设置标准值，即跑完初始值就结束了

注：最优解参考 [A memetic algorithm for graph coloring](http://www.sciencedirect.com/science/article/pii/S0377221709005177)

## 两者效率对比图
![ScreenShot](https://i.loli.net/2017/09/20/59c233b37e7c8.png "Contrast")

## 使用说明
### Python (Python3.5+ Windows10)
- [usage]: python GraphColoring.py [file path] [initial color number] [standard color number]
- [example]: `python GraphColoring.py ./test/DSJC125_1.txt 10 5`

### C++ (Windows10)
- [usage]: 
```
>> g++ GraphColoring.cpp
>> ./a.exe [file path] [initial color number]
```
- [example]: `./a.exe ./test/DSJC125_1.txt 5`
