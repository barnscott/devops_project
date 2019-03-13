#https://runnable.com/docker/python/dockerize-your-python-application

FROM python:3

ADD main.py /
#RUN pip install somepipfile
CMD [ "python", "./main.py" ]