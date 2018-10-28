#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn

# run the created app from run.py
exec gunicorn run:app        \
  --name animoos             \
  --bind 0.0.0.0:5999        \
  --worker-class gevent      \
  --workers 3                \

  # add env_var
  # --env APP_NAME=$APP_NAME   \
