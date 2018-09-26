# base image
FROM python:2

# where the app will live in the container
WORKDIR /usr/src/app

# install any requirements to workdir
COPY api/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# first dot is project directory, second dot is container workdir
COPY . .

# expose port
EXPOSE 3001

# give the container commands to run
CMD [ "python", "api/routes.py" ]
