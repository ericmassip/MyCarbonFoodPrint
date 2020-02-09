FROM python:3.7
ENV FLASK_ENV development
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["flask","run","-h","0.0.0.0"]