FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED 1

EXPOSE 8000
WORKDIR /app

#COPY pyproject.toml ./
#RUN #pip install poetry && poetry config virtualenvs.in-project true
#RUN poetry install --no-dev
RUN apt-get update && \
    apt-get -y install gcc python3-dev
COPY requirements.txt ./
RUN pip install -r  ./requirements.txt --no-cache-dir

COPY app/services/ai_model/yolov5/requirements.txt ./requirements-yolov5.txt

RUN pip install -r ./requirements-yolov5.txt --no-cache-dir
RUN apt-get install ffmpeg libsm6 libxext6  -y
#RUN apt-get install -y \
#        libgl1-mesa-glx \
#        libx11-xcb1 \
#     && apt-get clean all


#COPY ./app ./app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
