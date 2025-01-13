FROM python:3.13

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Required to install mysqlclient with Pip
RUN apt-get update \
  && apt-get install python3-dev default-libmysqlclient-dev gcc -y

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Copy the requirements.txt file to the working directory
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the application files into the image
COPY . /app/

# Expose port 8000 on the container
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]