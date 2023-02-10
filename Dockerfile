FROM python:3.9

WORKDIR /github-actions-cd

ADD . /github-actions-cd

RUN pip install -r requirements.txt

CMD ["python", "main.py"]