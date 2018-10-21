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

to test, run `curl http://localhost:3001/api/test` or visit that location in your browser.


<!-- Load any ENV_VARS -->





## API query resources

https://github.com/AniList/ApiV2-GraphQL-Docs/tree/master/migration
