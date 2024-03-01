FROM python:3.10-slim-buster

WORKDIR /text-similarity

# RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

RUN pip install Flask==3.0.2 scikit-learn==1.4.1.post1 Levenshtein==0.25.0

RUN pip install simhash==2.1.2
 
ADD ./templates/ ./templates/
ADD ./static/ ./static/
ADD app_docker.py .

CMD ["python", "app_docker.py"]
