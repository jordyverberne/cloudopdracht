FROM python:2.7
EXPOSE 443
ADD . /todo
WORKDIR /todo
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
