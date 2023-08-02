
# 本地简单对话机器人

### 一、快速开始

```yaml
# 安装相关依赖
pip install chatterbot spacy

# 需要使用cuda版本spacy可以参考官网文档
https://spacy.io/usage

# 下载中文基础模型
python -m spacy download zh_core_web_sm

# 运行 robot.py 开始对话
python robot.py
```

```yaml
# 需要使用虚拟环境可按下述方式操作
python -m venv .env
source .env/bin/activate
pip install -U pip setuptools wheel
pip install -U spacy
```

<br/>

### 二、训练自己的对话数据

```text
1. 填写对话数据到 datasets.py 文件中。
   数据格式为二维列表，参考现有对话内容即可。
   
2. 运行 train.py 开始训练。
   如果需要清除以前的训练内容，训练前请删除 db.sqlite3 文件。

3. 运行 robot.py 即可开始对话。
```

<br/>

### 三、常见问题解决

```text
报错:
AttributeError: module 'collections' has no attribute 'xxx'

原因:
Python 3.10+ 版本 collections 将 等一些属性放到了 collections.abc 子模块下。
所以会出现 collections’ has no attribute 的错误。

解决:
找到报错文件，修改 collections.xxx 为 collections.abc.xxx 即可。
```

```text
错误:
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.

原因:
安装环境时，已存在不同版本的包。

解决:
卸载版本不一致的包或者使用虚拟环境。
```
