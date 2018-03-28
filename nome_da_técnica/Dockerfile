FROM ubuntu:16.04
RUN mkdir /container  
ADD . /webservice /container/  
RUN apt-get update && apt-get install -y python-pip
WORKDIR container/webservice/
RUN pip install -r requirements.txt 
CMD gunicorn --workers=3 --timeout=30 --keep-alive 10 --bind 127.0.0.1:$PORT tecnica.wsgi:application



