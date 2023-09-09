# Use the official Ubuntu 20.04 image as the base
FROM python:3.10

# Copy files and install dependencies
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./
RUN pip3 install --default-timeout=100 -r requirements.txt

#Starting the python application
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
