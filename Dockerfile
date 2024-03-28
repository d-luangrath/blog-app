FROM python:3.11-slim-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app

RUN echo 'export PS1="🐳 \[\e[1;92m\]\u\[\e[0;36m\]@\[\e[1;92m\]\h\[\e[0;36m\]:\[\e[0;36m\][\[\e[0;36m\]\D{%T}\[\e[0;36m\]]\[\e[0;36m\]:\[\e[1;34m\]\w \[\e[0;36m\]# \[\e[0m\]"' >> ~/.bashrc && \
    pip install -r requirements.txt

CMD [ "python3" , "hello.py"]