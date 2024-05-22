FROM python:3.11.3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /celery

# Install dependencies
COPY requirements.txt /celery/
RUN pip install -r requirements.txt

COPY . /celery/


