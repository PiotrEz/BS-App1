FROM python:3.10
WORKDIR /app
COPY ./main.py /app/main.py
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
ENV ip=123
CMD ["bash", "-c", "python3 ./main.py -i ${ip}"]
EXPOSE 3000
