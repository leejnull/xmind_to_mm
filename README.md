# xmind_to_mm
Xmind文件转换脚本，生成MindNode可打开的mm文件

需要Python环境，没有Python的请先安装

需要xmindparser库，没有安装的请先
```
pip3 install xmindparser
```

由于 < 号会导致xml识别错误，我转成了'小于'，可自行修改代码自定义

执行
```
python3 xmind_to_mm.py ./xmind文件名
```
会自动在同级目录生成.mm后缀文件
