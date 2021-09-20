FROM python:3
COPY . /usr/src/app
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN python3 -m pip install -r requirements.txt
WORKDIR /usr/src/app
CMD ["python3","api.py"]
