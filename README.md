# Topology Visualization
## 拓扑图可视化
基于 [D3v4.js](https://github.com/d3/d3) 及其示例 [Curved Links](https://bl.ocks.org/mbostock/4600693) 的拓扑图可视化工具.

## 使用方法:
配置好 web 服务器后, 在浏览器地址栏输入 `$(address):$(port)[/index.html]?$(file).json` 访问.
其中 `$(address)` 是服务器的 IP 地址或域名, `$(port)` 是端口, `$(file)` 是输入文件名, 使用数字命名可以使用方向键翻页.

示例
- https://lewistian.github.io/show/?0.json
- http://127.0.0.1?0.json
- http://127.0.0.1:8080?0.json

由于安全原因, chrome 等浏览器禁止 js 读写本地文件, 需要在启动时添加 `--allow-file-access-from-files` 参数才能不搭建 web 服务器使用该工具. 
    
## 拓扑图界面内的操作方式和基本元素解释

### 图中可进行的操作
1. 当点击节点时会隐藏或者显示该节点的ID，同时在Node properties显示出该节点的信息
2. 当点击边时会在Link properties显示出该边的信息
3. 在图中可通过滚轮放大缩小图片

### 按钮的使用
1. 隐藏所有标签：即隐藏所有节点的信息
2. 显示所有标签：即显示所有节点的信息
3. 停止迭代拓扑图：停止拓扑图的迭代，再次点击继续迭代
4. 保存为Json文件：将节点的信息保存到Json中
5. 将svg另存为图片：将svg以图片的形式保存

### Simulation properties
1. Strength：节点间斥力的调节
2. Distance：边长度的调节
3. Iterations：迭代次数的调节

### Note properties
1. Node'ID：表示当前显示节点的ID
2. Color：节点颜色的调节
3. Radius：节点大小的调节

### Link properties
1. Link'ID：表示当前显示边的ID
2. Color：边的颜色的调节
3. Width：边的宽度的调节

## [修改日志](./log.md)

### 当前效果图可访问[网页](https://lewistian.github.io/show/?0.json)

