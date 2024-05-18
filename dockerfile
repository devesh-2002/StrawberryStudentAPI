FROM python:3.9

ENV DYNAMODB_REGION=ap-south-1
ENV DYNAMODB_TABLE_NAME=studentTable
COPY requirements.txt /requirements.txt

RUN pip3 install -r requirements.txt

COPY schema.py /schema.py

EXPOSE 8000
CMD ["strawberry", "server", "schema"]
