FROM python:3.12-slim
WORKDIR /app
COPY server.py index.html tasks.json ./
COPY js/ ./js/
COPY css/ ./css/
COPY tasks/ ./tasks/
EXPOSE 8000
CMD ["python", "server.py"]
