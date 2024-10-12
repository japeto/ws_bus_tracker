# pull python image
FROM python:3.12.3
# set language/unicode
ENV LANG C.UTF-8
# Set main directory 
WORKDIR /usr/share/bus_tracker_backend
# Copy code and python scripts to image
COPY . .
# Set python environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Update pip 
RUN pip install --upgrade pip
# Install c & c++
RUN apt-get update \
  && apt-get -y install libpq-dev gcc
# Install requirements
RUN pip install -r requirements/prod.txt
# Open port
EXPOSE 8000
# Entrypoint
CMD ["sh", "./entrypoint.sh"]










