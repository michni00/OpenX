FROM python:3.9

WORKDIR /backend
COPY requirements.txt /backend
RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt
COPY . /backend

EXPOSE 8000
CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"]