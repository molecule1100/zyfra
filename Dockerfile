FROM python:3.13

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir --no-input

COPY . .

RUN cd zyfra_test && python manage.py makemigrations
RUN cd zyfra_test && python manage.py migrate


EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--chdir", "zyfra_test", "zyfra_project.wsgi:application"]