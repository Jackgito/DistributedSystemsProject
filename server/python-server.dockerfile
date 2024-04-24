FROM python:latest

COPY server.py /
COPY requirements.txt /

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=${PYTHONUNBUFFERED:-1}
CMD [ "python", "./server.py" ]
