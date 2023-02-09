FROM python:3.9

WORKDIR /fastapi-car-price-pred

ADD . /fastapi-car-price-pred

RUN pip install -r requirements.txt

CMD ["python", "main.py"]