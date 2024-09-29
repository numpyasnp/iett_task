FROM python:3.10-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED 1

WORKDIR /vehicle_tracking

COPY requirements.txt .

RUN pip install --upgrade pip
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD python3 manage.py runserver 0.0.0.0:8000
