FROM python:3.11-slim

WORKDIR /backend
COPY requirements.txt /backend
RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt
COPY backend /backend/backend

EXPOSE 8080
CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8080"]
