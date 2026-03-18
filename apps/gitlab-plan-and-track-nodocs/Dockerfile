FROM python:3.12-slim
WORKDIR /app
COPY server.py index.html ./
COPY js/ ./js/
COPY css/ ./css/
EXPOSE 8000
CMD ["python", "server.py"]
