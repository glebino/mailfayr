FROM python
COPY mail.py /app/
COPY requirements.txt /app/
WORKDIR /app
RUN apt update && pip install -r requirements.txt
