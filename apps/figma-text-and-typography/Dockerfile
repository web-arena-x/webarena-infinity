FROM python:3.12-slim
WORKDIR /app
COPY server.py index.html ./
COPY js/ ./js/
COPY css/ ./css/
COPY real-tasks/ ./real-tasks/
EXPOSE 8000
CMD ["python", "server.py"]
