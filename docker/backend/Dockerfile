FROM python:3.7

WORKDIR /app
COPY requirements.txt .

RUN python --version
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn

ADD ./backend /app/backend
ADD ./docker /app/docker
ADD ./research /app/research

RUN mkdir -p /app/backend/server/staticfiles
RUN mkdir -p /app/backend/server/static




