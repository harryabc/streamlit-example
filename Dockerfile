
# 基础镜像信息
FROM registry.local/cloudtogo/python:3.6.12-alpine3.12
# 创建目录
RUN mkdir -p /usr/local/ph
# 拷贝文件
ADD ./ /usr/local/ph
# 设置工作目录
WORKDIR /usr/local/ph

RUN pip install --upgrade pip
# 安装requirements
RUN pip install --no-cache-dir -r requirements.txt
 
CMD ["streamlit", "run"，"streamlit_app.py"]

EXPOSE 8501
