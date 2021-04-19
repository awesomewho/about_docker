# Base Images
## 从天池基础镜像构建
FROM registry.cn-shanghai.aliyuncs.com/tcc-public/python:3

## 把当前文件夹里的文件构建到镜像的根目录下
ADD . /workspace

## 指定默认工作目录为根目录
WORKDIR /workspace

## 安装python运行时依赖的包
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

## 镜像启动后统一执行　sh run.sh
CMD ["sh", "run.sh"]
