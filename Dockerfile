
FROM python:3.7

# This command create folder
# And makes it as workdir
WORKDIR /fastapi-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

CMD ["python", "./app/main.py"]


