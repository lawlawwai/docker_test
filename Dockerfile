FROM python

WORKDIR /test

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY config.ini ./
COPY main.py ./

CMD ["python", "main.py"]

