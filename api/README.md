# API Documentation


## Getting Started

  Python Version 2.7.15


### Starting up the environemt
Python uses a concept of virtual environment to ... keep code environment stable and install all things via requirements, much like package.json

This project uses python 2.7, Brew recently upgraded in Mar 2018 to use [Python3](https://discourse.brew.sh/t/virtualenv-uses-nonexistent-python-interpreter/1744/16). So To setup try this code block first.
```
virtualenv v-animoos
if errors try: virtualenv -p /usr/bin/python2.7 v-animoos
```

If that doesn't work it's not that much extra work to get this going. Try this block instead
```
brew install python@2
pip2.7 install virtualenv virtualenvwrapper
mkvirtualenv v-animoos --python /usr/local/bin/python
```
if mkvirtualenv is not found try running this command: `source /usr/local/bin/virtualenvwrapper.sh`


And then to run the virtual environment
`source v-animoos/bin/activate`


Akin to install node_modules, python's package dependency's are noted in `requirements.txt`, so to install those run,
`pip install -r requirements.txt`

to run the host on local, run
`python run.py in the root folder`

to test, run `curl http://localhost:5999/api/test` or visit that location in your browser.


<!-- Load any ENV_VARS -->
<br/>



## Docker

  To run animoos in docker, we'll build the image for docker to run a container on, create a container, test that the container is serving the app correctly, and remove container and image from the local machine.


  ### **Building an Image**
  command: `docker build -t animoos:1.0.0 .`
  <br/>
  expanded: The `-t` or `tag` option is for organizational purposes. Followup this command with `docker images` to see a list of built images on your local machine.

  <br/>

  
  ### **Create a Container**
  command: `docker run -d -p 5999:5999 --n animoos <IMAGE_ID>`
  <br />
  expanded: Following this command a long string. Verify the container is running with `docker ps`. There should be something similar to this:
  ```
  CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS              PORTS  NAMES
b58b9200e368        18f3a5cb2dfe        "/bin/sh -c /app/doc…"   About a minute ago   Up About a minute   0.0.0.0:5999->5999/tcp  animoos
  ```
  The `-d` or `detached` option is used to run a container in the background. The `-p` or `port` tag is used to map ports for the container. The `--name` option is for organizational purposes, if you have a number of containers running on your local machine, the name will be easier to refer to than looking at container or image ids.
  
  <br/>


  ### **Test the Container**
  The docker container should be running successfully, now to test if the application is running and serving request as expected. There is a lifecheck endpoint at `/api/`. Visit [localhost:5999/api/](localhost:5999/api/) shoud return a json response in browser. Alternatively, running `curl http://localhost:5999/api/` in a terminal window should also return that json resposne.
  
  <br/>


  ### **Cleanup Container & Image**
  command: `docker kill <CONTAINER_ID>` followed by `docker rm <CONTAINER_ID>`
  <br/>
  expanded:As we continue to make changes and deploy new containers, the old running containers may build up. Cleaning up involves 2 commands, one to stop the container and one to remove the stopped containers.


  <br/>

  ## **API query resources**

  https://github.com/AniList/ApiV2-GraphQL-Docs/tree/master/migration
