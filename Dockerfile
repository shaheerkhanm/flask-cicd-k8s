# Stage 1: Build
FROM python:3.11-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Stage 2: Run
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY app/app.py .

ENV PATH=/root/.local/bin:$PATH
ENV FLASK_ENV=production

EXPOSE 5000
CMD ["python", "app.py"]