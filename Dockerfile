FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt
ENTRYPOINT [ "bash", "-c", "python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000 --settings=myproject.settings" ]

