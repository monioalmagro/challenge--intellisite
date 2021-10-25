FROM python:3.8

WORKDIR /usr/app

ADD ./requirements.txt ./
RUN pip install -r requirements.txt
ADD ./ ./

ENV KAFKA_BROKER_URL: 'broker:9092'
ENV DETECTIONS_TOPIC: 'intellisite.detections'

CMD ["python3", "main.py"]
