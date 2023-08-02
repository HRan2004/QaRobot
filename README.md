
# 本地简单对话机器人

### 一、快速开始

```yaml
# 安装相关依赖
pip install chatterbot spacy

# 运行 robot.py 开始对话
python robot.py
```

### 二、训练自己的对话数据

```text
1. 填写对话数据到 datasets.py 文件中。
   数据格式为二维列表，参考现有对话内容即可。
   
2. 运行 train.py 开始训练。
   如果需要清除以前的训练内容，训练前请删除 db.sqlite3 文件。

3. 运行 robot.py 即可开始对话。
```
