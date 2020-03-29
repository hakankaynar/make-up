FROM python:3.8.2-slim-buster

COPY ./ /root/make-up
ENV PYTHONPATH=/root/make-up
WORKDIR /root/make-up

RUN pip install -r requirements.txt

EXPOSE 8000/tcp

CMD ["gunicorn", "--config", ".docker/gunicorn.conf.py", "routes" ]