# 基础镜像信息
FROM registry.local/official/python:3.7
# 创建目录
RUN mkdir -p /usr/local/ph
# 拷贝文件
ADD ./ /usr/local/ph
# 设置工作目录
WORKDIR /usr/local/ph
# 安装requirements
RUN pip install paddlepaddle==2.2.2 -i https://mirror.baidu.com/pypi/simple
RUN pip install --no-cache-dir -r requirements.txt
 
CMD ["streamlit", "run"，"./streamlit_app.py"]

EXPOSE 8501
