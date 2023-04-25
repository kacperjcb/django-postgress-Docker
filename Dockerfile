FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt
RUN echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('root', 'admin@example.com', 'admin123!')" | python manage.py shell
CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000", "--settings=myproject.settings" ]
