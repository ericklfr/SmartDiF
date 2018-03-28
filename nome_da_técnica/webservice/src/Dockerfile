FROM python:3.5
RUN mkdir /container  
ADD /tecnica/ /container/  
RUN pip install -r /tecnica/requirements.pip  
CMD gunicorn --bind 127.0.0.1:8004 tecnica.wsgi:application
WORKDIR /tecnica  
