FROM python:3.8.5

WORKDIR /code
COPY . .
RUN python3 -m pip install --upgrade pip
RUN pip install -r /code/requirements.txt

CMD gunicorn ilr_league.wsgi:application --bind 0.0.0.0:8000
