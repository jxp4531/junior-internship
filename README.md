# Topology Visualization
## 拓扑图可视化
- 本项目为大三暑假实习 (2017/6/28-2017/7/31) 第二个任务，第一个任务为 [图着色编程](https://github.com/LewisTian/GraphColoring)
- 基于 [D3v4.js](https://github.com/d3/d3) 及其示例 [Curved Links](https://bl.ocks.org/mbostock/4600693) 的拓扑图可视化工具.
- [项目修改日志](./Log.md)

## 使用方法
配置好 web 服务器后, 在浏览器地址栏输入 `$(address):$(port)[/index.html]?$(file).json` 访问.
其中 `$(address)` 是服务器的 IP 地址或域名, `$(port)` 是端口, `$(file)` 是输入文件名, 使用数字命名可以使用方向键翻页.

### 示例
- https://lewistian.github.io/show/?0.json
- http://127.0.0.1?0.json
- http://127.0.0.1:8080?0.json

由于安全原因, chrome 等浏览器禁止 js 读写本地文件, 需要在启动时添加 `--allow-file-access-from-files` 参数才能不搭建 web 服务器使用该工具. 

## 简单操作说明
详细操作说明在页面点击`显示帮助`按钮或者敲击`h`键
- ← [方向左键]: 加载前一个拓扑图
- → [方向右键]: 加载下一个拓扑图