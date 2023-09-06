# Use the official Ubuntu 20.04 image as the base
FROM python:3.10

COPY requirements.txt .
RUN pip3 install --default-timeout=100 -r requirements.txt

# Copy the rest of the application code to the working directory
COPY model.json model.json
COPY server.py server.py

#Exposing the port 5000 from the container
EXPOSE 5000

#Starting the python application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "server:app"]
