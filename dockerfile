# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
FROM python:alpine

# If you prefer miniconda:
#FROM continuumio/miniconda3

LABEL Name=django-factory Version=0.0.1
EXPOSE 8000

# Install ptvsd (the debugger) into the container
# RUN python3 -m pip install ptvsd 
# Using pip:
# RUN python3 -m pip install -r requirements.txt
ADD requirements.txt /requirements.txt
RUN python3 -m pip install -r requirements.txt

WORKDIR /app/
# First line below launches the debug server and listens on port 5678
# Second line starts django in development mode after the debugger attaches
CMD ["python3", "-m", "debugpy", "--listen", "0.0.0.0:5678", "--log-to-stderr", "--wait-for-client", \
    "manage.py", "runserver", "--noreload", "--nothreading", "0.0.0.0:8000"]
