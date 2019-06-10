FROM docker.io/python:3.6

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./*.py ./server/python/

EXPOSE 9090
CMD ["python", "-u", "./server/python/server.py"]