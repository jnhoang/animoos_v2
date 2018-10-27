import os


# this class will be used to configure the app
# we'll use this to set environment variables (env_vars) here.
# these should be saved in your ~/.bash_profile or ~/.zshrc in the following format:
# EXPORT YOUR_VARIABLE=your_variable

class Config:
  # note we use the .get() method in the event that the variable is not set,
  # this get method will default the value to None as opposed to running into an exception
  # MY_VARIABLE= os.environ.get('YOUR_VARIABLE')
  
  # using a pass statement to run "nothing", used to stub this class
  pass
