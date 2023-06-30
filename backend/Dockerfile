#FROM python:3.10.1-slim
FROM tiangolo/uvicorn-gunicorn:python3.7

WORKDIR /app

RUN apt-get update
RUN apt-get install 'ffmpeg'\
    'libsm6'\
    'libxext6'  -y

COPY requirements.txt .
RUN pip install -r requirements.txt -f https://download.pytorch.org/whl/torch_stable.html

COPY . .

EXPOSE 8080

CMD ["python3", "main.py"]