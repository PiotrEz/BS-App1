FROM python:3.10
WORKDIR /app
COPY ./main.py /app/main.py
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
ENTRYPOINT ["python3", "main.py"]
EXPOSE 3000
