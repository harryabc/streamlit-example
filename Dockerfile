FROM python:3.7
WORKDIR /app
 
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt  -i https://pypi.tuna.tsinghua.edu.cn/simple
 
EXPOSE 8501
COPY . /app
ENTRYPOINT ["streamlit", "run"]
 
CMD ["streamlit_app.py"]
