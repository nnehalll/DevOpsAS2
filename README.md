# Assignment 2: Dockerizing a Python Application

***Objective***: Containerize a Flask or FastAPI application using Docker and Docker Compose.

***Tasks***:
1. ***Dockerfile***:
   - Write a Dockerfile to create a Docker image for your Flask or FastAPI application.
   - Ensure the Dockerfile includes all necessary dependencies and exposes the correct port.

2. ***Build and Run***:
   - Build the Docker image locally using the Dockerfile.
   - Run the Docker container to ensure the application works correctly inside the container.

3. ***Docker Compose***:
   - Create a docker-compose.yml file to define services for the web application and a database (e.g., PostgreSQL).
   - Configure networks and volumes in the Docker Compose file.


4. ***Push to Docker Hub***:
   - Tag the Docker image and push it to Docker Hub.
  
# Assignment 3: Free Style Job  with Jenkins

**Objective**: Set a free style job in jenkins to take a git pull of dockerrise application created in assignment 2

**Tasks**:
1. **Jenkins Setup**:
   - Install Jenkins on your local machine or use a cloud instance.
   - Configure Jenkins to connect to your Git repository.

 2. **Launching of App**:
       - Take an updated pull of dockerrise application and launch it on port 5003 ,do the changes in git repo and take fresh pull in jenkins to make sure changes getting reflected on web browser
