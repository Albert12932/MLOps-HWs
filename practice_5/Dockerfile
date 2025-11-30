FROM python:3.11-slim

WORKDIR /app

COPY train_model.py /app/train_model.py

RUN pip install scikit-learn

RUN mkdir -p /app/models

ENTRYPOINT ["python", "train_model.py"]
