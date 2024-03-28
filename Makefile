build:
    docker build -t test:latest .

run:
    docker run -rm -p 127.0.0.1:8000:8000 test:latest