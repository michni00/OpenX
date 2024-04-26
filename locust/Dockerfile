FROM python:3.11-slim

WORKDIR /locust
RUN pip install --pre locust
COPY locustfile.py /locust/
EXPOSE 8089
CMD ["locust", "-f", "locustfile.py", "--csv", "example", "-u", "100", "--headless", "-t5m", "-H", "<address>"]
