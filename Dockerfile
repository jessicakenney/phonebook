#FROM ubuntu:latest

# Use an official Python runtime as a parent image
FROM python:3.6-slim-stretch

MAINTAINER Jessica Sheridan "jessica@tura.io"

# Set the working directory to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
#RUN pip install --trusted-host pypi.python.org -r requirements.txt

#RUN apt-get install software-properties-common python-software-properties
#RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update
RUN apt-get install -y python3.6

#RUN apt-get install -y python3 python3-pip python3-dev

# Copy the current directory contents into the container at /app
COPY . /app

#
# RUN pip3 install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

#
ENTRYPOINT ["python3.6"]

# Run app.py when the container launches
CMD ["phonebook.py"]