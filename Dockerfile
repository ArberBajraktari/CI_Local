# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

#docker run --rm --detach --publish 8081:8080 --publish 50000:50000 --name jenkins --volume jenkins-data-home:/var/jenkins_home --volume /var/run/docker.sock:/var/run/docker.sock jenkins-with-docker