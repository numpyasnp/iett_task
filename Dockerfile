FROM python:3.10-buster

ENV PYTHONUNBUFFERED 1


WORKDIR /iett_vehicle_tracking

COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD python3 manage.py runserver 0.0.0.0:8000
