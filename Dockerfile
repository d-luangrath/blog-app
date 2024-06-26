FROM python:3.11-slim-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app

RUN echo 'export PS1="🐳 \[\e[1;92m\]\u\[\e[0;36m\]@\[\e[1;92m\]\h\[\e[0;36m\]:\[\e[0;36m\][\[\e[0;36m\]\D{%T}\[\e[0;36m\]]\[\e[0;36m\]:\[\e[1;34m\]\w \[\e[0;36m\]# \[\e[0m\]"' >> ~/.bashrc && \
    pip install -r requirements.txt

EXPOSE 8000

CMD gunicorn blogapp.wsgi -w 2 -b 0.0.0.0:8000
