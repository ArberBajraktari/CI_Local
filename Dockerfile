# 
FROM python:3.10.2

# 
WORKDIR /app

# 
COPY ./requirements.txt requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 
COPY ./app /app

EXPOSE 5000

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]

#docker run --rm --detach --publish 8081:8080 --publish 50000:50000 --name jenkins --volume jenkins-data-home:/var/jenkins_home --volume /var/run/docker.sock:/var/run/docker.sock jenkins-with-docker