# Here I'm using alpine dis because it's lightweight.
FROM python:3.10-slim-buster

WORKDIR /app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# NOTE: this won't copy venv dir as it was already ignored
COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]