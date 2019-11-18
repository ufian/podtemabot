FROM python:3.7.5-slim
ADD . /src
WORKDIR /src
RUN pip install -r requirements.txt
CMD python /src/run.py
