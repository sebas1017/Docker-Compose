FROM python:3
COPY . /usr/src/app
RUN python3 -m pip install flask
RUN pip install psycopg2-binary==2.9.1
WORKDIR /usr/src/app
CMD ["python3","api.py"]
