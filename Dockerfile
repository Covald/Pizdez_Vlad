FROM python:3.12.3-bookworm

RUN apt-get update && apt-get upgrade -y

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache -r requirements.txt

COPY ./main.py /app/main.py

CMD ["python", "main.py"]