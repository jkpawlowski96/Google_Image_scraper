FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
RUN apk add --no-cache gcc musl-dev linux-headers
EXPOSE 5000
COPY . .
RUN pip install -r requirements.txt
CMD ["flask", "run"]