# base image
FROM python:2.7-slim

# where the app will live in the container
WORKDIR /app

# install any requirements to workdir
ADD requirements.txt /app

# install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copy the current directory contents into the container at /app
ADD . /app

# expose port
EXPOSE 5999

# give the container commands to run
CMD [ "python", "run.py" ]
