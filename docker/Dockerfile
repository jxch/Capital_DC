FROM python:slim

WORKDIR /opt/capital_dc/
COPY /app .

RUN pip install -r requirements.txt

ENTRYPOINT python app.py