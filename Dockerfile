FROM python:2.7
ADD . /todo
WORKDIR /todo
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
#CMD ["python", "test.py"]
